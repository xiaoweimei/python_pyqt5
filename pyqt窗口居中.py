import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
 
class Example(QWidget):
 
 def __init__(self):
  super().__init__()
 
  self.initUI()
 
 def initUI(self):
 
  #self.setGeometry(300, 300, 300, 220)
 
  self.center()
 
  self.setWindowTitle('窗口居中')  
  self.show()
 
 def center(self):
 
  qr = self.frameGeometry()
  cp = QDesktopWidget().availableGeometry().center()
  qr.moveCenter(cp)
  self.move(qr.topLeft())
 
if __name__ == '__main__':
 
 app = QApplication(sys.argv)
 ex = Example()
 sys.exit(app.exec_())
