#!/usr/bin/env python
#coding:utf-8 

import cx_Oracle  
import csv  
import xlrd  

class ImportOracle(object):  
    def inoracle(self):  
        pass  

    def ConnOracle(self):  
        conn = cx_Oracle.connect('stat_yg/yg12345@cd')  
        cursor = conn.cursor()  

        fields = [i+' varchar2(200)' for i in self.title]  
        fields_str = ', '.join(fields)  
        sql = 'create table %s (%s)' % (self.table_name, fields_str)  
        print sql  
        cursor.execute(sql)  

        a = [':%s' %i for i in range(len(self.title)+1)]  
        value= ','.join(a[1:])  
        sql = 'insert into %s values(%s)' %(self.table_name, value)  
        print sql  

        cursor.prepare(sql)  
        cursor.executemany(None, self.data)  

        cursor.close()  
        conn.commit()  
        conn.close()  



class ImportOracleCsv(ImportOracle):  
    def inoracle(self):  
        with open(self.filename, 'rb') as f:  
            reader = csv.reader(f)  
            contents = [i for i in reader]  

        title = contents[0]  
        data = contents[1:]  

        return (title, data)  

class ImportOracleExcel(ImportOracle):  
    def inoracle(self):  
        wb = xlrd.open_workbook(self.filename)  
        sheet1 = wb.sheet_by_index(0)  

        title = sheet1.row_values(0)  
        data = [sheet1.row_values(row) for row in range(1, sheet1.nrows)]  
        return (title, data)  

class ImportError(ImportOracle):  
    def inoracle(self):  
        print 'Undefine file type'  
        return 0         


class ChooseFactory(object):  
    choose = {}  
    choose['csv'] = ImportOracleCsv()  
    choose['xlsx'] = ImportOracleExcel()  
    choose['xls'] = ImportOracleExcel()  

    def choosefile(self, ch):  
        if ch in self.choose:  
            op = self.choose[ch]  
        else:  
            op = ImportError()  

        return op  

if __name__ =="__main__":  
    file_name = '11.csv'  
    table_name= 'ygl_test111'  
    op = file_name.split('.')[-1]  
    factory = ChooseFactory()  
    cal = factory.choosefile(op)  
    cal.filename = file_name  
    (cal.title, cal.data) = cal.inoracle()  
    cal.table_name = table_name  
    cal.ConnOracle()  