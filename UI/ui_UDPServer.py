# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UDPServer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(555, 488)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_Recv_To_File = QtWidgets.QCheckBox(self.tab)
        self.checkBox_Recv_To_File.setObjectName("checkBox_Recv_To_File")
        self.gridLayout_2.addWidget(self.checkBox_Recv_To_File, 1, 0, 1, 1)
        self.lineEdit_Port = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Port.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.gridLayout_2.addWidget(self.lineEdit_Port, 0, 1, 1, 1)
        self.lineEdit_Recv_File_Path = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Recv_File_Path.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_Recv_File_Path.setObjectName("lineEdit_Recv_File_Path")
        self.gridLayout_2.addWidget(self.lineEdit_Recv_File_Path, 1, 1, 1, 2)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_IP.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.gridLayout_2.addWidget(self.lineEdit_IP, 0, 0, 1, 1)
        self.pushButton_Connect = QtWidgets.QPushButton(self.tab)
        self.pushButton_Connect.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.gridLayout_2.addWidget(self.pushButton_Connect, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 0, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 97, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textEdit_send_client = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_send_client.setObjectName("textEdit_send_client")
        self.horizontalLayout_6.addWidget(self.textEdit_send_client)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_ip_client = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_ip_client.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_ip_client.setObjectName("lineEdit_ip_client")
        self.horizontalLayout_9.addWidget(self.lineEdit_ip_client)
        self.lineEdit_port_client = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_port_client.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_port_client.setObjectName("lineEdit_port_client")
        self.horizontalLayout_9.addWidget(self.lineEdit_port_client)
        self.lineEdit_clinet_counts = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_clinet_counts.setMaximumSize(QtCore.QSize(82, 16777215))
        self.lineEdit_clinet_counts.setObjectName("lineEdit_clinet_counts")
        self.horizontalLayout_9.addWidget(self.lineEdit_clinet_counts)
        self.pushButton_create = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_create.setObjectName("pushButton_create")
        self.horizontalLayout_9.addWidget(self.pushButton_create)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_send_client = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_send_client.setObjectName("pushButton_send_client")
        self.horizontalLayout_8.addWidget(self.pushButton_send_client)
        self.checkBox_hex_client = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_hex_client.setObjectName("checkBox_hex_client")
        self.horizontalLayout_8.addWidget(self.checkBox_hex_client)
        self.checkBox_times_client = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_times_client.setObjectName("checkBox_times_client")
        self.horizontalLayout_8.addWidget(self.checkBox_times_client)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_times_client = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_times_client.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_times_client.setObjectName("lineEdit_times_client")
        self.horizontalLayout_8.addWidget(self.lineEdit_times_client)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_Display_Time = QtWidgets.QCheckBox(Form)
        self.checkBox_Display_Time.setObjectName("checkBox_Display_Time")
        self.horizontalLayout.addWidget(self.checkBox_Display_Time)
        self.checkBox_Display_Hex = QtWidgets.QCheckBox(Form)
        self.checkBox_Display_Hex.setObjectName("checkBox_Display_Hex")
        self.horizontalLayout.addWidget(self.checkBox_Display_Hex)
        self.checkBox_Pause_Display = QtWidgets.QCheckBox(Form)
        self.checkBox_Pause_Display.setObjectName("checkBox_Pause_Display")
        self.horizontalLayout.addWidget(self.checkBox_Pause_Display)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_Clear_Recv = QtWidgets.QPushButton(Form)
        self.pushButton_Clear_Recv.setObjectName("pushButton_Clear_Recv")
        self.horizontalLayout.addWidget(self.pushButton_Clear_Recv)
        self.pushButton_Clear_Count = QtWidgets.QPushButton(Form)
        self.pushButton_Clear_Count.setObjectName("pushButton_Clear_Count")
        self.horizontalLayout.addWidget(self.pushButton_Clear_Count)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_RX = QtWidgets.QLabel(Form)
        self.label_RX.setMinimumSize(QtCore.QSize(30, 0))
        self.label_RX.setObjectName("label_RX")
        self.horizontalLayout_2.addWidget(self.label_RX)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_TX = QtWidgets.QLabel(Form)
        self.label_TX.setMinimumSize(QtCore.QSize(30, 0))
        self.label_TX.setObjectName("label_TX")
        self.horizontalLayout_3.addWidget(self.label_TX)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "UDP/IP_Server"))
        self.textEdit.setPlaceholderText(_translate("Form", "网络数据接收"))
        self.checkBox_Recv_To_File.setText(_translate("Form", "接收转向文件"))
        self.lineEdit_Port.setPlaceholderText(_translate("Form", "端口"))
        self.lineEdit_IP.setPlaceholderText(_translate("Form", "本机地址"))
        self.pushButton_Connect.setText(_translate("Form", "连接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "UDP服务器"))
        self.textEdit_send_client.setPlaceholderText(_translate("Form", "数据发送输入"))
        self.lineEdit_ip_client.setPlaceholderText(_translate("Form", "目标地址"))
        self.lineEdit_port_client.setPlaceholderText(_translate("Form", "端口"))
        self.lineEdit_clinet_counts.setPlaceholderText(_translate("Form", "客户端个数"))
        self.pushButton_create.setText(_translate("Form", "创建"))
        self.pushButton_send_client.setText(_translate("Form", "发送"))
        self.checkBox_hex_client.setText(_translate("Form", "十六进制"))
        self.checkBox_times_client.setText(_translate("Form", "循环发送"))
        self.label_7.setText(_translate("Form", "间隔:"))
        self.label_8.setText(_translate("Form", "ms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "UDP客户端"))
        self.checkBox_Display_Time.setText(_translate("Form", "显示时间"))
        self.checkBox_Display_Hex.setText(_translate("Form", "Hex"))
        self.checkBox_Pause_Display.setText(_translate("Form", "暂停"))
        self.pushButton_Clear_Recv.setText(_translate("Form", "清空显示"))
        self.pushButton_Clear_Count.setText(_translate("Form", "清空计数"))
        self.label_3.setText(_translate("Form", "RX"))
        self.label_RX.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "TX"))
        self.label_TX.setText(_translate("Form", "0"))

import img_rc
