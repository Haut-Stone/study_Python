# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 17:03:11
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 17:06:38

# 这里用了标准库中的一个，作为例子
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is:")
	print(language.title() + ".")