#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time
import board
import neopixel

LED_PIN = board.D21
LED_COUNT = 165
LED_BRIGHTNESS = 0.2
LED_ORDER = neopixel.GRB

class COLOR:
	BLACK = (0, 0, 0)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)


pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)


LINES_LED = [
	[1, 14],    #0
	[14, 27],   #1
	[27, 41],   #2
	[41, 55],   #3
	[123, 136], #4
	[69, 82],   #5
	[109, 122], #6
	[95, 109],  #7
	[82, 95],   #8
	[55, 69],   #9
	[151, 164], #10
	[137, 150]  #11
]

LINES = [
	[0, 1], #0
	[1, 2], #1
	[2, 3], #2
	[3, 0], #3
	[4, 3], #4
	[5, 4], #5
	[6, 5], #6
	[7, 6], #7
	[4, 7], #8
	[0, 5], #9
	[6, 1], #10
	[2, 7]  #11
]

SURFACES = [
	[0, 1, 2, 3], 	#0
	[5, 8, 7, 6], 	#1
	[2, 11, 8, 4], 	#2
	[0, 9, 6, 10], 	#3
	[1, 10, 7, 11], #4
	[3, 4, 5, 9]  	#5
]

POLYHEDRONS = [
	[0, 1, 2, 3, 4, 5] #0
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
	start_point = LINES_LED[line][0]
	end_point = LINES_LED[line][1]

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

def randomline(point, ignore_line):
	lines = []

	lines_all = POINT_LINES[str(point)]
	if lines_all:
		for line in lines_all:
			if contain(ignore_line, line) == 0:
				lines.append(line);

	if len(lines) > 0:
		line_index = random.randint(0, len(lines) - 1)
		return lines[line_index]

	return -1

def randomsurface(line, ignore_surface):
	surfaces = []

	surfaces_all = LINE_SURFACES[str(line)]
	if surfaces_all:
		for surface in surfaces_all:
			if contain(ignore_surface, surface) == 0:
				surfaces.append(surface);

	if len(surfaces) > 0:
		surface_index = random.randint(0, len(surfaces) - 1)
		return surfaces[surface_index]

	return -1


# 从一条边向另一条相邻的边流动点亮
def flow(start_point, flow_line_number, interval):
	pixels.fill(COLOR.GREEN)
	pixels.show()	

	ignore_line = [];
	pre_line = -1
	pre_start_led = -1
	pre_end_led = -1

	index = 0
	while index < flow_line_number:
		line = randomline(start_point, ignore_line)
		if line == -1:
			return

		if pre_line == -1:
			line_led = LINES_LED[line]
			start_led = -1
			end_led = -1
			if LINES[line][0] == start_point:
				start_led = line_led[0]
				end_led = line_led[1]
			else:
				start_led = line_led[1]
				end_led = line_led[0]

			pre_line = line
			pre_start_led = start_led
			pre_end_led = end_led

			pre_led_count = abs(pre_start_led - pre_end_led) + 1
			for x in range(0, pre_led_count):
				if pre_start_led > pre_end_led:
					pixels[pre_start_led - x] = COLOR.RED;
				else:
					pixels[pre_start_led + x] = COLOR.RED;
				pixels.show()

				time.sleep(interval)
		else:
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
			max_led_count = pre_led_count 
			led_count = abs(start_led - end_led) + 1
			if led_count > max_led_count:
				max_led_count = led_count

			for x in range(0, max_led_count):
				if x < pre_led_count:
					if pre_start_led > pre_end_led:
						pixels[pre_start_led - x] = COLOR.GREEN;
					else:
						pixels[pre_start_led + x] = COLOR.GREEN;
					pixels.show()

				if x < led_count:
					if start_led > end_led:
						pixels[start_led - x] = COLOR.RED;
					else:
						pixels[start_led + x] = COLOR.RED;
					pixels.show()

				time.sleep(interval)

			pre_line = line
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
				pixels[pre_start_led - x] = COLOR.GREEN;
			else:
				pixels[pre_start_led + x] = COLOR.GREEN;
			pixels.show()

			time.sleep(interval)


def flash(second):
	pre_index = -1

	index = 0
	while index < 10:
		surface_index = random.randint(0, len(SURFACES) - 1)
		if surface_index == pre_index:
			continue

		lines = SURFACES[surface_index]
		if lines:
			for line in lines:
				light_line(line, COLOR.RED)

		time.sleep(second)
		pixels.fill(COLOR.BLACK)
		pre_index = surface_index

		index += 1


def scroll(line, second):
	ignore_surface = [];
	index = 0
	while index < 10:
		surface = randomsurface(line, ignore_surface)
		target_line = -1
		lines = SURFACES[surface]
		if lines:
			lines_len = len(lines)
			for x in range(0, lines_len):
				if lines[x] == line:
					if (x + 2) < lines_len:
						target_line = lines[x + 2]
					elif x - 2 >= 0:
						target_line = lines[x - 2]

		if target_line > -1:
			light_line(target_line, COLOR.RED)
		else:
			return

		time.sleep(second)
		pixels.fill(COLOR.BLACK)
		ignore_surface = [surface];
		line = target_line;

		index += 1


if __name__ == '__main__':
	while True:	
		flow(0, 40, 0.2)
		# flash(1)
		# scroll(8, 0.5)
