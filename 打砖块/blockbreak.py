# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-01-06 13:00:54
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-16 22:51:52

import pygame, sys, random
from pygame.locals import *

#刷新速度
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


#小球常量定义
BallStart_Y = (DisplayHeight // 2 + 50)
BallSize = 6

#板子常量定义
PaddleStart_X = (DisplayWidth//2 - 100)
PaddleStart_Y = (DisplayHeight - 100)
PaddleWidth = 100
PaddleHight = 20

#砖块常量定义
RowNumber = 4
ColumnNumber = 9
BlockGap = 2
BlockWidth = 50
BlockHigth = 20
BlockOriginX = (DisplayWidth - (BlockWidth+BlockGap)*ColumnNumber)//2
BlockOriginY = 60
BlockColor = SpaceGray

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
	ballX = random.randint(100, 500)
	ballY = BallStart_Y
	ChangeX = -3
	ChangeY = -4
	blocks = initBlocks();

	while True:
		#球的速度
		
		ballX += ChangeX
		ballY += ChangeY

		#小球的矩形框
		sampRect = pygame.Rect(ballX, ballY, BallSize, BallSize)

		#砖块碰撞检测-----bug重灾区23333
		
		curX = BlockOriginX
		curY = BlockOriginY
		flag = 0
		for row in range(RowNumber):
			curX = BlockOriginX
			for col in range(ColumnNumber):
				tempRect = pygame.Rect(curX, curY, BlockWidth, BlockHigth)
				if blocks[row][col] == 1:
					#从下面撞
					print('球的顶部高度=',sampRect.top,'-','砖块的底部高度=',tempRect.bottom)
					if sampRect.top < tempRect.bottom and tempRect.left < sampRect.centerx < tempRect.right:
						blocks[row][col] = 0
						ChangeY = -ChangeY
						flag = 1
						break
					#从上面撞
					if sampRect.bottom < tempRect.top and tempRect.left < sampRect.centerx < tempRect.right:
						blocks[row][col] = 0
						ChangeY = -ChangeY
						flag = 1
						break
				curX += BlockWidth + BlockGap
			if flag == 1:
				break	
			curY += BlockHigth + BlockGap

		#边界碰撞检测
		if sampRect.bottom > DisplayHeight:
			return 
		if sampRect.top < 0 or (PaddleStart_Y <= sampRect.bottom <= PaddleStart_Y+20 and nowX < sampRect.centerx < nowX + PaddleWidth):
			if sampRect.centerx > nowX + ((PaddleWidth)/4)*3:
				if ChangeX < 0:
					ChangeX = -ChangeX
			elif sampRect.centerx < nowX + (PaddleWidth)/4:
				if ChangeX > 0:
					ChangeX = -ChangeX
			elif PaddleWidth/4 + nowX < sampRect.centerx < nowX + PaddleWidth/2:
				if ChangeX > 0:
					ChangeX = (-ChangeX)-1
				else:
					ChangeX = ChangeX+1
			elif (PaddleWidth/4)*3 + nowX < sampRect.centerx < nowX + PaddleWidth:
				if ChangeX < 0:
					ChangeX = (-ChangeX)+1
				else:
					ChangeX = ChangeX-1
			ChangeY = -ChangeY
		elif sampRect.left < 0 or sampRect.right > DisplayWidth:
			ChangeX = -ChangeX

		#事件监测
		for event in pygame.event.get():
			if event.type == QUIT:
				terminal()
			elif event.type == MOUSEMOTION:
				mouseX, mouseY = event.pos
				if mouseX + PaddleWidth > DisplayWidth:
					nowX = DisplayWidth - PaddleWidth
				else:
					nowX = mouseX

		#绘图			
		DisplaySurf.fill(Black)
		drawTotalLife()
		drawBlocks(blocks)
		drawPaddle(nowX)
		drawBall(ballX, ballY)
		#按键动作检查
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

#初始化砖块状态
def initBlocks():
	blocks = []
	for row in range(RowNumber):
		blocks.append([1]*ColumnNumber)
	return blocks;

#画出砖块
def drawBlocks(blocks):
	curX = BlockOriginX
	curY = BlockOriginY
	for row in range(RowNumber):
		curX = BlockOriginX
		for col in range(ColumnNumber):
			# print(curX,'-',curY,' row:',row,'col:',col,'状态',blocks[row][col])
			if (blocks[row][col] == 1):
				pygame.draw.rect(DisplaySurf, BlockColor, (curX, curY, BlockWidth, BlockHigth))
			curX += BlockWidth + BlockGap
		curY += BlockHigth + BlockGap

#画出总生命
def drawTotalLife():
	LifeFont = pygame.font.Font('freesansbold.ttf', 20)
	textSurface = LifeFont.render('life:', True, White, Black)
	textRect = textSurface.get_rect()
	textRect.center = (DisplayWidth-80,30)
	DisplaySurf.blit(textSurface, textRect)

#画出球
def drawBall(ballX, ballY):
	pygame.draw.circle(DisplaySurf, Blue, (ballX, ballY), BallSize, 0)

#画出挡板
def drawPaddle(x):
	paddle = pygame.Rect(x, PaddleStart_Y, PaddleWidth, PaddleHight)
	pygame.draw.rect(DisplaySurf, Red, paddle)

if __name__ == '__main__':
	main()