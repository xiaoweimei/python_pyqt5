import sys,os,http.client
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json,base64,time,datetime
 # 图片路径
img_path=r'‪C:\Users\root\Desktop\0.jpg'
# 设置展示控件
pic_show_label =QLabel()
# 设置窗口尺寸
pic_show_label.resize(500,500)
# 加载图片,并自定义图片展示尺寸
image = QPixmap(img_path).scaled(400, 400)
# 显示图片
pic_show_label.setPixmap(image)
pic_show_label.show()
