# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCPServer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(551, 537)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_Display_Time = QtWidgets.QCheckBox(Form)
        self.checkBox_Display_Time.setObjectName("checkBox_Display_Time")
        self.horizontalLayout_2.addWidget(self.checkBox_Display_Time)
        self.checkBox_Display_Hex = QtWidgets.QCheckBox(Form)
        self.checkBox_Display_Hex.setObjectName("checkBox_Display_Hex")
        self.horizontalLayout_2.addWidget(self.checkBox_Display_Hex)
        self.checkBox_Pause_Display = QtWidgets.QCheckBox(Form)
        self.checkBox_Pause_Display.setObjectName("checkBox_Pause_Display")
        self.horizontalLayout_2.addWidget(self.checkBox_Pause_Display)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_Clear_Recv = QtWidgets.QPushButton(Form)
        self.pushButton_Clear_Recv.setObjectName("pushButton_Clear_Recv")
        self.horizontalLayout_2.addWidget(self.pushButton_Clear_Recv)
        self.pushButton_Clear_Count = QtWidgets.QPushButton(Form)
        self.pushButton_Clear_Count.setObjectName("pushButton_Clear_Count")
        self.horizontalLayout_2.addWidget(self.pushButton_Clear_Count)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_TX = QtWidgets.QLabel(Form)
        self.label_TX.setMinimumSize(QtCore.QSize(50, 0))
        self.label_TX.setObjectName("label_TX")
        self.horizontalLayout_3.addWidget(self.label_TX)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_RX = QtWidgets.QLabel(Form)
        self.label_RX.setMinimumSize(QtCore.QSize(50, 0))
        self.label_RX.setObjectName("label_RX")
        self.horizontalLayout_2.addWidget(self.label_RX)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_IP = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_IP.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_IP.setText("")
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.horizontalLayout_6.addWidget(self.lineEdit_IP)
        self.lineEdit_Port = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Port.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.horizontalLayout_6.addWidget(self.lineEdit_Port)
        self.pushButton_Connect = QtWidgets.QPushButton(self.tab)
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.horizontalLayout_6.addWidget(self.pushButton_Connect)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_Recv_To_File = QtWidgets.QCheckBox(self.tab)
        self.checkBox_Recv_To_File.setObjectName("checkBox_Recv_To_File")
        self.horizontalLayout.addWidget(self.checkBox_Recv_To_File)
        self.lineEdit_Recv_File_Path = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Recv_File_Path.setObjectName("lineEdit_Recv_File_Path")
        self.horizontalLayout.addWidget(self.lineEdit_Recv_File_Path)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 107, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 6, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textEdit_send = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_send.setObjectName("textEdit_send")
        self.gridLayout_5.addWidget(self.textEdit_send, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_send = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_5.addWidget(self.pushButton_send)
        self.checkBox_hex = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_hex.setObjectName("checkBox_hex")
        self.horizontalLayout_5.addWidget(self.checkBox_hex)
        self.checkBox_times = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_times.setObjectName("checkBox_times")
        self.horizontalLayout_5.addWidget(self.checkBox_times)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit_times = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_times.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_times.setObjectName("lineEdit_times")
        self.horizontalLayout_5.addWidget(self.lineEdit_times)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.textEdit_send.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TCP/IP_Server"))
        self.checkBox_Display_Time.setText(_translate("Form", "接收时间"))
        self.checkBox_Display_Hex.setText(_translate("Form", "HEX显示"))
        self.checkBox_Pause_Display.setText(_translate("Form", "暂停"))
        self.pushButton_Clear_Recv.setText(_translate("Form", "清空显示"))
        self.pushButton_Clear_Count.setText(_translate("Form", "清空计数"))
        self.label_4.setText(_translate("Form", "TX"))
        self.label_TX.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "RX"))
        self.label_RX.setText(_translate("Form", "0"))
        self.lineEdit_IP.setPlaceholderText(_translate("Form", "本机地址"))
        self.lineEdit_Port.setPlaceholderText(_translate("Form", "端口"))
        self.pushButton_Connect.setText(_translate("Form", "连接"))
        self.checkBox_Recv_To_File.setText(_translate("Form", "接收转向文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "配置"))
        self.textEdit_send.setPlaceholderText(_translate("Form", "发送数据输入"))
        self.pushButton_send.setText(_translate("Form", "发送"))
        self.checkBox_hex.setText(_translate("Form", "十六进制"))
        self.checkBox_times.setText(_translate("Form", "循环发送"))
        self.label.setText(_translate("Form", "间隔:"))
        self.label_2.setText(_translate("Form", "ms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "发送数据"))
        self.textEdit.setPlaceholderText(_translate("Form", "接收到的数据"))

import img_rc
