# Imports go at the top
from microbit import *
import music
import time

#original menu
flag = 0
    #0:初始界面
    #1：准备(校准）界面-左右手
    #2：游戏界面
    #6：准备(校准）界面-方向校准


music.play(music.NYAN,wait=False)
display.scroll('Welcome to Music Master! Shake to begin calibration!',delay=80,loop=False,wait=True)

#通过shake手势开始准备环节
while flag == 0:
    display.show(Image.HAPPY)
    if accelerometer.was_gesture('shake'):
        flag=1

#flag2=0#direction
flag3=-1#music
flag4=0#左右手
        

while flag==1:#确认所佩戴机器位于左手或右手
    if accelerometer.was_gesture('left'):#左手初始判定
      display.show(Image.ARROW_W)
      flag4=1
    elif accelerometer.was_gesture('right'):#右手初始判定
        flag4=2
        display.show(Image.ARROW_E)
    time.sleep(2)#间隔二秒进行二次判定确认所佩戴手
    if flag4==1 and accelerometer.was_gesture('left'):
        display.show('L')
        time.sleep(2)
        flag=6
    elif flag4==2 and accelerometer.was_gesture('right'):
        display.show('R')
        time.sleep(2)
        flag=6
    

while flag==6:
    if 130<=compass.heading() <=140:#初始位于135°±5°范围内-一次判定
        flag2=0
        if flag2+flag3!=0:
            flag2=0
            flag3=0
            music.play(music.BA_DING,wait=False)
        display.show(Image.HEART)
        time.sleep(2)
        if  130<=originPoint<=140:#二次判定
            flag2=1
            music.play(music.ODE,wait=False)#判定成功提示音
            display.scroll('Ready! Raise your hands to Play',delay=80,loop=False,wait=True)#举起双手-准备开始演奏
            while flag == 6:
                display.show(Image.HAPPY)
                time.sleep(1)
                display.show(Image('00900:'
                       '09000:'
                       '99999:'
                       '09000:'
                       '00900'))
                if accelerometer.was_gesture('up'):
                    flag=2#激活成功
                    display.show(Image.ARROW_N)
                    music.play(music.BA_DING)
    else: #增加背景音乐和旋转提示
        flag2=1
        if flag2+flag3!=2:
            flag2=1
            flag3=1
            music.play(music.BLUES,loop=True,wait=False)
        if 0< compass.heading() < 130 or 315<compass.heading()<360:#
            display.show(Image('00900:'
                       '00090:'
                       '99999:'
                       '00090:'
                       '00900'))
        elif 140 < compass.heading() < 315:
            display.show(Image('00900:'
                       '09000:'
                       '99999:'
                       '09000:'
                       '00900'))
                       
                       
dic={0:['c'],1:['d'],2:['e'],3:['f'],4:['g'],5:['a'],6:['b'],7:['c5']}#音阶字典
flag6=0#标记打击状态
while flag==2:
    display.show(Image.HAPPY)
    sleep(400)
    if accelerometer.was_gesture('face up'):
        flag6=1
    if flag6:
        if 0 < compass.heading() < 270:#音符激发范围为0°-270°
            rg=int((compass.heading())/270*4+4)%4+(flag4-1)*4
            #int((compass.heading())/270*4+4)%4表示四分区，
            #(flag4-1)*4为左右手区分
            music.play(dic[rg])
        flag6=0
    if pin_logo.is_touched():#当logo被触摸时游戏暂停
        display.scroll("Paused. Press A to Continue Press B to Quit",delay=80,loop=True,wait=False)
        flag5=1
        while flag5:
            if button_a.was_pressed():#按下A建游戏继续
                flag=2
                flag5=0
            elif button_b.was_pressed():#按下B键游戏结束
                flag=0
                flag5=0
                display.show(Image.HAPPY)
                time.sleep(2)
                display.scroll("Goodbye!",delay=80,loop=True,wait=False)
                music.play(music.PYTHON)