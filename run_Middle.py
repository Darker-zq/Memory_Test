import sys
import xlwt
import random
import sched,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread,QDateTime,QObject
from PyQt5.QtGui import QIcon,QTextCursor
from PyQt5.QtWidgets import QApplication, QWidget,QDialog
from MiddleWin import Ui_MiddleWindow

class runMiddle(QtWidgets.QMainWindow):
    global sumnum
    sumnum = []
    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()

        self.Middle = Ui_MiddleWindow()
        self.Middle.setupUi(self)

        self.logo = QIcon('./cumtlogo.png')
        self.setWindowTitle("中等测试")
        self.setWindowIcon(self.logo)
        #创建线程实例
        self.workThread = workThread()
        #信号与槽连接
        self.workThread.tb_left.connect(self.shownum1)
        self.workThread.tb_right.connect(self.shownum2)
        #按钮控制实现
        self.Middle.pbt_start1.clicked.connect(self.workstart)
        self.Middle.pbt_over1.clicked.connect(self.workover)
        self.Middle.pbt_back1.clicked.connect(self.handle_close)
        self.Middle.lineEdit.returnPressed.connect(self.getinput)
    #显示左侧文本槽函数
    def shownum1(self):
        self.Middle.textBrowser_left.clear()
        self.Middle.textBrowser_left.setText("  " + str(self.workThread.num1))
        print("num1_show", time.ctime())
    #显示右侧文本槽函数
    def shownum2(self):
        self.Middle.textBrowser_right.clear()
        QApplication.processEvents()
        time.sleep(0.25)
        self.Middle.textBrowser_right.setText("  " + str(self.workThread.num2))
        print("num2_show", time.ctime())
        print("clear","\n")

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
        worksheet.write(0, 0, '显示数字1')
        worksheet.write(0, 1, '显示数字2')
        worksheet.write(0, 2, '输入结果')
        for i,j,k in zip(range(len(num1)),range(len(num2)),range(len(sumnum))):
            # 写入excel
            # 参数对应 行, 列, 值
            worksheet.write(i+1, 0, num1[i])
            worksheet.write(j+1, 1, num2[j])
            worksheet.write(k+1, 2, sumnum[k])

        # 保存
        file_name = "中等记忆" + time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())).replace(":",
                                                                                                      "-") + ".xls"
        workbook.save(file_name)
        # 清空储存数组
        self.Middle.textBrowser_left.clear()
        self.Middle.textBrowser_right.clear()
        num1.clear()
        num2.clear()
        sumnum.clear()
    def getinput(self):
        text = self.Middle.lineEdit.text()
        sumnum.append(text)
        self.Middle.lineEdit.clear()
        print(sumnum)
    def handle_click(self):
        if not self.isVisible():
            self.show()
    def handle_close(self):
        self.workThread.terminate()
        self.close()


#TextBroswer的显示数字线程类
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
    MidWindow = runMiddle()
    MidWindow.show()
    sys.exit(app.exec_())