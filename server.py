#!/usr/bin/env python
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import wave
import time

connections = []

		
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")		
		
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("client connected")
        #Add the connection to the list of connections
        connections.append(self)
    def on_message(self, message):
        #Check if message is Binary or Text
        if type(message) == str:
			pass
        else:
            print(message)
            self.write_message('ok')
    def on_close(self):
        #Remove the connection from the list of connections
        connections.remove(self)
        print("client disconnected")

class NCCOHandler(tornado.web.RequestHandler):
    def get(self):
        with open("ncco.json", 'r') as f:
            ncco = f.read()
        self.write(ncco)
        self.set_header("Content-Type", 'application/json')
        self.finish()

class EventHandler(tornado.web.RequestHandler):
    def post(self):
		print self.request.body
		self.write('ok')
		self.set_header("Content-Type", 'text/plain')
		self.finish()
	
class SoundHandler(tornado.websocket.WebSocketHandler):
	    def open(self):
	        print("client connected")
	    def on_message(self, message):
			print message
			data = message
			fn = 'audio/{}.wav'.format(data)
			f = wave.open(fn)
			lgth = f.getnframes()
			while f.tell() < lgth:
				data = f.readframes(320)
				for c in connections:
					c.write_message(data, binary=True)
					time.sleep(0.018)
	    def on_close(self):
	        print("client disconnected")
		
		
		
		
		
		
application = tornado.web.Application([(r'/', MainHandler),
										(r'/socket', WSHandler),
										(r'/event', EventHandler),
										(r'/browser', SoundHandler),
                                        (r'/ncco', NCCOHandler)])
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()