from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout,QPushButton,QVBoxLayout,QComboBox,QLabel,QFileDialog,QHBoxLayout,QDialog,QDesktopWidget,QGroupBox
# from PyQt5 import QtGui
# font = QtGui.QFont()
# font.setFamily("Arial")
# font.setPointSize(18)
# QGroupBox("mywin").setFont(font)
import sys

class lineEditDemo(QWidget):
    def __init__(self,parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle('纪委')
        self.resize(1200,800)

        #全局布局
        wlayout=QVBoxLayout()
        #局部布局 水平布局和 垂直布局
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        hlayout3 = QHBoxLayout()
        hlayout4 = QHBoxLayout()
        hlayout5 = QHBoxLayout()
        hlayout6 = QHBoxLayout()
        vlayout=QVBoxLayout()
        
        #创建4个文本输入框
        self.name=QLineEdit()
        self.gender=QLineEdit()
        self.year=QLineEdit()
        self.id=QLineEdit()

        #添加到表单布局中
        #flo.addRow(文本名称（可以自定义），文本框)
        self.combo = QComboBox(self)
        typeLabel = QLabel("请选择你的人员类型")
        self.combo.addItem("")
        self.combo.addItem("村社干部")
        self.combo.addItem("雇员")
        self.combo.addItem("公务员")

        hlayout4.addWidget(typeLabel)
        hlayout4.addWidget(self.combo)
        
        self.combo1 = QComboBox(self)
        yearLabel = QLabel("请选择年度")
        self.combo1.addItem("")
        self.combo1.addItem("2020")
        self.combo1.addItem("2021")
        self.combo1.addItem("2022")
        hlayout5.addWidget(yearLabel)
        hlayout5.addWidget(self.combo1)
        #设置setPlaceholderText()文本框浮现的文字
        nameLabel = QLabel("请输入你的姓名")
        self.name.setPlaceholderText('姓名')

        hlayout1.addWidget(nameLabel)
        hlayout1.addWidget(self.name)
        
        
        genderLabel = QLabel("请输入你的性别")
        self.gender.setPlaceholderText('性别')

        hlayout2.addWidget(genderLabel)
        hlayout2.addWidget(self.gender)

        idLabel = QLabel("请输入你的身份证号")
        self.id.setPlaceholderText('身份证号')

        hlayout3.addWidget(idLabel)
        hlayout3.addWidget(self.id)
        

        
        self.label = QLabel(self)
        self.label.setText("显示图片")
        self.label.setFixedSize(300, 200)
        #self.label.move(400, 400)
        self.label.setStyleSheet("border:2px solid red;font-size:20px;text-align:center;")

        self.btnButton1=QPushButton('打开图片')
        self.btnButton1.clicked.connect(self.openimage)
        #点击确定校验是否符合规则
        self.btnButton=QPushButton('确定')
        # self.btnButton.clicked.connect(self.buttonClick)
        # self.btnButton.clicked.connect(self.onButtonClick)
        self.btnButton.clicked.connect(self.showsecond)
        #s=SecondWindow()
        #self.btnButton.clicked.connect(s.show)
        #self.btnButton.clicked.connect(self.buttonClick)
        #setEchoMode()：设置显示效果

        #QLineEdit.Normal：正常显示所输入的字符，此为默认选项

        
        layout = QVBoxLayout()
        #设置窗口的布局
        #wlayout.addWidget(hlayout1)
        #wlayout.addWidget(hlayout2)
        #wlayout.addWidget(hlayout3)
        #wlayout.addWidget(hlayout4)
        #wlayout.addWidget(hlayout5)

        
        wlayout.addWidget(self.name)
        wlayout.addWidget(self.gender)
   
        wlayout.addWidget(self.id)
        wlayout.addWidget(self.combo)
        wlayout.addWidget(self.combo1)
        wlayout.addWidget(self.btnButton1)
        wlayout.addWidget(self.label)
        wlayout.addWidget(self.btnButton)
        
        self.setLayout(wlayout)
    def buttonClick(self):
        print(self.name.text())
        print(self.gender.text())
        print(self.id.text())
        print(self.combo.currentText())
        print(self.combo1.currentText())
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")     
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        self.label.setScaledContents(True)

#判断条件，进入第二个表格
    def showsecond(self):
        print(self.name.text)
        print(self.gender.text())
        print(self.id.text())
        print(self.combo.currentText())
        print(self.combo1.currentText())
        if(self.name.text()==''):
            self.btn3 = QPushButton()
            self.btn3.setText("警告对话框")

            print(11111111111)
            pass
        else:
            self.hide()
            print("wdnmdsb")
            self.newwindow=SecondWindow()
            self.newwindow.show()


#按下确定按钮，关闭窗格

    def onButtonClick(self):
        sender=self.sender()
        print(sender.text()+'被按下了')
        qApp = QApplication.instance()
        qApp.quit()
#    def showsecond(self):
#        second = SecondWindow()
#        print("该功能被按下了")
#        second.show()
#        second.exec()
'''
第二个窗格
'''
class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.resize(1200, 800)
        self.setStyleSheet("background: #675622")
        self.center()
        #self.btn = QToolButton(self)
        #self.btn.setText("导出文件")
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #def handle_click(self):
        #if not self.isVisible():
            #self.show()

    # def handle_close(self):
    #     self.close()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    first=lineEditDemo()
    #second = SecondWindow()
    #first.btnButton.clicked.connect(second.show)
    #win.btnButton.clicked.connect(win.click)
    #win.btnButton.clicked.connect(win.buttonClick)
    #win.close_signal.connect(ex.close)
    first.show()
    sys.exit(app.exec_())
