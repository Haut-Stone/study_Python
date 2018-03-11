'''
这个例子里的队列可以用于线程间通信，还需要增加适当的锁和信号机制，请参见12.3节的实例
'''

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 这里的堆遵循的格式，可以查dash
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    # 这个就是固定一个输出格式
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

# 这里可以看到这是一个正确的优先队列
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
