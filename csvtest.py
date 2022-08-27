# -*- coding=utf-8 -*-
# @Time: 2022/8/23 20:50
# @Author: John
# @File: csvtest.py
# @Software: PyCharm
import codecs
import csv

# csv_list=[]
# with open('test1.csv') as f:
#     for row in csv.DictReader(f, skipinitialspace=True):
#         next(row)
#         if row["process-id"]=='aaaa-test':
#             csv_list.append(row)
# print(len(csv_list))
# print(csv_list)


with open('test1.csv') as f:
    reader = csv.reader(f)
    print(type(reader))
    row1 = next(reader)


    # print(next(row1))

