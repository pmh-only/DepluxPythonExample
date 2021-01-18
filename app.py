from http.server import BaseHTTPRequestHandler, HTTPServer

to_ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

class Handler (BaseHTTPRequestHandler):
  count = 0
  def do_GET(self):
    Handler.count += 1
    self.send_response(200)
    self.send_header("Content-type", "text/html; charset=UTF-8")
    self.end_headers()
    self.wfile.write(bytes("Hello, world! you're %s visitor!" % to_ordinal(self.count), "utf-8"))

addr = ('0.0.0.0', 80)
httpd = HTTPServer(addr, Handler)
httpd.serve_forever()
