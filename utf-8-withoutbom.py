# -*- coding=utf-8 -*-
# @Time: 2022/8/21 11:12
# @Author: John
# @File: utf-8-withoutbom.py
# @Software: PyCharm

import codecs


def check_file_charset(file):
    # 检查文件是否包含bom的三个字符codecs.BOM_UTF8
    with open(file, 'rb') as source_file:
        data = source_file.read()
        # print(data[:3])
        if data[:3] == codecs.BOM_UTF8:
            print('******* Have BOM  *******')
            return True
        else:
            print('******* No BOM  *******')
            return False


def change_file_withoutbom(file):
    # 将文件编码转换为UF8-无bom格式
    with open(file, 'rb') as source_file:
        data = source_file.read()
        with open(file_path, 'wb') as f:
            #utf-8-sig会自动忽略
            u = data.decode('utf-8-sig')
            data = u.encode('utf-8')
            f.write(data)
    print(f"{file}编码改成utf-8无BOM")


if __name__ == '__main__':
    file_path="test.json"
    # print(check_file_charset(file_path))
    if check_file_charset(file_path):
        change_file_withoutbom(file_path)

