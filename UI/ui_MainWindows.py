# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    background: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    padding: 1px 10px;\n"
"    border-radius:2px;\n"
"    border: 1px groove #AAAAAA;\n"
"    color: #000000;\n"
"}\n"
" QPushButton:hover\n"
"{\n"
"    background-color:3DAAFD;\n"
"    background: #3DAAFD;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #C2C2C2;\n"
"    background: #C2C2C2;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #FFFFFF;\n"
"    border:1px groove #AAAAAA; \n"
"    border-radius:2px;\n"
"    padding: 1px 5px;                  \n"
"}\n"
" QLineEdit:focus \n"
"{\n"
"    background-color: #FFFFFF;\n"
"    border-image:none;\n"
"    border:1px groove #3DAAFD; \n"
"    border-radius:2px;\n"
"}\n"
"\n"
"QListWidget\n"
"{\n"
"    color: black; \n"
"    background: #FFFFFF;\n"
"    border-left: 0px solid gray;\n"
"    border-bottom: 0px solid gray;\n"
"    border-top: 0px solid gray;\n"
"    border-right: 1px solid #D7DCE0;\n"
"    padding-top: 6px;\n"
"    outline:0px;\n"
"}\n"
"\n"
"QListWidget::Item\n"
"{\n"
"    height: 40px;\n"
"    border: 0px solid #FFFFFF;\n"
"    padding-left: 12;\n"
"}\n"
"\n"
"QListWidget::Item:hover\n"
"{\n"
"    color: #3DAAFD;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QListWidget::Item:selected\n"
"{\n"
"    color: #3DAAFD;\n"
"    background: #E7E7EB;\n"
"    border-left: 5px solid #3DAAFD;\n"
"}\n"
"/*\n"
"QListWidget::Item:selected:active\n"
"{\n"
"    background: #E7E7EB;\n"
"    color:  #3DAAFD;\n"
"    border-left:2px solid #3DAAFD;\n"
"}*/\n"
"\n"
"QTextEdit\n"
"{\n"
"    border: 0px;\n"
"    padding: 16px 2px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox{\n"
"    spacing: 5px;\n"
"}\n"
" \n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
" \n"
"QCheckBox::indicator:unchecked{    \n"
"    image: url(:/img/images/check_box.png);\n"
"}\n"
" \n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/img/images/checked_box.png);\n"
"}\n"
" \n"
"QCheckBox::indicator:checked:disabled{\n"
"    image: url(:/img/images/check_box_disabled.png);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMinimumSize(QtCore.QSize(115, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(115, 100000))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/TCP服务器.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/images/TCP客户端.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/images/UDP工具.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/images/帮助.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网络调试工具"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "TCP服务器"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "TCP客户端"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "UDP工具组"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "关于/帮助"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

import img_rc
