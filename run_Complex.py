import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from ComplexWin import Ui_ComplexWindow
class runComplex(QtWidgets.QMainWindow):
    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()

        self.Simple = Ui_ComplexWindow()
        self.Simple.setupUi(self)

        self.logo = QIcon('./cumtlogo.png')
        self.setWindowTitle("简单测试")
        self.setWindowIcon(self.logo)

        self.Simple.pbt_back1.clicked.connect(self.handle_close)
        #self.Simple.pbt_back1.clicked.connect()

    def handle_click(self):
        if not self.isVisible():
            self.show()
    def handle_close(self):
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建并显示窗口
    ComWindow = runComplex()
    ComWindow.show()
    sys.exit(app.exec_())