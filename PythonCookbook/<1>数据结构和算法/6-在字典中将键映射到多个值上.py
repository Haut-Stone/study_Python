'''
用多重字典相比手写会简洁不少
'''

from collections import defaultdict


# 这个字典的好处是会初始化第一个值，你只需要关注添加元素即可

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['a'].add(1)
print(d2)


# 下面是纯手写， 和运用defaultdict的对比

pairs = [(1, 11), (2, 22), (1, 1), (1, 111), (2, 2), (3, 3), (2, 2)]

d3 = {}
for key, value in pairs:
    if key not in d3:
        d3[key] = []
    d3[key].append(value)
print(d3)

d4 = defaultdict(list)
for key, value in pairs:
    d4[key].append(value)
print(d4)
