#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import threading
import model26
import model20
from rpi_ws281x import Color
import threading

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


# 双随机面闪烁
def double_flash_surface():
	model26.fill(COLOR.GREEN)
	model20.fill(COLOR.RED)
	threading.Thread(target=model20.flash_surface,args=(20, 0.2)).start()
	threading.Thread(target=model26.flash_surface,args=(20, 0.2)).start()


# 双流动点亮
def double_flow():
	model26.fill(COLOR.GREEN)
	model20.fill(COLOR.GREEN)
	threading.Thread(target=model20.flow,args=(0, 40, 0.1)).start()
	threading.Thread(target=model26.flow,args=(0, 40, 0.1)).start()


# 双平行滚动
def double_scroll():
	model26.fill(COLOR.GREEN)
	model20.fill(COLOR.RED)
	threading.Thread(target=model26.parallel_line_scroll,args=(0, 40, 0.2)).start()
	threading.Thread(target=model26.parallel_line_scroll,args=(1, 40, 0.2)).start()


if __name__ == '__main__':
	while True:
		# alternate_flash(20, 0.2)
		double_flow()
		time.sleep(300)


		