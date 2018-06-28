# mysql
import pymysql
import os
# 读excel
import xlrd

baseDir = 'C:/Users/yangzhi/Desktop/E宁波注册用户信息采集-原始-15306663750'
connectInfo = {
    "host": '192.168.71.109',
    'port': 3306,
    'user': 'root',
    'passwd': 'grid',
    'db':'nbgrid'
}


def exeSql(sql):
    db = pymysql.connect(host=connectInfo['host'], port=connectInfo['port'], user=connectInfo['user'],
                         passwd=connectInfo['passwd'],db=connectInfo['db'])
    # 获取游标对象
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def readExcel(fileName):
    excelFile = xlrd.open_workbook(fileName)
    result = []
    sheet = excelFile.sheet_by_index(0)
    # 标题行
    rowNum = sheet.nrows
    for i in range(1, rowNum):
        rowVal = []
        row = sheet.row_values(i)
        for r in row:
            r = str(r).replace('[\u3000 ]', '')
            rowVal.append(r)
        result.append(rowVal)
    print(result)


def getFiles(path):
    files = []
    for filePath in os.listdir(path):
        print(filePath)


if __name__ == '__main__':
    #readExcel(baseDir + '/' + '镇海区.xls')
    res = exeSql('select * from grid_datebase_nb_corporateservice_info;')
    print(res)
