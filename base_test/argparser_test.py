# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-09-26 11:44:18
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-09-26 11:44:21


# 定位参数，其实就是必填的参数

'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integer', type=int, help='display an integer')
args = parser.parse_args()

print(args.integer)
'''

# 可选参数就是可选的不同的方法，便于将多个函数整合在一起

'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--square', help='display a square of a given number', type=int)
parser.add_argument('--cubic', help='display a cubic of a given number', type=int)

args = parser.parse_args()


if args.square:
	print(args.square**2)

if args.cubic:
	print(args.cubic**3)
'''

# 混合使用

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an \
					integer for the accmulator')
parser.add_argument('--sum', dest='accmulate', action='store_const', const=sum,\
					default=max, help='sum the integers( default:find the max)')

args = parser.parse_args()
print(args.accmulate(args.integers))