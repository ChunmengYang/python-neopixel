#!/usr/bin/python
# -*- coding: UTF-8 -*-

import librosa
import numpy as np
from time import sleep
import threading
from pygame import mixer 
import board
import neopixel

def playmp3():
	mixer.init()
	mixer.music.load('./demo.wav')
	mixer.music.play()

playThread = threading.Thread(target=playmp3)


LED_PIN = board.D21
LED_COUNT = 165
LED_BRIGHTNESS = 0.2
LED_ORDER = neopixel.GRB

class COLOR:
	BLACK = (0, 0, 0)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)

def getColor(max, num):
	return (255 * num / max, 0, 0)

pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False,
pixel_order=LED_ORDER)

def getDuration(filepath):
	y, sr = librosa.load(filepath, sr=None)
	return librosa.get_duration(y=y, sr=sr)


def getSubBeatTimes(filepath, offset, duration):
	y, sr = librosa.load(filepath, offset=offset, duration=duration)
	
	# 节拍点（帧索引）
	tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
	# 节拍点 （时间点，单位秒）
	return librosa.frames_to_time(beats, sr=sr)


# 节拍时间点
beat_times_all = []

def getBeatTimes():
	global beat_times_all

	filepath = "./demo.wav"
	total_duration = getDuration(filepath)
	offset = 0
	duration = 5.0

	while total_duration > 0:
		total_duration -= duration
		if total_duration < duration:
			duration += total_duration
			total_duration = 0
		
		beat_times = getSubBeatTimes(filepath, offset, duration)
		
		if beat_times.size > 0:
			for beat_time in beat_times:
				beat_times_all.append(beat_time + offset)

		offset += duration


getBeatTimes()
playThread.start()
pre_beat_time = 0
index = 0
for beat_time in beat_times_all:
	pixels.fill(COLOR.BLACK)
	pixels.show()
	sleep(beat_time - pre_beat_time)

	print(beat_time)
	pixels.fill(COLOR.RED)
	pixels.show()

	pre_beat_time = beat_time
	index += 1
