#!/usr/bin/python
# -*- coding: UTF-8 -*-

import librosa
import numpy as np
from time import sleep
import threading
from pygame import mixer 
import board
import neopixel

# def playmp3():
# 	mixer.init()
# 	mixer.music.load('./demo.wav')
# 	mixer.music.play()

# playThread = threading.Thread(target=playmp3)
# playThread.start()


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



offset = 10
# 节拍时间点
beat_times = []
# 节拍点的八音12度最强度的索引
beat_chroma_max_index = []

def setupBeatChroma():
	global beat_times
	global beat_chroma_max_index
	y, sr = librosa.load("./demo.wav", offset=offset, duration=10.0)
	
	# # 八音12度的强度
	# chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
	# 节拍点（帧索引）
	tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
	# 节拍点 （时间点，单位秒）
	beat_times = librosa.frames_to_time(beats, sr=sr)

	# for beat in beats:
	# 	max_chroma = 0
	# 	max_chroma_index = 0
	# 	chr_st_index = 0
	# 	for chr_st in chroma_stft:
	# 		if chr_st[beat] > max_chroma:
	# 			max_chroma = chr_st[beat]
	# 			max_chroma_index = chr_st_index
	# 		chr_st_index += 1

	# 	beat_chroma_max_index.append(max_chroma_index)


setupBeatChroma()

pre_beat_time = 0
index = 0
for beat_time in beat_times:
	pixels.fill(COLOR.BLACK)
	pixels.show()
	sleep(beat_time - pre_beat_time)

	print(beat_time)
	pixels.fill(COLOR.RED)
	pixels.show()

	pre_beat_time = beat_time
	index += 1
