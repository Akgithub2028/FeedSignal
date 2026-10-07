"""Wake the optional sleeping Render preview after publishing a Celery job.

The request is advisory: Redis dispatch and webhook responses never wait for
it. This does not keep an idle service awake or guarantee scheduled execution.
"""
import logging
import os
import threading
import time
from urllib.parse import urlsplit

import httpx
from celery.signals import after_task_publish

logger = logging.getLogger(__name__)
_lock = threading.Lock()
_last_wake = float('-inf')


def _ping_worker(url):
    try:
        httpx.get(url, timeout=4.0, follow_redirects=False)
    except httpx.HTTPError:
        # A cold-start timeout still initiates Render's wake-up. Queue work
        # remains in Redis; do not leak request details or change dispatch.
        logger.info('Worker preview wake request did not complete')


@after_task_publish.connect(weak=False)
def wake_worker_preview(**_kwargs):
    global _last_wake
    url = os.getenv('WORKER_PREVIEW_HEALTH_URL', '').strip()
    if not url:
        return
    try:
        parsed = urlsplit(url)
        valid = (parsed.scheme == 'https' and parsed.hostname
                 and parsed.hostname.endswith('.onrender.com')
                 and parsed.path == '/health' and not parsed.query
                 and not parsed.fragment and not parsed.username
                 and not parsed.password and parsed.port in (None, 443))
        if not valid:
            logger.warning('Invalid worker preview health URL; wake skipped')
            return
        with _lock:
            now = time.monotonic()
            if now - _last_wake < 30:
                return
            _last_wake = now
            threading.Thread(target=_ping_worker, args=(url,), daemon=True).start()
            logger.info('Worker preview wake requested after task publish')
    except (ValueError, RuntimeError):
        logger.warning('Worker preview wake could not start; job remains queued')
