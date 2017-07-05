# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 12:20:57
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 12:23:24

# 这是一个模块导入的例子
def out_make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings")
	for topping in toppings:
		print("- " + topping)