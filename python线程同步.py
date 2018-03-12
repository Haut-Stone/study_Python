# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2018-03-12 20:26:11
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2018-03-12 20:58:52

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程: " + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成,确实，只有都join了才会执行之后的代码
for t in threads:
    t.join()
print("退出主线程")
