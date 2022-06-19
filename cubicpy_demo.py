# name: cubicpy_demo.py, version: 0.1.0, author: paoyung.chang@gmail.com
# Released under the MIT License (MIT). See LICENSE link:
# https://gist.github.com/paoyung/7e465ad984a6cf24024508831ec54516
# Copyright (c) 2022 Paoyung Chang

from framebuf import FrameBuffer, MONO_VLSB
from my_font import words
# from my_font16 import words as words16
from my_util import get_display   #自訂的 ssd1306 設定 function

def write_font(display, wordsBuf, x, y, invert=False):
    for buf in wordsBuf:
        if invert: # 反白
            buf = [b^0xff for b in buf]
        width = len(buf) // 2 #判斷字寬
        fbuf = FrameBuffer(bytearray(buf), width, 16, MONO_VLSB)
        display.blit(fbuf, x, y, 0)
        x += width
        if x > 128:
            break

# 把 wordsBuf 轉好才送入 write_font 才可以換不同字體
def wb(sentense):
    return [words[each] for each in sentense]

#def wb16(sentense):
#    return [words16[each] for each in sentense]

def demo():
    # 啟用 SSD1306
    disp = get_display()
    disp.invert(0)
    disp.rotate(True)
    # 顯示
    write_font(disp, wb('Hello，大家好。'), 0, 0)
    write_font(disp, wb('向各位介紹免費、開源'), 0, 13)
    write_font(disp, wb('可商用自由改造及衍生'), 0, 25)
    write_font(disp, wb('的中文點陣字體 --'), 0, 37)
    write_font(disp, wb('『俐方體11號』'), 20, 51)
    disp.show()
