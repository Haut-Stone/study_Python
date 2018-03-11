'''
坐下，基本操作
'''

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 用自带的基本操作就可以
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())


# 下面是高端操作，直接用已有字典，建立一个特殊要求的字典
# 字典推倒式
c = {
    key: a[key] for key in a.keys() - {'z', 'w'}
}
print(c)
