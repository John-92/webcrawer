# -*- coding=utf-8 -*-
# @Time: 2022/8/14 16:23
# @Author: John
# @File: NetEase.py
# @Software: PyCharm
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json


url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
data={
"csrf_token": "",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo": "1",
"pageSize": "20",
"rid": "R_SO_4_28996919",
"threadId": "R_SO_4_28996919"
}
e='010001'
g='0CoJUm6Qyw8W8jud'
f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
i="W83hy0RjLVZNQkc5"

'''
function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)//循环a+1次
            e = Math.random() * b.length,//随机数
            e = Math.floor(e),//向下取整
            c += b.charAt(e);//从b中取某个序号的字符
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,  //iv为AES中的偏移量
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
   //d(d, e, f, g) 中e,f,g均为固定值,i=a(16)虽然为随机值，但是可以采取固定值来固定，因此encSecKey是一个固定值
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }

    window.asrsea = d,
    }
'''

def get_encSecKey():
    return "2033891d563fae234dfcab09d9ef0a910bfae7a946959ccac3ebcd36283e9b3176db830c885697d0672d97a7815b5a36b21290a8e15774513d1a5dcd0482464f971cd3bbf3ab1fb7a76bb22e86e147e90cea599227472d9fff9b949b0a32e5123ea3155febefc9cc065ce62e80e0d69055c368a2edda81b0e0c1ab0d1f791ed0"

#return h.encText = b(d, g),h.encText = b(h.encText, i), h.encSecKey = c(i, e, f), h
#根据js代码解析的Python代码
def get_params(data):
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second

"""
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
"""

def to_16(data):
    pad=16-len(data)%16
    data += chr(pad) * pad
    return data



def enc_params(data,key):
    iv="0102030405060708"
    data = to_16(data)
    aes=AES.new(key=key.encode("utf-8"),iv=iv.encode("utf-8"),mode=AES.MODE_CBC)

    bs=aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs),"utf-8")

resp = requests.post(url, data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})

print(resp.text)