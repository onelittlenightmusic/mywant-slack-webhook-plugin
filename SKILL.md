---
name: mywant-slack-webhook-plugin
description: Slack Events APIのメッセージをMyWant want typeとして受信するプラグイン。SlackからのHTTP POSTメッセージを受信・バッファリングし、下流のwantに転送する。URL verification challengeを自動処理。
compatibility:
  requires:
    - MyWant server running
    - Slack App with Event Subscriptions enabled
metadata:
  output-format: agent-based
  note: This plugin requires the slack_notify Go implementation in the main binary. YAML-only installation requires the binary to include slack_webhook_types.go and agent_monitor_slack_webhook.go.
---

## 使い方

MyWant want typeとして使用する:

```yaml
metadata:
  name: slack-inbox
  type: slack_notify
spec:
  params:
    signing_secret: ""
    channel_filter: ""
```

WebhookエンドポイントURL:
```
POST /api/v1/webhooks/{want-name}
```

## 状態フィールド

- `slack_latest_message` — 最新受信メッセージ
- `slack_messages` — 直近20件のFIFOバッファ
- `slack_message_count` — 受信件数
- `webhook_url` — このwantのwebhookエンドポイントパス
