# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2016-12-30 13:24:14
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2016-12-30 21:51:54

import  random , pygame, sys
from pygame.locals import *

FPS = 30#帧率

WINDOWWIDHT = 700#画布宽
WINDOWHEJGHT = 700#画布高
REVERALSPEED = 8#揭开的速度
BOXSIZE = 40#盒子大小
GAPSIZE = 10#间距大小
BOARDWIDTH = 5#板子行个数
BOARDHEIGHT = 4#板子列个数
assert (BOARDWIDTH*BOARDHEIGHT) % 2 == 0, 'Sorry we need an even number of boxes'

XMARGIN = int((WINDOWWIDHT - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)#左右间距
YMARGIN = int((WINDOWHEJGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)#上下间距

#颜色			R 	 G 	  B
GRAY 		= (100, 100, 100)
NAVYBLUE 	= ( 60,  60, 100)
WHITE 		= (255, 255, 255)
BLACK		= (  0,   0,   0)
BLUE		= (  0,   0, 255)
RED 		= (255,   0,   0)
GREEN		= (  0, 255,   0)
CYAN 		= (  0, 255, 255)
PURPLE		= (255,   0, 255)
YELLOW		= (255, 255,   0)
ORANGE		= (255, 128,   0)
#场景颜色
BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'#python自带画图
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)#所有颜色
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)#所有形状
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH*BOARDHEIGHT, 'Sorry, that is too big' #如果情况多了。。。断言

def main():
	global FPSCLOCK, DISPLAYSURF #定义全局的计时器 && 画布
	pygame.init()
	FPSCLOCK = pygame.time.Clock()#开始计时
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDHT , WINDOWHEJGHT))#创建画布

	mousex = 0#初始化鼠标位置
	mousey = 0
	test = None
	firstSection = None #初始化没有第一次点击
	pygame.display.set_caption('Emojy Memory Game')#标题
	#以上为初始化定义

	mainBoard = getRandomizedBoard()#创建所有可能的图形的基础单位的表
	revealedBoxes = generateRevealedBoxesData(False)#刚开始均盖住->返回的是表示状态的一个列表
	DISPLAYSURF.fill(BGCOLOR)
	# startGameAnimation(mainBoard)#开场动画
	while True:#一次刷新循环
		mouseClicked = False #鼠标刚开始没有按下
		DISPLAYSURF.fill(BGCOLOR)#加载背景
		drawBoard(mainBoard, revealedBoxes)#加载板子

		for event in pygame.event.get():#查找事件

			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):#如果点击ESC
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:#如果鼠标移动
				mousex, mousey = event.pos #获取鼠标位置
			elif event.type == MOUSEBUTTONUP:#如果鼠标抬起
				mousex, mousey = event.pos
				mouseClicked = True#更新鼠标状态

		boxx, boxy = getBoxAtPixel(mousex, mousey)#将鼠标位置换成对应的块的位置
		if boxx != None and boxy != None:

			if not revealedBoxes[boxx][boxy]:#如果没有被反转
				drawHighlightBox(boxx, boxy)#加载提示框

			if not revealedBoxes[boxx][boxy] and mouseClicked:
				# revealBoxesAnimation(mainBoard, [(boxx, boxy)])#揭开的动画
				revealedBoxes[boxx][boxy]  = True #标记已揭开
				if firstSection == None:
					firstSection = (boxx, boxy)#标记是不是第一个块
				else:
					#分别得到两块的颜色和形状
					icon1Shape, icon1Color = getShapeAndColor(mainBoard, firstSection[0], firstSection[1])
					icon2Shape, icon2Color = getShapeAndColor(mainBoard, boxx, boxy)

					if icon1Shape != icon2Shape or icon1Color != icon2Color:#如果不一样
						# for wait in [1,2,3,4,5,6,7,8,9]:
						drawBoard(mainBoard, revealedBoxes)
						
						# pygame.display.update()#更新画面
						# FPSCLOCK.tick(FPS)
						# 	if revealedBoxes[firstSection[0]][firstSection[1]] == True:
						# 		revealedBoxes[firstSection[0]][firstSection[1]] = False
						# 	else:
						# 		revealedBoxes[firstSection[0]][firstSection[1]] = True
						# 		print('运行到这里了')
						# print('测试部分已经结束')
						# coverBoxesAnimation(mainBoard, [(firstSection[0], firstSection[1]), (boxx, boxy)])#合上两个方块
						revealedBoxes[firstSection[0]][firstSection[1]] = False #标记没有被揭开
						revealedBoxes[boxx][boxy] = False #标记没有被揭开
					elif hasWon(revealedBoxes):#如果赢了
						# gameWonAnimation(mainBoard)

						#重置板子
						mainBoard = getRandomizedBoard()

						revealedBoxes = generateRevealedBoxesData(False)

						#展示新板子
						drawBoard(mainBoard, revealedBoxes)
						pygame.display.update()

						# startGameAnimation(mainBoard)
					firstSection = None

		pygame.display.update()#更新背景，板子，提示框
		FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(val):#盖子是否打开的布尔列表
	revealedBoxes = []
	for i in range(BOARDWIDTH):
		revealedBoxes.append([val] * BOARDHEIGHT)
	return revealedBoxes
