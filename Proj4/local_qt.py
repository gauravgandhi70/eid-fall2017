# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eid_proj_1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT as ad
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime as d
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import argparse
import threading
import paho.mqtt.client as mqtt
import asyncio

import aiocoap.resource as resource
import aiocoap
import pika

start_time = 0

class Ui_Dialog(QtWidgets.QWidget): 
	gl_h,gl_t,curr_position,sample = [0,0,25,0]
	f_flag,c_flag = [0,1]
	avg_t, avg_h = [0,0]
	h_min,t_min = ad.read_retry(22,4)
	t_max,h_max = t_min,h_min
	t_mt = str(d.datetime.now())
	t_mh,t_it,t_ih = t_mt,t_mt,t_mt
	myAWSIoTMQTTClient = None

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.mqttSetup()
	def mqttSetup(self):
		self.myAWSIoTMQTTClient = AWSIoTMQTTClient("clientId")
		self.myAWSIoTMQTTClient.configureEndpoint("a2lybklkk15nvm.iot.us-west-2.amazonaws.com", 8883)
		self.myAWSIoTMQTTClient.configureCredentials("root-CA.crt","Pi-Server.private.key", "Pi-Server.cert.pem")
		
		self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
		self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
		self.myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
		self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
		self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
		
		self.myAWSIoTMQTTClient.connect()
		self.myAWSIoTMQTTClient.subscribe('eid_proj3', 1, None)
		
            
	def setupUi(self, Dialog):
