'''
这就很有意思了
'''


items = [0, 1, 2, 3, 4, 5, 6]
# 给切片取了一个有实际意义的名字
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)