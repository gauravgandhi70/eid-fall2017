# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eid_proj_1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
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
        self.lineEdit_humid_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_humid_3.setGeometry(QtCore.QRect(280, 470, 151, 31))
        self.lineEdit_humid_3.setReadOnly(True)
        self.lineEdit_humid_3.setObjectName("lineEdit_humid_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(190, 10, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_3.setGeometry(QtCore.QRect(280, 10, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(260, 10, 68, 19))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 10, 131, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(380, 10, 68, 19))
        self.label_12.setObjectName("label_12")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_4.setGeometry(QtCore.QRect(420, 10, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_5.setGeometry(QtCore.QRect(500, 10, 64, 23))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_6.setGeometry(QtCore.QRect(580, 10, 64, 23))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
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

        self.retranslateUi(Dialog)
        self.Plot_Data.clicked.connect(Dialog.accept)
        self.temperature.clicked.connect(self.lineEdit_temp.paste)
        self.humidity.clicked.connect(self.lineEdit_humid.paste)
        self.AlarmControl.valueChanged['int'].connect(self.lcdNumber.display)
        self.radioButton.clicked.connect(self.label_9.clear)
        self.radioButton.clicked.connect(self.label_7.clear)
        self.radioButton_2.clicked.connect(self.label_9.clear)
        self.radioButton_2.clicked.connect(self.label_7.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.temperature.setText(_translate("Dialog", "Get Temp"))
        self.humidity.setText(_translate("Dialog", "Get Humidity"))
        self.Plot_Data.setText(_translate("Dialog", "Plot Graph"))
        self.label.setText(_translate("Dialog", "Maximum Values"))
        self.label_2.setText(_translate("Dialog", "Minimum Values"))
        self.label_3.setText(_translate("Dialog", "Set Alarm Trigger"))
        self.label_4.setText(_translate("Dialog", "Message Display"))
        self.label_5.setText(_translate("Dialog", "Average Values"))
        self.label_6.setText(_translate("Dialog", "%"))
        self.label_7.setText(_translate("Dialog", "C"))
        self.label_8.setText(_translate("Dialog", "%"))
        self.label_9.setText(_translate("Dialog", "C"))
        self.label_10.setText(_translate("Dialog", ":"))
        self.label_11.setText(_translate("Dialog", "Data Requested at"))
        self.label_12.setText(_translate("Dialog", "on"))
        self.label_13.setText(_translate("Dialog", "/"))
        self.label_14.setText(_translate("Dialog", "/"))
        self.radioButton.setText(_translate("Dialog", "C"))
        self.radioButton_2.setText(_translate("Dialog", "F"))
        self.label_15.setText(_translate("Dialog", "C"))
        self.label_16.setText(_translate("Dialog", "%"))
        self.label_17.setText(_translate("Dialog", "C"))
        self.label_18.setText(_translate("Dialog", "%"))

