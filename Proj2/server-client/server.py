import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import csv
import time
import datetime as d

from collections import deque
'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
#variable for checking if a client is authenticated
access_granted = 0

#Handler for websocket events
class WSHandler(tornado.websocket.WebSocketHandler):
	
	def open(self):
		print ('new connection')
      #function to handle event messages
	def on_message(self, message):	
		print ('message received:  ' + message)
		# Reverse Message and send it back

		self.write_message(message)

	def on_close(self):
		print ('connection closed')

	def check_origin(self, origin):
		return True
 
#defining application for websockets and hosting images
application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r"/(Weather_data.jpg)", tornado.web.StaticFileHandler, {'path':'./'})
])
 
#function to parse data for the client
def parsedata(data):	
	global access_granted
	print("AG - ",access_granted)
	if access_granted:
		
		with open('Weather_Data.csv','r') as csvfile:
			deq=deque(csv.reader(csvfile),1)
		
		for sub_list in deq:
			ch,ct,ah,at,curr_t,mh,mh_time,mt,mt_time,ih,ih_time,it,it_time = sub_list
		for i in range(0,13):
			if (sub_list[i] == "0"):
				if i == 12:
					return "sd"		
			else:
				#print(sub_list[i],i)
				break
				
	
		if data == "ct":
			return (ct + " " + curr_t)
		elif data == "ch":
			return (ch + " " + curr_t)
		elif data == "at":
			return (at+ " " + curr_t)
		elif data == "ah":
			return (ah + " " + curr_t)
		elif data == "mt":
			return (mt+ " " + mt_time)
		elif data == "mh":
			return (mh + " " + mh_time)
		elif data == "it":
			return (it+ " " + it_time)
		elif data == "ih":
			return (ih + " " + ih_time)
		elif data == "lo":
			access_granted = 0
			return "Logged_Out"
		else:
			return "invalid_command" 
	else:
		return "Not_Granted"





#main loop to run the server and listen for requests continuously
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
