#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:model20.py

import random
import time
import board
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


LED_COUNT = 2340      # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM! GPIO 13 or 18 on RPi 3).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 11          # DMA channel to use for generating signal (Between 1 and 14)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # 0 or 1
LED_STRIP = ws.WS2811_STRIP_GRB


STRIP = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
STRIP.begin()


class COLOR:
	BLACK = Color(0, 0, 0)
	GREEN = Color(0, 255, 0)
	RED = Color(255, 0, 0)
	BLUE = Color(0, 0, 255)
	YELLOW = Color(255, 255, 0)
	PURPLE = Color(255, 0, 255)
	TURQUOISE = Color(0, 255, 255)


LINES_LED = [
	[0, 77], 	    #0
	[234, 311], 	#1
	[312, 389], 	#2
	[546, 623], 	#3
	[468, 545], 	#4
	[78, 155], 	    #5
	[156, 233], 	#6
	[390, 467], 	#7
	[624, 701], 	#8
	[702, 779], 	#9
	[1482, 1559], 	#10
	[780, 857],  	#11
	[858, 935],  	#12
	[936, 1013],  	#13
	[1014, 1091],  	#14
	[1092, 1169],  	#15
	[1170, 1247],  	#16
	[1248, 1325],  	#17
	[1326, 1403],  	#18
	[1404, 1481],  	#19
	[1950, 2027],  	#20
	[2184, 2261],  	#21
	[2262, 2339],  	#22
	[1638, 1715],  	#23
	[1560, 1637],  	#24
	[1872, 1949],  	#25
	[2106, 2183],  	#26
	[2028, 2105],  	#27
	[1716, 1793],  	#28
	[1794, 1871]  	#29
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


POINT_LINES = {}
line_index = 0
for line in LINES:
	for point in line:
		point_key = str(point)
		if not (point_key in POINT_LINES.keys()):
			POINT_LINES[point_key] = []
		POINT_LINES[point_key].append(line_index)
	line_index += 1


LINE_SURFACES = {}
surface_index = 0
for surface in SURFACES:
	for line in surface:
		line_key = str(line)
		if not (line_key in LINE_SURFACES.keys()):
			LINE_SURFACES[line_key] = []
		LINE_SURFACES[line_key].append(surface_index)
	surface_index += 1


def contain(items, item):
	if len(items) > 0:
		for i in items:
			if i == item:
				return 1
	return 0


def light_line(line, color):
	line_led = LINES_LED[line]

	start_point = line_led[0]
	end_point = line_led[1]

	if start_point > end_point:
		current_point = start_point
		while current_point >= end_point:
			STRIP.setPixelColor(current_point - 1, color)
			current_point -= 1
	else:
		current_point = start_point
		while current_point <= end_point:
			STRIP.setPixelColor(current_point - 1, color)
			current_point += 1
	STRIP.show()

def random_line(point, ignore_line):
	lines_all = POINT_LINES[str(point)]
	lines = []

	if lines_all:
		for line in lines_all:
			if contain(ignore_line, line) == 0:
				lines.append(line)

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
				surfaces.append(surface)

	if len(surfaces) > 0:
		surface_index = random.randint(0, len(surfaces) - 1)
		return surfaces[surface_index]

	return -1


def fill(color):
	for i in range(STRIP.numPixels()):
		STRIP.setPixelColor(i, color)
	STRIP.show()

# 逐个点亮一条边上的所有灯
def flow_line(start_point, line, color, interval):
	line_led = LINES_LED[line]
	start_led = -1
	end_led = -1
	if LINES[line][0] == start_point:
		start_led = line_led[0]
		end_led = line_led[1]
	else:
		start_led = line_led[1]
		end_led = line_led[0]

	led_count = abs(start_led - end_led) + 1
	for x in range(0, led_count):
		if start_led > end_led:
			STRIP.setPixelColor(start_led - x, color)
		else:
			STRIP.setPixelColor(start_led + x, color)
		STRIP.show()
		time.sleep(interval)


# 逐个点亮两条边上的所有灯
def flow_double_line(pre_start_point, pre_line, pre_color, start_point, line, color, interval):
	pre_line_led = LINES_LED[pre_line]
	pre_start_led = -1
	pre_end_led = -1
	if LINES[pre_line][0] == pre_start_point:
		pre_start_led = pre_line_led[0]
		pre_end_led = pre_line_led[1]
	else:
		pre_start_led = pre_line_led[1]
		pre_end_led = pre_line_led[0]

	line_led = LINES_LED[line]
	start_led = -1
	end_led = -1
	if LINES[line][0] == start_point:
		start_led = line_led[0]
		end_led = line_led[1]
	else:
		start_led = line_led[1]
		end_led = line_led[0]

	pre_led_count = abs(pre_start_led - pre_end_led) + 1
	led_count = abs(start_led - end_led) + 1
	max_led_count = pre_led_count 
	if led_count > max_led_count:
		max_led_count = led_count

	for x in range(0, max_led_count):
		if x < pre_led_count:
			if pre_start_led > pre_end_led:
				STRIP.setPixelColor(pre_start_led - x, pre_color)
			else:
				STRIP.setPixelColor(pre_start_led + x, pre_color)

		if x < led_count:
			if start_led > end_led:
				STRIP.setPixelColor(start_led - x, color)
			else:
				STRIP.setPixelColor(start_led - x, color)

		STRIP.show()
		time.sleep(interval)


# 从一条边向另一条相邻的边流动点亮
def flow(start_point, flow_line_number, interval):
	ignore_line = []
	
	pre_start_point = -1
	pre_line = -1

	index = 0
	while index < flow_line_number:
		line = random_line(start_point, ignore_line)
		if line == -1:
			return

		if pre_line == -1:
			flow_line(start_point, line, COLOR.RED, interval)
			pre_start_point = start_point
			pre_line = line
		else:
			flow_double_line(pre_start_point, pre_line, COLOR.GREEN, start_point, line, COLOR.RED, interval)
			pre_start_point = start_point
			pre_line = line

		ignore_line = [line]
		if LINES[line][0] == start_point:
			start_point = LINES[line][1]
		else:
			start_point = LINES[line][0]

		index += 1

	if pre_line > -1:
		flow_line(pre_start_point, pre_line, COLOR.GREEN, interval)


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
					lines_dict[str(line)] = line
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
			start_led_list = []
			end_led_list = []
			led_count_list = []
			max_led_count = 0
			end_points_dict = {}

			for line in lines:
				line_led = LINES_LED[line]
				start_led = -1
				end_led = -1
				end_point = -1
				if LINES[line][0] == point_index:
					start_led = line_led[0]
					end_led = line_led[1]
					end_point = LINES[line][1]
				else:
					start_led = line_led[1]
					end_led = line_led[0]
					end_point = LINES[line][0]
				if end_point > -1:
					end_points_dict[str(end_point)] = end_point

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
				for y in range(0, len(start_led_list)):
					start_led = start_led_list[y]
					end_led = end_led_list[y]
					led_count = led_count_list[y]
					
					if x < led_count:
						if start_led > end_led:
							STRIP.setPixelColor(start_led - x, COLOR.RED)
						else:
							STRIP.setPixelColor(start_led + x, COLOR.RED)
				STRIP.show()
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
					end_point = LINES[line][1]
				else:
					end_point = LINES[line][0]
				if end_point > -1:
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
