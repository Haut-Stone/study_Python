# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-01-06 13:00:54
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-06 15:24:51

import pygame, sys
from pygame.locals import *

Fps = 60
TotalLife = 5

#窗口常量定义
DisplayWidth = 600
DisplayHeight = 600

#颜色常量定义
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
SpaceGray = (96, 96, 96)


#游戏状态常量定义
GameState_Init = 0
GameState_Start = 1
GameState_Run = 2
GameState_Over = 3
GameState_ShutDown = 4
GameState_Exit = 5

#小球常量定义
BallStart_Y = (DisplayHeight // 2)
BallSize = 4

#板子常量定义
PaddleStart_X = (DisplayHeight/2 - 100)
PaddleStart_Y = (DisplayWidth - 100)
PaddleWidth = 100
PaddleHight = 30

#砖块常量定义
RowNumber = 4
ColumnNumber = 8
BlockWidth = 20
BlockHigth = 20
BlockColor = Red

assert (DisplayWidth % BlockWidth == 0), '请给一个合适的方块宽度'



def main():
	#初始化
	pygame.init()
	global DisplaySurf, FpsClock
	FpsClock = pygame.time.Clock()
	DisplaySurf = pygame.display.set_mode((DisplayWidth,DisplayHeight), 0, 32)
	pygame.display.set_caption = ('弹砖块')

	#主进程
	gameStartscreen()
	while True:
		runGame()
		gameOver()
		print('进行了一次循环')

#语法糖
def terminal():
	pygame.quit()
	sys.exit()

#绘制press key message
def drawPressKeyMeg():
	PressKey = pygame.font.Font('freesansbold.ttf', 20)
	pressKeyMeg = PressKey.render('Press any key to start...', True, SpaceGray, Black)
	pressKeyRect = pressKeyMeg.get_rect()
	pressKeyRect.center = (DisplayWidth-150, DisplayHeight-40)
	DisplaySurf.blit(pressKeyMeg, pressKeyRect)

#检查按键动作
def checkKeyPress():
	if len(pygame.event.get(QUIT)) > 0:
		terminal()

	keyUpEvents = pygame.event.get(KEYUP)
	if len (keyUpEvents) == 0:
		return None
	if keyUpEvents[0].key == K_ESCAPE:
		terminal()
	return keyUpEvents[0].key

#开始界面
def gameStartscreen():
	#建立文字
	fontObj = pygame.font.Font('freesansbold.ttf', 64)
	textSurfaceObj = fontObj.render('Start Game ?', True, White, Black)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (DisplayWidth/2, DisplayHeight/2)
	
	while True:
		#绘图
		DisplaySurf.fill(Black)
		DisplaySurf.blit(textSurfaceObj, textRectObj)
		drawPressKeyMeg()
		#监测按键动作
		if checkKeyPress():
			pygame.event.get()
			return 
		pygame.display.update()
		FpsClock.tick(Fps)

def runGame():
	nowX = PaddleStart_X

	while True:
		DisplaySurf.fill(Black)

		for event in pygame.event.get():
			if event.type == QUIT:
				terminal()
			elif event.type == MOUSEMOTION:
				mouseX, mouseY = event.pos
				if mouseX + PaddleWidth > DisplayWidth:
					nowX = DisplayWidth - PaddleWidth
				else:
					nowX = mouseX

		drawPaddle(nowX)
		if checkKeyPress():
			pygame.event.get()
			return
		pygame.display.update()
		FpsClock.tick(Fps)
def gameOver():
	#建立文字
	fontObj2 = pygame.font.Font('freesansbold.ttf', 64)
	textSurfaceObj2 = fontObj2.render('Game Over :(', True, White, Black)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center = (DisplayWidth/2, DisplayHeight/2)
	
	while True:
		#绘图
		DisplaySurf.fill(Black)
		DisplaySurf.blit(textSurfaceObj2, textRectObj2)
		drawPressKeyMeg()
		#监测按键动作
		if checkKeyPress():
			pygame.event.get()
			return 
		pygame.display.update()
		FpsClock.tick(Fps)

# def drawBlocks():


# def drawBall():


def drawPaddle(x):
	paddle = pygame.Rect(x, PaddleStart_Y, PaddleWidth, PaddleHight)
	pygame.draw.rect(DisplaySurf, Red, paddle)

if __name__ == '__main__':
	main()