def getRandomizedBoard():#返回板子元素列表
	icons = []
	for color in ALLCOLORS:
		for shape in ALLSHAPES:
			icons.append((shape, color))

	random.shuffle(icons)#调用随机函数

	numIconsUsed = int(BOARDHEIGHT * BOARDWIDTH / 2)
	icons = icons[:numIconsUsed] * 2#		???
	random.shuffle(icons)#调用随机函数

	board = []
	for x in range(BOARDWIDTH):#将图像加载到板子	
		column = []
		for y in range(BOARDHEIGHT):
			column.append(icons[0])
			del icons[0]
		board.append(column)
	return board #返回到mainboard		
def splitIntoGroupsOf(groupSize, theList):#制造列表的列表，，，不懂		？？
	result = []
	for i in range(0, len(theList), groupSize):
		result.append(theList[i:i + groupSize])
	return result
def leftTopCoorsOfBox(boxx, boxy):#求出元素左上角的坐标，为了绘制长方形
	left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
	top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
	return (left, top)
def getBoxAtPixel(x, y):#建造覆盖块，如果鼠标位置被覆盖，则返回对应的块的坐标
	for boxx in range(BOARDWIDTH):#遍历所有元素位置
		for boxy in range(BOARDHEIGHT):
			left, top = leftTopCoorsOfBox(boxx, boxy)
			boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)#建造一个覆盖块
			if boxRect.collidepoint(x, y):#如果压住，则返回对应的元素位置
				return (boxx, boxy)
	return (None, None)#如果没有
def getShapeAndColor(board, boxx, boxy):#得到元素的形状颜色

	return board[boxx][boxy][0], board[boxx][boxy][1]
# def revealBoxesAnimation(board, boxesToReveal):#打开板子的动画
# # 	for coverage in range(BOXSIZE, (-REVERALSPEED) - 1, -REVERALSPEED):
# # 		drawBoxCovers(board, boxesToReveal, coverage)
# def coverBoxesAnimation(board, boxesToCover):#盖上板子的动画
#  	for coverage in range(0, BOXSIZE + REVERALSPEED, REVERALSPEED):
#  		drawBoxCovers(board, boxesToCover, coverage)
# def startGameAnimation(board):#开始的提示动画
# # 	coveredBoxes = generateRevealedBoxesData(False)#刚开始均盖住
# # 	boxes = []#新建元素表单
# # 	for x in range(BOARDWIDTH):
# # 		for y in range(BOARDHEIGHT):
# # 			boxes.append((x, y))
# # 	random. shuffle(boxes)#打乱元素
# # 	boxGroups = splitIntoGroupsOf(8, boxes)#		？？

# # 	drawBoard(board, coveredBoxes)
# # 	for boxGroup in boxGroups:
# # 		revealBoxesAnimation(board, boxGroup)#翻开动画
# # 		pygame.time.wait(100)
# # 		coverBoxesAnimation(board, boxGroup)#合上动画
# def gameWonAnimation(board):#获胜动画
# # 	coveredBoxes = generateRevealedBoxesData(True) #创建状态列表
# # 	color1 = LIGHTBGCOLOR
# # 	color2 = BGCOLOR

# # 	for i in range(13):
# # 		color1, color2 = color2, color1
# # 		DISPLAYSURF.fill(color1) #快速改变背景颜色
# # 		drawBoard(board, coveredBoxes)#重画板子
# # 		pygame.display.update()#更新画面
# # 		pygame.time.wait(300)
def drawBoard(board, revealed):#绘制board
	for boxx in range(BOARDWIDTH):
		for boxy in range(BOARDHEIGHT):
			left, top = leftTopCoorsOfBox(boxx, boxy)
			pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))#画背景颜色，覆盖之前
			if not revealed[boxx][boxy]:
				pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
			else:
				shape, color = getShapeAndColor(board, boxx, boxy)
				drawIcon(shape, color, boxx, boxy)
def drawHighlightBox(boxx, boxy):#绘制高亮框
	left , top = leftTopCoorsOfBox(boxx, boxy)
	pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left-5, top-5, BOXSIZE+10, BOXSIZE+10), 4)
def drawBoxCovers(board, boxes, coverage):#绘制覆盖的板子
	for box in boxes:
		left, top = leftTopCoorsOfBox(box[0], box[1])
		pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))#画背景颜色，覆盖之前
		shape, color  = getShapeAndColor(board, box[0], box[1])
		drawIcon(shape, color, box[0], box[1])#画图形
		if coverage > 0:
			pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))#有盖子则画盖子
	pygame.display.update()
	FPSCLOCK.tick(FPS)
def drawIcon(shape, color, boxx, boxy):#画出板子元素所对应的图形
    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    half =    int(BOXSIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoorsOfBox(boxx, boxy) # get pixel coords from board coords
    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))
def hasWon(revealedBoxes):#如果全部都翻开了，就赢了
	for i in revealedBoxes:
		if False in i:
			return False
	return True

if __name__ == '__main__':
	main()


