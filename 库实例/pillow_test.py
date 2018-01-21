# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2018-01-21 10:52:06
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2018-01-21 11:15:40

# 缩小保存文件
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000

# from PIL import Image, ImageFilter

# img = Image.open('test.png')

# w, h = img.size

# print('Original image size: %sx%s' % (w, h))

# img.thumbnail((w//2, h//2))

# print('Resize image to: %sx%s' % (w//2, h//2))

# img.save('thumbnail.jpg', 'jpeg')

# img2 = img.filter(ImageFilter.BLUR)
# img2.save('blur.jpg', 'jpeg')

# 生成字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60*4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())

for t in range(4):
	draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')