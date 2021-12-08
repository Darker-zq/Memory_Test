from PyQt5.QtCore import pyqtSignal, QObject


class signal(QObject):
    # 自定义一个信号
    my_sighal = pyqtSignal(str)

    # 定义一个发送信号的函数
    def run(self, text):
        self.my_sighal.emit(text)


class slot(QObject):
    # 这个函数将用于绑定信号
    def action(self, text):
        print("I received that signal:" + text)


if __name__ == '__main__':
    # 创建类的对象
    send = signal()
    receive = slot()

    # 将信号与动作进行绑定
    send.my_sighal.connect(receive.action)
    # 发送信号
    send.run("hello")

    # 将信号与槽函数解绑
    send.my_sighal.disconnect(receive.action)
    send.run("hello")