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
	def __init__(self):
		super().__init__()
		self.setupUi(self)
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(671, 531)
		self.temperature = QtWidgets.QPushButton(Dialog)
		self.temperature.setGeometry(QtCore.QRect(50, 60, 112, 34))
		self.temperature.setObjectName("temperature")
		self.humidity = QtWidgets.QPushButton(Dialog)
		self.humidity.setGeometry(QtCore.QRect(50, 130, 112, 34))
		self.humidity.setObjectName("humidity")
		self.Plot_Data = QtWidgets.QPushButton(Dialog)
		self.Plot_Data.setGeometry(QtCore.QRect(430, 100, 161, 41))
		self.Plot_Data.setObjectName("Plot_Data")
		self.lineEdit_temp = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_temp.setGeometry(QtCore.QRect(192, 64, 141, 31))
		self.lineEdit_temp.setFrame(True)
		self.lineEdit_temp.setReadOnly(True)
		self.lineEdit_temp.setObjectName("lineEdit_temp")
		self.lineEdit_humid = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_humid.setGeometry(QtCore.QRect(190, 130, 141, 31))
		self.lineEdit_humid.setReadOnly(True)
		self.lineEdit_humid.setObjectName("lineEdit_humid")
		self.progressBar = QtWidgets.QProgressBar(Dialog)
		self.progressBar.setGeometry(QtCore.QRect(50, 250, 201, 41))
		self.progressBar.setMaximum(30)
		self.progressBar.setProperty("value", 24)
		self.progressBar.setObjectName("progressBar")

		self.retranslateUi(Dialog)
		self.Plot_Data.clicked.connect(self.plot_graph)
		self.temperature.clicked.connect(self.query_temp)
		self.humidity.clicked.connect(self.query_humidity)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		self._translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(self._translate("Dialog", "Dialog"))
		self.temperature.setText(self._translate("Dialog", "Get Temp"))
		self.humidity.setText(self._translate("Dialog", "Get Humid"))
		self.Plot_Data.setText(self._translate("Dialog", "Plot"))

	def query_temp(self):
		#self._translate = QtCore.QCoreApplication.translate
		humidity, temp = ad.read_retry(22,4)
		humidity_string = '{0:.2f}'.format(humidity)
		temp_string = '{0:.2f}'.format(temp)
		self.lineEdit_temp.setText(self._translate("Dialog", temp_string))
		self.progressBar.setValue(temp)
		with open('Weather_Data.csv', 'a') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow([humidity_string,temp_string])

	def query_humidity(self):
		#self._translate = QtCore.QCoreApplication.translate
		humidity, temp = ad.read_retry(22,4)
		humidity_string = '{0:.2f}'.format(humidity)
		temp_string = '{0:.2f}'.format(temp)
		self.lineEdit_humid.setText(self._translate("Dialog", humidity_string))
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
	


if __name__ == '__main__':
	
	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_Dialog();
	ex.show();
	sys.exit(app.exec_())


    

