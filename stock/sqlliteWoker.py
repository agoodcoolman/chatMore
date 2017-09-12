# -*- coding:utf-8 -*-
#数据库相关的操作
import sqlite3
import sys

#保存定时任务
def createDatabase():
    connect = sqlite3.connect('timerWorker.db')
    cursor = connect.cursor()
    cursor.execute(' create table if not EXISTS timeworker (id varchar(20) PRIMARY key,groupname varchar(100), groupid varchar(150),'
                   ' fromname varchar(20), fromid varchar(200), stockNumber VARCHAR(10),'
                   ' alarmTop varchar (5), alarmBottom varchar (5))')
    cursor.close()
    connect.commit()
    connect.close()

# 谁发的， id， 股票号码，最高价 最低价格
def saveInfo(fromname, fromid, stockNumber,alarmTop, alarmBottom, groupname, groupid):
    connect = sqlite3.connect('timerWorker.db')
    cursor = connect.cursor()


    cursor.execute('insert into timeworker (groupname, groupid, fromname, fromid, stockNumber, alarmTop, alarmBottom)' \
                   ' values ' \
                   ' (?,?,?,?,?,?,?)', (groupname, groupid, fromname, fromid, stockNumber, alarmTop, alarmBottom))
    cursor.close();
    connect.commit();
    connect.close();

def removeInfo(fromname, fromid, stockNumber,alarmTop, alarmBottom, groupname, groupid):
    connect = sqlite3.connect('timerWorker.db')
    cursor = connect.cursor()
    cursor.execute('DELETE * from timeworker where fromid=' + fromid);
    cursor.close();
    connect.commit();
    connect.close();

def getInfo():
    connect = sqlite3.connect('timerWorker.db')
    cursor = connect.cursor()
    cursor.execute('select * from timeworker');

    fetchall = cursor.fetchall()

    cursor.close();
    connect.commit();
    connect.close();

    return fetchall;

if __name__ == '__main__':
    # createDatabase()
    # saveInfo("haod", "@gjeiojgeojgeo", "600027", "5.52", "5.00", "gijeio", "@@mjgpejpogejpgjepgepkegpk")
    print getInfo();