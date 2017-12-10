import sys

from twisted.internet.defer import Deferred
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log

import txthings.coap as coap
import txthings.resource as resource

from ipaddress import ip_address
from threading import Thread


class Agent():
    def __init__(self, protocol):
        self.protocol = protocol
        self.requestResource()

    def requestResource(self):
        request = coap.Message(code=coap.GET)
        #Send request to "coap://coap.me:5683/test"
        request.opt.uri_path = ('block',)
        request.opt.observe = 0
        request.remote = (ip_address("10.0.0.241"), coap.COAP_PORT)
        d = protocol.request(request, observeCallback=self.printLaterResponse)
        d.addCallback(self.printResponse)
        d.addErrback(self.noResponse)
        
    def putResource(self):
        payload = "Riders on the storm.\nRiders on the storm.\nInto this house we're born\nInto this world we're thrown"
        request = coap.Message(code=coap.PUT, payload=payload)
        request.opt.uri_path = ("large-update",)
        request.opt.content_format = coap.media_types_rev['text/plain']
        request.remote = (ip_address('198.41.30.241'), coap.COAP_PORT)
        d = protocol.request(request)
        d.addCallback(self.printResponse)

    def printResponse(self, response):
        print 'First result: ' + response.payload
        #reactor.stop()

    def printLaterResponse(self, response):
        print 'Observe result: ' + response.payload

    def noResponse(self, failure):
        print 'Failed to fetch resource:'
        print failure
        #reactor.stop()


log.startLogging(sys.stdout)

endpoint = resource.Endpoint(None)
protocol = coap.Coap(endpoint)

reactor.listenUDP(61616, protocol)#, interface="::")
Thread(target=reactor.run, args=(False,)).start()
client = Agent(protocol)

client.putResource()
