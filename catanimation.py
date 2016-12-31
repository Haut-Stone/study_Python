# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2016-12-29 21:08:30
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2016-12-31 12:44:02

# 导入库
import pygame , sys
from pygame.locals import *

#创建背景
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('hello world')

#定义常量，变量
FPS = 60
WHITE = (255, 0, 255)
fpsClock = pygame.time.Clock()
catImg = pygame.image.load('cat.png')#加载图片
catx = 10
caty = 10
direction = 'right'

#动作变换循环
while True:
	DISPLAYSURF.fill(WHITE)

	if direction == 'right':
		catx += 10
		if catx == 280:
			direction = 'down'
	elif direction == 'down':
		caty += 10
		if caty == 220:
			direction = 'left'
	elif direction == 'left':
		catx -= 10
		if catx == 10:
			direction = 'up'
	elif direction == 'up':
		caty -= 10
		if caty == 10:
			direction = 'right'
	
	DISPLAYSURF.blit(catImg, (catx, caty))#将图片显示在画布上
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)#改变程序运行的帧率