# All the elements in the GUI are represented here including their name, geometry and type
		self.sample_freq = QtCore.QTimer(self)
		self.sample_freq.timeout.connect(self.timeout_isr)
		Dialog.setObjectName("Dialog")
		Dialog.resize(696, 593)
		self.temperature = QtWidgets.QPushButton(Dialog)
		self.temperature.setGeometry(QtCore.QRect(400, 60, 112, 34))
		self.temperature.setObjectName("temperature")
		self.humidity = QtWidgets.QPushButton(Dialog)
		self.humidity.setGeometry(QtCore.QRect(110, 60, 112, 34))
		self.humidity.setObjectName("humidity")
		self.Plot_Data = QtWidgets.QPushButton(Dialog)
		self.Plot_Data.setGeometry(QtCore.QRect(50, 460, 161, 41))
		self.Plot_Data.setObjectName("Plot_Data")
		self.lineEdit_temp = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_temp.setGeometry(QtCore.QRect(350, 130, 181, 31))
		self.lineEdit_temp.setFrame(True)
		self.lineEdit_temp.setReadOnly(True)
		self.lineEdit_temp.setObjectName("lineEdit_temp")
		self.lineEdit_humid = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_humid.setGeometry(QtCore.QRect(50, 130, 191, 31))
		self.lineEdit_humid.setReadOnly(True)
		self.lineEdit_humid.setObjectName("lineEdit_humid")
		self.AlarmControl = QtWidgets.QDial(Dialog)
		self.AlarmControl.setGeometry(QtCore.QRect(490, 450, 50, 64))
		self.AlarmControl.setSliderPosition(25)
		self.AlarmControl.setObjectName("AlarmControl")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(250, 340, 151, 31))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(260, 260, 151, 31))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(Dialog)
		self.label_3.setGeometry(QtCore.QRect(500, 510, 141, 31))
		self.label_3.setObjectName("label_3")
		self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
		self.lcdNumber.setGeometry(QtCore.QRect(570, 450, 71, 51))
		self.lcdNumber.setAutoFillBackground(False)
		self.lcdNumber.setProperty("intValue", 25)
		self.lcdNumber.setObjectName("lcdNumber")
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
		self.label_10 = QtWidgets.QLabel(Dialog)
		self.label_10.setGeometry(QtCore.QRect(260, 10, 68, 19))
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(Dialog)
		self.label_11.setGeometry(QtCore.QRect(40, 10, 131, 21))
		self.label_11.setObjectName("label_11")
		self.label_12 = QtWidgets.QLabel(Dialog)
		self.label_12.setGeometry(QtCore.QRect(380, 10, 68, 19))
		self.label_12.setObjectName("label_12")
		self.label_13 = QtWidgets.QLabel(Dialog)
		self.label_13.setGeometry(QtCore.QRect(490, 10, 68, 19))
		self.label_13.setObjectName("label_13")
		self.label_14 = QtWidgets.QLabel(Dialog)
		self.label_14.setGeometry(QtCore.QRect(570, 10, 68, 19))
		self.label_14.setObjectName("label_14")
		self.radioButton = QtWidgets.QRadioButton(Dialog)
		self.radioButton.setGeometry(QtCore.QRect(540, 50, 119, 23))
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
		self.curr_hum_time = QtWidgets.QLabel(Dialog)
		self.curr_hum_time.setGeometry(QtCore.QRect(90, 170, 161, 21))
		self.curr_hum_time.setObjectName("curr_hum_time")
		self.min_hum_time = QtWidgets.QLabel(Dialog)
		self.min_hum_time.setGeometry(QtCore.QRect(80, 330, 151, 21))
		self.min_hum_time.setObjectName("min_hum_time")
		self.min_temp_time = QtWidgets.QLabel(Dialog)
		self.min_temp_time.setGeometry(QtCore.QRect(380, 330, 161, 21))
		self.min_temp_time.setObjectName("min_temp_time")
		self.max_hum_time = QtWidgets.QLabel(Dialog)
		self.max_hum_time.setGeometry(QtCore.QRect(80, 420, 161, 21))
		self.max_hum_time.setObjectName("max_hum_time")
		self.max_temp_time = QtWidgets.QLabel(Dialog)
		self.max_temp_time.setGeometry(QtCore.QRect(380, 420, 161, 21))
		self.max_temp_time.setObjectName("max_temp_time")
		self.curr_temp_time = QtWidgets.QLabel(Dialog)
		self.curr_temp_time.setGeometry(QtCore.QRect(380, 170, 161, 21))
		self.curr_temp_time.setObjectName("curr_temp_time")
		self.avg_hum_time = QtWidgets.QLabel(Dialog)
		self.avg_hum_time.setGeometry(QtCore.QRect(90, 250, 161, 21))
		self.avg_hum_time.setObjectName("avg_hum_time")
		self.avg_temp_time = QtWidgets.QLabel(Dialog)
		self.avg_temp_time.setGeometry(QtCore.QRect(380, 250, 161, 21))
		self.avg_temp_time.setObjectName("avg_temp_time")
		
		
		self.Hour_disp = QtWidgets.QLCDNumber(Dialog)
		self.Hour_disp.setGeometry(QtCore.QRect(190, 10, 64, 23))
		self.Hour_disp.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.Hour_disp.setSmallDecimalPoint(False)
		self.Hour_disp.setDigitCount(2)
		self.Hour_disp.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
		self.Hour_disp.setObjectName("Hour_disp")
		
		self.Min_lcd = QtWidgets.QLCDNumber(Dialog)
		self.Min_lcd.setGeometry(QtCore.QRect(280, 10, 64, 23))
		self.Min_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.Min_lcd.setDigitCount(2)
		self.Min_lcd.setObjectName("Min_lcd")
		
		self.date = QtWidgets.QLCDNumber(Dialog)
		self.date.setGeometry(QtCore.QRect(420,10,64,23))
		self.date.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.date.setDigitCount(2)
		self.date.setObjectName("date")
				
		self.month = QtWidgets.QLCDNumber(Dialog)
		self.month.setGeometry(QtCore.QRect(490, 10, 64, 23))
		self.month.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.month.setDigitCount(2)
		self.month.setObjectName("month")
		#Events generated after button press 		
		
		self.sample_freq.start(5000)
		
		self.retranslateUi(Dialog)
		self.Plot_Data.clicked.connect(self.plot_graph)
		self.temperature.clicked.connect(self.query_temp)
		self.humidity.clicked.connect(self.query_humidity)	        
		self.AlarmControl.sliderMoved['int'].connect(self.set_prg)
		self.AlarmControl.valueChanged['int'].connect(self.lcdNumber.display)
		self.radioButton.clicked.connect(self.ftoc)
		self.radioButton_2.clicked.connect(self.ctof)
		
		
		
		QtCore.QMetaObject.connectSlotsByName(Dialog)

