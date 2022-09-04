# -*- coding=utf-8 -*-
# @Time: 2022/9/3 19:04
# @Author: John
# @File: gen.py
# @Software: PyCharm
# def gen_func():
#     html=yield "hello"
#     print(html)
#     yield 1
#     yield 2
#     print(html)
#     yield 3
#
# if __name__ == '__main__':
#     gen=gen_func()
#     html="888"
#
#     next(gen)
#     gen.send(html)
#     next(gen)
#     next(gen)

final_result={}

def sales_num(pro_name):
    #生成器
    total =0
    nums=[]
    while True:
        x=yield
        print(pro_name+"销量",x)
        if not x:
            break
        total += x
        print("nums ",nums)
        print("x ",x)
        nums.append(x)
    return total,nums


def middle(key):
    while True:
        final_result[key] = yield from sales_num(key)
        print("final_result",type(final_result[key]))
        print("final_result",final_result[key])
        print(key+"销量统计完成")


def main():
    data_sets={
        "john面膜":[100,200,300],
        "john手机":[10,20,30]
    }
    for key,data_set in data_sets.items():
        print("start key ",key)
        print("start data_set ",data_set)
        m=middle(key)
        m.send(None)
        for value in data_set:
            m.send(value)
            print(m)
        m.send(None)
    print("final result:",final_result)

if __name__ == '__main__':
    main()
