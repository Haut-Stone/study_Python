'''
想要在对字典做迭代或序列化操作时，也能控制其中元素的顺序
'''

from collections import OrderedDict
import json


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# 会按照初始添加顺序进行
for key in d:
    print(key, d[key])

# 在字典转json时如果想让内容是有序的，那就用OrderedDict就行
j = json.dumps(d)
print(j)
