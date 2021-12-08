# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComplexWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ComplexWindow(object):
    def setupUi(self, ComplexWindow):
        ComplexWindow.setObjectName("ComplexWindow")
        ComplexWindow.resize(1123, 832)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        ComplexWindow.setFont(font)
        ComplexWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(ComplexWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_left = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_left.setGeometry(QtCore.QRect(40, 110, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_left.setFont(font)
        self.textBrowser_left.setObjectName("textBrowser_left")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(510, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pbt_start1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_start1.setGeometry(QtCore.QRect(50, 700, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_start1.setFont(font)
        self.pbt_start1.setObjectName("pbt_start1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(890, 510, 161, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_tip1 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1.setGeometry(QtCore.QRect(840, 160, 271, 141))
        self.label_tip1.setMinimumSize(QtCore.QSize(271, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip1.setFont(font)
        self.label_tip1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tip1.setTextFormat(QtCore.Qt.PlainText)
        self.label_tip1.setWordWrap(True)
        self.label_tip1.setObjectName("label_tip1")
        self.label_tips = QtWidgets.QLabel(self.centralwidget)
        self.label_tips.setGeometry(QtCore.QRect(850, 110, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tips.setFont(font)
        self.label_tips.setObjectName("label_tips")
        self.label_tip2 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip2.setGeometry(QtCore.QRect(840, 310, 271, 101))
        self.label_tip2.setMinimumSize(QtCore.QSize(271, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip2.setFont(font)
        self.label_tip2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tip2.setTextFormat(QtCore.Qt.PlainText)
        self.label_tip2.setWordWrap(True)
        self.label_tip2.setObjectName("label_tip2")
        self.pbt_back1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_back1.setGeometry(QtCore.QRect(650, 700, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_back1.setFont(font)
        self.pbt_back1.setObjectName("pbt_back1")
        self.pbt_over1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_over1.setGeometry(QtCore.QRect(360, 700, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_over1.setFont(font)
        self.pbt_over1.setObjectName("pbt_over1")
        self.textBrowser_left_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_left_2.setGeometry(QtCore.QRect(40, 430, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_left_2.setFont(font)
        self.textBrowser_left_2.setObjectName("textBrowser_left_2")
        self.textBrowser_left_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_left_3.setGeometry(QtCore.QRect(350, 270, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_left_3.setFont(font)
        self.textBrowser_left_3.setObjectName("textBrowser_left_3")
        self.textBrowser_left_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_left_4.setGeometry(QtCore.QRect(660, 110, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_left_4.setFont(font)
        self.textBrowser_left_4.setObjectName("textBrowser_left_4")
        self.textBrowser_left_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_left_5.setGeometry(QtCore.QRect(660, 430, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_left_5.setFont(font)
        self.textBrowser_left_5.setObjectName("textBrowser_left_5")
        ComplexWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ComplexWindow)
        QtCore.QMetaObject.connectSlotsByName(ComplexWindow)

    def retranslateUi(self, ComplexWindow):
        _translate = QtCore.QCoreApplication.translate
        ComplexWindow.setWindowTitle(_translate("ComplexWindow", "MainWindow"))
        self.textBrowser_left.setHtml(_translate("ComplexWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:80pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_title.setText(_translate("ComplexWindow", "复杂测试"))
        self.pbt_start1.setText(_translate("ComplexWindow", "开始测试"))
        self.label_tip1.setText(_translate("ComplexWindow", "    数字出现的频率是40次/分钟，每组数字先后在五个位置随机出现，每个数字显示时间为0.1秒，给您1.2秒计算和填写的时间。即每1.5秒计算一组数字。"))
        self.label_tips.setText(_translate("ComplexWindow", "注意："))
        self.label_tip2.setText(_translate("ComplexWindow", "    点击开始后，5秒后出现第一组数字，请保证鼠标光标放在右侧的输入栏中。"))
        self.pbt_back1.setText(_translate("ComplexWindow", "返回主界面"))
        self.pbt_over1.setText(_translate("ComplexWindow", "结束测试"))
        self.textBrowser_left_2.setHtml(_translate("ComplexWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:80pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_left_3.setHtml(_translate("ComplexWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:80pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_left_4.setHtml(_translate("ComplexWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:80pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_left_5.setHtml(_translate("ComplexWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:80pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

