# -*- coding:utf-8 -*-
'''
我们希望有一个通用的解决方案能找出一周中上一次出现某天时的日期。比方说上周五是几月几号
'''

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    '''
    获得上周某耀日的日期
    '''
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago is 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(datetime.today())
print(get_previous_byday('Monday'))
print(get_previous_byday('Thursday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

# 当然也有执行相同功能的库函数可以使用

d = datetime.now()
print(d)
print(d + relativedelta(weekday=FR))  # 下一个周五
print(d + relativedelta(weekday=FR(-1)))  # 上一个周五
