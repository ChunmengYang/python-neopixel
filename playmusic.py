#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pygame import mixer 
from time import sleep

def playmusic():
	mixer.init()
	mixer.music.load("./music/1.mp3")
	mixer.music.play()

playmusic()

while True:
	sleep(10)