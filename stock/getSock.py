# -*- coding:utf-8 -*-
import sys,urllib,urllib2
import re

#http://blog.csdn.net/simon803/article/details/7784682
def getStockPrintFromText(stockNumber):
    search = re.compile(r'(600[0-9]{3})').findall(stockNumber)
    if len(search) == 0:
        return u'股票号码错误！'
    else:
        result = "";
        for n in search:
            result += getStockPriceInfo(n)
        return result;


def getStockPriceInfo(stockNumber):

    url = "http://hq.sinajs.cn/list=sh" + stockNumber;
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
    result = ""

    while True:
        date = fd.read(1024)
        if not len(date):
            break
        result =  date

    # print result
    send = result.split("=")[1].split(",")
    changeLine = u'\n'
    stockResult = u'股票:' + send[0].decode("gbk") + changeLine

    stockResult += u'今日开盘'  + send[1].decode("gbk") + changeLine
    stockResult += u'昨日收盘' + send[2].decode("gbk") + changeLine
    stockResult += u'当前价格' + send[3].decode("gbk") + changeLine
    stockResult += u'今日最高价' + send[4].decode("gbk") + changeLine
    stockResult += u'今日最低价' + send[5].decode("gbk") + changeLine
    stockResult += u'买一报价' + send[11].decode("gbk") + changeLine
    stockResult += u'买二报价' + send[13].decode("gbk") + changeLine
    stockResult += u'买三报价' + send[15].decode("gbk") + changeLine
    stockResult += u'买四报价' + send[17].decode("gbk") + changeLine
    stockResult += u'买五报价' + send[19].decode("gbk") + changeLine

    stockResult += u'卖一报价' + send[21].decode("gbk") + changeLine
    stockResult += u'卖二报价' + send[23].decode("gbk") + changeLine
    stockResult += u'卖三报价' + send[25].decode("gbk") + changeLine
    stockResult += u'卖四报价' + send[27].decode("gbk") + changeLine
    stockResult += u'卖五报价' + send[29].decode("gbk") + changeLine

    return stockResult

def getStockPrice(stockNumber):
    url = "http://hq.sinajs.cn/list=sh" + stockNumber;
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
    result = ""

    while True:
        date = fd.read(1024)
        if not len(date):
            break
        result = date

    # print result
    send = result.split("=")[1].split(",")
    # 股票名字 當前價
    return [send[0],send[3]]

# 判斷
def dujest(stockNumber, setTopPrice, setBottomPrice):
    currentPrice = getStockPrice(stockNumber)

    return isAlarm(currentPrice[1], setTopPrice, setBottomPrice),

def getStockName(stockNumber):
    return getStockPrice(stockNumber)[0]

#判斷是否在用戶設定的價格外。
def isAlarm(currentPrice, setTopPrice, setBottomPrice):
    if float(currentPrice ) > float(setTopPrice) or float(currentPrice) < float(setBottomPrice):
        return True
    else:
        return False

if __name__ == '__main__':
    # getStockPrice("600027")

    print getStockPrintFromText("hoge 600027  600028")