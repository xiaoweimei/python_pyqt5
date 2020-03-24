from PyQt5.QtWidgets import *
import sys

class QLabelDemo(QDialog):
    def __init__(self):
        super(QLabelDemo, self).__init__()

        #设置标题
        self.setWindowTitle('Qlabel例子')
        #设置标签1的内容，并添加快捷键Alt+Q
        nameLb1=QLabel('&QQ',self)
        #建立单行文本输入框
        nameEd1=QLineEdit(self)
        #标签与文本框继续绑定,按快捷键Alt+Q可以定位到单行输入框
        nameLb1.setBuddy(nameEd1)

        #与前面相同
        nameLb2 = QLabel('&Password', self)
        nameEd2 = QLineEdit(self)
        nameLb2.setBuddy(nameEd2)

        #创建两个按钮，ok与cancel并添加快捷键
        btnok=QPushButton('&OK')
        btnCancel=QPushButton('&Cancel')

        #窗口布局栅格，分为一个个的格子，部件放在格子内
        mainLayout=QGridLayout(self)



        #布局内标签初始坐标设置（标签，格子0行，格子0列）默认标签大小显示
        mainLayout.addWidget(nameLb1,0,0)
        #文本框初始坐标设置（文本输入框，格子0行，格子1列，所占位置起始格子1，结束格子2）
        mainLayout.addWidget(nameEd1,0,1,1,2)

        mainLayout.addWidget(nameLb2, 1, 0)
        mainLayout.addWidget(nameEd2, 1, 1, 1, 2)

        mainLayout.addWidget(btnok, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

    def link_hovered(self):
        print('当用鼠标点击label2标签时，触发事件')

    def link_clicked(self):
        print('当用鼠标点击label4标签时，触发事件')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=QLabelDemo()
    win.show()
    sys.exit(app.exec_())
