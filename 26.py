#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time
import board
import neopixel

LED_BRIGHTNESS = 0.2
LED_ORDER = neopixel.GRB

pixels_26 = [];
pixels_26[0] = neopixel.NeoPixel(board.D16, 960, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)
pixels_26[1] = neopixel.NeoPixel(board.D20, 960, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)
pixels_26[2] = neopixel.NeoPixel(board.D21, 960, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)

pixels_20 = [];
pixels_20[0] = neopixel.NeoPixel(board.D19, 1170, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)
pixels_20[1] = neopixel.NeoPixel(board.D26, 1170, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)


class COLOR:
	BLACK = (0, 0, 0)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)

LINES_LED_26 = [
	{c: 0, n: [1, 14]} 	#0
]

LINES_26 = [
	[0, 1], 	#0
	[1, 2], 	#1
	[2, 3], 	#2
	[3, 0], 	#3
	[0, 4], 	#4
	[0, 5], 	#5
	[1, 6], 	#6
	[1, 7], 	#7
	[2, 8], 	#8
	[2, 9], 	#9
	[3, 10], 	#10
	[3, 11],  	#11
	[4, 5],  	#12
	[5, 6],  	#13
	[6, 7],  	#14
	[7, 8],  	#15
	[8, 9],  	#16
	[9, 10],  	#17
	[10, 11],  	#18
	[11, 4],  	#19
	[4, 12],  	#20
	[5, 13],  	#21
	[6, 14],  	#22
	[7, 15],  	#23
	[8, 16],  	#24
	[9, 17],  	#25
	[10, 18],  	#26
	[11, 19],  	#27
	[12, 13],  	#28
	[13, 14],  	#29
	[14, 15],  	#30
	[15, 16],  	#31
	[16, 17],  	#32
	[17, 18],  	#33
	[18, 19],  	#34
	[19, 12],  	#35
	[12, 20],  	#36
	[13, 20],  	#37
	[14, 21],  	#38
	[15, 21],  	#39
	[16, 22],  	#40
	[17, 22],  	#41
	[18, 23],  	#42
	[19, 23],  	#43
	[20, 21],  	#44
	[21, 22],  	#45
	[22, 23],  	#46
	[23, 20]  	#47
]

SURFACES_26 = [
	[0, 1, 2, 3], 		#0

	[0, 6, 13, 5], 		#1
	[7, 14, 6], 		#2
	[1, 8, 15, 7], 		#3
	[9, 16, 8], 		#4
	[2, 10, 17, 9],  	#5
	[11, 18, 10],  		#6
	[3, 4, 19, 11],  	#7
	[5, 12, 4],  		#8

	[12, 21, 28, 20],  	#9
	[13, 22, 29, 21],  	#10
	[14, 23, 30, 22],  	#11
	[15, 24, 31, 23],  	#12
	[16, 25, 32, 24],  	#13
	[17, 26, 33, 25],  	#14
	[18, 27, 34, 26],  	#15
	[19, 20, 35, 27],  	#16

	[28, 37, 36],  		#17
	[29, 38, 44, 37],  	#18
	[30, 39, 38],  		#19
	[31, 40, 45, 39],  	#20
	[32, 41, 40],  		#21
	[33, 42, 46, 41],  	#22
	[34, 43, 42],  		#23
	[35, 36, 47, 43],  	#24

	[44, 45, 46, 47]  	#25
]

LINES_LED_20 = [
	{'c': 0, 'n': [1, 14]} 	#0
]

LINES_20 = [
	[0, 1], 	#0
	[0, 2], 	#1
	[0, 3], 	#2
	[0, 4], 	#3
	[0, 5], 	#4
	[1, 2], 	#5
	[2, 3], 	#6
	[3, 4], 	#7
	[4, 5], 	#8
	[5, 1], 	#9
	[1, 6], 	#10
	[1, 7],  	#11
	[2, 7],  	#12
	[2, 8],  	#13
	[3, 8],  	#14
	[3, 9],  	#15
	[4, 9],  	#16
	[4, 10],  	#17
	[5, 10],  	#18
	[5, 6],  	#19
	[6, 7],  	#20
	[7, 8],  	#21
	[8, 9],  	#22
	[9, 10],  	#23
	[10, 6],  	#24
	[6, 11],  	#25
	[7, 11],  	#26
	[8, 11],  	#27
	[9, 11],  	#28
	[10, 11]  	#29
]

SURFACES_20 = [
	[0, 5, 1], 		#0
	[1, 6, 2], 		#1
	[2, 7, 3], 		#2
	[3, 8, 4], 		#3
	[4, 9, 0], 		#4

	[5, 11, 12],  	#5
	[12, 21, 13],  	#6
	[6, 13, 14],  	#7
	[14, 22, 15],  	#8
	[7, 15, 16],  	#9
	[16, 23, 17],  	#10
	[8, 17, 18],  	#11
	[18, 24, 19],  	#12
	[9, 19, 10],  	#13
	[10, 20, 11],  	#14

	[20, 25, 26],  	#15
	[21, 26, 27],  	#16
	[22, 27, 28],  	#17
	[23, 28, 29],  	#18
	[24, 29, 25] 	#19	
]


