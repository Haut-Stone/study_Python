#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2018-03-12 19:39:49
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2018-03-12 20:58:18


# import _thread
import threading
import time


# _thread库提供的方法比较低级


# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))

# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2, ))
#     _thread.start_new_thread(print_time, ("Thread-2", 4, ))
# except:
#     print("Error: 无法启动线程")

# while 1:
#     pass

# 更高级的操作可以考虑用threading

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程: " + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程: " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主进程")