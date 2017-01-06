# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-01-01 19:07:00
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-03 17:31:13
import random, pygame, sys
from pygame.locals import *

Fps = 15#图像刷新率
WindowHeight = 800#屏幕宽高
WindowWeight = 800
CellSize = 20#各自大小

assert WindowHeight % CellSize == 0, '亲，要给一个合适的长宽'
assert WindowWeight % CellSize == 0, '亲，要给一个合适的长宽'
CellEverRom = WindowWeight / CellSize#每行的单位格子数
CellEverColumn = WindowHeight / CellSize

White = (255, 255, 255)#定义颜色
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
DarkGray = (40, 40, 40)
DarkGreen = (0, 155, 0)
DarkRed = (155, 0, 0)

BgColor= Black#颜色的语法糖
LineColor = White

Up = 'up'#方向的语法糖
Down = 'down'
Left = 'left'
Right = 'right'

Head = 0#头部的语法糖

def main():

	global FpsClock, DisplaySurf, BasicFont, SoundObj1, SoundObj2

	pygame.init()
	FpsClock = pygame.time.Clock()
	DisplaySurf = pygame.display.set_mode((WindowWeight, WindowHeight), 0, 32)
	BasicFont = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('你好贪吃蛇')
	SoundObj1 = pygame.mixer.Sound('myWormy.wav')
	SoundObj2 = pygame.mixer.Sound('badswap.wav')

	#--^--各种初始化
	#
	#--_--主进程


	showStartScreen()
	while True:
		runGame()
		showGameOverScreen()

def runGame():
	speed = 10
	lastLen = -1
	startX = random.randint(5, CellEverRom - 6)#加载初始位置
	startY = random.randint(5, CellEverColumn - 6)
	pythonBody = [{'x':startX, 'y':startY}, {'x':startX-1, 'y':startY}, {'x':startX-2, 'y':startY}]#初始身体段
	direction = Right
	apple = getRandomLocation()


	#--^--初始化
	#
	#--_--主循环


	while True:
		for event in pygame.event.get():#侦测键盘
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if(event.key == K_LEFT or event.key == K_a) and direction != Right:
					direction = Left
				elif(event.key == K_RIGHT or event.key == K_d) and direction != Left:
					direction = Right
				elif(event.key == K_DOWN or event.key == K_s) and direction != Up:
					direction = Down
				elif(event.key == K_UP or event.key == K_w) and direction != Down:
					direction = Up
				elif event.key == K_ESCAPE:
					terminate()

		if pythonBody[Head]['x'] == -1 or pythonBody[Head]['x'] == CellEverRom or pythonBody[Head]['y'] == -1 or pythonBody[Head]['y'] == CellEverColumn:
			SoundObj2.play()
			return
		for perBody in pythonBody[1:]:
			if perBody['x'] == pythonBody[Head]['x'] and perBody['y'] == pythonBody[Head]['y']:
				SoundObj2.play()
				return
		if pythonBody[Head]['x'] == apple['x'] and pythonBody[Head]['y'] == apple['y']:
			SoundObj1.play()
			apple = getRandomLocation()
		else:
			del pythonBody[-1]

		#--^--碰撞检测
		#
		#--_--身体移动

		if direction == Up:
			newHead = {'x':pythonBody[Head]['x'], 'y':pythonBody[Head]['y'] - 1}
		elif direction == Down:
			newHead = {'x':pythonBody[Head]['x'], 'y':pythonBody[Head]['y'] + 1}
		elif direction == Right:
			newHead = {'x':pythonBody[Head]['x'] + 1, 'y':pythonBody[Head]['y']}
		elif direction == Left:
			newHead = {'x':pythonBody[Head]['x'] - 1, 'y':pythonBody[Head]['y']}


		pythonBody.insert(0, newHead)
		DisplaySurf.fill(BgColor)
		drawLine()
		drawApple(apple)
		drawPython(pythonBody)
		drawScore(len(pythonBody) - 3)
		if len(pythonBody)-3 > lastLen:
			lastLen = len(pythonBody)-3
			speed += 0.5#							加速，0.5让加速不是很快，通过这里可以调节难度
			print('现在的速度是-->' ,speed)
		pygame.display.update()
		FpsClock.tick(speed)

		#--^--更新画面
		#
		#--_--函数定义

