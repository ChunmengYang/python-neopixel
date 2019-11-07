#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:colors.py

from rpi_ws281x import Color

class COLOR:
	BLACK = Color(0, 0, 0)			#黑
	
	RED = Color(255, 0, 0)			#红
	MAGENTA = Color(207, 0, 112)	#品红
	CARMINE = Color(215, 0, 64)		#洋红
	RUBY = Color(200, 8, 83)		#宝石红
	ROSE_RED = Color(230, 28, 100)	#玫瑰红
	CAMELLIA = Color(220, 91, 111)	#山茶红

	ORANGE = Color(255, 165, 0)		#橙色
	TANGERINE = Color(234, 85, 32)	#橘色
	PERSIMMOM = Color(237, 110, 61)	#柿子色
	TANGERINE_YELLOW = Color(237, 109, 0)	#橘黄色
	SUN_ORANGE = Color(241, 241, 0)	#太阳橙
	TROPICAL_ORANGE = Color(243, 152, 57)	#热带橙

	YELLOW = Color(255, 255, 0)		#黄色
	MARIGOLD = Color(247, 171, 0)	#金盏花
	CHROME_YELLOW = Color(253, 208, 0)	#铬黄
	JASMINE = Color(254, 221, 120)	#茉莉
	CREAM = Color(255, 234, 180)	#淡黄色
	LVORY = Color(255, 229, 209)	#象牙色

	GREEN = Color(0, 255, 0)		#绿色
	YELLOW_GREEN = Color(196, 215, 0)	#黄绿色
	APPLE_GREEN = Color(158, 189, 25)	#苹果绿
	FRESH_LEAVES = Color(169, 208, 107)	#嫩绿
	FOLIAGE_GREEN = Color(135, 162, 86)	#叶绿色
	GRASS_GREEN = Color(170, 196, 104)	#草绿色

	BLUE = Color(0, 0, 255)			#蓝色
	HORIZON_BLUE = Color(176, 220, 213)		#地平线
	LIGHTSKY_BLUE = Color(161, 216, 230)	#浅天蓝色
	AQUA_BLUE = Color(89, 195, 226)	#水蓝色
	AZURE_BLUE = Color(34, 174, 230)	#蔚蓝色
	SKY_BLUE = Color(148, 198, 221)	#天蓝色

	INDIGO = Color(19, 64, 152)	#靛色
	SALVIA_BLUE = Color(91, 119, 175)	#鼠尾草
	WEDGWOOD_BLUE = Color(102, 132, 176)	#韦奇伍德蓝
	SLATE_BLUE = Color(100, 121, 151)	#青蓝
	SAPPHIRE_BLUE = Color(0, 87, 137)	#宝石蓝

	PURPLE = Color(146, 61, 146)		#紫色
	WISTERIA = Color(115, 91, 159)		#紫藤
	MAUVE = Color(124, 80, 157)		#浅紫色
	CLEMATIS = Color(216, 191, 203)		#铁线莲
	LILAC = Color(187, 161, 203)		#丁香
	LAVENDER = Color(166, 136, 177)		#薰衣草