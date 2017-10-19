import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import csv
from collections import deque
'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
      
    def on_message(self, message):
        print ('message received:  ' + message)
        # Reverse Message and send it back
        print ('sending back message: ' + message)
        self.write_message(message + " " + str(parsedata(message)))
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
def parsedata(data):	
	with open('Weather_Data.csv','r') as csvfile:
		deq=deque(csv.reader(csvfile),1)
	
	for sub_list in deq:
		ch,ct,ah,at = sub_list

	if data == "ct":
		return ct
	elif data == "ch":
		return ch
	elif data == "at":
		return at
	elif data == "ah":
		return ah
	elif data == "mt":
		return 70
	elif data == "mh":
		return 80
	elif data == "it":
		return 90
	elif data == "ih":
		return 100
	else:
		return 110


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
