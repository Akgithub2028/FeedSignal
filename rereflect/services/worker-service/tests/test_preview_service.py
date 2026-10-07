"""The preview health endpoint must never report dead children as healthy."""
import subprocess
import sys
import socket
from http.server import HTTPServer

import pytest


def test_running_children_are_reported_without_claiming_broker_readiness():
    from src.preview_service import health_status, stop_processes
    children = [subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)']) for _ in range(2)]
    try:
        status, payload = health_status(children)
        assert status == 200
        assert payload == {'worker_process_alive': True, 'scheduler_process_alive': True,
                           'broker_ready': 'not_checked', 'mode': 'sleeping-free-tier-preview'}
    finally:
        stop_processes(children)


@pytest.mark.parametrize('failed_child', [0, 1])
def test_either_child_exit_makes_health_unavailable(failed_child):
    from src.preview_service import health_status, stop_processes
    children = [subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)']) for _ in range(2)]
    try:
        children[failed_child].terminate()
        children[failed_child].wait(timeout=5)
        status, payload = health_status(children)
        assert status == 503
        assert payload['worker_process_alive'] is (failed_child != 0)
        assert payload['scheduler_process_alive'] is (failed_child != 1)
    finally:
        stop_processes(children)


def test_shutdown_reaps_both_children_and_is_safe_to_repeat():
    from src.preview_service import stop_processes
    children = [subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)']) for _ in range(2)]
    stop_processes(children)
    assert all(p.poll() is not None for p in children)
    stop_processes(children)


def test_accepted_connection_has_bounded_read_time(monkeypatch):
    from src.preview_service import PreviewHTTPServer
    connection, peer = socket.socketpair()
    monkeypatch.setattr(HTTPServer, 'get_request', lambda self: (connection, ('local', 0)))
    try:
        accepted, _ = PreviewHTTPServer.get_request(PreviewHTTPServer.__new__(PreviewHTTPServer))
        assert accepted.gettimeout() == 2
        with pytest.raises(TimeoutError):
            accepted.recv(1)
    finally:
        connection.close()
        peer.close()
