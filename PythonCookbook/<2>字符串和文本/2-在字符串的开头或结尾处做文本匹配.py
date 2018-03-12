'''
常用于文件拓展名检查，和URL检查，（看起来还是蛮重要的）
'''

import os
from urllib.request import urlopen


# 简单的方法使用，str.startwith()和str.endswith()

filename = 'test.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.startswith('1')])
print(any(name.endswith('.py') for name in filenames))


# 另一个例子

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# 当然，你用切片来完成这个任务也可以，但是不够优雅，同样正则表达式也可以，但是过于重量级，且运行慢
