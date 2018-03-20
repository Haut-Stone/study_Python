'''

'''

from decimal import Decimal
from decimal import localcontext


a = 4.2
b = 2.1
print(a + b)
print((a+b) == 6.3)

# 如果期待更高的精度，可以使用decimal模块
# 可以指定精度
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)

a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

# decimal模块主要用于金融业务的程序
