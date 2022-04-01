# @File  : Background_Login.py
# @Author: Zeng Yixuan
# @Date  :  2019/12/01
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QApplication, QListWidget, QListWidgetItem, QHBoxLayout, \
    QVBoxLayout, QLineEdit, QFormLayout, QMessageBox
import CollectView

# QWidget:是一切窗口类的基类。
class LoginView(QWidget):
    # 构造函数
    def __init__(self):
        super(LoginView,self).__init__()   # 实现父类的构造函数，super()实现父类的方法
        self.readUser()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("后台登录")
        self.resize(200,100)
        formlayout = QFormLayout(self)  # 布局——表单布局
        self.setLayout(formlayout)      # 为窗口设置布局——表单布局
        self.userLabel = QLabel("用户名：", self)
        self.userInput = QLineEdit(self)
        formlayout.addRow(self.userLabel,self.userInput)
        self.password = QLabel("密 码：", self)
        self.passInput = QLineEdit(self)
        formlayout.addRow(self.password, self.passInput)
        self.log=QPushButton("登录",self)
        self.exit=QPushButton("退出",self)
        formlayout.addRow(self.log,self.exit)
        # 为登录按钮添加登录槽函数    clicked--信号
        self.log.clicked.connect(self.verify)
        self.exit.clicked.connect(self.do_exit)


    def verify(self):
        username = self.userInput.text()   # 获取用户名
        password = self.passInput.text()   # 获取密码
        # 2.匹配    文件IO进行匹配
        userList = self.readUser()
        # 索引 元素

        for index,user in enumerate(userList):
            print(index,user)
            if username == user[0] and password==user[1]:
                self.mesBox("Success","登录成功！")
                self.backcollectView()
                break

        else:
            # 当循环自然执行结束后，就会运行下方代码
            self.mesBox("Fail", "用户名或密码不存在")


    def readUser(self):
        userList = []
        with open("./user.txt",'r') as f:   # 便利的打开文件的方式，不用在意文件是否关闭
            # 逐行读取文本
            for line in f.readlines():   # f.readlines()的类型是list
                userList.append(line.strip().split('*'))
                # 列表添加元素 append()
            return userList

    def do_exit(self):
        self.close()

    def backcollectView(self):
        self.close()
        self.view = CollectView.collectView()   # 实例化主界面对象，传入了登录界面窗口
        self.view.show()                  # 主页面显示

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

# 如果直接运行的是当前文件__name__==__main__    __name__表示
if __name__=='__main__':
    # 实例化APP
    app = QApplication(sys.argv)
    # 实例化对象
    loginBox = LoginView()
    # 展示窗口
    loginBox.show()
    # 保证程序可以被关掉
    sys.exit(app.exec_())