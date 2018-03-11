'''
比起直接合并， ChainMap相当于是引用而不是普通的复制
'''

from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])  # 只要在a中找到就不再b中找了

# 下面比较了update和ChainMap的不同

merged = dict(b)
merged.update(a)
print(merged)
a['x'] = 20
print(merged)


merged = ChainMap(a, b)
print(merged)
a['x'] = 50
print(merged)
