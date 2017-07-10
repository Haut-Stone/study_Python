# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-09 21:26:26
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-10 12:35:16

import json

filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)

for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		print(country_name + ": " + str(population))

