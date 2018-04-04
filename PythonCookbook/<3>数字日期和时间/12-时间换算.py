'''


'''

from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a+b
print(c.days)
print(c.seconds)  # 秒数
print(c.seconds/3600)
print(c.total_seconds()/3600)

# 如果需要表示特定的日期和时间，可以创建datetime实例并使用标准的数学运算来操纵他们

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

# 当然datetime是可以处理闰年的

a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
print((a-b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c-d).days)

# 更复杂的涉及时区，模糊时间范围的话可以用dateutil模组

print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))

b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d)
print(d.months)
print(d.days)