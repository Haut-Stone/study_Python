'''

'''

import math
from itertools import compress

# 简单起见，你可以用列表推倒式来筛选,缺点是数据较大时，产生的结果也比较大

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])


pos = (n for n in mylist if n > 0)  # 这是一个迭代器
print(pos)
for x in pos:
    print(x)


# 也可以用内建的filter()函数来处理

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

# 在列表推倒式中，你还可以对数据进行计算

mylist = [1, 3, 5, 6, 7, 3, 5, 2, -1, -3]
print([math.sqrt(n) if n > 0 else 0 for n in mylist])


# 还有一个很实用的筛选工具是compress

address = [
    '5412 N CLARK',
    '5415 N CLARK',
    '5413 N CLARK',
    '5418 N CLARK',
    '5410 N CLARK',
    '5419 N CLARK',
    '5417 N CLARK',
    '5411 N CLARK',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(address, more5)))
