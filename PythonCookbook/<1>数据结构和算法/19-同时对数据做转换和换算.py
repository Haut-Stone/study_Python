'''

'''


import math
import os


# 一个优雅的解决方式

nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print(s)


# 一些其他栗子

# 1
files = os.listdir('../<1>数据结构和算法/')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')


# 2
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))


# 3
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHHO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
