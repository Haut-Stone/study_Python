# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2016-12-27 23:37:13
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-04 11:47:49
# 
# 这个程序是方块的碰撞，小小的测试
import pygame, sys
from pygame.locals import *

Fps = 30
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0 ,255)
AlphaBlack = (0, 0, 0, 0)
AlphaWhite = (255, 255, 255, 12)#最后一个参数是透明度
AlphaBlue = (0, 0 ,255 ,132)

DisplayWidth = 400
DisplayHeight = 400


pygame.init()
DISPLAYSURF = pygame.display.set_mode((DisplayWidth, DisplayHeight),0, 32)
pygame.display.set_caption('这个模组要这么用')

def main():
	#初始坐标
	nowX = 20
	nowY = 10
	#单步变化大小
	changeX = 3
	changeY = 3

	while True:
		global FpsClock
		FpsClock = pygame.time.Clock()

		nowX += changeX
		nowY += changeY

		#边界判断
		sampRect = pygame.Rect(nowX, nowY, 100,50)
		if sampRect.bottom > DisplayHeight or sampRect.top < 0:
			changeY = -changeY
		if sampRect.left < 0 or sampRect.right > DisplayWidth:
			changeX = -changeX

		showInof(sampRect)
		drawEveryThing(sampRect)

		#事件监测
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
		FpsClock.tick(Fps)

def drawEveryThing(sampRect):
	DISPLAYSURF.fill(AlphaBlack)
	pygame.draw.rect(DISPLAYSURF, AlphaWhite, sampRect)
def showInof(sampRect):
	print('左边的坐标：',sampRect.left, '右边的坐标：', sampRect.right)
	print('顶部的坐标：',sampRect.top, '底部的坐标：', sampRect.bottom)

if __name__ == '__main__':
	main()
