#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:model20.py

import random
import time
import board
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
import RPi.GPIO as GPIO
import colors

COLOR = colors.COLOR

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


LINES_LED = [
	[0, 77], 	    #0
	[312, 234], 	#1
	[313, 389], 	#2
	[546, 623], 	#3
	[545, 468], 	#4
	[78, 155], 	    #5
	[156, 233], 	#6
	[390, 467], 	#7
	[624, 701], 	#8
	[702, 779], 	#9
	[1559, 1482], 	#10
	[780, 857],  	#11
	[935, 858],  	#12
	[936, 1013],  	#13
	[1091, 1014],  	#14
	[1092, 1169],  	#15
	[1247, 1170],  	#16
	[1248, 1325],  	#17
	[1403, 1326],  	#18
	[1404, 1481],  	#19
	[1950, 2027],  	#20
	[2184, 2261],  	#21
	[2262, 2339],  	#22
	[1715, 1638],  	#23
	[1637, 1560],  	#24
	[1949, 1872],  	#25
	[2183, 2106],  	#26
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

# 点所在的线
POINT_LINES = {}
line_index = 0
for line in LINES:
	for point in line:
		point_key = str(point)
		if not (point_key in POINT_LINES.keys()):
			POINT_LINES[point_key] = []
		POINT_LINES[point_key].append(line_index)
	line_index += 1

# 线所在的面
LINE_SURFACES = {}
surface_index = 0
for surface in SURFACES:
	for line in surface:
		line_key = str(line)
		if not (line_key in LINE_SURFACES.keys()):
			LINE_SURFACES[line_key] = []
		LINE_SURFACES[line_key].append(surface_index)
	surface_index += 1

# 面上的点
SURFACES_POINT = {}
surface_index = 0
for surface in SURFACES:
	surface_points_dict = {}
	for line in surface:
		for point in LINES[line]:
			point_key = str(point)
			if not (point_key in surface_points_dict.keys()):
				surface_points_dict[point_key] = point

	surface_points = []
	for _, point in surface_points_dict.items():
		surface_points.append(point)

	SURFACES_POINT[str(surface_index)] = surface_points
	surface_index += 1


# 查询列表是否包含了某子项。
# items，列表。
# item，子项。
# return, 包含返回1，不包含返回0
def contain(items, item):
	if len(items) > 0:
		for i in items:
			if i == item:
				return 1
	return 0


# 查找随机一条线。
# point，在要查找线上的点。
# ignore_line，要忽略的线的列表。
# return，返回线的编号，没有查询到返回-1。
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


# 查找随机一个面
# line，在要查找面上的线。
# ignore_surface，要忽略的面的列表。
# return，返回面的编号，没有查询到返回-1。
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


# 在所有线中查找起始点和结束点都在给定点列表中线
# points_dict, 点的字典，格式为{'0':0, '1':1...}。
def get_lines_by_start_end_at_points(points):
	result_lines_dict = {}
	result_lines = []
	points_dict = {}
	for point in points:
		points_dict[str(point)] = point

	for point in points:
		lines = POINT_LINES[str(point)]
		if lines:
			for line in lines:
				another_point = -1
				if LINES[line][0] == point:
					another_point = LINES[line][1]
				if LINES[line][1] == point:
					another_point = LINES[line][0]

				if str(another_point) in points_dict:
					result_lines_dict[str(line)] = line

	for _, line in result_lines_dict.items():
		result_lines.append(line)
	return result_lines


# 查找五边形的线
# point，一个顶点
def get_pentagon(point):
	lines = POINT_LINES[str(point)]
	if lines:
		end_points = []

		for line in lines:
			end_point = -1
			if LINES[line][0] == point:
				end_point = LINES[line][1]
			else:
				end_point = LINES[line][0]

			if end_point > -1:
				end_points.append(end_point)
		
		# 获取五边形线
		pentagon_lines = get_lines_by_start_end_at_points(end_points)

		return pentagon_lines
	return []


# 设置一条线的亮灯颜色，调用该函数之后要再调用STRIP.show()才能起作用。
# line，要设置的线编号。
# color，设置的颜色。
def light_line(line, color):
	line_led = LINES_LED[line]

	start_point = line_led[0]
	end_point = line_led[1]

	if start_point > end_point:
		current_point = start_point
		while current_point >= end_point:
			STRIP.setPixelColor(current_point, color)
			current_point -= 1
	else:
		current_point = start_point
		while current_point <= end_point:
			STRIP.setPixelColor(current_point, color)
			current_point += 1


# 设置一组线的亮灯颜色。
# lines，线的列表。
# color，设置的颜色。
def light_lines(lines, color):
	if len(lines) > 0:
		for line in lines:
			light_line(line, color)
		STRIP.show()


# 设置所有灯的亮灯颜色
# color，设置的颜色。
def fill(color):
	for i in range(STRIP.numPixels()):
		STRIP.setPixelColor(i, color)
	STRIP.show()


# 逐段点亮一条边上的所有灯
# start_point，开始点，该点为line的一段点。
# line，线的编号。
# color，设置的颜色。
# lamps_number，每段灯的数量。
# interval，时间间隔，单位为秒。
def flow_line(start_point, line, color, lamps_number, interval):
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
	interval_count = 0
	for x in range(0, led_count, 1):
		if start_led > end_led:
			STRIP.setPixelColor(start_led - x, color)
		else:
			STRIP.setPixelColor(start_led + x, color)

		interval_count += 1
		if interval_count == lamps_number:
			STRIP.show()
			time.sleep(interval)
			interval_count = 0

	if interval_count > 0:
		STRIP.show()
		time.sleep(interval)


# 逐个段亮两条边上的所有灯
# pre_start_point，第一条线的开始点，该点为pre_line的一段点。
# pre_line，第一条线的编号。
# pre_color，第一条线设置的颜色。
# start_point，第二条线开始点，该点为line的一段点。
# line，第二条线的编号。
# color，第二条设置的颜色。
# lamps_number，每段灯的数量。
# interval，时间间隔，单位为秒。
def flow_double_line(pre_start_point, pre_line, pre_color, start_point, line, color, lamps_number, interval):
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

	interval_count = 0
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
				STRIP.setPixelColor(start_led + x, color)

		interval_count += 1
		if interval_count == lamps_number:
			STRIP.show()
			time.sleep(interval)
			interval_count = 0

	if interval_count > 0:
		STRIP.show()
		time.sleep(interval)


# 从一条边向另一条相邻的边流动点亮
# start_point，开始点。
# max_line_number，最大亮灯线数，大于2。
# flow_line_number，流动经过的线数。
# color1，点亮颜色。
# color2，恢复到原来颜色。
# lamps_number，每次流动的灯数, 小于线的灯数（78）。
# interval，每次流动的时间间隔，单位为秒
def flow(start_point, max_line_number, flow_line_number, color1, color2, lamps_number, interval):
	# 已经亮起的线列表
	light_up_lines = []

	index = 0
	while index < flow_line_number:
		ignore_line = []
		for line_dict in light_up_lines:
			ignore_line.append(line_dict["line"])

		line = random_line(start_point, ignore_line)
		if line == -1:
			return

		if len(light_up_lines) < max_line_number:
			flow_line(start_point, line, color1, lamps_number, interval)
		else:
			pre_line_dict = light_up_lines.pop(0)
			pre_start_point = pre_line_dict["start_point"]
			pre_line = pre_line_dict["line"]
			flow_double_line(pre_start_point, pre_line, color2, start_point, line, color1, lamps_number, interval)

		light_up_lines.append({"start_point": start_point, "line": line})

		if LINES[line][0] == start_point:
			start_point = LINES[line][1]
		else:
			start_point = LINES[line][0]

		index += 1

	light_up_lines_count = len(light_up_lines)
	if light_up_lines_count > 0:
		for x in range(0, light_up_lines_count):
			pre_line_dict = light_up_lines.pop(0)
			pre_start_point = pre_line_dict["start_point"]
			pre_line = pre_line_dict["line"]
			flow_line(pre_start_point, pre_line, color2, lamps_number, interval)


# 随机点亮某个面
# color1，点亮颜色。
# color2，恢复到原来颜色。
# flash_number，点亮次数。
# interval，点亮时间间隔，单位为秒。
def flash_surface(color1, color2, flash_number, interval):
	pre_index = -1
	index = 0
	while index < flash_number:
		surface_index = random.randint(0, len(SURFACES) - 1)
		if surface_index == pre_index:
			continue

		lines = SURFACES[surface_index]
		light_lines(lines, color1)

		STRIP.show()
		time.sleep(interval)

		light_lines(lines, color2)
		STRIP.show()

		pre_index = surface_index

		index += 1


# 随机点亮一条线所在的面
# color1，点亮颜色。
# color2，恢复到原来颜色。
# flash_number，点亮次数。
# interval，点亮时间间隔，单位为秒。
def flash_double_surface(color1, color2, flash_number, interval):
	pre_index = -1
	index = 0
	while index < flash_number:
		line_index = random.randint(0, len(LINES) - 1)
		if line_index == pre_index:
			continue

		surfaces = LINE_SURFACES[str(line_index)]
		lines = []
		if surfaces:
			for surface in surfaces:
				lines += SURFACES[surface]
				
		light_lines(lines, color1)
		time.sleep(interval)
		light_lines(lines, color2)

		pre_index = line_index
		index += 1

      
# 逐个点亮点所在线的所有灯点，再熄灭, 最后点亮五边形。 0-11每个点都执行一次效果，最后全部灯都点亮。
# color1，点亮颜色。
# color2，恢复到原来颜色。
# interval，点亮时间间隔，单位为秒。
def flow_lines_by_point(color1, color2, interval):
	pre_point_index = -1

	for x in range(0, 12, 3):
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
			end_points = []

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
					end_points.append(end_point)

				start_led_list.append(start_led)
				end_led_list.append(end_led)

				led_count = abs(start_led - end_led) + 1
				led_count_list.append(led_count)
				if led_count > max_led_count:
					max_led_count = led_count

			# 获取点下一层五边形线
			pentagon_lines = get_lines_by_start_end_at_points(end_points)

			# 几条边同时逐个点亮边上的灯点
			interval_count = 0
			for x in range(0, max_led_count):
				for y in range(0, len(start_led_list)):
					start_led = start_led_list[y]
					end_led = end_led_list[y]
					led_count = led_count_list[y]
					
					if x < led_count:
						if start_led > end_led:
							STRIP.setPixelColor(start_led - x, color1)
						else:
							STRIP.setPixelColor(start_led + x, color1)

				interval_count += 1
				if interval_count == 10:
					STRIP.show()
					time.sleep(interval)
					interval_count = 0

			if interval_count > 0:
				STRIP.show()
				time.sleep(interval)

			# 熄灭所有边的灯点
			light_lines(lines, color2)

			# 点亮五边形
			light_lines(pentagon_lines, color1)

			time.sleep(interval * 20)
			# 熄灭五边形
			light_lines(pentagon_lines, color2)

		pre_point_index = point_index


# 随机点亮五边形。
# color1，点亮颜色。
# color2，恢复到原来颜色。
# interval，点亮时间间隔，单位为秒。
def light_pentagon_lines(color1, color2, interval):
	pre_point_index = -1

	for x in range(0, 12, 2):
		point_index = x
		if point_index == pre_point_index:
			continue

		lines = get_pentagon(point_index)
		if lines:
			light_lines(lines, color1)

			time.sleep(interval)

			light_lines(lines, color2)

		pre_point_index = point_index


# 随机找个五边形，5条边颜色滚动。
# color，恢复到原来颜色。
# interval，滚动时间间隔，单位为秒。
def scroll_pentagon_lines(color, interval):
	pre_point_index = -1

	for x in range(0, 12, 3):
		point_index = x
		if point_index == pre_point_index:
			continue

		lines = get_pentagon(point_index)
		if lines:
			# 按照实际相邻关系排序
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
			colors = [COLOR.RED, COLOR.GREEN, COLOR.PURPLE, COLOR.INDIGO, COLOR.YELLOW, COLOR.BLUE]
			for x in range(0, len(order_lines)):
				last_color = colors.pop()
				colors.insert(0, last_color)
				index = 0
				for line in order_lines:
					light_line(line, colors[index])
					index += 1
				STRIP.show()
				time.sleep(interval)

			light_lines(order_lines, color)

		pre_point_index = point_index
