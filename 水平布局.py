from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Form():
    def __init__(self):
        super(Form, self).__init__()

        layout = QHBoxLayout()
        layout.addWidget(QLabel("A"))
        layout.addWidget(QLabel("B"))
        layout.addWidget(QLabel("C"))
        layout.addWidget(QLabel("D"))

        self.setLayout(layout)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
