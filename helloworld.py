# -*- coding: UTF-8 -*-
from  PAM30 import PAMIE
import time
testURL = "http://127.0.0.1/phpcms/index.php?m=comment&c=index&a=init&commentid=content_6-1807-1&iframe=1"
content = "nihao shijie!"
def iepost(item,content):
    ie = PAMIE()
    ie.navigate(item)
    ie.setTextArea("content",content)
    ie.clickButton("发表评论")
    time.sleep(5)
    ie.quit()
iepost(testURL,content)