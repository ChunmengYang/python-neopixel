#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time
import board
import neopixel
import threading


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
	YELLOW = (255, 255, 0)
	PURPLE = (255, 0, 255)
	TURQUOISE = (0, 255, 255)

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


def fill_26(color):
	for x in range(0, len(pixels_26)):
		pixels_26[x].fill(color)
		pixels_26[x].show()

def fill_20(color):
	for x in range(0, len(pixels_20)):
		pixels_20[x].fill(color)
		pixels_20[x].show()

# 从一条边向另一条相邻的边流动点亮
def flow_26(start_point, flow_line_number, interval):
	ignore_line = [];
	pre_line = -1
	pre_pixels = None
	pre_start_led = -1
	pre_end_led = -1

	index = 0
	while index < flow_line_number:
		line = random_line_26(start_point, ignore_line)
		if line == -1:
			return

		if pre_line == -1:
			light_line_26(line, COLOR.RED)
		else:
			line_led = LINES_LED_26[line]
			pixels = pixels_26[pre_line_led['c']]
			start_led = -1
			end_led = -1
			if LINES_26[line][0] == start_point:
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
						pre_pixels[pre_start_led - x] = COLOR.GREEN;
					else:
						pre_pixels[pre_start_led + x] = COLOR.GREEN;
					pre_pixels.show()

				if x < led_count:
					if start_led > end_led:
						pixels[start_led - x] = COLOR.RED;
					else:
						pixels[start_led + x] = COLOR.RED;
					pixels.show()

				time.sleep(interval)

			pre_line = line
			pre_pixels = pixels
			pre_start_led = start_led
			pre_end_led = end_led
		
		ignore_line = [line];
		if LINES_26[line][0] == start_point:
			start_point = LINES_26[line][1]
		else:
			start_point = LINES_26[line][0]

		index += 1

	if pre_line > -1:
		pre_led_count = abs(pre_start_led - pre_end_led) + 1
		for x in range(0, pre_led_count):
			if pre_start_led > pre_end_led:
				pre_pixels[pre_start_led - x] = COLOR.GREEN;
			else:
				pre_pixels[pre_start_led + x] = COLOR.GREEN;
			pre_pixels.show()

			time.sleep(interval)

# 从一条边向另一条相邻的边流动点亮
def flow_20(start_point, flow_line_number, interval):
	ignore_line = [];
	pre_line = -1
	pre_pixels = None
	pre_start_led = -1
	pre_end_led = -1

	index = 0
	while index < flow_line_number:
		line = random_line_20(start_point, ignore_line)
		if line == -1:
			return

		if pre_line == -1:
			light_line_20(line, COLOR.RED)
		else:
			line_led = LINES_LED_20[line]
			pixels = pixels_20[pre_line_led['c']]
			start_led = -1
			end_led = -1
			if LINES_20[line][0] == start_point:
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
						pre_pixels[pre_start_led - x] = COLOR.GREEN;
					else:
						pre_pixels[pre_start_led + x] = COLOR.GREEN;
					pre_pixels.show()

				if x < led_count:
					if start_led > end_led:
						pixels[start_led - x] = COLOR.RED;
					else:
						pixels[start_led + x] = COLOR.RED;
					pixels.show()

				time.sleep(interval)

			pre_line = line
			pre_pixels = pixels
			pre_start_led = start_led
			pre_end_led = end_led
		
		ignore_line = [line];
		if LINES_20[line][0] == start_point:
			start_point = LINES_20[line][1]
		else:
			start_point = LINES_20[line][0]

		index += 1

	if pre_line > -1:
		pre_led_count = abs(pre_start_led - pre_end_led) + 1
		for x in range(0, pre_led_count):
			if pre_start_led > pre_end_led:
				pre_pixels[pre_start_led - x] = COLOR.GREEN;
			else:
				pre_pixels[pre_start_led + x] = COLOR.GREEN;
			pre_pixels.show()

			time.sleep(interval)


# 随机点亮某个面
def flash_surface_26(flash_number, interval):
	pre_index = -1
	index = 0
	while index < flash_number:
		surface_index = random.randint(0, len(SURFACES_26) - 1)
		if surface_index == pre_index:
			continue

		lines = SURFACES_26[surface_index]
		if lines:
			for line in lines:
				light_line_26(line, COLOR.RED)

		time.sleep(interval)
		if lines:
			for line in lines:
				light_line_26(line, COLOR.GREEN)
		pre_index = surface_index

		index += 1

