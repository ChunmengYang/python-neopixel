#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import board
import neopixel


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
];

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
];

SURFACES = [
	[0, 1, 2, 3], 	#0
	[5, 8, 7, 6], 	#1
	[2, 11, 8, 4], 	#2
	[0, 9, 6, 10], 	#3
	[1, 10, 7, 11], #4
	[3, 4, 5, 9]  	#5
];


POINT_LINES = {};
line_index = 0;
for line in LINES:
	for point in line:
	    if not POINT_LINES[point]:
	    	POINT_LINES[point] = [];
	    POINT_LINES[point].append(line_index);
    line_index++;


LINE_SURFACES = {};
surface_index = 0;
for surface in SURFACES:
    for line in surface:
	    if not LINE_SURFACES[line]:
	    	LINE_SURFACES[line] = [];
	    LINE_SURFACES[line].append(surface_index);
    surface_index++;



def contain(items, item):
	if len(items) > 0:
		for i in items:
			if i == item:
				return 1
	return 0


LED_PIN = board.D18
LED_COUNT = 165
LED_BRIGHTNESS = 0.2
LED_ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)

while True:
	pixels.fill((255, 0, 0))
	pixels.show()
	time.sleep(1)
	pixels.fill((0, 255, 0))
	pixels.show()
	time.sleep(1)
	pixels.fill((0, 0, 255))
	pixels.show()
	time.sleep(1)
