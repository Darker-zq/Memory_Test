import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon   #添加图标的

#创建一个类，封装了所有和ui有关的对象，从QMainWindow中继承
class MainWin(QMainWindow):
    #初始化函数，保证QMainWindow是主窗口
    def __init__(self,parent=None):
        super(MainWin,self).__init__(parent)
        #设置主窗口标题
        self.setWindowTitle("简单记忆测试")
        #设置窗口的尺寸
        self.resize(1000,800)
        self.status = self.statusBar()
        self.status.showMessage("5秒时间显示测试",5000)

        #创建跳转的Button按钮
        self.button1 = QPushButton("退出程序")
        #将退出按键与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout
        layout.addWidget(self.button1)
        mainFtame = QWidget()
        mainFtame.setLayout(layout)

        self.setCentralWidget(mainFtame)


    #按钮单击事件方法，（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        #退出应用程序
        app.quit()
if __name__ =='__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./cumtlogo.png"))
    #使用类
    main = MainWin()
    main.show()
    #进入程序主循环
    sys.exit(app.exec_())