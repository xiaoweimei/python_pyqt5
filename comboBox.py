from PyQt5.Qt import * #刚开始学习可以这样一下导入
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox的学习")
        self.resize(400,400)
        self.set_ui()


    def set_ui(self):
        self.comboBox = QComboBox(self)
        self.comboBox.resize(100,30)
        self.comboBox.move(100,100)

        self.test()
        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(0,300)

        btn.clicked.connect(self.slot_test)

    def slot_test(self):
        ############################设置弹出列表###############################

        self.comboBox.showPopup()
        #它的用途是，自己自定义一个控制，然后通过点击自定义的也能弹出下拉框

        ############################设置弹出列表###############################
        
    def test(self):
        self.comboBox.addItems(["xx1","xx2","xx3"])

        self.comboBox.insertItem(1,QIcon("icon/view.png"),"xxx4")

        ############################常规操作###############################
        self.comboBox.setEditable(True)

        self.comboBox.setDuplicatesEnabled(True)  # 设置可重复

        self.comboBox.setFrame(False)  #将框架去掉

        self.comboBox.setIconSize(QSize(60,60))

        ############################尺寸调整策略###############################
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents) #参照最长的长度

        ############################尺寸调整策略###############################

        # self.comboBox.clear()  #清空所有项目
        # self.comboBox.clearEditText()  #清空编辑的文本


        ############################常规操作###############################
if __name__ == '__main__':
    app =QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
