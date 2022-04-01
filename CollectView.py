# @File  : CollectView.py
# @Author: Zeng Yixuan
# @Date  :  2019/12/01

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit
import collectFaces


class collectView(QWidget):
    def __init__(self):
        # 属性父窗口
        super(collectView,self).__init__()
        self.initUI()
        self.collect = collectFaces


    def initUI(self):
        self.resize(400,400)
        self.setWindowTitle("人脸采集")
        self.label = QLabel(self)
        self.label.setFixedSize(128,128)
        self.label.move(132,50)
        self.userlabel = QLabel("用户名id:",self)
        self.userlabel.setStyleSheet("font-size:18px;font-weight:normal;font-family:楷体")
        self.userlabel.move(165,190)
        self.userlabel.setFixedHeight(25)
        self.username = QLineEdit(self)
        self.username.move(132,220)
        self.collectbtn = QPushButton("开始采集", self)
        self.collectbtn.setStyleSheet("font-size:18px;font-weight:normal;font-family:楷体;background-color:rgb(255,215,0)")
        self.collectbtn.move(160,250)
        self.collectbtn.clicked.connect(lambda:collectFaces.CollectFaces(self))
        jpg = QtGui.QPixmap("admins.png")
        self.label.setPixmap(jpg)
        self.setStyleSheet("background-color:white")