# 随机点亮某个面
def flash_surface_20(flash_number, interval):
	pre_index = -1
	index = 0
	while index < flash_number:
		surface_index = random.randint(0, len(SURFACES_20) - 1)
		if surface_index == pre_index:
			continue

		lines = SURFACES_20[surface_index]
		if lines:
			for line in lines:
				light_line_20(line, COLOR.GREEN)

		time.sleep(interval)
		if lines:
			for line in lines:
				light_line_20(line, COLOR.RED)
		pre_index = surface_index

		index += 1


# 随机点亮一条线所在的面
def flash_double_surface_20(flash_number, interval):
	pre_index = -1
	index = 0
	while index < flash_number:
		line_index = random.randint(0, len(LINES_20) - 1)
		if line_index == pre_index:
			continue

		surfaces = LINE_SURFACES_20[str(line_index)]
		if surfaces:
			for surface in surfaces:
				lines = SURFACES_20[surface]
				if lines:
					for line in lines:
						light_line_20(line, COLOR.RED)

		time.sleep(interval)
		if surfaces:
			for surface in surfaces:
				lines = SURFACES_20[surface]
				if lines:
					for line in lines:
						light_line_20(line, COLOR.BLACK)

		pre_index = line_index
		index += 1


# 平行线滚动(只限于正方形的面)
def parallel_line_scroll_26(start_line, scroll_number, interval):
	light_line_26(start_line, COLOR.RED)
	time.sleep(interval)
	light_line_26(start_line, COLOR.GREEN)

	ignore_surface = [];
	index = 0
	while index < scroll_number:
		surface = random_surface_26(start_line, ignore_surface)
		target_line = -1
		lines = SURFACES_26[surface]
		if lines:
			lines_len = len(lines)
			for x in range(0, lines_len):
				if lines[x] == start_line:
					if (x + 2) < lines_len:
						target_line = lines[x + 2]
					elif x - 2 >= 0:
						target_line = lines[x - 2]

		if target_line > -1:
			light_line_26(target_line, COLOR.RED)
		else:
			return

		time.sleep(interval)
		light_line_26(target_line, COLOR.GREEN)

		ignore_surface = [surface];
		start_line = target_line;

		index += 1

# 以给定点查找线，线的起始点都必须在给定点里
def get_layer_lines_20(points_dict):
	lines_dict = {}

	for key, point in points_dict.items():
		lines = POINT_LINES_20[str(point)]
		if lines:
			for line in lines:
				another_point = -1
				if LINES_20[line][0] == point:
					another_point = LINES_20[line][1]
				if LINES_20[line][1] == point:
					another_point = LINES_20[line][0]

				if str(another_point) in points_dict:
					lines_dict[str(line)] = line;
	return lines_dict


# 逐个点亮点所在线的所有灯点，再熄灭, 最后点亮五边形。 0-11每个点都执行一次效果，最后全部灯都点亮。
def flow_lines_by_point_20(interval):
	pre_point_index = -1

	for x in range(0, 12):
		point_index = x
		if point_index == pre_point_index:
			continue

		lines = POINT_LINES_20[str(point_index)]
		if lines:
			# 获取几条边的灯带控制器、起始点的灯点索引、边的灯点数
			pixels_list = []
			start_led_list = []
			end_led_list = []
			led_count_list = []
			max_led_count = 0
			end_points_dict = {}

			for line in lines:
				line_led = LINES_LED_20[line]
				pixels = pixels_20[line_led['c']]
				start_led = -1
				end_led = -1
				end_point = -1
				if LINES_20[line][0] == point_index:
					start_led = line_led['n'][0]
					end_led = line_led['n'][1]
					end_point = LINES_20[line][1]
				else:
					start_led = line_led['n'][1]
					end_led = line_led['n'][0]
					end_point = LINES_20[line][0]
				end_points_dict[str(end_point)] = end_point

				pixels_list.append(pixels)
				start_led_list.append(start_led)
				end_led_list.append(end_led)

				led_count = abs(start_led - end_led) + 1
				led_count_list.append(led_count)
				if led_count > max_led_count:
					max_led_count = led_count

			# 获取点下一层五边形线
			lines_dict = get_layer_lines_20(end_points_dict)

			# 几条边同时逐个点亮边上的灯点，
			for x in range(0, max_led_count):
				for y in range(0, len(pixels_list)):
					pixels = pixels_list[y]
					start_led = start_led_list[y]
					end_led = end_led_list[y]
					led_count = led_count_list[y]
					
					if x < led_count:
						if start_led > end_led:
							pixels[start_led - x] = COLOR.RED;
						else:
							pixels[start_led + x] = COLOR.RED;
						pixels.show()

				time.sleep(interval)

			# 熄灭所有边的灯点
			for line in lines:
				light_line_20(line, COLOR.BLACK)

			# 点亮五边形
			for key, line in lines_dict.items():
				light_line_20(line, COLOR.RED)

			time.sleep(interval * )
		pre_point_index = point_index

	fill_20(COLOR.RED)


