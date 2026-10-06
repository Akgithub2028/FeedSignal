import importlib.util
from pathlib import Path
from unittest.mock import Mock

import pytest


@pytest.mark.parametrize('service', ['backend-api', 'worker-service'])
def test_missing_sender_disables_delivery_even_with_api_key(service, monkeypatch):
    monkeypatch.setenv('RESEND_API_KEY', 'test-only-key')
    monkeypatch.delenv('FROM_EMAIL', raising=False)
    root = Path(__file__).resolve().parents[2]
    path = root / service / 'src' / ('services/email_service.py' if service == 'backend-api' else 'email.py')
    spec = importlib.util.spec_from_file_location(f'owner_email_{service}', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    post = Mock(side_effect=AssertionError('must not send without configured sender'))
    monkeypatch.setattr(module.requests, 'post', post)
    assert module._send_email('recipient@example.com', 'Test subject', '<p>Test</p>') is False
    post.assert_not_called()
