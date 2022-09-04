# -*- coding=utf-8 -*-
# @Time: 2022/9/3 14:50
# @Author: John
# @File: dec.py
# @Software: PyCharm
import time
def decorate(func):
    def decorated(arg):
        t1=time.time()
        print("hello")
        sum=func(arg)
        print("end")
        t2 = time.time()
        print(f"time consuming{t2-t1}---{sum}")
        return sum
    return decorated

@decorate
def origin(arg):
    print(f"origin func for   {arg}")
    sum=0
    for i in range(100):
        sum += i

    return sum


origin("test")