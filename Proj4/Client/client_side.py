# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eid_proj_1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib.pyplot as plt
import time
import datetime as d
import boto3 as bo
import ast
import asyncio
import time
from aiocoap import *
import pika
import threading
import time
import paho.mqtt.client as mqtt

start_time_coap = 0
start_time_amqp = 0
start_time_mqtt = 0
amqp_times = list()
coap_times = list()
mqtt_times = list()

def on_publish(client,obj,mid):
    global start_time_mqtt
    start_time_mqtt = time.time()
    #print("published")

def on_message(client,obj,msg):
    global start_time_mqtt
    global mqtt_times
    elapsed_time = time.time() - start_time_mqtt
    #print(elapsed_time)
    mqtt_times.append(round(elapsed_time,3))
    
class amqp_init:
    def __init__(self):
        self.channel = None
        self.exchange = None
        self.connection = None
        self.queue = None
        self.consume_tag=None
        
    def amqp_on_connection_open(self, unused_connection):
        print("connection opened")
        self.channel=self.connection.channel(on_open_callback=self.amqp_on_channel_open)
        
    def amqp_on_channel_open(self,ch):
        print("channel opened")
        self.exchange = self.channel.exchange_declare(self.amqp_on_exchange_declareok,"eid_exchange",'topic')
        
    def amqp_on_exchange_declareok(self,unused_frame):
        print("exchange declared")
        self.queue= self.channel.queue_declare(self.amqp_on_queue_declareok, 'eid_queue')
        
    def amqp_on_queue_declareok(self,method_frame):
        print("queue declared")
        self.channel.queue_bind(self.amqp_on_bindok, 'eid_queue','eid_exchange', 'example.text')
        
    def amqp_on_bindok(self,unused_frame):
        print("binded with the queue")
        self.consume_tag = self.channel.basic_consume(self.amqp_on_message,'eid_queue')
        
    def establish_conn(self):
        self.connection = pika.SelectConnection(pika.URLParameters('amqp://eid:eid@10.0.0.241:5672'),on_open_callback=self.amqp_on_connection_open,)
        self.connection.ioloop.start()
        
    def publish_string(self,string):
        properties = pika.BasicProperties(app_id='client',content_type='application/json')
        global start_time_amqp
        start_time_amqp= time.time()
        self.channel.basic_publish('eid_exchange','example.text',string,properties)
        
    def amqp_on_message(self, unused_channel, basic_deliver, properties, body):
        global start_time_amqp
        global amqp_times
        if(properties.app_id == 'server'):
            stop_time = time.time()-start_time_amqp
            amqp_times.append(round(stop_time,3))
            #print("stop time: ",stop_time)
            #print(properties.app_id)
            self.channel.basic_ack(basic_deliver.delivery_tag)
            #print("got message: %s", body)


class coap_client():
    async def send(self,message):
        """Perform a single PUT request to localhost on the default port, URI
        "/other/block". The request is sent 2 seconds after initialization.

        The payload is bigger than 1kB, and thus sent as several blocks."""
        global start_time_coap
        global coap_times
        context = await Context.create_client_context()

        #await asyncio.sleep(2)

        payload = message
        start_time_coap = time.time()
        request = Message(code=PUT, payload=payload)
        # These direct assignments are an alternative to setting the URI like in
        # the GET example:
        request.opt.uri_host = '10.0.0.241'
        request.opt.uri_path = ("other", "block")

        response = await context.request(request).response
        end_time = time.time() - start_time_coap
        coap_times.append(round(end_time,3))
 #       print("End time:%d",end_time)
  #      print('Result: %s\n%r'%(response.code, response.payload))

    def main(self,message):
        asyncio.get_event_loop().run_until_complete(self.send(message))


class Ui_Dialog(QtWidgets.QWidget): 
        gl_h,gl_t,curr_position,sample = [0,0,25,0]
        t_mt = str(d.datetime.now())
        t_mh,t_it,t_ih = t_mt,t_mt,t_mt
        message_array=list()
        temp_list = list()
        hum_list = list()
        avg_temp = list()
        avg_hum = list()
        max_temp = list()
        max_hum = list()
        min_temp = list()
        min_hum = list()
        prot_test_msg_array= list()
        coap_client = coap_client()
        amqp_client = amqp_init()
        
        def publish_thread(self):
                global start_time
                self.client = mqtt.Client()
                self.client.connect("10.0.0.241", 1883, 60)
                self.client.subscribe("/EID",0)
                self.client.on_publish = on_publish
                self.client.on_message = on_message
                self.client.loop_start()
        
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.amqp_thread = threading.Thread(target = self.amqp_client.establish_conn,name='amqp_thread')
                self.amqp_thread.start()
                self.mqtt_thread = threading.Thread(target = self.publish_thread,name='mqtt_thread')
                self.mqtt_thread.start()
                
        def setupUi(self, Dialog):
