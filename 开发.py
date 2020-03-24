#coding: utf-8
#本工具基于python3.7 和 PyQt5 开发
#pip3.7 install   ==5.10.1     更高版本的pyqt不包含PyQt5.QtWebEngineWidgets模块
#PyQt5 有四种布局：水平（QHBoxLayout）、竖直（QVBoxLayout）、网格（QGridLayout）、表单（QFormLayout）
import sys
  
from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout,QGroupBox
  
  
# 先来个窗口
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
  
    def setup(self):
        #self.box = QVBoxLayout(self)                      # 创建一个垂直布局来放控件
        self.allbox = QVBoxLayout(self)                     #全局布局：垂直
        self.btn_box = QHBoxLayout(self)                      #创建局部布局
        self.info_box = QHBoxLayout(self)
        self.btn_get = QPushButton('点击获取cookies')   # 创建一个按钮用来点击获取cookie
        self.btn_info = QPushButton('测试按钮')   # 创建一个按钮用来点击获取cookie
        self.style = """
                        QPushButton{color:black}
                        QPushButton:hover{color:red}
                        QPushButton:checked{color:red}
                        QPushButton{background-color:rgb(78,255,255)}
                        QPushButton{border:2px}
                        QPushButton{border-radius:10px}
                        QPushButton{padding:2px 4px}
                     """
        self.setStyleSheet(self.style)#设置按钮的样式
        self.btn_get.clicked.connect(self.get_cookie)     # 绑定按钮点击事件
        self.web = MyWebEngineView()                      # 创建浏览器组件对象,链接到get_cookie函数
        #self.web.resize(1100, 600)                         # 设置大小
        self.setGeometry(300, 300, 1000, 700)               #设置窗口的位置和大小
        self.setWindowTitle('支付宝浏览器')                      #设置窗口的标题
        self.web.load(QUrl("https://www.alipay.com/"))  # 打开支付宝页面
        #布局添加控件
        self.btn_box.addWidget(self.btn_get)        # 将组件放到布局内，先在顶部放一个按钮  
        self.btn_box.addWidget(self.btn_info)
        self.info_box.addWidget(self.web)                         # 再放浏览器
        #准备2个部件
        self.header_btn = QWidget()
        self.content_info = QWidget()
        #2个部件设置局部布局
        self.header_btn.setLayout(self.btn_box)
        self.content_info.setLayout(self.info_box)
        #2个部件加载至全局布局
        self.allbox.addWidget(self.header_btn)
        self.allbox.addWidget(self.content_info)
        self.setLayout(self.allbox)
        self.web.show()                                   # 最后让页面显示出来
  
    def get_cookie(self):
        cookie = self.web.get_cookie()
        print('获取到cookie: ', cookie)
  
  
# 创建自己的浏览器控件，继承自QWebEngineView
class MyWebEngineView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(MyWebEngineView, self).__init__(*args, **kwargs)
        # 绑定cookie被添加的信号槽
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        self.cookies = {}          # 存放cookie字典
  
    def onCookieAdd(self, cookie):                       # 处理cookie添加的事件
        name = cookie.name().data().decode('utf-8')     # 先获取cookie的名字，再把编码处理一下
        value = cookie.value().data().decode('utf-8')   # 先获取cookie值，再把编码处理一下
        self.cookies[name] = value                       # 将cookie保存到字典里
  
    # 获取cookie
    def get_cookie(self):
        cookie_str = ''
        for key, value in self.cookies.items():         # 遍历字典
            cookie_str += (key + '=' + value + ';')     # 将键值对拿出来拼接一下
        return cookie_str                               # 返回拼接好的字符串
  
  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())
