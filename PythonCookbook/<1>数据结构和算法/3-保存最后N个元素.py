'''
保存有限的历史记录
用队列的话超出的部分会从最早的部分开始舍弃
这里主要要注意生成器是如何使用的
yield的主要作用就是把一个函数变成一个迭代器，从而做到高效啊和高复用性
'''
from collections import deque


def search(lines, pattern, maxlen=5):
    pre_lines = deque(maxlen=maxlen)
    for line in lines:
        if pattern in line:
            yield line, pre_lines
        pre_lines.append(line)


def show():
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    q.append(5)
    print(q)
    q2 = deque()
    q2.append(1)
    q2.append(2)
    q2.append(3)
    print(q2)
    q2.appendleft(4)
    print(q2)
    print(q2.pop())
    print(q2)
    print(q2.popleft())
    print(q2)


if __name__ == '__main__':
    with open('test.txt') as f:
        for line, pre_lines in search(f, 'python', 5):
            for pline in pre_lines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
    show()