# All the elements in the GUI are represented here including their name, geometry and type
                Dialog.setObjectName("Dialog")
                Dialog.resize(1112, 596)
                self.temperature = QtWidgets.QPushButton(Dialog)
                self.temperature.setGeometry(QtCore.QRect(450, 470, 141, 31))
                self.temperature.setObjectName("temperature")
                self.Plot_Data = QtWidgets.QPushButton(Dialog)
                self.Plot_Data.setGeometry(QtCore.QRect(50, 460, 161, 41))
                self.Plot_Data.setObjectName("Plot_Data")
                self.Test_Protocol = QtWidgets.QPushButton(Dialog)
                self.Test_Protocol.setGeometry(QtCore.QRect(450, 520, 161, 41))
                self.Test_Protocol.setObjectName("TestProtocols")
                self.lineEdit_msg = QtWidgets.QTextEdit(Dialog)
                self.lineEdit_msg.setGeometry(QtCore.QRect(640, 80, 441, 471))
                self.lineEdit_msg.setReadOnly(True)
                self.lineEdit_temp = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_temp.setGeometry(QtCore.QRect(350, 130, 181, 31))
                self.lineEdit_temp.setFrame(True)
                self.lineEdit_temp.setReadOnly(True)
                self.lineEdit_temp.setObjectName("lineEdit_temp")
                self.lineEdit_humid = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_humid.setGeometry(QtCore.QRect(50, 130, 191, 31))
                self.lineEdit_humid.setReadOnly(True)
                self.lineEdit_humid.setObjectName("lineEdit_humid")
                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(250, 340, 151, 31))
                self.label.setObjectName("label")
                self.label_1 = QtWidgets.QLabel(Dialog)
                self.label_1.setGeometry(QtCore.QRect(260, 100, 121, 19))
                self.label_1.setObjectName("label_5")
                self.label_2 = QtWidgets.QLabel(Dialog)
                self.label_2.setGeometry(QtCore.QRect(260, 260, 151, 31))
                self.label_2.setObjectName("label_2")
                self.label_4 = QtWidgets.QLabel(Dialog)
                self.label_4.setGeometry(QtCore.QRect(300, 510, 121, 20))
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(Dialog)
                self.label_5.setGeometry(QtCore.QRect(260, 180, 121, 19))
                self.label_5.setObjectName("label_5")
                self.lineEdit_humid_2 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_humid_2.setGeometry(QtCore.QRect(50, 210, 191, 31))
                self.lineEdit_humid_2.setReadOnly(True)
                self.lineEdit_humid_2.setObjectName("lineEdit_humid_2")
                self.lineEdit_temp_2 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_temp_2.setGeometry(QtCore.QRect(350, 210, 181, 31))
                self.lineEdit_temp_2.setText("")
                self.lineEdit_temp_2.setFrame(True)
                self.lineEdit_temp_2.setReadOnly(True)
                self.lineEdit_temp_2.setObjectName("lineEdit_temp_2")
                self.label_6 = QtWidgets.QLabel(Dialog)
                self.label_6.setGeometry(QtCore.QRect(250, 220, 21, 19))
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(Dialog)
                self.label_7.setGeometry(QtCore.QRect(540, 220, 21, 19))
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(Dialog)
                self.label_8.setGeometry(QtCore.QRect(250, 130, 21, 19))
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(Dialog)
                self.label_9.setGeometry(QtCore.QRect(540, 130, 21, 19))
                self.label_9.setObjectName("label_9")
                self.alarm = QtWidgets.QLineEdit(Dialog)
                self.alarm.setGeometry(QtCore.QRect(280, 470, 151, 31))
                self.alarm.setReadOnly(True)
                self.alarm.setObjectName("alarm")
                self.label_14 = QtWidgets.QLabel(Dialog)
                self.label_14.setGeometry(QtCore.QRect(570, 10, 68, 19))
                self.label_14.setObjectName("label_14")
                self.radioButton = QtWidgets.QRadioButton(Dialog)
                self.radioButton.setGeometry(QtCore.QRect(500, 90, 119, 23))
                self.radioButton.setObjectName("radioButton")
                self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
                self.radioButton_2.setGeometry(QtCore.QRect(540, 90, 119, 23))
                self.radioButton_2.setObjectName("radioButton_2")
                self.lineEdit_humid_4 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_humid_4.setGeometry(QtCore.QRect(50, 290, 191, 31))
                self.lineEdit_humid_4.setReadOnly(True)
                self.lineEdit_humid_4.setObjectName("lineEdit_humid_4")
                self.label_15 = QtWidgets.QLabel(Dialog)
                self.label_15.setGeometry(QtCore.QRect(540, 300, 21, 19))
                self.label_15.setObjectName("label_15")
                self.lineEdit_temp_3 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_temp_3.setGeometry(QtCore.QRect(350, 290, 181, 31))
                self.lineEdit_temp_3.setText("")
                self.lineEdit_temp_3.setFrame(True)
                self.lineEdit_temp_3.setReadOnly(True)
                self.lineEdit_temp_3.setObjectName("lineEdit_temp_3")
                self.label_16 = QtWidgets.QLabel(Dialog)
                self.label_16.setGeometry(QtCore.QRect(250, 300, 21, 19))
                self.label_16.setObjectName("label_16")
                self.lineEdit_humid_5 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_humid_5.setGeometry(QtCore.QRect(50, 380, 191, 31))
                self.lineEdit_humid_5.setReadOnly(True)
                self.lineEdit_humid_5.setObjectName("lineEdit_humid_5")
                self.label_17 = QtWidgets.QLabel(Dialog)
                self.label_17.setGeometry(QtCore.QRect(540, 390, 21, 19))
                self.label_17.setObjectName("label_17")
                self.lineEdit_temp_4 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_temp_4.setGeometry(QtCore.QRect(350, 380, 181, 31))
                self.lineEdit_temp_4.setText("")
                self.lineEdit_temp_4.setFrame(True)
                self.lineEdit_temp_4.setReadOnly(True)
                self.lineEdit_temp_4.setObjectName("lineEdit_temp_4")
                self.label_18 = QtWidgets.QLabel(Dialog)
                self.label_18.setGeometry(QtCore.QRect(250, 390, 21, 19))
                self.label_18.setObjectName("label_18")


