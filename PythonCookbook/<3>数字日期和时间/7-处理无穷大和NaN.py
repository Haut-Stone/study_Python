'''


'''

import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)


print(math.isinf(a))
print(math.isnan(c))

# 但是有几个很棘手的问题

a = float('inf')
print(a+45)
print(a*10)
print(10/a)

# 某些操作会导致未定义的行为并产生NaN结果
a = float('inf')
print(a/a)
b = float('-inf')
print(a+b)

# NaN会通过所有的操作进行串波，且不会引发异常
c = float('nan')
print(c + 23)
print(c / 2)
print(c * 2)
print(math.sqrt(c))
