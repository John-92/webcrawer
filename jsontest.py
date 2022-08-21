# -*- coding=utf-8 -*-
# @Time: 2022/8/21 13:10
# @Author: John
# @File: jsontest.py
# @Software: PyCharm
import json
import csv
with open('test.json') as json_file:
    jsondata = json.load(json_file)
data_file = open('test.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0
for data in jsondata:
    #将标签头写到第一行中，
    if count == 0:
        header = []
        #Python3中keys和values()返回的是可迭代对象，需要转换为list
        keys = list(data.keys())
        values = list(data.values())
        header.append(keys[0])
        header.extend(dict(values[1][0]).keys())
        csv_writer.writerow(header)
        count += 1
    values = list(data.values())
    for data in values[1]:
        v = []
        v.append(values[0])
        v.extend(dict(data).values())
        print(data)
        csv_writer.writerow(v)



data_file.close()