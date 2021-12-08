import sys
import random
import sched,time
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon,QTextCursor
from PyQt5.QtWidgets import QApplication, QWidget
from SimpleWin import Ui_SimpleWindow
class runSimple(QtWidgets.QMainWindow):
    _signal = pyqtSignal(str)
    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()

        self.Simple = Ui_SimpleWindow()
        self.Simple.setupUi(self)

        self.logo = QIcon('./cumtlogo.png')
        self.setWindowTitle("简单测试")
        self.setWindowIcon(self.logo)
        self.Simple.textEdit.moveCursor(QTextCursor.End)
        self.Simple.pbt_back1.clicked.connect(self.handle_close)

        self.Simple.pbt_start1.clicked.connect(self.shownumber1)
        #self.Simple.pbt_start1.clicked.connect(self.shownumber2)
        #self.Simple.pbt_over1.clicked.connect(self.crenumber)

    # def crenumber(self,):
    #     self.num1 = random.choice(range(10))
    #     self._signal.emit(self.num1)
    #     print(self._signal)
    def shownumber1(self):
        self.Simple.pbt_start1.setText("结束测试")
        #self.Simple.textEdit.moveCursor(QTextCursor.End)
        flag =1
        while True:
            time.sleep(3)
            self.num1 = random.choice(range(10))
            print("num1=",self.num1)
            self.Simple.textBrowser_left.clear()
            self.Simple.textBrowser_left.setText("  " + str(self.num1))

            print("left", time.ctime())
            if flag ==1:
                time.sleep(1)
                print("right",time.ctime())
                self.num2 = random.choice(range(10))
                print("num2=", self.num2)
                self.Simple.textBrowser_right.clear()
                self.Simple.textBrowser_right.append("  " + str(self.num2))
            else:
                self.num2 = random.choice(range(10))
                print("num2=", self.num2)
                self.Simple.textBrowser_right.clear()
                self.Simple.textBrowser_right.append("  " + str(self.num2))

        QApplication.processEvents()






    def handle_click(self):
        if not self.isVisible():
            self.show()
    def handle_close(self):
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建并显示窗口
    SimWindow = runSimple()
    SimWindow.show()
    sys.exit(app.exec_())