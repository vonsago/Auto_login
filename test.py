#!/usr/bin/env python
# coding=utf-8
'''
> File Name: test.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  5/31 17:17:56 2018
'''
import requests
import pytesseract
from PIL import Image

rep = {'O': '0',
       'I': '1', 'L': '1',
       'Z': '2',
       'S': '8'
       }


def denoising(im):
    pixdata = im.load()
    w, h = im.size
    for j in range(1, h - 1):
        for i in range(1, w - 1):
            count = 0
            if pixdata[i, j - 1][0] > 245:
                count = count + 1
            if pixdata[i, j + 1][0] > 245:
                count = count + 1
            if pixdata[i + 1, j][0] > 245:
                count = count + 1
            if pixdata[i - 1, j][0] > 245:
                count = count + 1
            if count > 2:
                pixdata[i, j] = 255
    return im

def binarizing(im, threshold):
    im = denoising(im)
    pixdata = im.load()
    w, h = im.size
    for j in range(h):
        for i in range(w):
            if pixdata[i, j][0] < threshold or pixdata[i, j][0] > 190:
                pixdata[i, j] = 0
            else:
                pixdata[i, j] = 255
    im.show()
    return im

def get_bin_table(threshold = 230):
	# 获取灰度转二值的映射table
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table


def test_image(im_name='checkcode.png'):
    image = Image.open(im_name)
    print(pytesseract.image_to_string(image))
    imgry = image.convert('L')  # 转化为灰度图
    table = get_bin_table()
    out = imgry.point(table, '1')
    #out.show()
    code = pytesseract.image_to_string(out)
    print('code---')
    print(code)
    print('---code')


if __name__ == '__main__':
    test_image()
