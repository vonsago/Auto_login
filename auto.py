#!/usr/bin/env python
# coding=utf-8
'''
> File Name: auto.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 二  5/29 10:35:00 2018
'''

import requests
import pytesseract
from PIL import Image


URL = 'https://member.etest.net.cn/login/loginSuccess'
URL_CODE = 'https://member.etest.net.cn/login/createCode'
DATA = {}

def process_image(image):
    Lim = image.convert('L')
    threshold = 80
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    Bim = Lim.convert()
    Bim.save('fun_binary.png')
    image = Image.open('fun_binary.png')
    return image
def autologin():
    session = requests.Session()
    r = session.get(URL_CODE)
    with open('checkcode.png', 'wb') as f:
        f.write(r.content)
        f.close()
    image = Image.open('checkcode.png')
    image = process_image(image)
    code = pytesseract.image_to_string(image)
    print('code:---------')
    print(code)
    DATA['loginName']='811194414@qq.com'
    DATA['loginPwd']='842631795F'
    DATA['verificationCode']=code
    res = session.post(URL,data=DATA)
    print(res.status_code)
    print('=====-------======')
    print(res.content)

if __name__ == '__main__':
    autologin()