# 随机找个五边形，5条边颜色滚动。
def scroll_pentagon_lines_20(interval):
	pre_point_index = -1

	for x in range(0, 12):
		point_index = x
		if point_index == pre_point_index:
			continue

		lines = POINT_LINES_20[str(point_index)]
		if lines:
			end_points_dict = {}

			for line in lines:
				end_point = -1
				if LINES_20[line][0] == point_index:
					end_proint = LINES_20[line][1]
				else:
					end_proint = LINES_20[line][0]
				end_points_dict[str(end_point)] = end_point
	
			# 获取五边形线
			pentagon_lines_dict = get_layer_lines_20(end_points_dict)

			# 按照实际相邻关系排序
			lines = []
			for _, line in pentagon_lines_dict.items():
				lines.append(line)
			order_lines = []
			first_line = lines.pop()
			order_lines.append(first_line)
			next_point = LINES_20[first_line][1]
			count = len(lines)
			for x in range(0, count):
				for line in lines:
					if next_point == LINES_20[line][0]:
					 	order_lines.append(line)
					 	next_point = LINES_20[line][1]
					 	lines.remove(line)
					 	break
					elif next_point == LINES_20[line][1]:
						order_lines.append(line)
						next_point = LINES_20[line][0]
						lines.remove(line)
						break

			colors = [COLOR.RED, COLOR.GREEN, COLOR.PURPLE, COLOR.TURQUOISE, COLOR.YELLOW, COLOR.BLUE]
			for x in range(0, len(order_lines)):
				color = colors.pop()
				colors.insert(0, color)
				index = 0
				for line in order_lines:
					light_line_20(line, colors[index])
					index += 1
				time.sleep(interval)

		pre_point_index = point_index


def get_layer_lines_26(points_dict, pre_points_dict):
	lines_dict = {}
	next_points_dict = {}

	for key, point in points_dict.items():
		lines = POINT_LINES_26[str(point)]
		if lines:
			for line in lines:
				another_point = -1
				if LINES_26[line][0] == point:
					another_point = LINES_26[line][1]
				if LINES_26[line][1] == point:
					another_point = LINES_26[line][0]

				if str(another_point) in points_dict:
					lines_dict[str(line)] = line;
					continue
				if str(another_point) in pre_points_dict:
					continue

				next_points_dict[str(another_point)] = another_point

	return lines_dict, next_points_dict


# 点亮一层线，再点亮相邻平行的下一层线，以此类推，没有下一层就返回
def light_layer_to_layer_26(layer_number, interval):
	pre_points_dict = {}
	points_dict = ["0": 0, "1": 1, "2": 2, "3": 3]
	pre_lines_dict = {}

	index = 0
	while index < layer_number:
		lines_dict, next_points_dict = get_layer_lines_26(points_dict, pre_points_dict)

		for key, line in pre_lines_dict.items():
			light_line_26(line, COLOR.BLACK)

		for key, line in lines_dict.items():
			light_line_26(line, COLOR.RED)

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
def get_surface_by_line_26(line, ignore_surface):
	surfaces = LINE_SURFACES_26[str(line)]
	if surfaces:
		for surface in surfaces:
			if surface == ignore_surface:
				continue
			return surface
	return -1

