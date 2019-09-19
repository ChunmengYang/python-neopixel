#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:model26.py

import random
import time
import board
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


# LED_COUNT = 15        # Number of LED pixels.
# LED_PIN = 13          # GPIO pin connected to the pixels (must support PWM! GPIO 13 or 18 on RPi 3).
# LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA = 11          # DMA channel to use for generating signal (Between 1 and 14)
# LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
# LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
# LED_CHANNEL = 1       # 0 or 1
# LED_STRIP = ws.WS2811_STRIP_GRB

STRIPS = [1,2,3];
STRIPS[0] = Adafruit_NeoPixel(960, 18, 800000, 7, False, 128, 1, ws.WS2811_STRIP_GRB)
STRIPS[0].begin()

STRIPS[1] = Adafruit_NeoPixel(960, 23, 800000, 8, False, 128, 1, ws.WS2811_STRIP_GRB)
STRIPS[1].begin()

STRIPS[2] = Adafruit_NeoPixel(960, 24, 800000, 9, False, 128, 1, ws.WS2811_STRIP_GRB)
STRIPS[2].begin()

class COLOR:
	BLACK = Color(0, 0, 0)
	GREEN = Color(0, 255, 0)
	RED = Color(255, 0, 0)
	BLUE = Color(0, 0, 255)
	YELLOW = Color(255, 255, 0)
	PURPLE = Color(255, 0, 255)
	TURQUOISE = Color(0, 255, 255)


LINES_LED = [
	{'c': 0, 'n': [0, 59]},		#0
	{'c': 0, 'n': [0, 59]}, 	#1
	{'c': 0, 'n': [0, 59]}, 	#2
	{'c': 0, 'n': [0, 59]}, 	#3
	{'c': 0, 'n': [0, 59]}, 	#4
	{'c': 0, 'n': [0, 59]}, 	#5
	{'c': 0, 'n': [0, 59]}, 	#6
	{'c': 0, 'n': [0, 59]}, 	#7
	{'c': 0, 'n': [0, 59]}, 	#8
	{'c': 0, 'n': [0, 59]}, 	#9
	{'c': 0, 'n': [0, 59]}, 	#10
	{'c': 0, 'n': [0, 59]}, 	#11
	{'c': 0, 'n': [0, 59]},  	#12
	{'c': 0, 'n': [0, 59]}, 	#13
	{'c': 0, 'n': [0, 59]},  	#14
	{'c': 0, 'n': [0, 59]},  	#15
	{'c': 1, 'n': [0, 59]},  	#16
	{'c': 1, 'n': [0, 59]},  	#17
	{'c': 1, 'n': [0, 59]},  	#18
	{'c': 1, 'n': [0, 59]},  	#19
	{'c': 1, 'n': [0, 59]},  	#20
	{'c': 1, 'n': [0, 59]},  	#21
	{'c': 1, 'n': [0, 59]},  	#22
	{'c': 1, 'n': [0, 59]},  	#23
	{'c': 1, 'n': [0, 59]},  	#24
	{'c': 1, 'n': [0, 59]},  	#25
	{'c': 1, 'n': [0, 59]},  	#26
	{'c': 1, 'n': [0, 59]},  	#27
	{'c': 1, 'n': [0, 59]},  	#28
	{'c': 1, 'n': [0, 59]},  	#29
	{'c': 1, 'n': [0, 59]},  	#30
	{'c': 1, 'n': [0, 59]},  	#31
	{'c': 2, 'n': [0, 59]},  	#32
	{'c': 2, 'n': [0, 59]},  	#33
	{'c': 2, 'n': [0, 59]},  	#34
	{'c': 2, 'n': [0, 59]},  	#35
	{'c': 2, 'n': [0, 59]},  	#36
	{'c': 2, 'n': [0, 59]},  	#37
	{'c': 2, 'n': [0, 59]},  	#38
	{'c': 2, 'n': [0, 59]},  	#39
	{'c': 2, 'n': [0, 59]},  	#40
	{'c': 2, 'n': [0, 59]},  	#41
	{'c': 2, 'n': [0, 59]},  	#42
	{'c': 2, 'n': [0, 59]},  	#43
	{'c': 2, 'n': [0, 59]},  	#44
	{'c': 2, 'n': [0, 59]},  	#45
	{'c': 2, 'n': [0, 59]},  	#46
	{'c': 2, 'n': [0, 59]}  	#47
]