POINT_LINES_26 = {};
line_index = 0;
for line in LINES_26:
	for point in line:
		point_key = str(point)
		if not (point_key in POINT_LINES_26.keys()):
			POINT_LINES_26[point_key] = [];
		POINT_LINES_26[point_key].append(line_index);
	line_index += 1


LINE_SURFACES_26 = {};
surface_index = 0;
for surface in SURFACES_26:
	for line in surface:
		line_key = str(line)
		if not (line_key in LINE_SURFACES_26.keys()):
			LINE_SURFACES_26[line_key] = [];
		LINE_SURFACES_26[line_key].append(surface_index);
	surface_index += 1



POINT_LINES_20 = {};
line_index = 0;
for line in LINES_20:
	for point in line:
		point_key = str(point)
		if not (point_key in POINT_LINES_20.keys()):
			POINT_LINES_20[point_key] = [];
		POINT_LINES_20[point_key].append(line_index);
	line_index += 1


LINE_SURFACES_20 = {};
surface_index = 0;
for surface in SURFACES_20:
	for line in surface:
		line_key = str(line)
		if not (line_key in LINE_SURFACES_20.keys()):
			LINE_SURFACES_20[line_key] = [];
		LINE_SURFACES_20[line_key].append(surface_index);
	surface_index += 1



def contain(items, item):
	if len(items) > 0:
		for i in items:
			if i == item:
				return 1
	return 0


def light_line(pixels, start_point, end_point):
	if start_point > end_point:
		current_point = start_point
		while current_point >= end_point:
			pixels[current_point - 1] = color;
			current_point -= 1
	else:
		current_point = start_point
		while current_point <= end_point:
			pixels[current_point - 1] = color;
			current_point += 1
	
	pixels.show()

def light_line_26(line, color):
	line_led = LINES_LED_26[line]

	pixels = pixels_26[line_led['c']]

	start_point = line_led['n'][0]
	end_point = line_led['n'][1]

	light_line(pixels, start_point, end_point)
	

def light_line_20(line, color):
	line_led = LINES_LED_26[line]

	pixels = pixels_26[line_led['c']]

	start_point = line_led['n'][0]
	end_point = line_led['n'][1]

	light_line(pixels, start_point, end_point)


def random_line(lines_all, point, ignore_line):
	lines = []

	if lines_all:
		for line in lines_all:
			if contain(ignore_line, line) == 0:
				lines.append(line);

	if len(lines) > 0:
		line_index = random.randint(0, len(lines) - 1)
		return lines[line_index]

	return -1

def random_line_26(point, ignore_line):
	lines_all = POINT_LINES_26[str(point)]
	return random_line(lines_all, point, ignore_line)

def random_line_20(point, ignore_line):
	lines_all = POINT_LINES_20[str(point)]
	return random_line(lines_all, point, ignore_line)


def random_surface(surfaces_all, line, ignore_surface):
	surfaces = []

	if surfaces_all:
		for surface in surfaces_all:
			if contain(ignore_surface, surface) == 0:
				surfaces.append(surface);

	if len(surfaces) > 0:
		surface_index = random.randint(0, len(surfaces) - 1)
		return surfaces[surface_index]

	return -1

def random_surface_26(line, ignore_surface):
	surfaces_all = LINE_SURFACES_26[str(line)]
	return random_surface(surfaces_all, line, ignore_surface)

def random_surface_20(line, ignore_surface):
	surfaces_all = LINE_SURFACES_20[str(line)]
	return random_surface(surfaces_all, line, ignore_surface)


def flow_26(start_point, second):
	ignore_line = [];

	while True:
		line = random_line_26(start_point, ignore_line)
		if line == -1:
			return

		light_line_26(line, COLOR.RED)
		time.sleep(second)

		light_line_26(line, COLOR.BLACK)
		ignore_line = [line];

		if LINES_26[line][0] == start_point:
			start_point = LINES_26[line][1]
		else:
			start_point = LINES_26[line][0]


def flash_surface_26(second):
	pre_index = -1

	while True:
		surface_index = random.randint(0, len(SURFACES) - 1)
		if surface_index == pre_index:
			continue

		lines = SURFACES_26[surface_index]
		if lines:
			for line in lines:
				light_line_26(line, COLOR.RED)

		time.sleep(second)
		if lines:
			for line in lines:
				light_line_26(line, COLOR.BLACK)
		pre_index = surface_index


def scroll_26(line, second):
	ignore_surface = [];

	while True:
		surface = random_surface_26(line, ignore_surface)
		target_line = -1
		lines = SURFACES_26[surface]
		if lines:
			lines_len = len(lines)
			for x in range(0, lines_len):
				if lines[x] == line:
					if (x + 2) < lines_len:
						target_line = lines[x + 2]
					elif x - 2 >= 0:
						target_line = lines[x - 2]

		if target_line > -1:
			light_line_26(target_line, COLOR.RED)
		else:
			return

		time.sleep(second)
		light_line_26(target_line, COLOR.BLACK)
		ignore_surface = [surface];
		line = target_line;


if __name__ == '__main__':
	# flow_26(0, 0.2)
	# flash_surface_26(1)
	scroll_26(8, 0.5)
