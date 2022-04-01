# @File  : Front_Login.py
# @Author: Zeng Yixuan
# @Date  :  2019/12/01

import sys

from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QApplication, QListWidget, QListWidgetItem, QHBoxLayout, \
    QVBoxLayout, QLineEdit, QFormLayout, QMessageBox
import facesTest
import mainView


class LoginView(QWidget):
    # 构造函数
    def __init__(self):
        super(LoginView,self).__init__()   # 实现父类的构造函数，super()实现父类的方法
        self.initUI()

    def initUI(self):
        self.setWindowTitle("人脸识别登录")
        self.resize(700,500)
        self.log=QPushButton("人脸识别",self)
        self.log.setStyleSheet("font-size:22px;font-weight:normal;font-family:楷体;background-color:white")
        #self.log.move(100,50)
        self.log.clicked.connect(self.verify)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("background.jpg")))
        self.setPalette(palette)

    def verify(self):
        if(facesTest.FacesTest()):
            self.mesBox("Success", "检测成功！")
            self.backmain()
        else:
            self.mesBox("Fail", "检测失败。")

    def backmain(self):
        self.close()
        self.main = mainView.MainView()   # 实例化主界面对象，传入了登录界面窗口
        self.main.show()                  # 主页面显示

    def mesBox(self,title,info):
        """
        弹窗提示
        :param title:标题
        :param info:对话框提示内容
        :return:
        """
        messbox = QMessageBox()
        messbox.setWindowTitle(title)
        messbox.resize(200,40)
        messbox.setText(info)   # 对话框提示文本
        messbox.setIcon(QMessageBox.Information)        # 设置图标类型
        messbox.setStandardButtons(QMessageBox.Ok)
        messbox.exec_()


if __name__ == '__main__':
    # 实例化APP
    app = QApplication(sys.argv)
    # 实例化对象
    loginBox = LoginView()
    # 展示窗口
    loginBox.show()
    # 保证程序可以被关掉
    sys.exit(app.exec_())