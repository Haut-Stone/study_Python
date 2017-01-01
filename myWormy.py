# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-01-01 19:07:00
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-01 20:38:50
import random, pygame, sys
from pygame.locals import *

Fps = 30
WindowHeight = 600
WindowWeight = 600
CellSize = 20
assert WindowHeight % CellSize == 0 '亲，要给一个合适的长宽'
assert WindowWeight % CellSize == 0 '亲，要给一个合适的长宽'
CellEverRom = WindowWeight / CellSize
CellEverColumn = WindowHeight / CellSize

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
DarkGray = (40, 40, 40)
DarkGreen = (0, 155, 0)

BgColor= Black
LineColor = White

Up = 'up'
Down = 'down'
Left = 'left'
Right = 'right'

Head = 0

def main():
	global FpsClock, DisplaySurf, BasicFont
	pygame.init()
	FpsClock = pygame.time.Clock()
	DisplaySurf = pygame.display.set_mode((WindowWeight, WindowHeight), 0, 32)
	BasicFont = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('你好贪吃蛇')

	#--^--各种初始化
	#
	#--_--主进程


	showStartScreen()
	while True:
		runGame()
		showGameOverScreen()

def runGame():
	startX = random.randint(5, CellEverRom - 6)#加载初始位置
	startY = random.randint(5, CellEverColumn - 6)
	pythonBody = [{'x':startX, 'y':startY}, {'x':startX-1, 'y':startY}, {'x':startX-2, 'y':startY}]
	direction = Right
	apple = getRandomLocation()


	#--^--初始化
	#
	#--_--主循环


	while True:
		for event in pygame.event.get():
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
				else event.key == K_ESCAPE:
					terminate()

		if pythonBody[Head]['x'] == -1 or pythonBody[Head]['x'] == CellEverRom or pythonBody[Head]['y'] == -1 or pythonBody[Head]['y'] == CellEverColumn:
			return
		for perBody in pythonBody[1:]:
			if perBody['x'] == pythonBody[Head]['x'] and perBody['y'] == pythonBody[Head]['y']:
				return
		if pythonBody[Head]['x'] == apple['x'] and pythonBody[Head]['y'] == apple['y']:
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
		drawApple()
		drawPython(pythonBody)
		drawScore(len(pythonBody) - 3)
		pygame.display.update()
		FpsClock.tick(Fps)

		#--^--更新画面
		#
		#--_--函数定义

def drawPressKeyMsg():
	pressKeySurf = BasicFont.render('Press any key to start', True, DarkGray)
	pressKeyRect = pressKeySurf.get_rect()
	pressKeyRect.topleft = (WindowWeight-200, WindowHeight - 30)
	DisplaySurf.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
	if len(pygame.event.get(QUIT)) > 0:
		terminate()

	keyUpEvents = pygame.event.get(KEYUP)
	if len(keyUpEvents) == 0:
		return None
	if keyUpEvents[0].key == K_ESCAPE:
		terminate()
	return keyUpEvents[0].key

def showStartScreen():
	titleFont = pygame.font.Font('freesansbold.ttf', 100)
	titleSurf1 = titleFont.render('Wormy', True, White, DarkGreen)
	titleSurf2 = titleFont.render('Wormy', True, Green)

	degree1 = 0
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

def terminate():
	pygame.quit()
	sys.exit()

def getRandomLocation():
	return {'x':random.randint(0,CellEverRom - 1), 'y':random.randint(0, CellEverColumn - 1)}

def showGameOverScreen():
	gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
	gameSurf = gameOverFont.render('Game', True, White)
	overSurf = gameOverFont.render('Over', True, White)
	gameRect = gameSurf.get_rect()
	overRect = overSurf.get_rect()
	gameRect.mintop = (WindowWeight/2, 10)
	overRect.mintop = (WindowWeight/2, gameRect.height + 10 + 25)
	



