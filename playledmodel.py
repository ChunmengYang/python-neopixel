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
	LIGHT_GREEN = Color(0, 128, 0)
	RED = Color(255, 0, 0)
	BLUE = Color(0, 0, 255)
	LIGHT_BLUE = Color(0, 0, 128)
	YELLOW = Color(255, 255, 0)
	PURPLE = Color(255, 0, 255)
	TURQUOISE = Color(0, 255, 255)


# 两个模型交替亮起(信号有干扰，颜色不对)alternate_flash(40, 1.5)
def alternate_flash(flash_number, interval):
	index = 0
	while index < flash_number:
		model26.fill(COLOR.RED)
		model20.fill(COLOR.TURQUOISE)
		time.sleep(interval)

		model26.fill(COLOR.LIGHT_GREEN)
		model20.fill(COLOR.BLUE)
		time.sleep(interval)

		model26.fill(COLOR.TURQUOISE)
		model20.fill(COLOR.RED)
		time.sleep(interval)

		index += 1


# 双随机面闪烁
def double_flash_surface():
	model26.fill(COLOR.GREEN)
	model20.fill(COLOR.GREEN)

	thread20 = threading.Thread(target=model20.flash_surface,args=(COLOR.RED, COLOR.GREEN, 10, 0.5))
	thread20.start()
	thread26 = threading.Thread(target=model26.flash_surface,args=(COLOR.RED, COLOR.GREEN, 10, 0.5))
	thread26.start()

	thread20.join()
	thread26.join()


# 双流动点亮
def double_flow():
	model26.fill(COLOR.BLACK)
	model20.fill(COLOR.BLACK)

	thread20 = threading.Thread(target=model20.flow,args=(0, 6, 0.01))
	thread20.start()
	thread26 = threading.Thread(target=model26.flow,args=(0, 6, 0.05))
	thread26.start()

	thread20.join()
	thread26.join()


# 双平行滚动
def double_pentagon_octagon():
	model26.fill(COLOR.GREEN)
	model20.fill(COLOR.GREEN)

	thread1 = threading.Thread(target=model20.light_pentagon_lines, args=(COLOR.RED, COLOR.GREEN, 1))
	thread1.start()
	thread2 = threading.Thread(target=model26.light_octagon_lines, args=(COLOR.RED, COLOR.GREEN, 1))
	thread2.start()

	thread1.join()
	thread2.join()


# if __name__ == '__main__':
# 	while True:
# 		alternate_flash(3, 1.5)
# 		double_flash_surface()
# 		double_flow()
# 		double_pentagon_octagon()

# 		model26.fill(COLOR.GREEN)
# 		model20.fill(COLOR.GREEN)

# 		model26.flash_triangle_square_triangle(COLOR.RED, COLOR.GREEN, 10, 0.5)
# 		model26.light_layer_to_layer(COLOR.RED, COLOR.GREEN, 0, 10, 0.3)
# 		model26.light_layer_to_layer(COLOR.RED, COLOR.GREEN, 1, 10, 0.3)

# 		model26.fill(COLOR.GREEN)

# 		model20.flash_double_surface(COLOR.RED, COLOR.GREEN, 10, 0.5)
# 		model20.flow_lines_by_point(COLOR.RED, COLOR.GREEN, 0.1)
# 		model20.scroll_pentagon_lines(COLOR.GREEN, 0.5)

# 		model26.fill(COLOR.GREEN)
# 		model20.fill(COLOR.GREEN)


if __name__ == '__main__':
	while True:
		alternate_flash(3, 1)
		double_flash_surface()
		double_flow()
		double_pentagon_octagon()

		model20.fill(COLOR.BLACK)
		model26.fill(COLOR.GREEN)
		model26.light_octagon_lines(COLOR.BLUE, COLOR.GREEN, 0.5)
		time.sleep(0.5)

		model26.fill(COLOR.GREEN)
		model26.light_layer_to_layer(COLOR.RED, COLOR.RED, 0, 4, 0.2)
		model26.light_layer_to_layer(COLOR.GREEN, COLOR.GREEN, 1, 4, 0.2)

		model26.light_layer_to_layer(COLOR.RED, COLOR.RED, 2, 4, 0.2)
		model26.light_layer_to_layer(COLOR.GREEN, COLOR.GREEN, 3, 4, 0.2)
		time.sleep(0.5)

		model26.flash_triangle_square_triangle(COLOR.RED, COLOR.GREEN, 10, 0.3)
		time.sleep(0.5)

		model26.fill(COLOR.BLACK)
		model20.fill(COLOR.GREEN)
		time.sleep(0.5)
		model20.flash_double_surface(COLOR.RED, COLOR.GREEN, 10, 0.3)
		time.sleep(0.5)
		model20.flow_lines_by_point(COLOR.RED, COLOR.GREEN, 0.01)
		time.sleep(0.5)
		model20.scroll_pentagon_lines(COLOR.GREEN, 0.3)
		time.sleep(0.5)
		