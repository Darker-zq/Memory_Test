# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 450)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_complex = QtWidgets.QPushButton(self.centralwidget)
        self.bt_complex.setGeometry(QtCore.QRect(510, 90, 161, 141))
        self.bt_complex.setObjectName("bt_complex")
        self.bt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exit.setGeometry(QtCore.QRect(90, 290, 581, 61))
        self.bt_exit.setObjectName("bt_exit")
        self.bt_middle = QtWidgets.QPushButton(self.centralwidget)
        self.bt_middle.setGeometry(QtCore.QRect(300, 90, 161, 141))
        self.bt_middle.setObjectName("bt_middle")
        self.bt_simple = QtWidgets.QPushButton(self.centralwidget)
        self.bt_simple.setGeometry(QtCore.QRect(90, 90, 161, 141))
        self.bt_simple.setObjectName("bt_simple")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(290, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label_main.setFont(font)
        self.label_main.setObjectName("label_main")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_complex.setText(_translate("MainWindow", "复杂测试"))
        self.bt_exit.setText(_translate("MainWindow", "退出"))
        self.bt_middle.setText(_translate("MainWindow", "中等测试"))
        self.bt_simple.setText(_translate("MainWindow", "简单测试"))
        self.label_main.setText(_translate("MainWindow", "记忆测试程序主界面"))

