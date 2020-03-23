from PyQt5 import QtGui, QtCore

class Images():
    def __init__(self, images):
        super().__init__()

        self.content = QtGui.QWidget()
        self.layout = QtGui.QGridLayout(self.content)
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        col = 0
        for image in images:
            thumb = QtGui.QLabel()
            thumb.setPixmap(QtGui.QPixmap(image))
            self.layout.addWidget(thumb, 0, col)
            col += 1

        self.setWidget(self.content)
        self.setMinimumWidth(self.content.sizeHint().width())
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

app = QtGui.QApplication([])

window = QtGui.QWidget()
layout = QtGui.QVBoxLayout(window)
scroll_area = Images(['test.png','test.png','test.png','test.png'])
layout.addWidget(scroll_area)
window.show()

app.exec_()
