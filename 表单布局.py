#coding = 'utf-8'

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):


        formlayout = QFormLayout()
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("啦啦啦")
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")

        formlayout.addRow(nameLabel,nameLineEdit)
        formlayout.addRow(introductionLabel,introductionLineEdit)
        self.setLayout(formlayout)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    print()
    app.exit(app.exec_())
