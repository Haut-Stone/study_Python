# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-10 12:31:37
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-10 12:34:18

from pygal.i18n import COUNTRIES

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	return None