#Events generated after button press            
        
                self.retranslateUi(Dialog)
                self.Plot_Data.clicked.connect(self.plot_graph)
                self.temperature.clicked.connect(self.get_sqs_messages)
                self.radioButton.clicked.connect(self.ftoc)
                self.radioButton_2.clicked.connect(self.ctof)
                self.Test_Protocol.clicked.connect(self.test_protocols)


                QtCore.QMetaObject.connectSlotsByName(Dialog)
                self.sqs = bo.resource('sqs')
                self.q = self.sqs.get_queue_by_name(QueueName='message')
                
                

#Initial display test of all the elements
                
        def retranslateUi(self, Dialog):
                self._translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(self._translate("Dialog", "Dialog"))
                self.temperature.setText(self._translate("Dialog", "Get Values"))
                self.Plot_Data.setText(self._translate("Dialog", "Plot Graph"))
                self.Test_Protocol.setText(self._translate("Dialog", "TestProtocols"))
                self.label.setText(self._translate("Dialog", "Maximum Values"))
                self.label_1.setText(self._translate("Dialog", "Current Values"))
                self.label_2.setText(self._translate("Dialog", "Minimum Values"))
                self.label_4.setText(self._translate("Dialog", "Message Display"))
                self.label_5.setText(self._translate("Dialog", "Average Values"))
                self.label_6.setText(self._translate("Dialog", "%"))
                self.label_7.setText(self._translate("Dialog", "C"))
                self.label_8.setText(self._translate("Dialog", "%"))
                self.label_9.setText(self._translate("Dialog", "C"))
                self.radioButton.setText(self._translate("Dialog", "C"))
                self.radioButton_2.setText(self._translate("Dialog", "F"))
                self.label_15.setText(self._translate("Dialog", "C"))
                self.label_16.setText(self._translate("Dialog", "%"))
                self.label_17.setText(self._translate("Dialog", "C"))
                self.label_18.setText(self._translate("Dialog", "%"))

