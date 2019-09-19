#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import threading
import model26
import model20
from rpi_ws281x import Color

class COLOR:
	BLACK = Color(0, 0, 0)
	GREEN = Color(0, 255, 0)
	RED = Color(255, 0, 0)
	BLUE = Color(0, 0, 255)
	YELLOW = Color(255, 255, 0)
	PURPLE = Color(255, 0, 255)
	TURQUOISE = Color(0, 255, 255)


# 两个模型交替亮起
def alternate_flash(flash_number, interval):
	index = 0
	while index < flash_number:
		if index > 0:
			if index % 2 == 1:
				model26.fill(COLOR.BLACK)
				model20.fill(COLOR.RED)
			else:
				model26.fill(COLOR.RED)
				model20.fill(COLOR.BLACK)
		else:
			model26.fill(COLOR.RED)
			model20.fill(COLOR.BLACK)

		time.sleep(interval)
		index += 1
		print(index)

if __name__ == '__main__':
	while True:
		alternate_flash(20, 0.2)
		