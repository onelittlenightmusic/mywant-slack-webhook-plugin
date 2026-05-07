# mywant-slack-webhook-plugin

A [MyWant](https://github.com/onelittlenightmusic/MyWant) plugin that adds the **Slack Notify** want type.

Receives messages from Slack via the Events API (HTTP POST) and exposes them to downstream wants.

## Requirements

- [MyWant](https://github.com/onelittlenightmusic/MyWant) installed and running
- Slack App with Event Subscriptions enabled

## Installation

```sh
git clone https://github.com/onelittlenightmusic/mywant-slack-webhook-plugin \
  ~/.mywant/custom-types/mywant-slack-webhook-plugin
```

Then restart MyWant (`./bin/mywant stop && ./bin/mywant start -D`).

## Usage

```yaml
metadata:
  name: slack-inbox
  type: slack_notify
spec:
  params:
    signing_secret: ""   # optional: Slack Signing Secret for HMAC verification
    channel_filter: ""   # optional: Slack channel ID to filter (e.g. C01ABCDEF23)
```

The webhook endpoint is available at:
```
POST /api/v1/webhooks/{want-name}
```

Configure this URL as the Request URL in your Slack App's Event Subscriptions settings. Slack URL verification challenges are handled automatically.

## Test with curl

```sh
curl -X POST http://localhost:8080/api/v1/webhooks/slack-inbox \
  -H "Content-Type: application/json" \
  -d '{"type":"event_callback","event":{"type":"message","user":"U01ABCDEF","text":"hello","channel":"C01ABCDEF23","ts":"1234567890.123456"}}'
```