#cleanup code after X is pressed in GUI     
        def closeEvent(self,event):
                print("Sensor Code Terminated")
                self.amqp_thread.join()
# Celcius to Faranheit

        def ctof(self):
                self.label_7.setText(self._translate("Dialog", "F"))
                self.label_9.setText(self._translate("Dialog", "F"))
                self.label_15.setText(self._translate("Dialog", "F"))
                self.label_17.setText(self._translate("Dialog", "F"))
                self.f_flag = 1
                self.c_flag = 0 
                self.lineEdit_temp_2.setText(self._translate("Dialog", '{0:.2f}'.format((self.avg_temp[0]*1.8)+32)))
                self.lineEdit_temp.setText(self._translate("Dialog", '{0:.2f}'.format((self.temp_list[0]*1.8)+32)))             
                self.lineEdit_temp_3.setText(self._translate("Dialog", '{0:.2f}'.format((self.min_temp[0]*1.8)+32)))
                self.lineEdit_temp_4.setText(self._translate("Dialog", '{0:.2f}'.format((self.max_temp[0]*1.8)+32)))

#Faranheit to celcius
        def ftoc(self):
                self.label_7.setText(self._translate("Dialog", "C"))
                self.label_9.setText(self._translate("Dialog", "C"))
                self.label_15.setText(self._translate("Dialog", "C"))
                self.label_17.setText(self._translate("Dialog", "C"))
                self.f_flag = 0
                self.c_flag = 1 
                self.lineEdit_temp_2.setText(self._translate("Dialog", str(self.temp_list[0])))
                self.lineEdit_temp .setText(self._translate("Dialog", str(self.avg_temp[0])))
                self.lineEdit_temp_3.setText(self._translate("Dialog", str(self.min_temp[0])))
                self.lineEdit_temp_4.setText(self._translate("Dialog", str(self.max_temp[0])))
