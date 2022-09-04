# -*- coding=utf-8 -*-
# @Time: 2022/8/27 16:01
# @Author: John
# @File: csv_to_json.py
# @Software: PyCharm

import csv
import json
filename="test.csv"
#对csv文件内的内容全部打印出来
with open(filename) as f:
    pipeline={}

    node = []
    for row in csv.DictReader(f, skipinitialspace=True):
        #1、较好的方式，if 多个条件，一旦前面一个条件不成立，后面的条件直接不会执行
        if len(pipeline)!=0 and row["pipename"] != node[len(node)-1]["pipeline"]:
            json_data = json.dumps(pipeline)
            with open('res.json', 'w') as f_six:
                f_six.write(json_data)
            pipeline = {}
            node = []
            #下一行循环
            continue
        subnode = {}
        if len(pipeline)==0:
            pipeline["diagram"]=row["diagram"]
        subnode["jenkinsNodeName"] = row["jenkinsNodeName"]
        subnode["scriptPath"] = row["scriptPath"]
        subnode["pipeline"] = row["pipename"]
        subnode["actNodeId"] = row["actNodeId"]
        subnode["actNodeName"] = row["actNodeName"]
        node.append(subnode)
        pipeline["node"] = node
        print(len(node))
        #不好的方式
        # if row["pipename"] == node[0]["pipeline"]:
        #     pass
        #     subnode["jenkinsNodeName"] = row["jenkinsNodeName"]
        #     subnode["scriptPath"] = row["scriptPath"]
        #     subnode["pipeline"] = row["pipename"]
        #     node.append(subnode)
        #     # pipeline["node"] = node
        #     pipeline["node"] = node
        # else:
        #     break
        # print(pipeline)
