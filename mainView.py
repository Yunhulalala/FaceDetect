# @File  : mainView_Two.py
# @Author: Zeng Yixuan
# @Date  :  2019/11/22

import sys
import time
import cv2
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QLabel, QFileDialog, QLineEdit


class MainView(QWidget):
    def __init__(self):
        # 属性父窗口
        self.parent= self.parent
        super(MainView,self).__init__()
        self.now_img=""
        self.initUI()
        self.uniq = 0
        self.img_op = ImgOption()  # 在类中实例化对象

    def initUI(self):
        self.uniq=0
        self.setStyleSheet("backeground-color:pink")
        self.setWindowTitle("Main")
        self.resize(500,500)
        layout = QVBoxLayout()   # 总体布局：垂直布局
        self.setLayout(layout)
        top_layout=QHBoxLayout()      # 上方布局：水平布局
        self.top = QWidget(self)
        self.top.setLayout(top_layout)
        self.top.setMaximumHeight(50)
        self.open_file=QPushButton("打开文件",self)
        self.open_file.clicked.connect(self.open_image)  # 把打开图片槽函数绑定到打开图片按钮
        self.rotate1 = QPushButton("顺时针旋转",self)
        self.rotate1.clicked.connect(lambda :self.img_op.rotata(self, self.now_img,1))
        self.rotate2 = QPushButton("逆时针旋转",self)
        self.rotate2.clicked.connect(lambda :self.img_op.rotata(self, self.now_img,0))
        self.x = QPushButton("x轴翻折",self)
        self.x.clicked.connect(lambda :self.img_op.fold(self,self.now_img,0))
        self.y = QPushButton("y轴翻折",self)
        self.y.clicked.connect(lambda :self.img_op.fold(self,self.now_img,1))
        self.o = QPushButton("中心对称",self)
        self.o.clicked.connect(lambda :self.img_op.fold(self,self.now_img,-1))
        self.open_file.setStyleSheet("QPushButton{background-color:white}")
        top_layout.addWidget(self.open_file)
        top_layout.addWidget(self.rotate1)
        top_layout.addWidget(self.rotate2)
        top_layout.addWidget(self.x)
        top_layout.addWidget(self.y)
        top_layout.addWidget(self.o)
        layout.addWidget(self.top)
        # 中间布局
        self.middle = QWidget(self)
        self.middle.setMaximumHeight(50)
        mid_layout = QHBoxLayout(self)
        self.middle.setLayout(mid_layout)
        self.label_one = QLabel("x1", self)
        self.x1 = QLineEdit(self)
        self.label_two = QLabel("y1", self)
        self.y1 = QLineEdit(self)
        self.label_three = QLabel("x2", self)
        self.x2 = QLineEdit(self)
        self.label_four = QLabel("y2", self)
        self.y2 = QLineEdit(self)
        self.drawBtn = QPushButton("绘制", self)
        self.drawBtn.clicked.connect(lambda: self.img_op.draw_rec(self))
        mid_layout.addWidget(self.label_one)
        mid_layout.addWidget(self.x1)
        mid_layout.addWidget(self.label_two)
        mid_layout.addWidget(self.y1)
        mid_layout.addWidget(self.label_three)
        mid_layout.addWidget(self.x2)
        mid_layout.addWidget(self.label_four)
        mid_layout.addWidget(self.y2)
        mid_layout.addWidget(self.drawBtn)
        layout.addWidget(self.middle)
        self.showView = QLabel(self)
        self.showView.setStyleSheet("width:500px;height:500px;background-color:white")
        layout.addWidget(self.showView)

    def open_image(self):
        self.now_img, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "")
        # 时间戳
        self.uniq = str(int(time.time()))
        print(self.now_img)
        jpg = QtGui.QPixmap(self.now_img).scaled(self.showView.width(), self.showView.height())
        self.showView.setPixmap(jpg)

class ImgOption(object):
    def __init__(self):
        pass

    def rotata(self, win, src, type):
        """
        顺时针旋转
        :param type: 旋转类型:1：顺时针，0：逆时针
        :return:
        """
        img = cv2.imread(src)
        res1 = cv2.transpose(img)
        res2 = cv2.flip(res1, type)
        win.now_img = "./"+win.uniq+"rotate01.jpg"
        print(win.now_img)
        cv2.imwrite(win.now_img, res2)
        jpg1 = QtGui.QPixmap(win.now_img).scaled(win.showView.width(), win.showView.height())
        win.showView.setPixmap(jpg1)

    def fold(self,win,src, type):
        '''
        对折
        :param type: 翻折类型：0表示关于x轴进行翻折,1表示关于y进行翻折，-1表示关于原点翻折
        :return:
        '''
        img = cv2.imread(src)
        res = cv2.flip(img, type)
        win.now_img = "./"+win.uniq+"fold01.jpg"
        print(win.now_img)
        cv2.imwrite(win.now_img, res)
        jpg1 = QtGui.QPixmap(win.now_img).scaled(win.showView.width(), win.showView.height())
        win.showView.setPixmap(jpg1)

    def draw_rec(self,win):
        img=cv2.imread(win.now_img)
        x1 = int(win.x1.text())
        y1 = int(win.y1.text())
        x2 = int(win.x2.text())
        y2 = int(win.y2.text())
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        win.now_img = "./" + win.uniq + "draw.jpg"
        cv2.imwrite(win.now_img, img)
        jpg1 = QtGui.QPixmap(win.now_img).scaled(win.showView.width(), win.showView.height())
        win.showView.setPixmap(jpg1)


if __name__=='__main__':
    # 实例化APP
    app = QApplication(sys.argv)
    # 实例化对象
    regBox = MainView()
    # 展示窗口
    regBox.show()
    # 保证程序可以被关掉
    sys.exit(app.exec_())

    img = cv2.imread("./woman.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 转化为灰度模式
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 脸部识别
    faces = cascade_face.detectMultiScale(gray, 1.2, 5, cv2.CASCADE_SCALE_IMAGE)
    print(faces)  # 人脸左上角x1，y1， width， height
    for x, y, width, height in faces:
        print(x, y, width, height)
        x2 = x + width
        y2 = y + height
        cv2.rectangle(img_rgb, (x, y), (x2, y2), (255, 0, 0), 2)
        plt.imshow(img_rgb)
        plt.show()
