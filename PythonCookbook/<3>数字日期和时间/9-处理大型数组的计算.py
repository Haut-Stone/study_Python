'''
对于计算密集型数据集，请使用Numpy库
'''

import numpy as np


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x*2)
print(x+y)

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax*2)
print(ax+10)
print(ax+ay)
print(ax*ay)


def f(x):
    return 3*x**2 - 2*x + 7

print(f(ax))
print(np.sqrt(ax))
print(np.cos(ax))

# 你也可以创建一个超大数组
# grid = np.zeros(shape=(10000, 10000), dtype=float)
# grid += 10
# print(grid)
# print(np.sin(grid))

# 拓展python的索引功能
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

print(a[1])
print(a[:, 1])  # select column 1
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a[1:3, 1:3])
print(a + [100, 101, 102, 103])
print(np.where(a < 10, a, 10))
