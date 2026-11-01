"""Area 2, V4 — artefact rows -> canonical trajectories (§R5).

Canonical step dict: action_text, obs_text, is_error, is_retry, tool,
n_tokens, text_digest, marker_hits. Canonical trajectory dict:
task_id, task_rule, success (bool), steps (list), token_level.

Parsing choices are made from schema only, never outcomes, and are
recorded in code/BUILD_LOG_V4.md.
"""
from __future__ import annotations

import json
import re

from tcrc import FAILURE_MARKERS

_INSTANCE_RE = re.compile(r"[A-Za-z0-9_.\-]+__[A-Za-z0-9_.\-]+")


def extract_task_id(row: dict, family: str):
    """§R3 task-identifier priority: instance_id -> issue_id ->
    task_id -> (repository, issue) composite carried in a field.
    For CF (no id columns), the composite is sought as a SWE-bench
    instance pattern inside trajectory_id / image (build-log
    interpretation, recorded pre-census). Returns (task_id, rule)."""
    for key in ("instance_id", "issue_id", "task_id"):
        v = row.get(key)
        if v:
            return str(v), f"field:{key}"
    if family == "CF":
        # Census step (ii) finding (BUILD_LOG_V4 addendum, recorded
        # pre-eligibility): the artefact's `image` field is its
        # per-task environment identifier — a (repository, instance)
        # composite carried in a field (§R3 priority 4). Verified
        # mechanically: trajectory_id minus its _runK suffix equals
        # the image string on every inspected row.
        v = row.get("image")
        if v:
            return str(v), "field:image"
        v = row.get("trajectory_id")
        if v:
            m = _INSTANCE_RE.search(str(v))
            if m:
                return m.group(0), "pattern:trajectory_id"
    return None, None


def _msg_text(content) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for p in content:
            if isinstance(p, str):
                parts.append(p)
            elif isinstance(p, dict):
                for k in ("text", "content", "input", "arguments"):
                    if isinstance(p.get(k), str):
                        parts.append(p[k])
                        break
        return "\n".join(parts)
    return str(content)


def _role(m: dict) -> str:
    r = m.get("role") or m.get("from") or ""
    r = str(r).lower()
    if r in ("gpt", "assistant", "model"):
        return "assistant"
    if r in ("human", "user"):
        return "user"
    if r in ("tool", "function", "observation", "environment"):
        return "tool"
    if r == "system":
        return "system"
    return r or "user"


def _native_error(msg: dict) -> bool:
    if msg.get("is_error") is True:
        return True
    st = str(msg.get("status", "")).lower()
    if st in ("error", "failed", "failure"):
        return True
    e = msg.get("error")
    if e:
        return True
    return False


_TOKEN_KEYS = ("token_count", "n_tokens", "tokens")


def _msg_tokens(msg: dict):
    """Per-message token count if the message carries one (frozen
    priority sub-order, Gate 9 note X6): usage.total_tokens, else
    usage prompt+completion, else usage completion, else usage
    prompt, else a direct token field."""
    u = msg.get("usage")
    if isinstance(u, dict):
        if isinstance(u.get("total_tokens"), (int, float)):
            return float(u["total_tokens"])
        p, c = u.get("prompt_tokens"), u.get("completion_tokens")
        if isinstance(p, (int, float)) and isinstance(c, (int, float)):
            return float(p) + float(c)
        if isinstance(c, (int, float)):
            return float(c)
        if isinstance(p, (int, float)):
            return float(p)
    for k in _TOKEN_KEYS:
        if isinstance(msg.get(k), (int, float)):
            return float(msg[k])
    return None


def parse_messages(raw):
    """Parse an artefact `messages` value (JSON string or list) into
    canonical steps. A step = one assistant turn + the following
    observation (all non-assistant messages until the next assistant
    turn). System messages and the pre-first-assistant user message
    (the task prompt) are not steps. Returns (steps, token_level)."""
    if isinstance(raw, str):
        msgs = json.loads(raw)
    else:
        msgs = raw
    if isinstance(msgs, dict) and "messages" in msgs:
        msgs = msgs["messages"]
    if not isinstance(msgs, list):
        raise ValueError("messages is not a list")

    raw_steps = []  # (action_text, tool, obs_text, native_err, tok_list)
    cur = None
    for m in msgs:
        if not isinstance(m, dict):
            continue
        role = _role(m)
        if role == "system":
            continue
        if role == "assistant":
            if cur is not None:
                raw_steps.append(cur)
            action = _msg_text(m.get("content", m.get("value", "")))
            tool = None
            tcs = m.get("tool_calls") or m.get("function_call")
            if tcs:
                if isinstance(tcs, dict):
                    tcs = [tcs]
                names, args = [], []
                for tc in tcs:
                    if isinstance(tc, dict):
                        fn = tc.get("function") or tc
                        nm = fn.get("name") if isinstance(fn, dict) else None
                        if nm:
                            names.append(str(nm))
                        ag = fn.get("arguments") if isinstance(fn, dict) else None
                        if ag:
                            args.append(ag if isinstance(ag, str) else json.dumps(ag))
                if names and tool is None:
                    tool = names[0]
                if args:
                    action = (action + "\n" + "\n".join(args)).strip()
            cur = {"action": action, "tool": tool, "obs": [],
                   "native_err": _native_error(m), "toks": []}
            tk = _msg_tokens(m)
            if tk is not None:
                cur["toks"].append(tk)
        else:
            if cur is None:
                continue  # task prompt / prelude
            cur["obs"].append(_msg_text(m.get("content", m.get("value", ""))))
            if _native_error(m):
                cur["native_err"] = True
            tk = _msg_tokens(m)
            if tk is not None:
                cur["toks"].append(tk)
    if cur is not None:
        raw_steps.append(cur)

    steps = []
    token_level = 3
    prev_action = None
    for rs in raw_steps:
        action = rs["action"]
        obs = "\n".join(rs["obs"])
        obs_low = obs.lower()
        marker_hits = sum(1 for mk in FAILURE_MARKERS if mk in obs_low)
        is_error = 1 if (rs["native_err"] or marker_hits > 0) else 0
        tool = rs["tool"] or (action.split()[0] if action.split() else "")
        if rs["toks"]:
            n_tokens = float(sum(rs["toks"]))
            token_level = min(token_level, 1 if len(rs["toks"]) == 1 else 2)
        else:
            n_tokens = float(len((action + " " + obs).split()))
        steps.append({
            "action_text": action,
            "obs_text": obs,
            "is_error": is_error,
            "is_retry": 1 if (prev_action is not None and action == prev_action) else 0,
            "tool": tool,
            "n_tokens": n_tokens,
            "text_digest": (action + "\n" + obs)[:1000],
            "marker_hits": marker_hits,
        })
        prev_action = action
    return steps, token_level
