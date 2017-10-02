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
class Ui_Dialog(QtWidgets.QWidget): 
	gl_h,gl_t,curr_position,sample = [0,0,25,0]
	avg_t, avg_h = [0,0]
	def __init__(self):
		super().__init__()
		self.setupUi(self)
	def setupUi(self, Dialog):
		self.sample_freq = QtCore.QTimer(self)
		self.sample_freq.timeout.connect(self.timeout_isr)
		Dialog.resize(690, 539)
		self.temperature = QtWidgets.QPushButton(Dialog)
		self.temperature.setGeometry(QtCore.QRect(400, 50, 112, 34))
		self.temperature.setObjectName("temperature")
		self.humidity = QtWidgets.QPushButton(Dialog)
		self.humidity.setGeometry(QtCore.QRect(110, 50, 112, 34))
		self.humidity.setObjectName("humidity")
		self.Plot_Data = QtWidgets.QPushButton(Dialog)
		self.Plot_Data.setGeometry(QtCore.QRect(50, 440, 161, 41))
		self.Plot_Data.setObjectName("Plot_Data")
		self.lineEdit_temp = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_temp.setGeometry(QtCore.QRect(390, 130, 141, 31))
		self.lineEdit_temp.setFrame(True)
		self.lineEdit_temp.setReadOnly(True)
		self.lineEdit_temp.setObjectName("lineEdit_temp")
		self.lineEdit_humid = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_humid.setGeometry(QtCore.QRect(100, 130, 141, 31))
		self.lineEdit_humid.setReadOnly(True)
		self.lineEdit_humid.setObjectName("lineEdit_humid")
		self.temp_progress = QtWidgets.QProgressBar(Dialog)
		self.temp_progress.setGeometry(QtCore.QRect(380, 310, 201, 41))
		self.temp_progress.setMaximum(30)
		self.temp_progress.setProperty("value", 0)
		self.temp_progress.setObjectName("temp_progress")
		self.humid_progress = QtWidgets.QProgressBar(Dialog)
		self.humid_progress.setGeometry(QtCore.QRect(100, 310, 201, 41))
		self.humid_progress.setMaximum(100)
		self.humid_progress.setProperty("value", 0)
		self.humid_progress.setObjectName("humid_progress")
		self.alarm = QtWidgets.QLineEdit(Dialog)
		self.alarm.setGeometry(QtCore.QRect(280, 440, 141, 31))
		self.alarm.setObjectName("alarm")
		self.AlarmControl = QtWidgets.QDial(Dialog)
		self.AlarmControl.setGeometry(QtCore.QRect(490, 430, 50, 64))
		self.AlarmControl.setSliderPosition(25)
		self.AlarmControl.setObjectName("AlarmControl")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(390, 360, 151, 31))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(120, 360, 151, 31))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(Dialog)
		self.label_3.setGeometry(QtCore.QRect(500, 490, 141, 31))
		self.label_3.setObjectName("label_3")
		self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
		self.lcdNumber.setGeometry(QtCore.QRect(570, 430, 71, 51))
		self.lcdNumber.setAutoFillBackground(False)
		self.lcdNumber.setProperty("intValue", 25)
		self.lcdNumber.setObjectName("lcdNumber")
		self.label_4 = QtWidgets.QLabel(Dialog)
		self.label_4.setGeometry(QtCore.QRect(290, 490, 121, 20))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(Dialog)
		self.label_5.setGeometry(QtCore.QRect(270, 190, 121, 19))
		self.label_5.setObjectName("label_5")
		self.lineEdit_humid_2 = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_humid_2.setGeometry(QtCore.QRect(100, 220, 141, 31))
		self.lineEdit_humid_2.setReadOnly(True)
		self.lineEdit_humid_2.setObjectName("lineEdit_humid_2")
		self.lineEdit_temp_2 = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_temp_2.setGeometry(QtCore.QRect(390, 220, 141, 31))
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
		self.sample_freq.start(10000)
        
		self.retranslateUi(Dialog)
		self.Plot_Data.clicked.connect(self.plot_graph)
		self.temperature.clicked.connect(self.query_temp)
		self.humidity.clicked.connect(self.query_humidity)	        
		self.AlarmControl.sliderMoved['int'].connect(self.set_prg)
		self.AlarmControl.valueChanged['int'].connect(self.lcdNumber.display)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

		
	def retranslateUi(self, Dialog):
		self._translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(self._translate("Dialog", "Dialog"))
		self.temperature.setText(self._translate("Dialog", "Get Temp"))
		self.humidity.setText(self._translate("Dialog", "Get Humidity"))
		self.Plot_Data.setText(self._translate("Dialog", "Plot Graph"))
		self.label.setText(self._translate("Dialog", "Temperature Level"))
		self.label_2.setText(self._translate("Dialog", "Humidity Level"))
		self.label_3.setText(self._translate("Dialog", "Set Alarm Trigger"))
		self.label_4.setText(self._translate("Dialog", "Message Display"))
		self.label_5.setText(self._translate("Dialog", "Average Values"))
		self.label_6.setText(self._translate("Dialog", "%"))
		self.label_7.setText(self._translate("Dialog", "C"))
		self.label_8.setText(self._translate("Dialog", "%"))
		self.label_9.setText(self._translate("Dialog", "C"))


	def timeout_isr(self):
		print("Got Timed Reading")
		self.sample = self.sample + 1
		self.query_temp()
		self.query_humidity()
		self.avg_t = ((self.avg_t  * (self.sample-1))+ self.gl_t)/self.sample	
		self.avg_h = ((self.avg_h  * (self.sample-1))+ self.gl_h)/self.sample
		
		self.lineEdit_temp_2.setText(self._translate("Dialog", '{0:.2f}'.format(self.avg_t)))
		self.lineEdit_humid_2.setText(self._translate("Dialog", '{0:.2f}'.format(self.avg_h)))
	
	def query_temp(self):
		
		humidity, temp = ad.read_retry(22,4)
		if(temp == None):
			self.lineEdit_temp.setText(self._translate("Dialog", "Sensor Disconnected"))
		else:	
			self.gl_h,self.gl_t = humidity, temp
		
			humidity_string = '{0:.2f}'.format(humidity)
			temp_string = '{0:.2f}'.format(temp)
			print("Temp - ",temp_string)
			self.lineEdit_temp.setText(self._translate("Dialog", temp_string))
			self.temp_progress.setValue(temp)
			if(temp > self.curr_position):
				self.temp_progress.setMaximum(temp)
				self.alarm.setText(self._translate("Dialog", "Temp Alarm"))
			else:
				self.temp_progress.setMaximum(self.curr_position+1)
				self.alarm.setText(self._translate("Dialog", "Safe"))	

			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([humidity_string,temp_string])

	def query_humidity(self):
		humidity, temp = ad.read_retry(22,4)
		if(humidity == None):
			self.lineEdit_humid.setText(self._translate("Dialog", "Sensor Disconnected"))
		else:	
		
			self.gl_h,self.gl_t = humidity, temp
			humidity_string = '{0:.2f}'.format(humidity)
			temp_string = '{0:.2f}'.format(temp)
			print("Humidity - ",humidity_string)
			self.lineEdit_humid.setText(self._translate("Dialog", humidity_string))
			self.humid_progress.setValue(humidity)
			with open('Weather_Data.csv', 'a') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([humidity_string,temp_string])

	def plot_graph(self):
		humidity,temp = np.loadtxt('Weather_Data.csv', delimiter=',', unpack=True)
		i = range(0,len(humidity))
		fig = plt.figure()
		fig.subplots_adjust(hspace=.5)
		ax1 = fig.add_subplot(211)
		ax1.plot(i,humidity,)
		ax1.set_title('Humidity')
		
		ax2 = fig.add_subplot(212)
		ax2.plot(i,temp,'r-')
		ax2.set_title('Temperature')
		
		fig.show()

		fig.savefig('Weather_data.jpg')

	def set_prg(self):
		self.curr_position = self.AlarmControl.value()
		if(self.curr_position < self.gl_t):
			self.temp_progress.setMaximum(self.gl_t)
			self.alarm.setText(self._translate("Dialog", "Temp Alarm"))			
		else:
			self.temp_progress.setMaximum(self.curr_position)
			self.alarm.setText(self._translate("Dialog", "Safe"))	
		
		
	


if __name__ == '__main__':
	
	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_Dialog();
	ex.show();
	sys.exit(app.exec_())


    

