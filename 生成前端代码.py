def tablename():
    return '<h2 align=center><font color=red>{}</h2>'
def generateTable(tablename):
    if(tablename.rowCount()==0 or tablename.columnCount()==0):
        return ''
    a='<div><table><thead><tr>'
    for i in range(row):
        b='<th>{}</th>'*tablename.columnCount()
        p='<td>{}</td>'*tablename.columnCount()
    c='</tr></thead><tbody>'
    for i in range(column):
        dd=('<tr>'+p+'</tr>')*tablename.rowCount()
    gg='</tbody></table></div>'
    return a+b+c+dd+gg
def getTableValue(tablename):
    returnList=[]
    if(tablename.rowCount()==0 or tablename.columnCount()==0):
        return returnList
    for i in tablename.rowCount():
        for j in tablename.columnCount():
            returnList.append(tablename.item(i,j).text())
    return returnList
