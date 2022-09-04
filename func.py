# -*- coding=utf-8 -*-
# @Time: 2022/9/4 12:23
# @Author: John
# @File: func.py
# @Software: PyCharm
a=1
def make_avenger():
    series=[]
    def avenger(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)
    return avenger

def make_avenger2():
    count=0
    total=0
    dict2={}
    def avenger(new_value):
        global a
        nonlocal count,total
        dict2["count"]=total
        a +=1
        count += 1
        total+=new_value
        return total/count
    return avenger

class test:
    def test(self):
        print("tets")

if __name__ == '__main__':

    avg=make_avenger2()
    # avg=test()

    print(avg(10))
    print(avg.__closure__[0].cell_contents)
    print(avg(11))
    print(avg.__closure__[0].cell_contents)
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__[0].cell_contents)