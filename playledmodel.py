#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import threading
import model26
import model20
from rpi_ws281x import Color
import serial
import threading
import queue
import colors
import thread_close

COLOR = colors.COLOR

# 两个模型交替亮起
def alternate_flash(flash_number, interval):
	index = 0
	while index < flash_number:
		model26.fill(COLOR.RUBY)
		model20.fill(COLOR.INDIGO)
		time.sleep(interval)

		model26.fill(COLOR.JASMINE)
		model20.fill(COLOR.BLUE)
		time.sleep(interval)

		model26.fill(COLOR.INDIGO)
		model20.fill(COLOR.ORANGE)
		time.sleep(interval)

		index += 1

# 同时亮起两个模型
# color1，正20面体颜色
# color2，正26面体颜色
def double_fill(color1, color2):
	model20.fill(color1)
	model26.fill(color2)


# 灯组合效果
def compose():
	alternate_flash(3, 0.5)
	# double_flash_surface()
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

	model26.fill(COLOR.BLACK)
	model20.fill(COLOR.GREEN)
	time.sleep(0.5)
	model20.flash_double_surface(COLOR.RED, COLOR.GREEN, 10, 0.2)
	time.sleep(0.5)
	model20.flow_lines_by_point(COLOR.CARMINE, COLOR.GREEN, 0.01)
	time.sleep(0.5)
	model20.scroll_pentagon_lines(COLOR.GREEN, 0.2)
	time.sleep(0.5)

# 控制立体造型亮灯的线程
thread20 = None
thread26 = None
combination_thread = None

# model20线程任务队列
model20_methods_que = None
# model20线程任务参数队列
model20_args_que = None
# model26线程任务队列
model26_methods_que = None
# model26线程任务参数队列
model26_args_que = None

def push_model20_work(method, args):
	model20_methods_que.put(method)
	model20_args_que.put(args)

def push_model26_work(method, args):
	model26_methods_que.put(method)
	model26_args_que.put(args)

# model20线程
class Model20Thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global model20_methods_que
        global model20_args_que
        print('MODEL20线程运行开始')

        while True:
            method = model20_methods_que.get()
       	    args = model20_args_que.get()
            method(*args)
            model20_methods_que.task_done()

        print('MODEL20线程运行结束')


# model26线程
class Model26Thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global model26_methods_que
        global model26_args_que
        print('MODEL26线程运行开始')

        while True:
            method = model26_methods_que.get()
       	    args = model26_args_que.get()
            method(*args)
            model26_methods_que.task_done()

        print('MODEL26线程运行结束')


# 组合效果线程
class CombinationThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global model20_methods_que
        global model26_methods_que
        global model20_args_que
        global model26_args_que
        print('组合效果线程运行')
        while True:
            model20_methods_que.join()
            model26_methods_que.join()
            push_model20_work(alternate_flash, (3, 0.5))

            model20_methods_que.join()
            model26_methods_que.join()
            push_model20_work(double_fill, (COLOR.GREEN, COLOR.GREEN))

            model20_methods_que.join()
            model26_methods_que.join()
            time.sleep(0.5)
            push_model20_work(model20.flash_surface, (COLOR.RED, COLOR.GREEN, 10, 0.05))
            push_model26_work(model26.flash_surface, (COLOR.RED, COLOR.GREEN, 10, 0.05))

            model20_methods_que.join()
            model26_methods_que.join()
            push_model20_work(double_fill, (COLOR.GREEN, COLOR.GREEN))

            model20_methods_que.join()
            model26_methods_que.join()
            time.sleep(0.5)
            push_model20_work(model20.flow, (0, 4, 10, COLOR.RED, COLOR.GREEN, 16, 0.01))
            push_model26_work(model26.flow, (0, 4, 10, COLOR.RED, COLOR.GREEN, 16, 0.01))

            model20_methods_que.join()
            model26_methods_que.join()
            time.sleep(0.5)
            push_model20_work(model20.light_pentagon_lines, (COLOR.RED, COLOR.GREEN, 1))
            push_model26_work(model26.light_octagon_lines, (COLOR.RED, COLOR.GREEN, 1))

            model20_methods_que.join()
            model26_methods_que.join()
            push_model20_work(double_fill, (COLOR.GREEN, COLOR.GREEN))

            model20_methods_que.join()
            model26_methods_que.join()
            time.sleep(0.5)
            push_model26_work(model26.light_octagon_lines, (COLOR.BLUE, COLOR.GREEN, 0.5))
            push_model26_work(model26.fill, (COLOR.GREEN,))
            push_model26_work(model26.light_layer_to_layer, (COLOR.RED, COLOR.RED, 0, 4, 0.2))
            push_model26_work(model26.light_layer_to_layer, (COLOR.GREEN, COLOR.GREEN, 1, 4, 0.2))
            push_model26_work(model26.light_layer_to_layer, (COLOR.RED, COLOR.RED, 2, 4, 0.2))
            push_model26_work(model26.light_layer_to_layer, (COLOR.GREEN, COLOR.GREEN, 3, 4, 0.2))

            model20_methods_que.join()
            model26_methods_que.join()
            push_model20_work(double_fill, (COLOR.GREEN, COLOR.BLACK))

            model20_methods_que.join()
            model26_methods_que.join()
            time.sleep(0.5)
            push_model20_work(model20.flash_double_surface, (COLOR.RED, COLOR.GREEN, 10, 0.2))
            push_model20_work(model20.flow_lines_by_point, (COLOR.CARMINE, COLOR.GREEN, 0.01))
            push_model20_work(model20.scroll_pentagon_lines, (COLOR.GREEN, 0.2))


