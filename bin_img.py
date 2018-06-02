#!/usr/bin/env python
# coding=utf-8
'''
> File Name: bin_img.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  5/31 19:51:51 2018
'''
import numpy as np
from PIL import Image
import scipy.signal as signal
import cv2


def bin_img():
    im = Image.open('test.png')  # 读入图片并建立Image对象im
    data = []  # 存储图像中所有像素值的list(二维)
    width, height = im.size  # 将图片尺寸记录下来

    # 读取图像像素的值
    for h in range(height):  # 对每个行号h
        row = []  # 记录每一行像素
        for w in range(width):  # 对每行的每个像素列位置w
            try:
                value = im.getpixel((w, h))  # 用getpixel读取这一点像素
                row.append(value)  # 把它加到这一行的list中去
            except:
                pass
        data.append(row)  # 把记录好的每一行加到data的子list中去，就建立了模拟的二维list
    data = signal.medfilt(data, kernel_size=3)  # 二维中值滤波
    data = np.int32(data)  # 转换为int类型，以使用快速二维滤波
    # 创建并保存结果
    for h in range(height):  # 对每一行
        for w in range(width):  # 对该行的每一个列号
            im.putpixel((w, h), tuple(data[h][w]))  # 将data中该位置的值存进图像,要求参数为tuple
    im.save('result.png')  # 存储

if __name__ == '__main__':
    bin_img()
