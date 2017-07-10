# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-07 12:35:20
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-07 20:22:27

#42b6bf

from matplotlib import pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.figure(figsize=(10, 6), dpi=128)

# 渐变绘制所有的点
point_numbers = list(range(rw.num_points))
# plt.scatter(rw.x_values, rw.y_values, s=1, edgecolor='none', c=point_numbers, 
# 			cmap=plt.cm.Reds)
plt.plot(rw.x_values, rw.y_values, linewidth=1)

# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# 保存所有的图片
plt.savefig('test.png', bbox_inches='tight')