#Initial display test of all the elements
		
	def retranslateUi(self, Dialog):
		self._translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(self._translate("Dialog", "Dialog"))
		self.temperature.setText(self._translate("Dialog", "Get Temp"))
		self.humidity.setText(self._translate("Dialog", "Get Humidity"))
		self.Plot_Data.setText(self._translate("Dialog", "Plot Graph"))
		self.label.setText(self._translate("Dialog", "Maximum Values"))
		self.label_2.setText(self._translate("Dialog", "Minimum Values"))
		self.label_3.setText(self._translate("Dialog", "Set Alarm Trigger"))
		self.label_4.setText(self._translate("Dialog", "Message Display"))
		self.label_5.setText(self._translate("Dialog", "Average Values"))
		self.label_6.setText(self._translate("Dialog", "%"))
		self.label_7.setText(self._translate("Dialog", "C"))
		self.label_8.setText(self._translate("Dialog", "%"))
		self.label_9.setText(self._translate("Dialog", "C"))
		self.label_10.setText(self._translate("Dialog", ":"))
		self.label_11.setText(self._translate("Dialog", "Data Requested at"))
		self.label_12.setText(self._translate("Dialog", "on"))
		self.label_13.setText(self._translate("Dialog", "/"))
		self.radioButton.setText(self._translate("Dialog", "C"))
		self.radioButton_2.setText(self._translate("Dialog", "F"))
		self.label_15.setText(self._translate("Dialog", "C"))
		self.label_16.setText(self._translate("Dialog", "%"))
		self.label_17.setText(self._translate("Dialog", "C"))
		self.label_18.setText(self._translate("Dialog", "%"))
		t = d.datetime.now()
		self.curr_hum_time.setText(self._translate("Dialog", str(t.time())))
		self.min_hum_time.setText(self._translate("Dialog", str(t.time())))
		self.min_temp_time.setText(self._translate("Dialog", str(t.time())))
		self.max_hum_time.setText(self._translate("Dialog", str(t.time())))
		self.max_temp_time.setText(self._translate("Dialog", str(t.time())))
		self.curr_temp_time.setText(self._translate("Dialog", str(t.time())))
		self.avg_hum_time.setText(self._translate("Dialog", str(t.time())))
		self.avg_temp_time.setText(self._translate("Dialog", str(t.time())))
		
		
		
		now = (d.datetime.now())
		self.date.display(now.day)
		self.month.display(now.month)
#cleanup code after X is pressed in GUI	    
	def closeEvent(self,event):
		print("Sensor Code Terminated")
		with open('Weather_Data.csv', 'a') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow([0,0,0,0,0,0,0,0,0,0,0,0,0])
# Celcius to Faranheit

	def ctof(self):
		self.label_7.setText(self._translate("Dialog", "F"))
		self.label_9.setText(self._translate("Dialog", "F"))
		self.f_flag = 1
		self.c_flag = 0	
		self.lineEdit_temp_2.setText(self._translate("Dialog", '{0:.2f}'.format((self.avg_t*1.8)+32)))
		self.lineEdit_temp.setText(self._translate("Dialog", '{0:.2f}'.format((self.gl_t*1.8)+32)))		
		self.lineEdit_temp_3.setText(self._translate("Dialog", '{0:.2f}'.format((self.t_min*1.8)+32)))
		self.lineEdit_temp_4.setText(self._translate("Dialog", '{0:.2f}'.format((self.t_min*1.8)+32)))

#Faranheit to celcius
	def ftoc(self):
		self.label_7.setText(self._translate("Dialog", "C"))
		self.label_9.setText(self._translate("Dialog", "C"))
		self.f_flag = 0
		self.c_flag = 1	
		self.lineEdit_temp_2.setText(self._translate("Dialog", '{0:.2f}'.format(self.avg_t)))
		self.lineEdit_temp .setText(self._translate("Dialog", '{0:.2f}'.format(self.gl_t)))
		self.lineEdit_temp_3.setText(self._translate("Dialog", '{0:.2f}'.format(self.t_min)))
		self.lineEdit_temp_4.setText(self._translate("Dialog", '{0:.2f}'.format(self.t_min)))
