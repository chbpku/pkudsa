# Imports go at the top
from microbit import *
import random
import music

# Code in a 'while True:' loop repeats forever
def show_score(score):#分数展示模块
    display.clear()#清屏
    x=score#分数
    i=0#用于计数的模块
    while x!=0:#当有x可以二分的时候，采用二进制的显示法
        t=x%2#取余
        if t==1:#如果有余，对应的位置亮灯
            display.set_pixel(i%5,i//5,9)
        x=x//2#整除
        i=i+1
    return i

def random_show_key(i):#展示和按键模块
    Flag=True#表示有没有按错键
    k=random.randint(0,1)#随机模块，决定左右呈现
    if k==0:#左呈现
        t=random.randint(0,1)#随机择数，不同呈现
        if t==0:
            display.set_pixel(0,3,9)#呈现按键提示
            display.set_pixel(1,3,9)
            time=0
            while True and time <1000/i+100:#计时和按键
                Flag=False#如果超过按键时间，则表示错误
                time+=1#循环计时模块
                sleep(1)#延迟表示时间
                if button_a.is_pressed():#如果按右键
                    display.clear()
                    music.pitch(262)#放音乐
                    sleep(100)
                    music.stop()
                    Flag=True
                    break
                elif button_b.is_pressed():#错误按键
                    display.clear()
                    break
            return Flag
        if t==1:
            display.set_pixel(0,3,9)
            display.set_pixel(1,3,9)
            display.set_pixel(0,4,9)
            display.set_pixel(1,4,9)
            time=0
            while True and time <2000/i+100:
                Flag=False
                time+=1
                sleep(1)
                if button_a.is_pressed():
                    display.clear()
                    music.pitch(330)
                    sleep(100)
                    music.stop()
                    Flag=True
                    break
                elif button_b.is_pressed():
                    display.clear()
                    break
            return Flag
    if k==1:
        t=random.randint(0,1)
        if t==0:
            display.set_pixel(3,3,9)
            display.set_pixel(4,3,9)
            time=0
            while True and time <1000/i+100:
                Flag=False
                time+=1
                sleep(1)
                if button_b.is_pressed():
                    display.clear()
                    music.pitch(294)
                    sleep(100)
                    music.stop()
                    Flag=True
                    break
                elif button_a.is_pressed():
                    display.clear()
                    break
            return Flag
        if t==1:
            display.set_pixel(3,3,9)
            display.set_pixel(4,3,9)
            display.set_pixel(3,4,9)
            display.set_pixel(4,4,9)
            time=0
            while True and time <2000/i+100:
                Flag=False
                time+=1
                sleep(1)
                if button_b.is_pressed():
                    display.clear()
                    music.pitch(349)
                    sleep(100)
                    music.stop()
                    Flag=True
                    break
                elif button_a.is_pressed():
                    display.clear()
                    break
            return Flag
    
score=0
i=0
contin=True
while score<100 and contin:#判断循环是否继续
    contin=random_show_key(i+1)
    score=score+1
    i=show_score(score)
if contin:
    display.show('You Win!')
else:
    display.show('You Failed!')
display.clear()