LINES = [
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

SURFACES = [
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

POINT_LINES = {};
line_index = 0;
for line in LINES:
	for point in line:
		point_key = str(point)
		if not (point_key in POINT_LINES.keys()):
			POINT_LINES[point_key] = [];
		POINT_LINES[point_key].append(line_index);
	line_index += 1


LINE_SURFACES = {};
surface_index = 0;
for surface in SURFACES:
	for line in surface:
		line_key = str(line)
		if not (line_key in LINE_SURFACES.keys()):
			LINE_SURFACES[line_key] = [];
		LINE_SURFACES[line_key].append(surface_index);
	surface_index += 1


def contain(items, item):
	if len(items) > 0:
		for i in items:
			if i == item:
				return 1
	return 0


def light_line(line, color):
	line_led = LINES_LED[line]

	strip = STRIPS[line_led['c']]
	start_point = line_led['n'][0]
	end_point = line_led['n'][1]

	if start_point > end_point:
		current_point = start_point
		while current_point >= end_point:
			strip.setPixelColor(current_point - 1, color)
			current_point -= 1
	else:
		current_point = start_point
		while current_point <= end_point:
			strip.setPixelColor(current_point - 1, color)
			current_point += 1
	strip.show()


def random_line(point, ignore_line):
	lines_all = POINT_LINES[str(point)]
	lines = []

	if lines_all:
		for line in lines_all:
			if contain(ignore_line, line) == 0:
				lines.append(line);

	if len(lines) > 0:
		line_index = random.randint(0, len(lines) - 1)
		return lines[line_index]

	return -1



def random_surface(line, ignore_surface):
	surfaces_all = LINE_SURFACES[str(line)]
	surfaces = []

	if surfaces_all:
		for surface in surfaces_all:
			if contain(ignore_surface, surface) == 0:
				surfaces.append(surface);

	if len(surfaces) > 0:
		surface_index = random.randint(0, len(surfaces) - 1)
		return surfaces[surface_index]

	return -1



def fill(color):
	for x in range(0, len(STRIPS)):
		strip = STRIPS[x]
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, color)
		strip.show()


# 从一条边向另一条相邻的边流动点亮
def flow(start_point, flow_line_number, interval):
	ignore_line = [];
	pre_line = -1
	pre_strip = None
	pre_start_led = -1
	pre_end_led = -1

	index = 0
	while index < flow_line_number:
		line = random_line(start_point, ignore_line)
		if line == -1:
			return

		if pre_line == -1:
			line_led = LINES_LED[line]
			strip = STRIPS[line_led['c']]
			start_led = -1
			end_led = -1
			if LINES[line][0] == start_point:
				start_led = line_led['n'][0]
				end_led = line_led['n'][1]
			else:
				start_led = line_led['n'][1]
				end_led = line_led['n'][0]

			pre_line = line
			pre_strip = strip
			pre_start_led = start_led
			pre_end_led = end_led

			pre_led_count = abs(pre_start_led - pre_end_led) + 1
			for x in range(0, pre_led_count):
				if pre_start_led > pre_end_led:
					pre_strip.setPixelColor(pre_start_led - x, COLOR.RED)
				else:
					pre_strip.setPixelColor(pre_start_led + x, COLOR.RED)
				pre_strip.show()

				time.sleep(interval)
		else:
			line_led = LINES_LED[line]
			strip = STRIPS[line_led['c']]
			start_led = -1
			end_led = -1
			if LINES[line][0] == start_point:
				start_led = line_led['n'][0]
				end_led = line_led['n'][1]
			else:
				start_led = line_led['n'][1]
				end_led = line_led['n'][0]

			pre_led_count = abs(pre_start_led - pre_end_led) + 1
			max_led_count = pre_led_count 
			led_count = abs(start_led - end_led) + 1
			if led_count > max_led_count:
				max_led_count = led_count

			for x in range(0, max_led_count):
				if x < pre_led_count:
					if pre_start_led > pre_end_led:
						pre_strip.setPixelColor(pre_start_led - x, COLOR.GREEN)
					else:
						pre_strip.setPixelColor(pre_start_led + x, COLOR.GREEN)
					pre_strip.show()

				if x < led_count:
					if start_led > end_led:
						strip.setPixelColor(start_led - x, COLOR.RED)
					else:
						strip.setPixelColor(start_led - x, COLOR.RED)
					strip.show()

				time.sleep(interval)

			pre_line = line
			pre_strip = strip
			pre_start_led = start_led
			pre_end_led = end_led
		
		ignore_line = [line];
		if LINES[line][0] == start_point:
			start_point = LINES[line][1]
		else:
			start_point = LINES[line][0]

		index += 1

	if pre_line > -1:
		pre_led_count = abs(pre_start_led - pre_end_led) + 1
		for x in range(0, pre_led_count):
			if pre_start_led > pre_end_led:
				pre_strip.setPixelColor(pre_start_led - x, COLOR.GREEN)
			else:
				pre_strip.setPixelColor(pre_start_led + x, COLOR.GREEN)
			pre_strip.show()

			time.sleep(interval)


# 随机点亮某个面
def flash_surface(flash_number, interval):
	pre_index = -1
	index = 0
	while index < flash_number:
		surface_index = random.randint(0, len(SURFACES) - 1)
		if surface_index == pre_index:
			continue

		lines = SURFACES[surface_index]
		if lines:
			for line in lines:
				light_line(line, COLOR.RED)

		time.sleep(interval)
		if lines:
			for line in lines:
				light_line(line, COLOR.GREEN)
		pre_index = surface_index

		index += 1

# 平行线滚动(只限于正方形的面)
def parallel_line_scroll(start_line, scroll_number, interval):
	light_line(start_line, COLOR.RED)
	time.sleep(interval)
	light_line(start_line, COLOR.GREEN)

	ignore_surface = [];
	index = 0
	while index < scroll_number:
		surface = random_surface(start_line, ignore_surface)
		target_line = -1
		lines = SURFACES[surface]
		if lines:
			lines_len = len(lines)
			for x in range(0, lines_len):
				if lines[x] == start_line:
					if (x + 2) < lines_len:
						target_line = lines[x + 2]
					elif x - 2 >= 0:
						target_line = lines[x - 2]

		if target_line > -1:
			light_line(target_line, COLOR.RED)
		else:
			return

		time.sleep(interval)
		light_line(target_line, COLOR.GREEN)

		ignore_surface = [surface];
		start_line = target_line;

		index += 1


def get_layer_lines(points_dict, pre_points_dict):
	lines_dict = {}
	next_points_dict = {}

	for key, point in points_dict.items():
		lines = POINT_LINES[str(point)]
		if lines:
			for line in lines:
				another_point = -1
				if LINES[line][0] == point:
					another_point = LINES[line][1]
				if LINES[line][1] == point:
					another_point = LINES[line][0]

				if str(another_point) in points_dict:
					lines_dict[str(line)] = line;
					continue
				if str(another_point) in pre_points_dict:
					continue

				next_points_dict[str(another_point)] = another_point

	return lines_dict, next_points_dict


# 点亮一层线，再点亮相邻平行的下一层线，以此类推，没有下一层就返回
def light_layer_to_layer(layer_number, interval):
	pre_points_dict = {}
	points_dict = {"0": 0, "1": 1, "2": 2, "3": 3}
	pre_lines_dict = {}

	index = 0
	while index < layer_number:
		lines_dict, next_points_dict = get_layer_lines(points_dict, pre_points_dict)

		for key, line in pre_lines_dict.items():
			light_line(line, COLOR.BLACK)

		for key, line in lines_dict.items():
			light_line(line, COLOR.RED)

		pre_lines_dict = lines_dict

		if len(next_points_dict) > 0:
			pre_points_dict = points_dict
			points_dict = next_points_dict
		else:
			temp = points_dict
			points_dict = pre_points_dict
			pre_points_dict = temp
			temp = None

		time.sleep(interval)
		index += 1

# 查询一条边所在的面
def get_surface_by_line(line, ignore_surface):
	surfaces = LINE_SURFACES[str(line)]
	if surfaces:
		for surface in surfaces:
			if surface == ignore_surface:
				continue
			return surface
	return -1

# 查询一条边在一个正方形中的对面边和对面边所在正方形
def get_surface_by_opposite_line(line, surface):
	target_line = -1
	target_surface = -1
	lines = SURFACES[surface]
	if lines:
		lines_len = len(lines)
		for x in range(0, lines_len):
			if lines[x] == line:
				if (x + 2) < lines_len:
					target_line = lines[x + 2]
				elif x - 2 >= 0:
					target_line = lines[x - 2]

	if target_line >= 0:
		target_surface = get_surface_by_line(target_line, surface)

	return target_line, target_surface

# 查询一条边在一个面中相邻的两边所在的面
def get_surface_by_neighbouring_line(line, surface):
	target_line = -1
	target_surface = -1
	target_other_line = -1
	target_other_surface = -1

	lines = SURFACES[surface]
	if lines:
		lines_len = len(lines)
		for x in range(0, lines_len):
			if lines[x] == line:
				if (x + 1) > lines_len:
					target_line = lines[0]
					target_other_line = lines[x - 1]
				elif x - 1 < 0:
					target_line = lines[x + 1]
					target_other_line = lines[lines_len - 1]
				else:
					target_line = lines[x + 1]
					target_other_line = lines[x - 1]

	if target_line >= 0:
		target_surface = get_surface_by_line(target_line, surface)
	if target_other_line >= 0:
		target_other_surface = get_surface_by_line(target_other_line, surface)

	return target_surface, target_other_surface

# 正二六面体中一个正方形与其相邻的两个三角形一起点亮，然后熄灭随后下一组点亮
def flash_triangle_square_triangle(flash_number, interval):
	start_line = 13
	start_surface = 1

	index = 0
	while index < flash_number:
		if start_line < 0 or start_surface < 0:
			return

		target_surface, target_other_surface = get_surface_by_neighbouring_line(start_line, start_surface)

		if target_surface >= 0:
			lines = SURFACES[target_surface]
			if lines:
				for line in lines:
					light_line(line, COLOR.RED)

		lines = SURFACES[start_surface]
		if lines:
			for line in lines:
				light_line(line, COLOR.RED)
		
		if target_other_surface >= 0:
			lines = SURFACES[target_other_surface]
			if lines:
				for line in lines:
					light_line(line, COLOR.RED)

		time.sleep(interval)

		if target_surface >= 0:
			lines = SURFACES[target_surface]
			if lines:
				for line in lines:
					light_line(line, COLOR.RED)

		lines = SURFACES[start_surface]
		if lines:
			for line in lines:
				light_line(line, COLOR.RED)
		
		if target_other_surface >= 0:
			lines = SURFACES[target_other_surface]
			if lines:
				for line in lines:
					light_line(line, COLOR.RED)

		opposite_line, opposite_surface = get_surface_by_opposite_line(start_line, start_surface)
		if opposite_line >= 0 and opposite_surface >= 0:
			start_line, start_surface = get_surface_by_opposite_line(opposite_line, opposite_surface)

		
		index += 1
