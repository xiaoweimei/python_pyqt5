# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class myDialog(QDialog):
    """docstring for myDialog"""
    def __init__(self, arg=None):
        super(myDialog, self).__init__(arg)
        self.setWindowTitle("first window")
        self.resize(500,300);
        conLayout = QVBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)
        #设置编辑内容只可读不可写
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows);
        self.topFiller = QWidget()
        
        tableWidget.setHorizontalHeaderLabels(['起始日期','截止日期','工作单位/学习单位','职务/所学专业'])
        tableWidget.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])
        ########################################################################
        #第二个表格
        ########################################################################
        tableWidget1=QTableWidget()
        tableWidget1.setRowCount(4)
        tableWidget1.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget1.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget1.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget1.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget1.setHorizontalHeaderLabels(['称谓','姓名','身份证号','政治面貌','工作单位','职务','单位性质','手机号码'])
        tableWidget1.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])
        conLayout.addWidget(tableWidget)
        conLayout.addWidget(tableWidget1)
        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        self.setLayout(conLayout)

        ########################################################################
        #第三个表格
        ########################################################################
        tableWidget2=QTableWidget()
        tableWidget2.setRowCount(4)
        tableWidget2.setColumnCount(2)
        #设置编辑内容只可读不可写
        tableWidget2.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget2.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget2.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget2.setHorizontalHeaderLabels(['变化情况','变化时间'])
        tableWidget2.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第四个表格
        ########################################################################
        tableWidget3=QTableWidget()
        tableWidget3.setRowCount(4)
        tableWidget3.setColumnCount(5)
        #设置编辑内容只可读不可写
        tableWidget3.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget3.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget3.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget3.setHorizontalHeaderLabels(['证件名称','证件号码','失效日期','发证机关','保管机构'])
        tableWidget3.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第五个表格
        ########################################################################
        tableWidget4=QTableWidget()
        tableWidget4.setRowCount(4)
        tableWidget4.setColumnCount(4)
        #设置编辑内容只可读不可写
        tableWidget4.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget4.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget4.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget4.setHorizontalHeaderLabels(['所到国家','出国境是由','出发时间','返回时间'])
        tableWidget4.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        
        ########################################################################
        #第六个表格
        ########################################################################
        tableWidget5=QTableWidget()
        tableWidget5.setRowCount(4)
        tableWidget5.setColumnCount(5)
        #设置编辑内容只可读不可写
        tableWidget5.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget5.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget5.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget5.setHorizontalHeaderLabels(['姓名','移居时间','移居地点','移居类别','所在单位及从事职业'])
        tableWidget5.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        
        ########################################################################
        #第七个表格
        ########################################################################
        tableWidget6=QTableWidget()
        tableWidget6.setRowCount(4)
        tableWidget6.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget6.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget6.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget6.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget6.setHorizontalHeaderLabels(['两者关系','使用人','车主姓名','来源','汽车型号与排量','购买(出售)时间','交易价格(万元)','车牌号码'])
        tableWidget6.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        
        ########################################################################
        #第八个表格
        ########################################################################
        tableWidget7=QTableWidget()
        tableWidget7.setRowCount(4)
        tableWidget7.setColumnCount(7)
        #设置编辑内容只可读不可写
        tableWidget7.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget7.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget7.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget7.setHorizontalHeaderLabels(['姓名','与本人关系','合同名称和签订时间','合同主要条款','前年收益(万元)','去年收益(万元)','今年收益(万元)'])
        tableWidget7.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第九个表格
        ########################################################################
        tableWidget8=QTableWidget()
        tableWidget8.setRowCount(4)
        tableWidget8.setColumnCount(9)
        #设置编辑内容只可读不可写
        tableWidget8.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget8.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget8.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget8.setHorizontalHeaderLabels(['产权人','与本人关系','房产来源(去向)','详细地址','房产证号','建筑面积(m2)','产权性质','交易时间','交易价格(万元)'])
        tableWidget8.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第十个表格
        ########################################################################
        tableWidget9=QTableWidget()
        tableWidget9.setRowCount(4)
        tableWidget9.setColumnCount(9)
        #设置编辑内容只可读不可写
        tableWidget9.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget9.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget9.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget9.setHorizontalHeaderLabels(['持有人','与本人关系','不动产来源','"四类不动产"详细地址','证件号码','建筑面积(m2)','不动产类型','不动产用途','取得使用权或所有权时间'])
        tableWidget9.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
                ########################################################################
        #第十一个表格
        ########################################################################
        tableWidget10=QTableWidget()
        tableWidget10.setRowCount(4)
        tableWidget10.setColumnCount(9)
        #设置编辑内容只可读不可写
        tableWidget10.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget10.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget10.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget10.setHorizontalHeaderLabels(['任职单位','职务','任职单位与本人所在单位关系'])
        tableWidget10.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第十二个表格
        ########################################################################
        tableWidget11=QTableWidget()
        tableWidget11.setRowCount(4)
        tableWidget11.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget11.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget11.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget11.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget11.setHorizontalHeaderLabels(['称谓','姓名','企业名称','注册地和经营地','注册资金(万元)','个人出资额(万元)','统一社会信用代码/注册号','备注'])
        tableWidget11.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第十三个表格
        ########################################################################
        tableWidget12=QTableWidget()
        tableWidget12.setRowCount(4)
        tableWidget12.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget12.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget12.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget12.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget12.setHorizontalHeaderLabels(['摄影/n(万元/全年)','讲学/n(万元/全年)','写作/n(万元/全年)','咨询/n(万元/全年)','审稿/n(万元/全年)','书画/n(万元/全年)','其他'])
        tableWidget12.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第十四个表格
        ########################################################################
        tableWidget13=QTableWidget()
        tableWidget13.setRowCount(4)
        tableWidget13.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget13.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget13.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget13.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget13.setHorizontalHeaderLabels(['接收时间','上交时间','名称','类型','价值(万元)'])
        tableWidget13.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第十五个表格
        ########################################################################
        tableWidget14=QTableWidget()
        tableWidget14.setRowCount(4)
        tableWidget14.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget14.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget14.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget14.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget14.setHorizontalHeaderLabels(['接收时间','上交时间','名称','品牌','数量'])
        tableWidget14.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第十六个表格
        ########################################################################
        tableWidget15=QTableWidget()
        tableWidget15.setRowCount(4)
        tableWidget15.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget15.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget15.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget15.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget15.setHorizontalHeaderLabels(['事宜','举办时间','举办地点','参加人数','总开支(万元)','邀请范围'])
        tableWidget15.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);
        ########################################################################
        #第十七个表格
        ########################################################################
        tableWidget16=QTableWidget()
        tableWidget16.setRowCount(4)
        tableWidget16.setColumnCount(8)
        #设置编辑内容只可读不可写
        tableWidget16.setEditTriggers(QAbstractItemView.NoEditTriggers);
        #隐藏垂直方向列表头
        tableWidget16.verticalHeader().setVisible(False);
        #设置选取行
        #tableWidget16.setSelectionBehavior(QAbstractItemView.SelectRows);

        
        tableWidget16.setHorizontalHeaderLabels(['处理类型','处理时间','处理原因','处理结果'])
        tableWidget16.setVerticalHeaderLabels(['va','vb','vc','vd','ve'])

        #for i in range(5):
            #for j in range(4):
                #可以在单元格中加入控件
                #comBox = QComboBox();
                #comBox.addItem("Y");
                #comBox.addItem("N");
                #tableWidget.setCellWidget(i,j,comBox);  
        #将行和列的大小设为与内容相匹配
        conLayout.addWidget(tableWidget)
        conLayout.addWidget(tableWidget1)
        conLayout.addWidget(tableWidget2)
        conLayout.addWidget(tableWidget3)
        conLayout.addWidget(tableWidget4)
        conLayout.addWidget(tableWidget5)
        conLayout.addWidget(tableWidget6)
        conLayout.addWidget(tableWidget7)
        conLayout.addWidget(tableWidget8)
        conLayout.addWidget(tableWidget9)
        conLayout.addWidget(tableWidget10)
        conLayout.addWidget(tableWidget11)
        conLayout.addWidget(tableWidget12)
        conLayout.addWidget(tableWidget13)
        conLayout.addWidget(tableWidget14)
        conLayout.addWidget(tableWidget15)
        conLayout.addWidget(tableWidget16)
        tableWidget.resizeColumnsToContents();
        tableWidget.resizeRowsToContents();
        tableWidget1.resizeColumnsToContents();
        tableWidget1.resizeRowsToContents();
        tableWidget2.resizeColumnsToContents();
        tableWidget2.resizeRowsToContents();
        tableWidget3.resizeColumnsToContents();
        tableWidget3.resizeRowsToContents();
        tableWidget4.resizeColumnsToContents();
        tableWidget4.resizeRowsToContents();
        tableWidget5.resizeColumnsToContents();
        tableWidget5.resizeRowsToContents();
        tableWidget6.resizeColumnsToContents();
        tableWidget6.resizeRowsToContents();
        tableWidget7.resizeColumnsToContents();
        tableWidget7.resizeRowsToContents();
        tableWidget8.resizeColumnsToContents();
        tableWidget8.resizeRowsToContents();
        tableWidget9.resizeColumnsToContents();
        tableWidget9.resizeRowsToContents();
        tableWidget10.resizeColumnsToContents();
        tableWidget10.resizeRowsToContents();
        tableWidget11.resizeColumnsToContents();
        tableWidget11.resizeRowsToContents();
        tableWidget12.resizeColumnsToContents();
        tableWidget12.resizeRowsToContents();
        tableWidget13.resizeColumnsToContents();
        tableWidget13.resizeRowsToContents();
        tableWidget14.resizeColumnsToContents();
        tableWidget14.resizeRowsToContents();
        tableWidget15.resizeColumnsToContents();
        tableWidget15.resizeRowsToContents();
        tableWidget16.resizeColumnsToContents();
        tableWidget16.resizeRowsToContents();
        scroll=QScrollArea()
        #scroll.setWidget(conLayout)
        conLayout.addWidget(scroll)
        #将内容载入页面
        self.setLayout(conLayout)
app = QApplication(sys.argv)
#全局设置QPushButton的背景样式
dlg = myDialog()
dlg.show()
dlg.exec_()
app.exit()
