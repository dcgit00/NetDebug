# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UDPServer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 553)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(137, 16777215))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.verticalLayout.addWidget(self.lineEdit_IP)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_Port = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.verticalLayout.addWidget(self.lineEdit_Port)
        self.checkBox_Display_Time = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Display_Time.setObjectName("checkBox_Display_Time")
        self.verticalLayout.addWidget(self.checkBox_Display_Time)
        self.checkBox_Display_Hex = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Display_Hex.setObjectName("checkBox_Display_Hex")
        self.verticalLayout.addWidget(self.checkBox_Display_Hex)
        self.checkBox_Pause_Display = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Pause_Display.setObjectName("checkBox_Pause_Display")
        self.verticalLayout.addWidget(self.checkBox_Pause_Display)
        self.checkBox_Recv_To_File = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Recv_To_File.setObjectName("checkBox_Recv_To_File")
        self.verticalLayout.addWidget(self.checkBox_Recv_To_File)
        self.lineEdit_Recv_File_Path = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Recv_File_Path.setObjectName("lineEdit_Recv_File_Path")
        self.verticalLayout.addWidget(self.lineEdit_Recv_File_Path)
        self.pushButton_Connect = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.verticalLayout.addWidget(self.pushButton_Connect)
        self.pushButton_Clear_Recv = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_Clear_Recv.setObjectName("pushButton_Clear_Recv")
        self.verticalLayout.addWidget(self.pushButton_Clear_Recv)
        self.pushButton_Clear_Count = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_Clear_Count.setObjectName("pushButton_Clear_Count")
        self.verticalLayout.addWidget(self.pushButton_Clear_Count)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_RX = QtWidgets.QLabel(self.groupBox_2)
        self.label_RX.setObjectName("label_RX")
        self.horizontalLayout_2.addWidget(self.label_RX)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_TX = QtWidgets.QLabel(self.groupBox_2)
        self.label_TX.setObjectName("label_TX")
        self.horizontalLayout_3.addWidget(self.label_TX)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(5, 5, 5, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 170))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setContentsMargins(9, 0, 0, 10)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget.setMaximumSize(QtCore.QSize(129, 1000))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_4)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "UDP/IP_Server"))
        self.label.setText(_translate("Form", "本机IP地址:"))
        self.label_2.setText(_translate("Form", "本地端口:"))
        self.checkBox_Display_Time.setText(_translate("Form", "显示接收时间"))
        self.checkBox_Display_Hex.setText(_translate("Form", "十六进制显示"))
        self.checkBox_Pause_Display.setText(_translate("Form", "暂停接收显示"))
        self.checkBox_Recv_To_File.setText(_translate("Form", "接收转向文件"))
        self.pushButton_Connect.setText(_translate("Form", "连接"))
        self.pushButton_Clear_Recv.setText(_translate("Form", "清空显示"))
        self.pushButton_Clear_Count.setText(_translate("Form", "清空计数"))
        self.label_3.setText(_translate("Form", "RX"))
        self.label_RX.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "TX"))
        self.label_TX.setText(_translate("Form", "0"))
        self.groupBox.setTitle(_translate("Form", "网络数据接收"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
