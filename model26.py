#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:model26.py

import random
import time
import board
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_COUNT = 2880      # Number of LED pixels.
LED_PIN = 21          # GPIO pin connected to the pixels (must support PWM! GPIO 13 or 18 on RPi 3).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 12          # DMA channel to use for generating signal (Between 1 and 14)
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
	[960, 1019], 	#0
	[480, 539], 	#1
	[1440, 1499], 	#2
	[0, 59], 		#3
	[1020, 1079], 	#4
	[420, 479], 	#5
	[900, 959], 	#6
	[1380, 1439], 	#7
	[1860, 1919], 	#8
	[540, 599], 	#9
	[60, 119], 		#10
	[1500, 1559], 	#11
	[2100, 2159], 	#12
	[2040, 2099], 	#13
	[1980, 2039], 	#14
	[1920, 1979], 	#15
	[2340, 2399], 	#16
	[2280, 2339], 	#17
	[2220, 2279], 	#18
	[2160, 2219], 	#19
	[1080, 1139], 	#20
	[360, 419], 	#21
	[840, 899], 	#22
	[1320, 1379], 	#23
	[1800, 1859], 	#24
	[600, 659], 	#25
	[120, 179], 	#26
	[1560, 1619], 	#27
	[2580, 2639], 	#28
	[2520, 2579], 	#29
	[2460, 2519], 	#30
	[2400, 2459], 	#31
	[2820, 2879], 	#32
	[2760, 2819], 	#33
	[2700, 2759], 	#34
	[2640, 2699], 	#35
	[1140, 1199], 	#36
	[300, 359], 	#37
	[780, 839], 	#38
	[1260, 1319], 	#39
	[1740, 1799], 	#40
	[660, 719], 	#41
	[180, 239], 	#42
	[1620, 1679], 	#43
	[1200, 1259], 	#44
	[720, 779], 	#45
	[1680, 1739], 	#46
	[240, 299] 		#47
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


# 平行线滚动(只限于正方形的面)
def parallel_line_scroll(start_line, scroll_number, interval):
	light_line(start_line, COLOR.RED)
	time.sleep(interval)
	light_line(start_line, COLOR.GREEN)

	ignore_surface = []
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

		ignore_surface = [surface]
		start_line = target_line

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
					lines_dict[str(line)] = line
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
					light_line(line, COLOR.GREEN)

		lines = SURFACES[start_surface]
		if lines:
			for line in lines:
				light_line(line, COLOR.GREEN)
		
		if target_other_surface >= 0:
			lines = SURFACES[target_other_surface]
			if lines:
				for line in lines:
					light_line(line, COLOR.GREEN)

		opposite_line, opposite_surface = get_surface_by_opposite_line(start_line, start_surface)
		if opposite_line >= 0 and opposite_surface >= 0:
			start_line, start_surface = get_surface_by_opposite_line(opposite_line, opposite_surface)

		
		index += 1
