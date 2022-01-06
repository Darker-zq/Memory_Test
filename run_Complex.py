import sys
import time
import xlwt
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread,QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from ComplexWin import Ui_ComplexWindow
class runComplex(QtWidgets.QMainWindow):
    global sumnum
    sumnum =[]
    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()

        self.Complex = Ui_ComplexWindow()
        self.Complex.setupUi(self)

        self.logo = QIcon('./cumtlogo.png')
        self.setWindowTitle("复杂测试")
        self.setWindowIcon(self.logo)
        #self.Complex.pbt_back1.clicked.connect()
        # 创建线程实例
        self.workThread = workThread()
        # 信号与槽连接
        self.workThread.tb_left.connect(self.shownum)
        # 按钮控制实现
        self.Complex.pbt_start1.clicked.connect(self.workstart)
        self.Complex.pbt_over1.clicked.connect(self.workover)
        self.Complex.pbt_back1.clicked.connect(self.handle_close)
        self.Complex.lineEdit.returnPressed.connect(self.getinput)
        # 显示左侧文本槽函数

    def shownum(self):
        #self.flag = 1
        self.flag = random.choice(range(20))
        print("flag=",self.flag)
        self.time = QTimer()
        self.time.timeout.connect(self.upgradeProgress)
        #1
        if self.flag == 0: #12
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_2.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)
        #2
        if self.flag ==1:  #21
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_1.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)
        #3
        if self.flag ==2: ##13
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_3.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)
        #4
        if self.flag ==3: ##31
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_1.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)

        #5
        if self.flag == 4:  ##14
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_4.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)
        # 6
        if self.flag == 5:  ##41
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_1.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)

        # 7
        if self.flag == 6:  ##15
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_5.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)
        # 8
        if self.flag == 7:  ##51
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_1.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_1.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)

        #9
        if self.flag == 8:  ##23
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_3.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)
        # 10
        if self.flag == 9:  ##32
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_2.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num2))
            QApplication.processEvents()
            self.time.start(1350)

        # 11
        if self.flag == 10:  ##24
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_4.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num2))
            self.time.start(1350)
        # 12
        if self.flag == 11:  ##42
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_2.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num2))
            self.time.start(1350)

        # 13
        if self.flag == 12:  ##25
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_5.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num2))
            self.time.start(1350)
        # 14
        if self.flag == 13:  ##52
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_2.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_2.setText("  " + str(self.workThread.num2))
            self.time.start(1350)

        # 15
        if self.flag == 14:  ##34
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_4.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num2))
            self.time.start(1350)
        # 16
        if self.flag == 15:  ##43
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_3.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num2))
            self.time.start(1350)

        # 17
        if self.flag == 16:  ##35
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_5.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num2))
            self.time.start(1350)
        # 18
        if self.flag == 17:  ##53
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_3.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_3.setText("  " + str(self.workThread.num2))
            self.time.start(1350)

        # 19
        if self.flag == 18:  ##45
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_5.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num2))
            self.time.start(1350)
        # 20
        if self.flag == 19:  ##54
            self.Complex.textBrowser_5.setText("  " + str(self.workThread.num1))
            print("num1_show", time.ctime())
            self.Complex.textBrowser_4.clear()
            QApplication.processEvents()
            time.sleep(0.15)
            self.Complex.textBrowser_4.setText("  " + str(self.workThread.num2))
            self.time.start(1350)

    def workstart(self):
        self.workThread.start()
        # 结束显示槽函数，并将结果输入到excel表中

    def workover(self):
        self.workThread.terminate()
        print("num1的长度",len(num1))
        print(num1)
        print("num2的长度",len(num2))
        print(num2)
        print("sum的长度", len(num2))
        print(sumnum)
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('My Worksheet')
        worksheet.write(0, 0, '显示数字1')
        worksheet.write(0, 1, '显示数字2')
        worksheet.write(0, 2, '输入结果')
        for i, j, k in zip(range(len(num1)), range(len(num2)), range(len(sumnum))):
            # 写入excel
            # 参数对应 行, 列, 值
            worksheet.write(i + 1, 0, num1[i])
            worksheet.write(j + 1, 1, num2[j])
            worksheet.write(k + 1, 2, sumnum[k])

        # 保存
        file_name = "复杂记忆" + time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())).replace(":",
                                                                                                      "-") + ".xls"
        workbook.save(file_name)

        # 清空储存数组
        self.Complex.textBrowser_1.clear()
        self.Complex.textBrowser_2.clear()
        self.Complex.textBrowser_3.clear()
        self.Complex.textBrowser_4.clear()
        self.Complex.textBrowser_5.clear()
        num1.clear()
        num2.clear()
        sumnum.clear()
        self.time.stop()
    def getinput(self):
        text = self.Complex.lineEdit.text()
        sumnum.append(text)
        self.Complex.lineEdit.clear()
        print(sumnum)
    #实时刷新界面
    def upgradeProgress(self):
        self.Complex.textBrowser_1.clear()
        self.Complex.textBrowser_2.clear()
        self.Complex.textBrowser_3.clear()
        self.Complex.textBrowser_4.clear()
        self.Complex.textBrowser_5.clear()
        print("num2_show", time.ctime())
        print("clear", time.ctime(), "\n")
    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.workThread.terminate()
        self.close()

class workThread(QThread):
    # 通过类成员对象定义信号
    tb_left = pyqtSignal(str)
    tb_right = pyqtSignal(str)
    def run(self):
        global num1
        global num2
        num1 = []
        num2 = []
        while True:
            time.sleep(2)
            #左侧数字
            self.num1 = random.choice(range(10))
            #右侧数字
            self.num2 = random.choice(range(10))
            print("num1_create=",self.num1,time.ctime())
            print("num2_create", self.num2, time.ctime())
            self.tb_left.emit(str(self.num1))
            self.tb_right.emit(str(self.num2))
            num1.append(self.num1)
            num2.append(self.num2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建并显示窗口
    ComWindow = runComplex()
    ComWindow.show()
    sys.exit(app.exec_())