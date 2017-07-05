# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 16:55:29
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 16:57:53

from car import Car

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

