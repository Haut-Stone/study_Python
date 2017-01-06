# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2016-12-29 21:54:08
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-05 15:34:14

import pygame , sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('fonttext')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
C1 = (63, 161, 207)
C2 = (245, 206, 57)

fronObj = pygame.font.Font('freesansbold.ttf', 64)#传入python的一种自带字体，和字体的大小。
textSurfaceObj = fronObj.render('hello world', True, C1, C2)#字符，是否抗锯齿，文本颜色，背景颜色
textRectObj = textSurfaceObj.get_rect()#?
textRectObj.center = (250, 250)#设定中心位置

while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)#载入画布
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit
	pygame.display.update()
