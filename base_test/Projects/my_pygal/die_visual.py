# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-07 20:36:12
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-07 21:00:22

# 这个库，导入不了，我也不知道是因为什么，所以这个项目练习就直接放弃好了
import pygal
from die import Die

die = Die()

#随机掷骰子 
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

# 计算频率
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 items"
hist.x_label = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequence of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')