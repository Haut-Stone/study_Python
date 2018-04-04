'''

'''


from datetime import datetime
from pytz import timezone


d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# pytz貌似不建议使用了，但是建议使用UTC时间还是很重要的
