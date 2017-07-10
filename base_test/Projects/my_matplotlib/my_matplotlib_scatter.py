# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-06 22:02:52
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-07 12:55:41

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40, edgecolor='none', c=y_values, cmap=plt.cm
	        .Blues)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 24)
plt.ylabel("Square of Value", fontsize = 24)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.axis([0, 1100, 0, 1100000])

plt.savefig('square_plot.png', bbox_inches='tight')
