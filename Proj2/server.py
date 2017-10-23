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
access_granted = 0

class WSHandler(tornado.websocket.WebSocketHandler):
	
	def open(self):
		print ('new connection')
      
	def on_message(self, message):	
		global access_granted
		now = d.datetime.now()
		print ('message received:  ' + message)
		# Reverse Message and send it back
		if len(message) > 2:
			com,un,pw = message.split(' ')
			print(com,un,pw)
			if (com == "li" and un =="a" and pw == "b"):
				print("Main - ",access_granted)
				access_granted = 1
				self.write_message("OK")
			else:
				self.write_message("IU")
			return

		print ('sending back message: ' + message)
		self.write_message(message + " " + str(parsedata(message)) +" "+str(now.date())+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second))

	def on_close(self):
		print ('connection closed')

	def check_origin(self, origin):
		return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
def parsedata(data):	
	global access_granted
	print("AG - ",access_granted)
	if access_granted:
		
		with open('Weather_Data.csv','r') as csvfile:
			deq=deque(csv.reader(csvfile),1)
		
		for sub_list in deq:
			ch,ct,ah,at,mh,mt,ih,it = sub_list
		for i in range(0,8):
			if (sub_list[i] == "0"):
				if i == 7:
					return "sd"		
			else:
				print(sub_list[i],i)
				break
				
	
		if data == "ct":
			return ct
		elif data == "ch":
			return ch
		elif data == "at":
			return at
		elif data == "ah":
			return ah
		elif data == "mt":
			return mt
		elif data == "mh":
			return mh
		elif data == "it":
			return it
		elif data == "ih":
			return ih
		elif data == "lo":
			access_granted = 0
			return "Logged_Out"
		else:
			return "invalid_command" 
	else:
		return "Not_Granted"






if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
