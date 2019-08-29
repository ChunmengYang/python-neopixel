#!/usr/bin/python
# -*- coding: UTF-8 -*-

import librosa
import numpy as np
from time import sleep
import threading
from pygame import mixer 
# import board
# import neopixel

# LED_PIN = board.D18
# LED_COUNT = 165
# LED_BRIGHTNESS = 0.2
# LED_ORDER = neopixel.GRB

# class COLOR:
# 	BLACK = (0, 0, 0)
# 	GREEN = (0, 255, 0)
# 	RED = (255, 0, 0)
# 	BLUE = (0, 0, 255)

# def getColor(max, num):
# 	return (255*num/max, 0, 0)

# pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False,
# pixel_order=LED_ORDER)

def playmp3():
	mixer.init()
	mixer.music.load('./demo.wav')
	mixer.music.play()

playThread = threading.Thread(target=playmp3)


y, sr = librosa.load("./demo.wav", sr=None)
duration = librosa.get_duration(y=y, sr=sr)

# 音频时长，单位秒
print(duration)
# 音频采样率
print(sr)
S = np.abs(librosa.stft(y))
# 频率、振幅强度，横坐标是采样点，纵坐标是帧
pitches, magnitudes = librosa.piptrack(S=S, sr=sr)
# 八音12度的强度
chroma_stft = librosa.feature.chroma_stft(S=S, sr=sr)

def detect_pitch(t):
  index = magnitudes[:, t].argmax()
  pitch = pitches[index, t]
  return pitch


# 起点强度（音符按键起始点）
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
# 节拍点（帧索引）
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
# 节拍点 （时间点，单位秒）
beat_times = librosa.frames_to_time(beats, sr=sr)
# 节拍点的音高
beat_pitches = []
# 节拍点的八音12度的强度
beat_chroma = []
# 节拍点的八音12度最强度的索引
beat_chroma_max_index = []

for beat in beats:
	beat_pitches.append(detect_pitch(beat))

	chromas = []
	max_chroma = 0
	max_chroma_index = 0
	chr_st_index = 0
	for chr_st in chroma_stft:
		chromas.append(chr_st[beat])

		if chr_st[beat] > max_chroma:
			max_chroma = chr_st[beat]
			max_chroma_index = chr_st_index
		chr_st_index += 1

	beat_chroma.append(chromas)

	beat_chroma_max_index.append(max_chroma_index)


# playThread.start()
pre_beat_time = 0
index = 0
for beat_time in beat_times:
	sleep(beat_time - pre_beat_time)

	# pixels.fill(getColor(12, beat_chroma_max_index[index]))
	# pixels.show()
	sts = "";
	for st in beat_chroma[index]:
		sts += '%f ,' %st 
	print(sts)

	pre_beat_time = beat_time
	index += 1