# 查询一条边在一个正方形中的对面边和对面边所在正方形
def get_surface_by_opposite_line_26(line, surface):
	target_line = -1
	target_surface = -1
	lines = SURFACES_26[surface]
	if lines:
		lines_len = len(lines)
		for x in range(0, lines_len):
			if lines[x] == line:
				if (x + 2) < lines_len:
					target_line = lines[x + 2]
				elif x - 2 >= 0:
					target_line = lines[x - 2]

	if target_line >= 0:
		target_surface = get_surface_by_line_26(target_line, surface)

	return target_line, target_surface

# 查询一条边在一个面中相邻的两边所在的面
def get_surface_by_neighbouring_line_26(line, surface):
	target_line = -1
	target_surface = -1
	target_other_line = -1
	target_other_surface = -1

	lines = SURFACES_26[surface]
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
		target_surface = get_surface_by_line_26(target_line, surface)
	if target_other_line >= 0:
		target_other_surface = get_surface_by_line_26(target_other_line, surface)

	return target_surface, target_other_surface

# 正二六面体中一个正方形与其相邻的两个三角形一起点亮，然后熄灭随后下一组点亮
def flash_triangle_square_triangle_26(flash_number, interval):
	start_line = 13
	start_surface = 1

	index = 0
	while index < flash_number:
		if start_line < 0 or start_surface < 0:
			return

		target_surface, target_other_surface = get_surface_by_neighbouring_line_26(start_line, start_surface)

		if target_surface >= 0:
			lines = SURFACES_26[target_surface]
			if lines:
				for line in lines:
					light_line_26(line, COLOR.RED)

		lines = SURFACES_26[start_surface]
		if lines:
			for line in lines:
				light_line_26(line, COLOR.RED)
		
		if target_other_surface >= 0:
			lines = SURFACES_26[target_other_surface]
			if lines:
				for line in lines:
					light_line_26(line, COLOR.RED)

		time.sleep(interval)

		if target_surface >= 0:
			lines = SURFACES_26[target_surface]
			if lines:
				for line in lines:
					light_line_26(line, COLOR.RED)

		lines = SURFACES_26[start_surface]
		if lines:
			for line in lines:
				light_line_26(line, COLOR.RED)
		
		if target_other_surface >= 0:
			lines = SURFACES_26[target_other_surface]
			if lines:
				for line in lines:
					light_line_26(line, COLOR.RED)

		opposite_line, opposite_surface = get_surface_by_opposite_line_26(start_line, start_surface)
		if opposite_line >= 0 and opposite_surface >= 0:
			start_line, start_surface = get_surface_by_opposite_line_26(opposite_line, opposite_surface)

		
		index += 1


# 两个模型交替亮起
def double_flash_body(flash_number, interval):
	index = 0
	while index < flash_number:
		if index > 0:
			if index % 2 == 1:
				fill_26(COLOR.BLACK)
				fill_20(COLOR.RED)
			else:
				fill_26(COLOR.RED)
				fill_20(COLOR.BLACK)
		else:
			fill_26(COLOR.RED)
			fill_20(COLOR.BLACK)

		time.sleep(interval)
		index += 1


# 双随机面闪烁
def double_flash_surface():
	fill_26(COLOR.GREEN)
	fill_20(COLOR.RED)
	threading.Thread(target=flash_surface_26,args=(20, 0.5)).start()
	threading.Thread(target=flash_surface_20,args=(20, 0.5)).start()


# 双流动点亮
def double_flow():
	fill_26(COLOR.GREEN)
	fill_20(COLOR.GREEN)
	threading.Thread(target=flow_26,args=(0, 40, 0.2)).start()
	threading.Thread(target=flow_20,args=(0, 40, 0.2)).start()


# 双平行滚动
def double_scroll():
	fill_26(COLOR.GREEN)
	fill_20(COLOR.RED)
	threading.Thread(target=parallel_line_scroll_26,args=(0, 40, 0.2)).start()
	threading.Thread(target=parallel_line_scroll_26,args=(1, 40, 0.2)).start()


if __name__ == '__main__':
	while True:
		flow_lines_by_point_20(0.2)
		light_layer_to_layer_26(20, 0.2)
		double_flash_surface()
		double_flow()
		double_scroll()
