#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pygame import mixer 
import threading
from time import sleep

def playmp3():
	mixer.init()
	mixer.music.load('./demo.wav')
	mixer.music.play()

playThread = threading.Thread(target=playmp3)
playThread.start()

while True:
	sleep(10)