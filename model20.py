#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:model20.py

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
STRIPS[0] = Adafruit_NeoPixel(960, 12, 800000, 11, False, 128, 1, ws.WS2811_STRIP_GRB)
STRIPS[0].begin()

STRIPS[1] = Adafruit_NeoPixel(960, 16, 800000, 12, False, 128, 1, ws.WS2811_STRIP_GRB)
STRIPS[1].begin()

STRIPS[2] = Adafruit_NeoPixel(960, 21, 800000, 13, False, 128, 1, ws.WS2811_STRIP_GRB)
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
	{'c': 1, 'n': [0, 59]}, 	#10
	{'c': 1, 'n': [0, 59]}, 	#11
	{'c': 1, 'n': [0, 59]},  	#12
	{'c': 1, 'n': [0, 59]}, 	#13
	{'c': 1, 'n': [0, 59]},  	#14
	{'c': 1, 'n': [0, 59]},  	#15
	{'c': 1, 'n': [0, 59]},  	#16
	{'c': 1, 'n': [0, 59]},  	#17
	{'c': 1, 'n': [0, 59]},  	#18
	{'c': 1, 'n': [0, 59]},  	#19
	{'c': 2, 'n': [0, 59]},  	#20
	{'c': 2, 'n': [0, 59]},  	#21
	{'c': 2, 'n': [0, 59]},  	#22
	{'c': 2, 'n': [0, 59]},  	#23
	{'c': 2, 'n': [0, 59]},  	#24
	{'c': 2, 'n': [0, 59]},  	#25
	{'c': 2, 'n': [0, 59]},  	#26
	{'c': 2, 'n': [0, 59]},  	#27
	{'c': 2, 'n': [0, 59]},  	#28
	{'c': 2, 'n': [0, 59]}  	#29
]

LINES = [
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

SURFACES = [
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


# 随机点亮一条线所在的面
def flash_double_surface(flash_number, interval):
	pre_index = -1
	index = 0
	while index < flash_number:
		line_index = random.randint(0, len(LINES) - 1)
		if line_index == pre_index:
			continue

		surfaces = LINE_SURFACES[str(line_index)]
		if surfaces:
			for surface in surfaces:
				lines = SURFACES[surface]
				if lines:
					for line in lines:
						light_line(line, COLOR.RED)

		time.sleep(interval)
		if surfaces:
			for surface in surfaces:
				lines = SURFACES[surface]
				if lines:
					for line in lines:
						light_line(line, COLOR.BLACK)

		pre_index = line_index
		index += 1

# 以给定点查找线，线的起始点都必须在给定点里
def get_layer_lines(points_dict):
	lines_dict = {}

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
	return lines_dict


# 逐个点亮点所在线的所有灯点，再熄灭, 最后点亮五边形。 0-11每个点都执行一次效果，最后全部灯都点亮。
def flow_lines_by_point(interval):
	pre_point_index = -1

	for x in range(0, 12):
		point_index = x
		if point_index == pre_point_index:
			continue

		lines = POINT_LINES[str(point_index)]
		if lines:
			# 获取几条边的灯带控制器、起始点的灯点索引、边的灯点数
			strip_list = []
			start_led_list = []
			end_led_list = []
			led_count_list = []
			max_led_count = 0
			end_points_dict = {}

			for line in lines:
				line_led = LINES_LED[line]
				strip = STRIPS[line_led['c']]
				start_led = -1
				end_led = -1
				end_point = -1
				if LINES[line][0] == point_index:
					start_led = line_led['n'][0]
					end_led = line_led['n'][1]
					end_point = LINES[line][1]
				else:
					start_led = line_led['n'][1]
					end_led = line_led['n'][0]
					end_point = LINES[line][0]
				end_points_dict[str(end_point)] = end_point

				strip_list.append(strip)
				start_led_list.append(start_led)
				end_led_list.append(end_led)

				led_count = abs(start_led - end_led) + 1
				led_count_list.append(led_count)
				if led_count > max_led_count:
					max_led_count = led_count

			# 获取点下一层五边形线
			lines_dict = get_layer_lines(end_points_dict)

			# 几条边同时逐个点亮边上的灯点，
			for x in range(0, max_led_count):
				for y in range(0, len(strip_list)):
					strip = strip_list[y]
					start_led = start_led_list[y]
					end_led = end_led_list[y]
					led_count = led_count_list[y]
					
					if x < led_count:
						if start_led > end_led:
							strip.setPixelColor(start_led - x, COLOR.RED)
						else:
							strip.setPixelColor(start_led + x, COLOR.RED)
						strip.show()

				time.sleep(interval)

			# 熄灭所有边的灯点
			for line in lines:
				light_line(line, COLOR.BLACK)

			# 点亮五边形
			for key, line in lines_dict.items():
				light_line(line, COLOR.RED)

			time.sleep(interval)
		pre_point_index = point_index

	fill(COLOR.RED)


# 随机找个五边形，5条边颜色滚动。
def scroll_pentagon_lines(interval):
	pre_point_index = -1

	for x in range(0, 12):
		point_index = x
		if point_index == pre_point_index:
			continue

		lines = POINT_LINES[str(point_index)]
		if lines:
			end_points_dict = {}

			for line in lines:
				end_point = -1
				if LINES[line][0] == point_index:
					end_proint = LINES[line][1]
				else:
					end_proint = LINES[line][0]
				end_points_dict[str(end_point)] = end_point
	
			# 获取五边形线
			pentagon_lines_dict = get_layer_lines(end_points_dict)

			# 按照实际相邻关系排序
			lines = []
			for _, line in pentagon_lines_dict.items():
				lines.append(line)
			order_lines = []
			first_line = lines.pop()
			order_lines.append(first_line)
			next_point = LINES[first_line][1]
			count = len(lines)
			for x in range(0, count):
				for line in lines:
					if next_point == LINES[line][0]:
					 	order_lines.append(line)
					 	next_point = LINES[line][1]
					 	lines.remove(line)
					 	break
					elif next_point == LINES[line][1]:
						order_lines.append(line)
						next_point = LINES[line][0]
						lines.remove(line)
						break
			# 滚动变颜色
			colors = [COLOR.RED, COLOR.GREEN, COLOR.PURPLE, COLOR.TURQUOISE, COLOR.YELLOW, COLOR.BLUE]
			for x in range(0, len(order_lines)):
				color = colors.pop()
				colors.insert(0, color)
				index = 0
				for line in order_lines:
					light_line(line, colors[index])
					index += 1
				time.sleep(interval)

		pre_point_index = point_index
