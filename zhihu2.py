# -*- coding: utf-8 -*-
import threading
from time import sleep
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class A(Singleton):
    def __init__(self, name, male):
        self.name = name
        self.male = male

obj1 = A('ben', 'boy')
sleep(1)
obj2 = A('min', 'girl')
sleep(1)
obj3 = A('miao', 'boy')

print(id(obj1), id(obj2), id(obj3))
