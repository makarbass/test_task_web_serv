#! /usr/bin/env python3
import http.server
import webbrowser

PORT = 8000
script_path = "index.html"

server_class = http.server.HTTPServer
handler_class = http.server.CGIHTTPRequestHandler
server_address = ("", PORT)
httpd = server_class(server_address, handler_class)
url = 'http://localhost:{0}/{1}'.format(PORT, script_path)
webbrowser.open_new_tab(url)
print("serving at", url)
httpd.serve_forever()
