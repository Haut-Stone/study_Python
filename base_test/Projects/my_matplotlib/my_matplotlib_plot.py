# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 22:31:34
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-06 22:00:48

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

plt.plot(input_values, squares, linewidth = 5)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 24)
plt.ylabel("Square of Value", fontsize = 24)

plt.tick_params(axis = 'both', labelsize = 14)
plt.show()