def drawPressKeyMsg():#绘制提示文本
	pressKeySurf = BasicFont.render('Press any key to start', True, DarkGray)
	pressKeyRect = pressKeySurf.get_rect()
	pressKeyRect.topleft = (WindowWeight-200, WindowHeight - 30)
	DisplaySurf.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():#检查是否按下按键
	if len(pygame.event.get(QUIT)) > 0:
		terminate()

	keyUpEvents = pygame.event.get(KEYUP)
	if len(keyUpEvents) == 0:
		return None
	if keyUpEvents[0].key == K_ESCAPE:
		terminate()
	return keyUpEvents[0].key

def showStartScreen():#开始动画
	titleFont = pygame.font.Font('freesansbold.ttf', 100)
	titleSurf1 = titleFont.render('Wormy', True, White, DarkGreen)
	titleSurf2 = titleFont.render('Wormy', True, Green)

	degree1 = 0#图片的初始角度
	degree2 = 0

	while True:
		DisplaySurf.fill(BgColor)
		rotatedSurf1 = pygame.transform.rotate(titleSurf1, degree1)
		rotatedRect1 = rotatedSurf1.get_rect()
		rotatedRect1.center = (WindowWeight/2, WindowHeight/2)
		DisplaySurf.blit(rotatedSurf1, rotatedRect1)

		rotatedSurf2 = pygame.transform.rotate(titleSurf2, degree2)
		rotatedRect2 = rotatedSurf2.get_rect()
		rotatedRect2.center = (WindowWeight/2, WindowHeight/2)
		DisplaySurf.blit(rotatedSurf2, rotatedRect2)

		drawPressKeyMsg()

		if checkForKeyPress():
			pygame.event.get()
			return
		pygame.display.update()
		FpsClock.tick(Fps)
		degree1 += 3
		degree2 += 7

def terminate():#语法糖
	pygame.quit()
	sys.exit()

def getRandomLocation():#取得苹果的位置
	return {'x':random.randint(0,CellEverRom - 2), 'y':random.randint(0, CellEverColumn - 2)}

def showGameOverScreen():#展示游戏结束的画面
	gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
	gameSurf = gameOverFont.render('Game', True, White)
	overSurf = gameOverFont.render('Over', True, White)
	gameRect = gameSurf.get_rect()
	overRect = overSurf.get_rect()
	gameRect.midtop = (WindowWeight/2, 10)
	overRect.midtop = (WindowWeight/2, gameRect.height + 10 + 25)
	
	DisplaySurf.blit(gameSurf, gameRect)
	DisplaySurf.blit(overSurf, overRect)
	drawPressKeyMsg()
	pygame.display.update()
	pygame.time.wait(500)
	checkForKeyPress()

	while True:
		if checkForKeyPress():
			pygame.event.get()
			return

def drawScore(score):#画出分数
	scoreSurf = BasicFont.render('Score %s' % (score), True, White)#字体对象
	scoreRect = scoreSurf.get_rect()
	scoreRect.topleft = (WindowWeight - 120, 10)
	DisplaySurf.blit(scoreSurf, scoreRect)


def drawPython(pythonBody):#画出蛇的身体
	for perBody in pythonBody:
		x = perBody['x'] * CellSize
		y = perBody['y'] * CellSize
		pythonSegmentRect = pygame.Rect(x, y, CellSize, CellSize)
		pygame.draw.rect(DisplaySurf, DarkGreen, pythonSegmentRect)
		pythonInnerSegmentRect = pygame.Rect(x+4, y+4, CellSize-8, CellSize-8)
		pygame.draw.rect(DisplaySurf, Green, pythonInnerSegmentRect)

def drawApple(apple):#画出苹果
	x = apple['x'] * CellSize
	y = apple['y'] * CellSize
	appleRect = pygame.Rect(x, y, CellSize, CellSize)
	pygame.draw.rect(DisplaySurf, Red, appleRect)
	appleInnerRect = pygame.Rect(x+4,y+4, CellSize-8, CellSize-8)
	pygame.draw.rect(DisplaySurf, DarkRed, appleInnerRect)

def drawLine():#画出提示线
	for x in range(0, WindowWeight, CellSize):
		pygame.draw.line(DisplaySurf, DarkGray, (x, 0), (x, WindowHeight))
	for y in range(0, WindowHeight, CellSize):
		pygame.draw.line(DisplaySurf, DarkGray, (0,y), (WindowWeight, y))
	

if __name__ == '__main__':
	main()


