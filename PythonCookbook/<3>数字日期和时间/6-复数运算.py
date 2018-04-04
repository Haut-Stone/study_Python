'''

'''

import cmath
import numpy as np


a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

# 实部和虚部可以很方便的提取出来

print(a.real)
print(a.imag)
print(a.conjugate())

# 所有的常见数学运算都可以用语复数

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

# 高级操作可以用cmath模组

print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

# python中大部分和数学相关的模块都可以用于复数，例如numpy模块

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a+2)
print(np.sin(a))
