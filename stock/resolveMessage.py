# -*- coding:utf-8 -*-
#解析发送来的消息的
from itchat.storage import Chatroom

from getSock import *
from sqlliteWoker import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def resolveMessage(msgContent):
    match = re.match(".+?股票\s*[0-9]{6}".decode("utf8"),msgContent.Content)
    if match == None:
        return getStockPrintFromText(msgContent.Content)
    else:
        if isinstance(msgContent.User, Chatroom):
            stockNumber = re.compile(r'(600[0-9]{3})').findall(msgContent.Content)
            topprice = re.compile('.+?高\s*([0-9]{1,}\.[0-9]{2})'.decode("utf8")).findall(msgContent.Content)
            bottomPrice = re.compile('.+?低\s*([0-9]{1,}\.[0-9]{2})'.decode("utf8")).findall(msgContent.Content)

            saveInfo(msgContent.ActualNickName, msgContent.ActualUserName, stockNumber[0]
                     , topprice[0], bottomPrice[0], msgContent.User.NickName, msgContent.User.UserName )



if __name__ == '__main__':
    re_match = re.match(".+?股票.+?[0-9]{6}".decode("utf8"), "股票600027")
    match = re.match("[\u80a1\u7968]","这里的股票")
    match = re.match(".+?股票.+[0-9]{6}","这里的股票ge600029").group()
    match = re.match("[gup]","gjeiegi gupge")
