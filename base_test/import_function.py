# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 12:28:35
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 17:03:14
import pizza

# 用这种导入方法的话，下面调用的时候不需要加模块的名字
from pizza import out_make_pizz

# 用这种可以给导入的函数指定别名
from pizza import out_make_pizz as mp

# 用这种可以为模块指定别名
import pizza as p

# 导入模块中的所有函数，而且不需要加模块的名字
from pizza import *

