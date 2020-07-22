# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 03:04:42 2020

@author: aafym
"""


class Father(object):
    def __init__(self, name):
        self.name=name
        print ( "name: %s" %( self.name) )
    def getName(self):
        return 'Father ' + self.name

class Son(Father):
    def getName(self):
        return 'Son '+self.name

if __name__=='__main__':
    son=Son('runoob')
    print ( son.getName() )
    
'''
outcome:
    
name: runoob
Son runoob

如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。
子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。
因为调用了Father的init，所以有了name: runoob
'''