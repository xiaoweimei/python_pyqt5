#-*- coding:utf-8 -*-
 
import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,  QTableWidget,QHBoxLayout, QTableWidgetItem, QComboBox,QFrame
from PyQt5.QtGui import QFont,QColor,QBrush,QPixmap
class TableSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
 
    def initUi(self):
        horizontalHeader = ["工号","姓名","性别","年龄","职称"]
        
        self.table = QTableWidget() # 也可以QTableWidget(5,2)
        self.table.setColumnCount(5) # 5列
        self.table.setRowCount(2) # 3行
        # 隐藏垂直的表头，self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(horizontalHeader) # 水平表头，垂直表头setVerticalHeaderLabels()
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
 
        # QTableWidget.SelectRows 1 选中一行 
        # QTableWidget.SelectColumns 2 选中一列
        self.table.setSelectionBehavior(QTableWidget.SelectColumns)
 
        self.table.setSelectionMode(QTableWidget.SingleSelection  )
 
        # 表头也是由多个item构成的，所以通过循环操作对每一个item进行操作
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            # 单元格对齐方式：
            # 水平方向： 
            # Qt.AlignLeft 0x000  左对齐
            # Qt.AlignRight 0x0002 右对齐
            # Qt.AlignHCenter 0x0004 居中对齐
            # Qt.AlignJustify 0x0008 
            # 垂直方向： 
            # Qt.AlignTop 0x0020 上对齐
            # Qt.AlignBottom 0x0040 下对齐
            # Qt.AlignVCenter 0x0080 居中
            headItem.setTextAlignment(0x000 | Qt.AlignVCenter)
 
        # 根据内容自动调整单元格大小
        # self.table.resizeColumnsToContents()
        # self.table.resizeRowsToContents()
        self.table.setColumnWidth(4,200) # 设置第5列宽度200
        self.table.setRowHeight(0,40) # 设置第一行高度40
 
        self.table.setFrameShape(QFrame.HLine)#设定样式
        #self.table.setShowGrid(False)  # False不显示网格线，True显示网格线
 
        # 添加内容
        self.table.setItem(0,0, QTableWidgetItem("001"))
        self.table.setItem(0,1,QTableWidgetItem("Tom"))
        # 表项——添加自定义控件
        genderComb = QComboBox()
        genderComb.addItem("男性")
        genderComb.addItem("女性")
        genderComb.setCurrentIndex(0)
        self.table.setCellWidget(0,2,genderComb)
 
        self.table.setItem(0,3,QTableWidgetItem("30"))
        self.table.setItem(0,4,QTableWidgetItem("产品经理"))
 
        self.table.setItem(1,0, QTableWidgetItem("005"))
        self.table.setItem(1,1,QTableWidgetItem("Kitty"))
        genderComb = QComboBox()
        genderComb.addItem("男性")
        genderComb.addItem("女性")
        genderComb.setCurrentIndex(1)
        self.table.setCellWidget(1,2,genderComb)
        self.table.setItem(1,3,QTableWidgetItem("24"))
        self.table.setItem(1,4,QTableWidgetItem("程序猿安慰师"))
 
        self.table.horizontalHeader().sectionCliced.connect(self.HorSectionClicked)
        self.table.verticalHeader().sectionClicked.connect(self.VerSectionClicked)#表头单击信号
         
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.table)
        self.setLayout(mainLayout)
    def HorSectionClicked(self,index):
        print(index)
    def VerSectionClicked(self,index):
        print(index)
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    table = TableSheet()
    table.setWindowTitle('TableWidget Usage')
    table.resize(700,300)
    table.show()
    sys.exit(app.exec_())