def start_carousel():
    global model20_methods_que
    global model20_args_que
    global model26_methods_que
    global model26_args_que
    global thread20
    global thread26
    global combination_thread
    # model20线程任务队列
    model20_methods_que = queue.Queue()
    # model20线程任务参数队列
    model20_args_que = queue.Queue()
    # model26线程任务队列
    model26_methods_que = queue.Queue()
    # model26线程任务参数队列
    model26_args_que = queue.Queue()

    if (combination_thread is None) or (not combination_thread.is_alive()):
        combination_thread = CombinationThread("轮播效果线程")
        combination_thread.start()

    if (thread20 is None) or (not thread20.is_alive()):
        thread20 = Model20Thread("Model20效果线程")
        thread20.start()

    if (thread26 is None) or (not thread26.is_alive()):
        thread26 = Model26Thread("Model26果线程")
        thread26.start()


def stop_carousel():
    global model20_methods_que
    global model20_args_que
    global model26_methods_que
    global model26_args_que
    global thread20
    global thread26
    global combination_thread
    # model20线程任务队列
    model20_methods_que = None
    # model20线程任务参数队列
    model20_args_que = None
    # model26线程任务队列
    model26_methods_que = None
    # model26线程任务参数队列
    model26_args_que = None

    thread_close.stop_thread(thread20)
    thread20 = None

    thread_close.stop_thread(thread26)
    thread26 = None

    thread_close.stop_thread(combination_thread)
    combination_thread = None  


# 接收超声波串口数据线程
class SonarThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.sonar_led_thread = None
    def run(self):
        print('接收超声波串口数据线程运行')
        ser = None
        state = None
        usb_port = '/dev/ttyUSB0'
        while True:
            try:
                if ser is None:
                    ser = serial.Serial(usb_port, 9600, timeout=0.5)
                if not ser.isOpen():
                    ser.open()

                state = ser.readline()
                # print('超声波状态数据', state, time.time())
                if state == b'':
                    # print('没有超声波数据')
                    state = None
                else:
                    state = int(state)
            except:
                print('超声波串口连接失败')
                if usb_port == '/dev/ttyUSB0':
                    usb_port = '/dev/ttyUSB1'
                else:
                    usb_port = '/dev/ttyUSB0'
                ser = None
                state = None

            if state == None:
                continue

            if state == 1:
                if (self.sonar_led_thread is None) or (not self.sonar_led_thread.is_alive()):
                    stop_carousel() 

                    self.sonar_led_thread = SonarLedThread("超声波亮灯线程", 1)
                    self.sonar_led_thread.start()
            elif state == 2:
                if (self.sonar_led_thread is None) or (not self.sonar_led_thread.is_alive()):
                    stop_carousel() 

                    self.sonar_led_thread = SonarLedThread("超声波亮灯线程", 2)
                    self.sonar_led_thread.start()
            state = None
            

# 超声波亮灯线程
class SonarLedThread(threading.Thread):
    def __init__(self, name, sonar):
        threading.Thread.__init__(self)
        self.name = name
        self.sonar = sonar
    def run(self):
        if self.sonar == 1:
            double_fill(COLOR.BLACK, COLOR.BLACK)
            time.sleep(0.5)
            model26.flow(17, 4, 15, COLOR.RUBY, COLOR.BLACK, 16, 0.01)
        elif self.sonar == 2:
            double_fill(COLOR.BLACK, COLOR.BLACK)
            time.sleep(0.5)
            model26.light_layer_to_layer(COLOR.RED, COLOR.RED, 5, 4, 0.2)
            model26.light_layer_to_layer(COLOR.BLACK, COLOR.BLACK, 4, 4, 0.2)
        start_carousel()
        

if __name__ == '__main__':
    while True:
        start_carousel()

        sonar_thread = SonarThread("接收超声波串口数据线程")
        sonar_thread.start()
        sonar_thread.join()


	