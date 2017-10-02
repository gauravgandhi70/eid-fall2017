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

class Ui_Dialog(QtWidgets.QWidget): 
	gl_h,gl_t = [0,0]
	def __init__(self):
		super().__init__()
		self.setupUi(self)
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(671, 531)
		self.temperature = QtWidgets.QPushButton(Dialog)
		self.temperature.setGeometry(QtCore.QRect(400, 50, 112, 34))
		self.temperature.setObjectName("temperature")
		self.humidity = QtWidgets.QPushButton(Dialog)
		self.humidity.setGeometry(QtCore.QRect(110, 50, 112, 34))
		self.humidity.setObjectName("humidity")
		self.Plot_Data = QtWidgets.QPushButton(Dialog)
		self.Plot_Data.setGeometry(QtCore.QRect(250, 350, 161, 41))
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
		
		self.lineEdit_alarm = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_alarm.setGeometry(QtCore.QRect(270, 420, 121, 81))
		self.lineEdit_alarm.setReadOnly(True)
		self.lineEdit_alarm.setObjectName("lineEdit_alarm")
		
		self.temp_progress = QtWidgets.QProgressBar(Dialog)
		self.temp_progress.setGeometry(QtCore.QRect(380, 230, 201, 41))
		self.temp_progress.setMaximum(30)
		self.temp_progress.setProperty("value", 0)
		self.temp_progress.setObjectName("temp_progress")
		self.humid_progress = QtWidgets.QProgressBar(Dialog)
		self.humid_progress.setGeometry(QtCore.QRect(100, 230, 201, 41))
		self.humid_progress.setMaximum(100)
		self.humid_progress.setProperty("value", 0)
		self.humid_progress.setObjectName("humid_progress")
		#self.alarm = QtWidgets.QGraphicsView(Dialog)
		#self.alarm.setGeometry(QtCore.QRect(270, 420, 121, 81))
		#self.alarm.setObjectName("alarm")
		self.AlarmControl = QtWidgets.QDial(Dialog)
		self.AlarmControl.setGeometry(QtCore.QRect(430, 420, 50, 64))
		self.AlarmControl.setObjectName("AlarmControl")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(390, 280, 151, 31))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(120, 280, 151, 31))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(Dialog)
		self.label_3.setGeometry(QtCore.QRect(410, 490, 141, 31))
		self.label_3.setObjectName("label_3")
		self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
		self.lcdNumber.setGeometry(QtCore.QRect(510, 430, 71, 51))
		self.lcdNumber.setObjectName("lcdNumber")

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

	def query_temp(self):
		#self._translate = QtCore.QCoreApplication.translate
		humidity, temp = ad.read_retry(22,4)
		self.gl_h,self.gl_t = humidity, temp
		humidity_string = '{0:.2f}'.format(humidity)
		temp_string = '{0:.2f}'.format(temp)
		self.lineEdit_temp.setText(self._translate("Dialog", temp_string))
		self.temp_progress.setValue(temp)
		with open('Weather_Data.csv', 'a') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow([humidity_string,temp_string])

	def query_humidity(self):
		#self._translate = QtCore.QCoreApplication.translate
		humidity, temp = ad.read_retry(22,4)
		self.gl_h,self.gl_t = humidity, temp
		humidity_string = '{0:.2f}'.format(humidity)
		temp_string = '{0:.2f}'.format(temp)
		self.lineEdit_humid.setText(self._translate("Dialog", humidity_string))
		self.humid_progress.setValue(humidity)
		with open('Weather_Data.csv', 'a') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow([humidity_string,temp_string])

	def plot_graph(self):
		humidity,temp = np.loadtxt('Weather_Data.csv', delimiter=',', unpack=True)
		i = range(0,len(humidity))
		fig = plt.figure()
		plt.plot(i,humidity,label='Humidity')
		plt.show()
		fig.savefig('Weather_data.jpg')

	def set_prg(self):
		curr_position = self.AlarmControl.value()
		if(curr_position < self.gl_t):
			self.temp_progress.setMaximum(self.gl_t)
			self.lineEdit_alarm.setText(self._translate("Dialog", "High Temperature Warning"))			
		else:
			self.temp_progress.setMaximum(curr_position+1)
			self.lineEdit_alarm.setText(self._translate("Dialog", "Safe"))	
		
		
	


if __name__ == '__main__':
	
	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_Dialog();
	ex.show();
	sys.exit(app.exec_())


    

