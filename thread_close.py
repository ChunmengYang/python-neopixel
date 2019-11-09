#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:thread_close.py
import inspect
import ctypes

# 线程操作方法开始
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    # tid = ctypes.c_ulong(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    if not (thread is None) and thread.is_alive():
        print('停止的线程为 ##########%s##########' % thread.name)
        _async_raise(thread.ident, SystemExit)