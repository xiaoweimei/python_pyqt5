import sys,os,http.client
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json,base64,time,datetime

text = QByteArray(b"Qt is great!")
print(text,type(text))
text1=text.toBase64()
print(text1,type(text1))
text2 = QByteArray.fromBase64(b"UXQgaXMgZ3JlYXQh")
print(text2,type(text2))
png1=QPixmap(r'‪C:\Users\root\Desktop\0.jpg')
print(type(png1))
print(1234567)
print(7654321)
