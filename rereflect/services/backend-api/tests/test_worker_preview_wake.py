"""Free-preview dispatch wakes never block or interfere with queued jobs."""
from unittest.mock import patch
import httpx
from src.background import worker_preview as preview

URL = 'https://feedsignal-worker-preview.onrender.com/health'


def test_disabled_without_config(monkeypatch):
    monkeypatch.delenv('WORKER_PREVIEW_HEALTH_URL', raising=False)
    with patch.object(preview.threading, 'Thread') as thread:
        preview.wake_worker_preview()
    thread.assert_not_called()


def test_dispatch_starts_one_daemon_and_throttles_burst(monkeypatch):
    monkeypatch.setenv('WORKER_PREVIEW_HEALTH_URL', URL)
    monkeypatch.setattr(preview, '_last_wake', float('-inf'))
    with patch.object(preview.threading, 'Thread') as thread:
        preview.wake_worker_preview()
        preview.wake_worker_preview()
    thread.assert_called_once_with(target=preview._ping_worker, args=(URL,), daemon=True)
    thread.return_value.start.assert_called_once()


def test_request_is_bounded_and_does_not_follow_redirects():
    with patch.object(preview.httpx, 'get') as get:
        preview._ping_worker(URL)
    get.assert_called_once_with(URL, timeout=4.0, follow_redirects=False)


def test_cold_start_timeout_is_nonfatal():
    with patch.object(preview.httpx, 'get', side_effect=httpx.ReadTimeout('cold start')):
        preview._ping_worker(URL)


def test_invalid_destinations_do_not_start_thread(monkeypatch):
    for url in ['http://localhost/health', 'https://user:password@x.onrender.com/health',
                'https://example.com/health', URL + '?token=secret', URL + '/run']:
        monkeypatch.setenv('WORKER_PREVIEW_HEALTH_URL', url)
        with patch.object(preview.threading, 'Thread') as thread:
            preview.wake_worker_preview()
        thread.assert_not_called()


def test_thread_start_failure_does_not_break_publish(monkeypatch):
    monkeypatch.setenv('WORKER_PREVIEW_HEALTH_URL', URL)
    monkeypatch.setattr(preview, '_last_wake', float('-inf'))
    with patch.object(preview.threading, 'Thread') as thread:
        thread.return_value.start.side_effect = RuntimeError('cannot start thread')
        preview.wake_worker_preview()