# Timed readings after every 5 seconds, This includes average reading, min max finding

	def timeout_isr(self):
		self.sample = self.sample + 1
		humidity,temp = ad.read_retry(22,4)
		
		self.gl_t = temp
		now = str(d.datetime.now())
		t = d.datetime.now()
		if(temp != None  or humidity != None):
			
			self.myAWSIoTMQTTClient.publish("eid_proj3", '{ "count":' +str(self.sample) +', "temp":' + '{0:.2f}'.format(temp) +  ', "humidity":' + '{0:.2f}'.format(humidity) + ' }', 1)


			if humidity>self.h_max and humidity<100:
				self.h_max = humidity
				self.t_mh = now
				self.max_hum_time.setText(self._translate("Dialog", str(t.time())))

			elif humidity<self.h_min:
				self.h_min = humidity
				self.t_ih = humidity
				self.min_hum_time.setText(self._translate("Dialog", str(t.time())))
		
			if temp > self.t_max:
				self.t_max = temp
				self.t_mt = now
				self.max_temp_time.setText(self._translate("Dialog", str(t.time())))

			elif temp < self.t_min:	
				self.t_min = temp
				self.t_it = now
				self.min_temp_time.setText(self._translate("Dialog", str(t.time())))	

			self.curr_temp_time.setText(self._translate("Dialog", str(t.time())))
			self.curr_hum_time.setText(self._translate("Dialog", str(t.time())))
			self.avg_hum_time.setText(self._translate("Dialog", str(t.time())))
			self.avg_temp_time.setText(self._translate("Dialog", str(t.time())))

			self.avg_t = ((self.avg_t  * (self.sample-1))+ temp)/self.sample	
			self.avg_h = ((self.avg_h  * (self.sample-1))+ humidity)/self.sample
			if self.c_flag:
				self.lineEdit_temp_2.setText(self._translate("Dialog", '{0:.2f}'.format(self.avg_t)))
				self.lineEdit_humid_2.setText(self._translate("Dialog", '{0:.2f}'.format(self.avg_h)))
				self.lineEdit_temp.setText(self._translate("Dialog", '{0:.2f}'.format(temp)))
				self.lineEdit_humid.setText(self._translate("Dialog", '{0:.2f}'.format(humidity)))
				self.lineEdit_temp_3.setText(self._translate("Dialog", '{0:.2f}'.format(self.t_min)))
				self.lineEdit_humid_4.setText(self._translate("Dialog", '{0:.2f}'.format(self.h_min)))
				self.lineEdit_temp_4.setText(self._translate("Dialog", '{0:.2f}'.format(self.t_max)))
				self.lineEdit_humid_5.setText(self._translate("Dialog", '{0:.2f}'.format(self.h_max)))

				
			else:
				self.lineEdit_temp_2.setText(self._translate("Dialog", '{0:.2f}'.format((self.avg_t*1.8)+32)))
				self.lineEdit_humid_2.setText(self._translate("Dialog", '{0:.2f}'.format(self.avg_h)))
				self.lineEdit_temp.setText(self._translate("Dialog", '{0:.2f}'.format((temp*1.8)+32)))
				self.lineEdit_humid.setText(self._translate("Dialog", '{0:.2f}'.format(humidity)))
				self.lineEdit_temp_3.setText(self._translate("Dialog", '{0:.2f}'.format((self.t_min*1.8)+32)))
				self.lineEdit_humid_4.setText(self._translate("Dialog", '{0:.2f}'.format(self.h_min)))
				self.lineEdit_temp_4.setText(self._translate("Dialog", '{0:.2f}'.format((self.t_max*1.8)+32)))
				self.lineEdit_humid_5.setText(self._translate("Dialog", '{0:.2f}'.format(self.h_max)))
				
	
			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([str(humidity),str(temp),str(self.avg_h),str(self.avg_t),now,str(self.h_max),self.t_mh,str(self.t_max),self.t_mt,str(self.h_min),self.t_ih,str(self.t_min),self.t_it])
		else:
			self.lineEdit_temp_2.setText(self._translate("Dialog","Sensor Disconnected"))
			self.lineEdit_humid_2.setText(self._translate("Dialog", "Sensor Disconnected"))
			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([0,0,0,0,0,0,0,0,0,0,0,0,0])
	
