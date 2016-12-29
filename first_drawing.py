# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2016-12-29 20:26:23
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2016-12-29 21:12:57
import pygame, sys # 类似于c++的头文件
from pygame.locals import * #感觉像是name space 的样子

pygame.init() #初始化
									#	**宽**高**
DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32) #构建主界面
pygame.display.set_caption('hello world') #界面标题

#颜色常量
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#开始画图
DISPLAYSURF.fill(WHITE)
pygame.draw.line(DISPLAYSURF,GREEN, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 60), 100)
pygame.draw.line(DISPLAYSURF, BLUE, (123, 42), (23, 60))
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)#画圆
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 6)#画椭圆
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))#画长方形

pixObj = pygame.PixelArray(DISPLAYSURF)#画点
pixObj[480][380] = BLUE
pixObj[482][382] = BLACK
pixObj[484][384] = RED
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj#不懂。。。

while True:
	for event in pygame.event.get(): #在pygame.event.get()里面有许多的事件
		if event.type == QUIT: #如果事件类型是退出，便退出。
			pygame.quit()
			sys.exit()
	pygame.display.update()