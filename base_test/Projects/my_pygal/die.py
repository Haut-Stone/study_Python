# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-07 20:26:06
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-07 20:35:30

# 模拟投掷骰子
from random import randint

class Die():

	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)

	