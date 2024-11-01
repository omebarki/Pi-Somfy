from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/g?password=password":
            print(self.path)
            subprocess.run(
                ['/usr/bin/python3',
                 '/home/omar/code_workspace/Pi-Somfy/operateShutters.py',
                 '-c',
                 '/home/omar/code_workspace/Pi-Somfy/operateShutters.conf',
                 'garage',
                 '-u'
                 ]
            )
        self.wfile.write(b'OK!')


httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
