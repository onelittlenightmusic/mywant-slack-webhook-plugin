#!/usr/bin/env python3
"""What the Slack notifier does with a murmur it heard (spec.hear): a failure
(status: failed) it offers to post to Slack — to the incoming webhook in its
param outgoing_webhook_url. Asked of the person, not done."""
import json
import sys


def main() -> None:
    given = json.loads(sys.argv[1])
    heard = given.get("heard") or {}
    proposals = []
    failed = "failed" in (heard.get("timings") or []) or any(
        c.get("field") == "status" and c.get("to") == "failed" for c in heard.get("change") or [])
    if failed:
        who = heard.get("from_want_name") or "want"
        why = str(heard.get("result") or "").strip()
        text = f"「{who}」が失敗しました" + (f": {why}" if why else "")
        proposals.append({
            "action": "post_webhook",
            "url_param": "outgoing_webhook_url",
            "body": {"text": text},
            "ask": f"{text}。Slack に知らせますか？",
        })
    print(json.dumps({"proposals": proposals}, ensure_ascii=False))


if __name__ == "__main__":
    main()
