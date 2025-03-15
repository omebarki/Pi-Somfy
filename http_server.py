from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import threading


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/g?password=password" :
            t = threading.Thread(target=self.open_garage)
            t.start()
            self.wfile.write(b'OK!')
        self.wfile.write(b'OK!')

    def open_garage(self):
        subprocess.run(
                        ['/usr/bin/python3',
                         '/home/omar/code_workspace/Pi-Somfy/operateShutters.py',
                         '-c',
                         '/home/omar/code_workspace/Pi-Somfy/operateShutters.conf',
                         'garage',
                         '-u'
                         ]
                    )

httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