# Timed readings after every 5 seconds, This includes average reading, min max finding

            
# Function to plot graph from the csv file
        def plot_graph(self):
                if(len(self.message_array[0])==0):
                    self.lineEdit_msg.clear()
                    self.lineEdit_msg.setText(self._translate("Dialog", "No data available please refresh"))
                    return;

                now=d.datetime.now()
                title_date = "Date:" + str(now.month)+ '/' + str(now.day)+ '/' + str(now.year)
                title_time = " Time:" +str(now.hour) + ':'+ str(now.minute) + " to " + str(now.hour) + ":" + str((now.minute) -3)
                i = range(0,len(self.temp_list))
                fig1 = plt.figure()
                fig1.suptitle("Temperature Graphs( " +title_date + title_time+ " )")
                fig1.subplots_adjust(hspace=.5)
                ax1 = fig1.add_subplot(221)
                ax1.plot(i,self.temp_list,)
                ax1.set_title('Temperature')
                
                i = range(0,len(self.avg_temp))
                ax2 = fig1.add_subplot(222)
                ax2.plot(i,self.avg_temp,'r-')
                ax2.set_title('Average Temperature')
                
                i = range(0,len(self.max_temp))
                ax3 = fig1.add_subplot(223)
                ax3.plot(i,self.max_temp,'m-')
                ax3.set_title('Max Temperature')
                
                i = range(0,len(self.min_temp))
                ax3 = fig1.add_subplot(224)
                ax3.plot(i,self.min_temp,'g-')
                ax3.set_title('Min Temperature')
                
                fig1.show()

                i = range(0,len(self.hum_list))
                fig2 = plt.figure()
                fig2.suptitle("Humidity Graphs( " + title_date+ title_time+ ")")
                fig2.subplots_adjust(hspace=.5)
                ax1 = fig2.add_subplot(221)
                ax1.plot(i,self.hum_list,)
                ax1.set_title('Humidity')
                
                i = range(0,len(self.avg_hum))
                ax2 = fig2.add_subplot(222)
                ax2.plot(i,self.avg_hum,'r-')
                ax2.set_title('Average Humidity')
                
                i = range(0,len(self.max_hum))
                ax3 = fig2.add_subplot(223)
                ax3.plot(i,self.max_hum,'m-')
                ax3.set_title('Max Humidity')
                
                i = range(0,len(self.min_hum))
                ax3 = fig2.add_subplot(224)
                ax3.plot(i,self.min_hum,'g-')
                ax3.set_title('Min Humidity')
                
                fig2.show()
                #fig.savefig('Weather_data.jpg')

        def set_prg(self):
                self.curr_position = self.AlarmControl.value()
                if(self.curr_position < self.gl_t):
                        #self.temp_progress.setMaximum(self.gl_t)
                        self.alarm.setText(self._translate("Dialog", "Temp Alarm"))                     
                else:
                        #self.temp_progress.setMaximum(self.curr_position)
                        self.alarm.setText(self._translate("Dialog", "Safe"))   
                
        #function to get 30 messages  from the SQS queue        
        def get_sqs_messages(self):
                message_box_string = ''
                count = 0
                self.lineEdit_msg.clear()
                self.message_array = list()
                self.temp_list= list()
                self.hum_list=list()
                self.avg_temp=list()
                self.avg_hum=list()
                self.max_temp=list()
                self.max_hum=list()
                self.min_temp=list()
                self.min_hum=list()
                self.prot_test_msg_array = list()
                for i in range(0,3):
                        self.message_array.append(self.q.receive_messages(MaxNumberOfMessages=10))#query upto 10 messages
                        print(len(self.message_array[i]))
                        count = count + len(self.message_array[i])
                        if(len(self.message_array[i])==0):
                            self.lineEdit_msg.setText(self._translate("Dialog", "message queue exausted"))
                            return;
                        for j in range(0,len(self.message_array[i])):
                            message = self.message_array[i][j]
                            self.prot_test_msg_array.append(message.body)
                            message_box_string = message_box_string + message.body
                            message_box_string = message_box_string + '\n\n'
                            values = ast.literal_eval(message.body)
                            message.delete()
                            self.temp_list.append(values['temp'])
                            self.hum_list.append(values['humidity'])
                            self.avg_temp.append(round(values['avg_temp'],2))
                            self.avg_hum.append(round(values['avg_humidity'],2))
                            self.max_temp.append(values['max_temp'])
                            self.max_hum.append(values['max_humidity'])
                            self.min_temp.append(values['min_temp'])
                            self.min_hum.append(values['min_humidity'])
                        time.sleep(0.01)
                message_box_string = message_box_string +"Fetched " +str(count)+ " messages"
                self.lineEdit_msg.setText(self._translate("Dialog", message_box_string))
                self.lineEdit_temp_2.setText(self._translate("Dialog", str(self.avg_temp[0])))
                self.lineEdit_temp .setText(self._translate("Dialog", str(self.temp_list[0])))
                self.lineEdit_temp_3.setText(self._translate("Dialog",str(self.min_temp[0]) ))
                self.lineEdit_temp_4.setText(self._translate("Dialog", str(self.max_temp[0])))
                self.lineEdit_humid.setText(self._translate("Dialog", str(self.hum_list[0])))
                self.lineEdit_humid_2.setText(self._translate("Dialog", str(self.avg_hum[0])))
                self.lineEdit_humid_4.setText(self._translate("Dialog", str(self.min_hum[0])))
                self.lineEdit_humid_5.setText(self._translate("Dialog", str(self.max_hum[0])))

        def test_protocols(self):
                global coap_times
                global amqp_times
                global mqtt_times
                coap_times = list()
                amqp_times = list()
                mqtt_times = list()
                for i in range(0,len(self.prot_test_msg_array)):
                    bytes = str.encode(self.prot_test_msg_array[i])
                    self.coap_client.main(bytes)
                print(coap_times)
                for i in range(0,len(self.prot_test_msg_array)):
                    bytes = str.encode(self.prot_test_msg_array[i])
                    self.amqp_client.publish_string(bytes)
                    time.sleep(0.1)
                print(amqp_times)
                for i in range(0,len(self.prot_test_msg_array)):
                    bytes = str.encode(self.prot_test_msg_array[i])
                    self.client.publish('/EID',bytes)
                    time.sleep(0.1)
                print(mqtt_times)

if __name__ == '__main__':
        
        app = QtWidgets.QApplication(sys.argv)
        ex = Ui_Dialog();
        ex.show();
        sys.exit(app.exec_())


    


