#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
import RPi.GPIO as GPIO

GPIO.cleanup() 
GPIO.setmode(GPIO.BCM)
#12\18\21 0

LED_1_PIN = 21
LED_1_COUNT = 312
LED_1_BRIGHTNESS = 128

LED_2_PIN = 18
LED_2_COUNT = 300
LED_2_BRIGHTNESS = 128

LED_3_PIN = 12
LED_3_COUNT = 300
LED_3_BRIGHTNESS = 128


# GPIO.setup(LED_1_PIN, GPIO.OUT)
# GPIO.setup(LED_2_PIN, GPIO.OUT)
# GPIO.setup(LED_3_PIN, GPIO.OUT)
# pwm = GPIO.PWM(LED_PIN, 50)
# pwm.start(0)

class COLOR:
	BLACK = Color(0, 0, 0)
	GREEN = Color(0, 255, 0)
	RED = Color(255, 0, 0)
	BLUE = Color(0, 0, 255)
	YELLOW = Color(255, 255, 0)
	PURPLE = Color(255, 0, 255)
	TURQUOISE = Color(0, 255, 255)

strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, 800000, 5, False, LED_1_BRIGHTNESS, 0, ws.WS2811_STRIP_GRB)
strip1.begin()

# strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, 800000, 6, False, LED_2_BRIGHTNESS, 0, ws.WS2811_STRIP_GRB)
# strip2.begin()

# strip3 = Adafruit_NeoPixel(LED_3_COUNT, LED_3_PIN, 800000, 7, False, LED_2_BRIGHTNESS, 0, ws.WS2811_STRIP_GRB)
# strip3.begin()


if __name__ == '__main__':
	while True:	
		# flow(0, 40, 0.05)
		# flash(1)
		# scroll(8, 0.5)
		for i in range(strip1.numPixels()):
			if (i % 2) == 0:
				strip1.setPixelColor(i, COLOR.RED)
		strip1.show()

		# for i in range(strip2.numPixels()):
		# 	strip2.setPixelColor(i, COLOR.GREEN)
		# strip2.show()

		# for i in range(strip3.numPixels()):
		# 	strip3.setPixelColor(i, COLOR.BLUE)
		# strip3.show()

		time.sleep(1)

		for i in range(strip1.numPixels()):
			strip1.setPixelColor(i, COLOR.YELLOW)
		strip1.show()

		# for i in range(strip2.numPixels()):
		# 	strip2.setPixelColor(i, COLOR.BLUE)
		# strip2.show()

		# for i in range(strip3.numPixels()):
		# 	strip3.setPixelColor(i, COLOR.RED)
		# strip3.show()

		time.sleep(1)

		for i in range(strip1.numPixels()):
			strip1.setPixelColor(i, COLOR.BLUE)
		strip1.show()

		# for i in range(strip2.numPixels()):
		# 	strip2.setPixelColor(i, COLOR.RED)
		# strip2.show()

		# for i in range(strip3.numPixels()):
		# 	strip3.setPixelColor(i, COLOR.GREEN)
		# strip3.show()

		time.sleep(1)

