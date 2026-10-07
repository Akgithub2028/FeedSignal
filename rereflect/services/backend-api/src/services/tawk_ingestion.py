"""Normalize documented tawk.to transcripts/tickets, keeping visitor evidence only."""
from html.parser import HTMLParser


class _Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_endtag(self, tag):
        if tag in ("p", "div", "li"): self.parts.append("\n")

    def handle_starttag(self, tag, attrs):
        if tag == "br": self.parts.append("\n")


def _string(value, maximum=255):
    if value is None: return None
    if not isinstance(value, str) or len(value) > maximum:
        raise ValueError("Invalid text field")
    return value.strip() or None


def normalize(payload):
    event = payload.get("event")
    if event not in ("chat:transcript_created", "ticket:create"):
        return None
    record = payload.get("chat" if event == "chat:transcript_created" else "ticket")
    if not isinstance(record, dict): raise ValueError("Missing chat/ticket")
    external_id = _string(record.get("id"), 128)
    if not external_id: raise ValueError("Missing chat/ticket ID")
    visitor = record.get("visitor", {}) if event == "chat:transcript_created" else payload.get("requester", {})
    if not isinstance(visitor, dict): raise ValueError("Invalid visitor")
    texts = []
    if event == "chat:transcript_created":
        messages = record.get("messages")
        if not isinstance(messages, list): raise ValueError("Invalid messages")
        for message in messages:
            if not isinstance(message, dict) or not isinstance(message.get("sender"), dict):
                raise ValueError("Invalid message")
            if message["sender"].get("t") == "v" and message.get("type") == "msg":
                text = _string(message.get("msg"), 100_000)
                if text: texts.append(text)
    else:
        # Agent-created/internal tickets are not customer demand evidence.
        if visitor.get("type") in ("agent", "system"): return None
        subject = _string(record.get("subject"), 100_000)
        message = _string(record.get("message"), 100_000)
        if subject: texts.append(subject)
        if message:
            parser = _Text(); parser.feed(message)
            texts.append("".join(parser.parts).strip())
    text = "\n".join(texts).strip()
    if not text: return None
    if len(text) > 100_000: raise ValueError("Transcript too large")
    return {"text": text, "customer_email": _string(visitor.get("email")),
            "external_id": ("chat:" if event == "chat:transcript_created" else "ticket:") + payload["property"]["id"] + ":" + external_id,
            "metadata": {"property_id": payload["property"]["id"], "provider_id": external_id,
                         "event": event, "author_name": _string(visitor.get("name")),
                         "provider_time": _string(payload.get("time")),
                         "domain": _string(payload.get("domain"), 2048)}}
