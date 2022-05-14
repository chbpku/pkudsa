from microbit import *
import neopixel
import superbit
import speech
import os
import random
import math
import music
'''
sun yellow AB同时按下——晒太阳
sport green pin1——计步器
mood Blue pin2——小游戏
完成相应任务获取经验，进行升级，获取新技能

part1晒太阳，将microbit置于强光下一段时间即可，按A显示当前照光秒数，按B结束并获取相应经验和sun值

part2计步器，摇晃计步，按A显示当前步数，按B结束并获取相应经验和sport值

part3寻宝游戏，A键左右移动，B键上下移动，同时按下AB选中，
若不是目标块，则会显示距离目标块的曼哈顿距离，并可进行下一次尝试，
一共有五次机会，胜利即可获得心情值和经验

长按A查看经验值和等级'''
grade=1
exp=0
skill=[]
sun=1000
sport=1000
learn=1000
mood=1000
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
i = 0
time=0
stime=0
color=[]

while True:

    sun-=random.randrange(0,10)
    sport-=random.randrange(0,10)
    mood-=random.randrange(0,10)
    sleep(1000)
    if running_time()>=1800000:
        speech.say("I am sleepy")
    if sun<=100:
        color.append(Yellow)
    if sun>100 and Yellow in color:
        color.remove(Yellow)
    if sport<=100:
        color.append(Green)
    if sport>100 and Green in color:
        color.remove(Green)
    if mood<=100:
        color.append(Blue)
    if mood>100 and Blue in color:
        color.remove(Blue)

    if pin1.is_touched():
        display.scroll("sport")
        bu=0
        x2 = accelerometer.get_x()
        np.clear()
        while True:

            x1 = accelerometer.get_x()
            if math.fabs(x1 - x2) > 150:
                bu += 1
            x2 = x1
            sleep(550)
            if button_a.get_presses():
                display.scroll(bu)
            if button_b.get_presses():
                sport+=bu*0.2
                if bu>=10:
                    exp+=random.randrange(bu//10,bu//5)
                display.scroll('sport')
                display.scroll(sport)
                sleep(1000)
                display.scroll('exp')
                display.scroll(exp)
                break
    if pin2.is_touched():
        display.scroll("mood")
        np.clear()
        x=random.randrange(0,5)
        y=random.randrange(0,5)
        x1=0
        y1=0
        t=0
        while True:
            if button_a.get_presses():
                display.set_pixel(x1,y1,0)
                x1+=1
                x1=x1%5

            if button_b.get_presses():
                display.set_pixel(x1,y1,0)
                y1+=1
                y1=y1%5
            display.set_pixel(x1,y1,5)

            if pin_logo.is_touched():
                t+=1
                display.set_pixel(x1,y1,9)
                a=math.fabs(x1 - x)+math.fabs(y1 - y)
                x1=0
                y1=0
                if int(a)==0:
                    display.scroll("Perfect")
                    music.play(music.JUMP_UP)
                    mood+=600
                    exp+=30
                    display.scroll('mood')
                    display.scroll(600)
                    sleep(1000)
                    display.scroll('exp')
                    display.scroll(30)
                    break
                else:
                    display.show(Image.SAD)
                    sleep(500)

                    display.scroll(a)
                    display.clear()
            if t>=5:
                display.scroll("Game Over")
                music.play(music.WAWAWAWAA)
                break

    if button_a.get_presses() and button_b.get_presses():
        display.scroll("sunbathe")

        np.clear()
        while True:
            if int(display.read_light_level())>=50:
                stime+=1
                sleep(1)
            if button_a.get_presses():
                display.scroll(str(stime//1000))
            if button_b.get_presses():
                sun+=stime//1000
                exp+=random.randrange(stime//3000,stime//1000)
                display.scroll('sun')
                display.scroll(sun)
                sleep(1000)
                display.scroll('exp')
                display.scroll(exp)
                stime=0
                break

    if exp>=50:
        grade+=1
        exp-=50
        music.play(music.ENTERTAINER)
        sleep(1000)
    if grade==20:
        skill.append("DUCK HURRICANE")
    if grade==30:
        skill.append("ICE ZERO")



    with open("my.txt",'w') as a:
        a.write("exp")
        a.write(str(exp))
        a.write("grade")
        a.write(str(grade))
    with open("my.txt",'r') as a:
        q=a.readline()
    if button_a.is_pressed():
        display.scroll(q)
    if color:
        np.clear()
        np[0] = color[i]
        np[1] = color[i]
        np[2] = color[i]
        np[3] = color[i]
        np.show()
        sleep(1000)
        i = (i+1)
        if i>len(color)-1:
            i=0
# 在这里写上你的代码 :-)
