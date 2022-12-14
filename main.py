# import codecs
# file_path = 'test.json'
#
# with open(file_path,encoding="utf-8") as source_file:
#     data = source_file.read()
#     if data[:3] == codecs.BOM_UTF8:
#         print('******* Have BOM  *******')
#     else:
#         print('******* No BOM  *******')


#!/usr/bin/env python
#coding:utf-8
import  sys,codecs

def detectUTF8(file_name):
    state = 0
    line_num = 0
    file_obj = open(file_name,encoding="utf-8")
    all_lines = file_obj.readlines()
    file_obj.close()
    for line in all_lines:
        line_num += 1
        line_len = len(line)
        for index in range(line_len):
            if state == 0:
                if ord(line[index])&0x80 == 0x00:#上表中的第一种情况
                    state = 0
                elif ord(line[index])&0xE0 == 0xC0:#上表中的第二种情况
                    state = 1
                elif ord(line[index])&0xF0 == 0xE0:#第三种
                    state = 2
                elif ord(line[index])&0xF8 == 0xF0:#第四种
                    state = 3
                else:
                    print("%s isn't a utf8 file,line:	"%file_name+str(line_num))
                    sys.exit(1)
            else:
                if not ord(line[index])&0xC0 == 0x80:
                    print("%s isn't a utf8 file in line:	"%file_name+str(line_num))
                    sys.exit(1)
                state -= 1
    if existBOM(file_name):
        print("%s isn't a standard utf8 file,include BOM header."%file_name)
        sys.exit(1)

def existBOM(file_name):
    file_obj = open(file_name,'r',encoding="utf-8")
    code = file_obj.read(3)
    file_obj.close()
    if code == codecs.BOM_UTF8:#判断是否包含EF BB BF
        return  True
    return False

if __name__ == "__main__":
    file_name = 'test.json'
    detectUTF8(file_name)