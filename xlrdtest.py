# -*- coding: UTF-8 -*-
'''
Created on 2012-9-11

@author: Administrator
'''
import xlrd
data = xlrd.open_workbook('E:\Book1.xls')
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    print table.row_values(i)
_str=repr(u'害怕')
print _str         #u\'u60a8'
print eval(_str)