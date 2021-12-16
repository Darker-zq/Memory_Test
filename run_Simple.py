import sys
import xlwt
import random
import sched,time
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread,QDateTime,QObject
from PyQt5.QtGui import QIcon,QTextCursor
from PyQt5.QtWidgets import QApplication, QWidget,QDialog
from SimpleWin import Ui_SimpleWindow

class runSimple(QtWidgets.QMainWindow):
    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()

        self.Simple = Ui_SimpleWindow()
        self.Simple.setupUi(self)

        self.logo = QIcon('./cumtlogo.png')
        self.setWindowTitle("简单测试")
        self.setWindowIcon(self.logo)
        #创建线程实例
        self.workThread = workThread()
        #信号与槽连接
        self.workThread.tb_left.connect(self.shownum1)
        self.workThread.tb_right.connect(self.shownum2)
        #按钮控制实现
        self.Simple.pbt_start1.clicked.connect(self.workstart)
        self.Simple.pbt_over1.clicked.connect(self.workover)
        self.Simple.pbt_back1.clicked.connect(self.handle_close)
    #显示左侧文本槽函数
    def shownum1(self):
        self.Simple.textBrowser_left.clear()
        self.Simple.textBrowser_left.setText("  " + str(self.workThread.num1))
        print("num1_show", time.ctime())
    #显示右侧文本槽函数
    def shownum2(self):
        self.Simple.textBrowser_right.clear()
        QApplication.processEvents()
        time.sleep(0.5)
        self.Simple.textBrowser_right.setText("  " + str(self.workThread.num2))
        print("num2_show", time.ctime())


        print("clear",time.ctime(),"\n")

    def workstart(self):
        self.workThread.start()
    #结束显示槽函数，并将结果输入到excel表中
    def workover(self):
        self.workThread.terminate()
        print("num1的长度",len(num1))
        print(num1)
        print("num2的长度",len(num2))
        print(num2)
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('My Worksheet')
        for i,j in zip(range(len(num1)),range(len(num2))):
            # 写入excel
            # 参数对应 行, 列, 值
            worksheet.write(i, 0, num1[i])
            worksheet.write(j, 1, num2[j])

        # 保存
        file_name = "简单记忆" + time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())).replace(":",
                                                                                                      "-") + ".xls"
        workbook.save(file_name)
    def handle_click(self):
        if not self.isVisible():
            self.show()
    def handle_close(self):
        self.workThread.terminate()
        self.close()
#TextBroswer的显示数字线程类
class workThread(QThread):
    # 通过类成员对象定义信号
    tb_left = pyqtSignal(str)  #左侧
    tb_right = pyqtSignal(str) #右侧
    def run(self):
        global num1
        num1 = []
        global num2
        num2 = []
        while True:
            time.sleep(3)
            self.num1 = random.choice(range(10))
            self.num2 = random.choice(range(10))
            print("num1_create=",self.num1,time.ctime())
            print("num2_create=", self.num2, time.ctime())
            self.tb_left.emit(str(self.num1))
            self.tb_right.emit(str(self.num2))
            num1.append(self.num1)
            num2.append(self.num2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建并显示窗口
    SimWindow = runSimple()
    SimWindow.show()
    sys.exit(app.exec_())