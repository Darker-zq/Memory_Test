import sys
# 导入界面处理包
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, QCoreApplication, QThread
from PyQt5.QtGui import QImage, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QInputDialog
import MainWin as MainWin
from run_Simple import runSimple
from run_Middle import runMiddle
from run_Complex import runComplex
class MainWindow(QtWidgets.QMainWindow):
    # 类构造函数
    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()
        # self.ui = MainUI.Ui_Form()
        self.ui = MainWin.Ui_MainWindow()
        self.ui.setupUi(self)


        # 设置主窗口的logo
        self.logo = QIcon('./cumtlogo.png')
        # 设置提示框icon
        #self.info_icon = QIcon('./logo_imgs/info_icon.jpg')

        # ###################### 窗口初始化 ######################
        # 设置窗口名称和图标
        self.setWindowTitle('记忆测试系统v1.2')
        self.setWindowIcon(self.logo)

        #按钮事件
        #self.ui.bt_simple.clicked.connect(self.close)
        #self.ui.bt_simple.clicked.connect(Ui_SimpleWindow.show)
        #self.ui.bt_simple.clicked.connect(self.show)
        self.ui.bt_exit.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建并显示窗口
    mainWindow = MainWindow()
    mainWindow.show()
    SimWin = runSimple()
    MidWin = runMiddle()
    ComWin = runComplex()
    mainWindow.ui.bt_simple.clicked.connect(SimWin.handle_click)
    mainWindow.ui.bt_middle.clicked.connect(MidWin.handle_click)
    mainWindow.ui.bt_complex.clicked.connect(ComWin.handle_click)
    sys.exit(app.exec_())