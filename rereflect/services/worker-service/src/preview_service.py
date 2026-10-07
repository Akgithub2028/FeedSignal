"""Sleeping free-tier HTTP wrapper for controlled cloud worker tests.

This is not an always-on scheduler. Render can suspend this web service
after inactivity; health indicates process liveness, not broker readiness.
"""
import json
import os
import signal
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


class PreviewHTTPServer(HTTPServer):
    def get_request(self):
        connection, address = super().get_request()
        connection.settimeout(2)
        return connection, address


def health_status(children):
    worker_alive, scheduler_alive = (p.poll() is None for p in children)
    return (200 if worker_alive and scheduler_alive else 503), {
        'worker_process_alive': worker_alive,
        'scheduler_process_alive': scheduler_alive,
        'broker_ready': 'not_checked',
        'mode': 'sleeping-free-tier-preview',
    }


def stop_processes(children):
    for child in children:
        if child.poll() is None:
            child.terminate()
    for child in children:
        try:
            child.wait(timeout=10)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()


def main():
    children = []
    def shutdown(_signum, _frame):
        raise SystemExit(0)
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    try:
        prefix = [sys.executable, '-m', 'celery', '-A', 'src.celery_app']
        children.append(subprocess.Popen(prefix + ['worker', '--pool=solo', '--concurrency=1', '--loglevel=info']))
        children.append(subprocess.Popen(prefix + ['beat', '--loglevel=info', '--schedule=/tmp/feedsignal-beat']))

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path != '/health':
                    self.send_error(404)
                    return
                status, payload = health_status(children)
                body = json.dumps(payload).encode()
                self.send_response(status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, _format, *_args):
                pass

        with PreviewHTTPServer(('0.0.0.0', int(os.environ.get('PORT', '10000'))), Handler) as server:
            server.timeout = 1
            while all(p.poll() is None for p in children):
                server.handle_request()
        raise SystemExit(1)
    finally:
        stop_processes(children)


if __name__ == '__main__':
    main()
