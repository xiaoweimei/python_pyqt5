
#一：存表格数据
##savefile_btn_Clicked方法
s = {}
##update方法可以合并字典
s.update(self.addData(self.tableWidget0, 1))
s.update(self.addData(self.tableWidget1, 2))
s.update(self.addData(self.tableWidget2, 3))
s.update(self.addData(self.tableWidget3, 4))
s.update(self.addData(self.tableWidget4, 5))
s.update(self.addData(self.tableWidget5, 6))
s.update(self.addData(self.tableWidget6, 7))
s.update(self.addData(self.tableWidget7, 8))
s.update(self.addData(self.tableWidget8, 9))
s.update(self.addData(self.tableWidget9, 10))
s.update(self.addData(self.tableWidget10, 11))
s.update(self.addData(self.tableWidget11, 12))
s.update(self.addData(self.tableWidget12, 13))
s.update(self.addData(self.tableWidget13, 14))
s.update(self.addData(self.tableWidget14, 15))
s.update(self.addData(self.tableWidget15, 16))
s.update(self.addData(self.tableWidget16, 17))

###添加数据到字典中
def addData(self, i, pp):
    s = {}
    d1 = []
    rows = i.rowCount()
    lie = i.columnCount()
    for rows_index in range(rows):
        d = []
        for lie_index in range(lie):
            try:
                if (i.item(rows_index, lie_index) == None):
                    d.append('')
                else:
                    # print(f'第{rows_index}行第{lie_index}列的表格的值为:{data}')
                    d.append(
                        str(base64.b64encode(i.item(rows_index, lie_index).text().encode()),
                            encoding="utf-8"))

            except Exception as e:
                print('except:', e)

        d1.append(d)
    s[pp] = d1

    return s



##添加bg字典,值为上面的s字典
    keylist = ['xm', 'xb', 'mz', 'zzmm', 'sfzh', 'dhhm','bg']
     valuelist = [xm, xb, mz, zzmm, sfzh, dhhm,s]



#二：取表格数据

## def mysignalslot(self,dict)方法
bgdata = dict['bg']
for k, v in bgdata.items():
    # print(type(k))
    # 对二维数组进行遍历i
    len1 = len(v)
    for i in range(len1):
        # 获取每一表格每一行的数据（一维数组）
        vv = v[i]
        len2 = len(vv)
        # print(f'{vv}',end=',')
        for j in range(len2):
            # 对每一个表格单位的数据都进行解密
            vvv = vv[j]
            # print(f'{vvv}', end=',')
            biaoge = base64.b64decode(bytes(vvv, encoding="utf8")).decode("utf-8")
            print(f'第{k}的字典第{i}个数组中第{j}个数的值解密后的值为:{biaoge}')
            data = QTableWidgetItem(biaoge)
            # 根据不同的表格赋值给每个表格遍历赋值
            if (k == '1'):
                self.tableWidget0.setItem(i, j, data)
            elif (k == '2'):
                self.tableWidget1.setItem(i, j, data)
            elif (k == '3'):
                self.tableWidget2.setItem(i, j, data)
            elif (k == '4'):
                self.tableWidget3.setItem(i, j, data)
            elif (k == '5'):
                self.tableWidget4.setItem(i, j, data)
            elif (k == '6'):
                self.tableWidget5.setItem(i, j, data)
            elif (k == '7'):
                self.tableWidget6.setItem(i, j, data)
            elif (k == '8'):
                self.tableWidget7.setItem(i, j, data)
            elif (k == '9'):
                self.tableWidget8.setItem(i, j, data)
            elif (k == '10'):
                self.tableWidget9.setItem(i, j, data)
            elif (k == '11'):
                self.tableWidget10.setItem(i, j, data)
            elif (k == '12'):
                self.tableWidget11.setItem(i, j, data)
            elif (k == '13'):
                self.tableWidget12.setItem(i, j, data)
            elif (k == '14'):
                self.tableWidget13.setItem(i, j, data)
            elif (k == '15'):
                self.tableWidget14.setItem(i, j, data)
            elif (k == '16'):
                self.tableWidget5.setItem(i, j, data)
            elif (k == '17'):
                self.tableWidget16.setItem(i, j, data)



        xmm=self.xmLineEdit.text()#姓名
        xbb = self.comboxb.currentText()#性别
        csnyny = self.csnytime.text()#出生年月
        xll=self.comboxl.currentText()#学历
        zzmmmm = self.combozzmm.currentText()#政治面貌
        rdsjsj = self.rdsjtime.text()#入党时间
        mzz = self.combomz.currentText()  # 民族
        zyjszc = self.zyjszcLineEdit.text()#专业技术职称
        dhhmdh1 = self.dhhm1LineEdit.text()  # 电话号码1
        dhhmdh2 = self.dhhm2LineEdit.text()  # 电话号码2
        sfzhsf = self.sfzhLineEdit.text()#身份证号
        hjdzdz = self.hjdzLineEdit.text()#户籍地址
        jgjg = self.jgLineEdit.text()#籍贯
        csdcsd = self.csdLineEdit.text()#出生地
        dbdwsjsj = self.rbdwsjtime.text()#入本单位时间
        xgzdwdw = self.xgzdwLineEdit.text() #现工作单位
        zwzw = self.zwLineEdit.text() #职务
        hyxzxz = self.combohyxz.currentText()#婚姻现状
        xjzdzdz = self.xjzdzLineEdit.text()#现居住地址
        qtsxsx = self.qtsxtextEdit.toPlainText()#最后一条的其他事项

with open("C:\\Users\\root\\Desktop\\0.jpg", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    print('data:image/jpeg;base64,%s'%s)
