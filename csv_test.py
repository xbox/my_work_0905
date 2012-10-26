# -*- coding: UTF-8 -*-
import csv
from  PAM30 import PAMIE
import time
import xlrd
def iepost(link,content):
    ie = PAMIE()
    ie.navigate(link)
    ie.setTextArea("content",content)
    ie.clickButton("发表评论")
    time.sleep(4)
    ie.quit()
data = xlrd.open_workbook('E:\Book1.xls')
table = data.sheets()[0]
nrows = table.nrows
table2 = data.sheets()[1]

for line in range(nrows):
    testContent = str(table.row_values(line))
    testURL = str(table2.row_values(line))
    testURL2 = testURL.split("'")[1]
    testContent2 = eval(testContent[1:-1])
#    print eval(testContent[1:-1])
#    print testURL2
    iepost(testURL2,testContent2)
#    print type(content)
#    testURL = "http://127.0.0.1/phpcms/index.php?m=comment&c=index&a=init&commentid=content_6-1807-1&iframe=1"
#    iepost(testURL,content)