# function to process event generated by get temp button press
	def query_temp(self):
		
		humidity, temp = ad.read_retry(22,4)
		now = str(d.datetime.now())
		if(temp == None):
			self.lineEdit_temp.setText(self._translate("Dialog", "Sensor Disconnected"))
			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([0,0,0,0,0,0,0,0,0,0,0,0,0])
		else:	
			if humidity>self.h_max:
				self.h_max = humidity
			elif humidity<self.h_min:
				self.h_min = humidity

			if temp > self.t_max:
				self.t_max = temp
			elif temp < self.t_min:	
				self.t_min = temp

			self.sample = self.sample + 1
			self.gl_h,self.gl_t = humidity, temp
			self.avg_t = ((self.avg_t  * (self.sample-1))+ temp)/self.sample	
			self.avg_h = ((self.avg_h  * (self.sample-1))+ humidity)/self.sample
			
			humidity_string = '{0:.2f}'.format(humidity)
			temp_string = '{0:.2f}'.format(temp)
			print("Temp - ",temp_string)
			if self.c_flag:
				self.lineEdit_temp.setText(self._translate("Dialog", temp_string))
			else: 
				self.lineEdit_temp.setText(self._translate("Dialog", '{0:.2f}'.format((self.gl_t*1.8)+32)))
			#self.temp_progress.setValue(temp)
			if(temp > self.curr_position):
				#self.temp_progress.setMaximum(temp)
				self.alarm.setText(self._translate("Dialog", "Temp Alarm"))
			else:
				#self.temp_progress.setMaximum(self.curr_position+1)
				self.alarm.setText(self._translate("Dialog", "Safe"))	

			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([str(humidity),str(temp),str(self.avg_h),str(self.avg_t),now,str(self.h_max),self.t_mh,str(self.t_max),self.t_mt,str(self.h_min),self.t_ih,str(self.t_min),self.t_it])

# function to process event generated by get humidity button press
	def query_humidity(self):
		humidity, temp = ad.read_retry(22,4)
		now = str(d.datetime.now())
		if(humidity == None):
			self.lineEdit_humid.setText(self._translate("Dialog", "Sensor Disconnected"))
			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([0,0,0,0,0,0,0,0,0,0,0,0,0])

		else:	
			if humidity>self.h_max:
				self.h_max = humidity
			elif humidity<self.h_min:
				self.h_min = humidity

			if temp > self.t_max:
				self.t_max = temp
			elif temp < self.t_min:	
				self.t_min = temp

			self.sample = self.sample + 1
			self.gl_h,self.gl_t = humidity, temp
			self.avg_t = ((self.avg_t  * (self.sample-1))+ temp)/self.sample	
			self.avg_h = ((self.avg_h  * (self.sample-1))+ humidity)/self.sample
			humidity_string = '{0:.2f}'.format(humidity)
			temp_string = '{0:.2f}'.format(temp)
			print("Humidity - ",humidity_string)
			self.lineEdit_humid.setText(self._translate("Dialog", humidity_string))
			#self.humid_progress.setValue(humidity)
			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([humidity_string,temp_string,'{0:.2f}'.format(self.avg_h),'{0:.2f}'.format(self.avg_t),'{0:.2f}'.format(self.h_max),'{0:.2f}'.format(self.t_max),'{0:.2f}'.format(self.h_min),'{0:.2f}'.format(self.t_min)])

# Function to plot graph from the csv file
	def plot_graph(self):
		x = []
		y = []
		with open('Weather_Data.csv','r') as csvfile:
			plots = csv.reader(csvfile, delimiter=',')
			for row in plots:
				x.append(float(row[0]))
				y.append(float(row[1]))

		i = range(0,len(x))
		fig = plt.figure()
		fig.subplots_adjust(hspace=.5)
		ax1 = fig.add_subplot(211)
		ax1.plot(i,x,)
		ax1.set_title('Humidity')
		
		ax2 = fig.add_subplot(212)
		ax2.plot(i,y,'r-')
		ax2.set_title('Temperature')
		
		fig.show()
		fig.savefig('Weather_data.jpg')

	def set_prg(self):
		self.curr_position = self.AlarmControl.value()
		if(self.curr_position < self.gl_t):
			#self.temp_progress.setMaximum(self.gl_t)
			self.alarm.setText(self._translate("Dialog", "Temp Alarm"))			
		else:
			#self.temp_progress.setMaximum(self.curr_position)
			self.alarm.setText(self._translate("Dialog", "Safe"))
    
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))
    
