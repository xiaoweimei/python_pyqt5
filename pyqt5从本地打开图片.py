import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(600, 400)
        self.setWindowTitle("label显示图片")

        self.label = QLabel(self)
        self.label.setText("   显示图片")
        self.label.setFixedSize(300, 200)
        self.label.move(160, 160)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        btn = QPushButton(self)
        btn1 = QPushButton(self)
        btn.setText("打开图片")
        btn1.setText("更换图片")
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)
        btn1.clicked.connect(self.replaceimage)
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        print(imgName,type(imgName))
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
    def replaceimage(self):
        JPG1=r'C:\Users\root\Desktop\0.jpg'
        jpg = QtGui.QPixmap(JPG1).scaled(self.label.width(), self.label.height())
        print(1111111111111111111111111111111)
        print(type(QtGui.QPixmap(JPG1)))
        print(type(jpg))
        self.label.setPixmap(jpg)
        pass
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
