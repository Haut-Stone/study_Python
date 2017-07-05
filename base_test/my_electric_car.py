# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 16:58:35
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 17:00:39

# 导入方法的种类和import_function中的种类数量是一样的

from car import *

my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()