def on_message(mqttc, obj, msg):
    mqttc.publish("/EID",str(msg.payload))
    
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

def mqtt_connection_thread():
    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe
    mqttc.connect("10.0.0.241", 1883, 60)
    mqttc.subscribe("/EID", 0)
    
    mqttc.loop_forever()
    
class BlockResource(resource.Resource):
    """Example resource which supports the GET and PUT methods. It sends large
    responses, which trigger blockwise transfer."""

    def __init__(self):
        super().__init__()

    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)

    async def render_put(self, request):
        print('PUT payload: %s' % request.payload)
        return aiocoap.Message(code=aiocoap.CHANGED, payload=request.payload)


class SeparateLargeResource(resource.Resource):
    """Example resource which supports the GET method. It uses asyncio.sleep to
    simulate a long-running operation, and thus forces the protocol to send
    empty ACK first. """

    def get_link_description(self):
        # Publish additional data in .well-known/core
        return dict(**super().get_link_description(), title="A large resource")

    async def render_get(self, request):
        await asyncio.sleep(3)

        payload = "Three rings for the elven kings under the sky, seven rings "\
                "for dwarven lords in their halls of stone, nine rings for "\
                "mortal men doomed to die, one ring for the dark lord on his "\
                "dark throne.".encode('ascii')
        return aiocoap.Message(payload=payload)

class TimeResource(resource.ObservableResource):
    """Example resource that can be observed. The `notify` method keeps
    scheduling itself, and calles `update_state` to trigger sending
    notifications."""

    def __init__(self):
        super().__init__()

        self.handle = None

    def notify(self):
        self.updated_state()
        self.reschedule()

    def reschedule(self):
        self.handle = asyncio.get_event_loop().call_later(5, self.notify)

    def update_observation_count(self, count):
        if count and self.handle is None:
            print("Starting the clock")
            self.handle = self.reschedule()
        if count == 0 and self.handle:
            print("Stopping the clock")
            self.handle.cancel()
            self.handle = None

    async def render_get(self, request):
        payload = datetime.datetime.now().\
                strftime("%Y-%m-%d %H:%M").encode('ascii')
        return aiocoap.Message(payload=payload)

# logging setup

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

class coap_main():
    def coap_conn(self):
        # Resource tree creation
        root = resource.Site()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        root.add_resource(('.well-known', 'core'),
                resource.WKCResource(root.get_resources_as_linkheader))
        root.add_resource(('time',), TimeResource())
        root.add_resource(('other', 'block'), BlockResource())
        root.add_resource(('other', 'separate'), SeparateLargeResource())

        asyncio.Task(aiocoap.Context.create_server_context(root))

        asyncio.get_event_loop().run_forever()


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
        properties = pika.BasicProperties(app_id='server',content_type='application/json')
        self.channel.basic_publish('eid_exchange','example.text',string,properties)
        
    def amqp_on_message(self, unused_channel, basic_deliver, properties, body):
        if(properties.app_id == 'client'):
            self.channel.basic_ack(basic_deliver.delivery_tag)
            print(properties.app_id)
            self.publish_string(body)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Dialog()
    mqtt_thread = threading.Thread(target = mqtt_connection_thread, name='mqtt_thread')
    mqtt_thread.start()
    coap_main = coap_main()
    coap_thread = threading.Thread(target= coap_main.coap_conn, name='coap_thread')
    coap_thread.start()
    amqp = amqp_init()
    amqp_thread = threading.Thread(target = amqp.establish_conn,name='amqp_thread')
    amqp_thread.start()
    ex.show();
    sys.exit(app.exec_())
   
    
