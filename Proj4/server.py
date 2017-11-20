import sys
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import csv
import time
import datetime as d
from twisted.internet import defer
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log

import txthings.resource as resource
import txthings.coap as coap
from threading import Thread

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
		self.write_message(message + " " + parsedata(message))

	def on_close(self):
		print ('connection closed')

	def check_origin(self, origin):
		return True
 
#defining application for websockets and hosting images
application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r"/(Weather_data.jpg)", tornado.web.StaticFileHandler, {'path':'./'})
])


class BlockResource (resource.CoAPResource):
    def __init__(self):
        resource.CoAPResource.__init__(self)
        self.visible = True

    def render_GET(self, request):
        print 'Get Payload' + request.payload

        payload="Gaurav Gandhi"
        response = coap.Message(code=coap.CONTENT, payload=payload)
        return defer.succeed(response)

    def render_PUT(self, request):
        print 'PUT payload: ' + request.payload
        payload = "Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much."
        response = coap.Message(code=coap.CHANGED, payload=payload)
        return defer.succeed(response)


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
    log.startLogging(sys.stdout)
    root = resource.CoAPResource()

    block = BlockResource()
    root.putChild('block', block)

    endpoint = resource.Endpoint(root)
    reactor.listenUDP(coap.COAP_PORT, coap.Coap(endpoint)) #, interface="::")
    Thread(target=reactor.run, args=(False,)).start()

    http_server = tornado.httpserver.HTTPServer(application, )
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
