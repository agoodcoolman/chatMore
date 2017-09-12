# -*- coding:utf-8 -*-
# 工作查询的线程
from threading import Timer

import sqlliteWoker
import getSock
import chat
def run_proc():
    # infos = sqlliteWoker.getInfo()
    # for info in infos:
    #     pass
    # print time.time()
    infos = sqlliteWoker.getInfo()

    for info in infos:
        dujest = getSock.dujest(info[5], info[6], info[7])
        # info[1] 房間名 info「2」房間id info[3] 用戶名 #info「4」用戶id
        if dujest:
            chat.send_message(info[1], info[3], getSock.getStockName(info[5]))

    Timer(3, run_proc).start()


def start_proc():
    sqlliteWoker.createDatabase()
    Timer(3, run_proc).start()

if __name__ == '__main__':
    Timer(3, run_proc).start()

