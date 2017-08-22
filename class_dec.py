# -*- coding: utf-8 -*-

'''
class decorator:
    def __init__(self, func):
        self.func = func
		
    def __call__(self, *args):
        print "in call"
        self.func(*args) #调用被装饰的函数，当类的实例被调用时
@decorator
def fun(*args):
    print args

fun(1, 2, 3)
#每个装饰器都会产生一个实例来保持状态
#重写__call__方法，当实例被调用时，可以选择是否运行被装饰的func函数

类装饰器创建并返回类的一个新实例

def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper
    
@decorator
class C:
    def __init__(self, x, y):
        self.attr = "spam"
        
c = C(1, 2)
print c.attr

#C = Wrapper = decorator(C)

#多个装饰器
def f1(fn):
    def wrap1(*args):
        print "in wrap1"
        fn(*args) #要在包装器函数内运行被包装的函数，实现功能·
    return wrap1
        
def f2(fn):
    def wrap2(*args):
        print "in wrap2"
        fn(*args)
    return wrap2

@f1
@f2
def f0(*args):
    print "in original"
    print args

args = (1,2,3,4,5)
f0(1,2,3)
'''      
        
#编写一个追踪器实例

class tracer:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    def __call__(self, *args, **kwargs):
        self.calls += 1
        self.func(*args, **kwargs)
        print "{} called {}".format(self.func.__name__, self.calls)
        print "call func finished."

@tracer
def spam(*args, **kwargs):
    print args
    print kwargs
kwargs = {"k1": "foo", "k2": "bar"}
#spam(*(1,2,3))
#spam('a', 'b', 'c')
spam(**kwargs) #**在调用函数的时候是序列解包，解包成一个字典
spam(k1="foo", k2="bar") #**kwargs接受可变个关键字参数，并将它们打包成dict

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
