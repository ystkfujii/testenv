from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import cookies

import ssl

class RequestHandler(SimpleHTTPRequestHandler, object):
	def print_info(self):
		self.log_message("%s %s\n%s", self.command, self.path, self.headers)
	
	def do_GET(self):
		print("aaa")
		#self.print_info()
		"""
		if self.path == "/test":
			self.path = "/dummy_server.py"
		elif self.path == "/test2":
			return
		else:
		"""
		if self.path == "/sleep":
			print("bbb")
			from time import sleep
			self.path = "/"
			sleep(7)
		self.log_message(self.path)
		if self.path == "/location":
			self.send_response(303, self.responses[303][0])
			self.send_header("Location", "/")
			self.end_headers()
			return
		
		if self.path == "/setcookie":
			C = cookies.SimpleCookie()
			C["fig"] = "newton"
			#C["fig"]["path"]="/"
			self.send_response(200, 'OK')
			#self.wfile.write(C.output())
			self.send_header("Content-type", "text/html")
			self.send_header("Set-Cookie", C.output(header='', sep=''))
			self.end_headers()
			self.wfile.write(bytes("PAGE", 'utf-8'))
			self.path = "/"
			#return


		super(RequestHandler, self).do_GET()
	def do_POST(self):
		self.do_GET()

def run(host, port, ctx, handler):
	server = HTTPServer((host, port), handler)
	server.socket = ctx.wrap_socket(server.socket)
	print('Server Starts - %s:%s' % (host, port))
	
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass
	server.server_close()
	print('Server Stops - %s:%s' % (host, port))

if __name__ == '__main__':
	host = 'site.ystk.fj'
	port = 443
	
	ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
	ctx.load_cert_chain('server.crt', keyfile='server.key')
	ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
	#handler = SimpleHTTPRequestHandler
	handler = RequestHandler
	
	#handler.extensions_map['.xls']='text/html;charset=UTF-8'
	run(host, port, ctx, handler)
	
	
	
