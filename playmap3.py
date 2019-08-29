#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pygame import mixer 

def playmp3():
	mixer.init()
	mixer.music.load('./demo.wav')
	mixer.music.play()

playmp3()