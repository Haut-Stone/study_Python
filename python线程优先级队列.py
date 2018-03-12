# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2018-03-12 20:36:30
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2018-03-12 20:58:59

import queue
import threading
import time


exitFlag = 0


class myThread(threading.Thread):
    # 拓展线程类
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        # 处理数据
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(threadName, q):
    while not exitFlag:
        # 不退出就锁住
        queueLock.acquire()
        # 队列不空时
        if not workQueue.empty():
            data = q.get()
            # 释放
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            # 空了直接释放
            queueLock.release()
            print("空解锁")
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Tow", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
print("填充队列")
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
