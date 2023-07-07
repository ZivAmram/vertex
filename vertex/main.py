import os
import logging
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import pytz

LOG_FILENAME = '/app/logs/app.log'
TIMEZONE = 'Asia/Tel_Aviv'  # Replace with your actual timezone

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        current_time = get_local_time()
        log_message = f'{current_time} - Received GET request'
        logging.info(log_message)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

def get_local_time():
    tz = pytz.timezone(TIMEZONE)
    local_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    return local_time

def run_server():
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format='%(asctime)s - %(message)s')
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    logging.info('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()