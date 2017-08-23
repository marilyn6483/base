# -*- coding: utf-8 -*-
import functools

''' functools模块用法示例'''

def decorator1(func):
    def wrapper(*args, **kwargs):
        print "call {}".format(func.__name__)
        res = func(*args, **kwargs)
        return res
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print "call {}".format(func.__name__)
        res = func(*args, **kwargs)
    return functools.update_wrapper(wrapper, func)

@decorator1
def foo1():
    return "foo1"

@decorator2
def foo2():
    return "foo2"
foo1()
print foo1.__name__

foo2()
print foo2.__name__