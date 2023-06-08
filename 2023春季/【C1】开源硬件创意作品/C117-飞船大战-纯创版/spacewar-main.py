# Imports go at the top
from microbit import *


# Imports go at the top
from microbit import *
from random import randint
import time
import music


#Code in a 'while True:' loop repeats forever
#display.scroll("SNNY GO!")
gamestate=2
t=time.ticks_ms()
obstacles=[]
beginningcor=[3,2]
newcollide=[]
point=0
def setbegining():
    ob0=[randint(-15,-10),0]
    ob1=[randint(-15,-10),1]
    ob2=[randint(-15,-10),2]
    ob3=[randint(-15,-10),3]
    ob4=[randint(-15,-10),4]
    return [ob0,ob1,ob2,ob3,ob4]
def gamerefresh(obstacles):
    for i in obstacles:
        i[0]=i[0]+1
        if i[0]>5:
            i[0]=randint(-15,-1)
def showobstacles(l,cor):
    map1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in l:
        a=i[0]
        b=i[1]
        if 0<=a<5 and 0<=b<5:
            map1[a][b]=5+map1[a][b]
    c=cor[0]
    d=cor[1]
    map1[c][d]=min(9+int(map1[c][d]),9)
    for i in map1:
        for j in range(5):
            i[j]=str(i[j])
    map1=list(map(lambda x:"".join(x),map1))
    map1=":".join(map1)
    display.show(Image(map1))
def detectcollide(l,cor):
    for i in l:
        if i[0]==cor[0] and i[1]==cor[1]:
            i[0]=randint(-15,-10)
            music.play(["c4:2"])
            
            return 1
    else:
        return 0
def refresh_my_spaceship(beginningcor):
    if button_b.was_pressed():
        if beginningcor[1]<4:
            beginningcor[1]=beginningcor[1]+1
    if button_a.was_pressed():
        if beginningcor[1]>0:
            beginningcor[1]=beginningcor[1]-1
    if pin0.is_touched():
        beginningcor[0]=4
    if pin1.is_touched():
        beginningcor[0]=3
    if pin2.is_touched():
        beginningcor[0]=2

fail=0        
level=1
while True:
    if gamestate==0:
        display.scroll("zzZ",delay=50)
        if microphone.current_event() == SoundEvent.LOUD:
            gamestate=0.5     
        if pin_logo.is_touched():
            gamestate=0.5
    if gamestate==0.5 and button_b.was_pressed():
        gamestate=1
    if gamestate==1:
        display.clear()
        for i in range(5):
            for j in range(5):
                display.set_pixel(i,j,9)
                sleep(50)
        display.clear()
        display.set_pixel(2,3,9)
        sleep(600)
        display.clear()
        display.show(Image.ARROW_E)
        sleep(1000)
        display.clear()
        display.set_pixel(2,3,9)
        sleep(600)
        display.clear()
        display.set_pixel(3,3,9)
        sleep(600)
        display.clear()
        display.show(Image.ARROW_W)
        sleep(1000)
        display.clear()
        display.set_pixel(2,3,9)
        sleep(600)
        display.clear()
        display.set_pixel(1,3,9)
        sleep(1200)
        display.clear()
        sleep(500)
        gamestate=1.5
    if gamestate==1.5:
        display.show(Image.ARROW_W)
        gamestate=2
    if gamestate==2 and button_a.was_pressed():
        music.play(music.POWER_UP,wait=False)
        display.scroll("READY?",delay=80)
        display.show("3")
        sleep(500)
        display.show("2")
        sleep(800)
        display.show("1")
        sleep(800)
        display.scroll("GO!",delay=30)
        sleep(800)
        obstacles=setbegining()
        point=0
        newcollide=[False]*5
        gamestate=3
    if gamestate==4:
        music.play(music.WAWAWAWAA,wait=False)
        display.scroll("TRY AGAIN!",delay=60)
        if button_b.was_pressed():
            music.play(music.POWER_DOWN)
            display.scroll("GOODBYE",delay=80)
            break
        else:
            sleep(1000)
            gamestate=1.5
            level=1
    if gamestate==5:
        music.play(music.JUMP_UP)
        display.scroll("CONGRATS!LEVEL UP",delay=100)
        if button_b.was_pressed():
            music.play(music.POWER_DOWN)
            display.scroll("GOODBYE",delay=80)
            break
            
        else:
            sleep(1000)
            gamestate=1.5
            level+=1
    if gamestate==3:
        for i in range(200):
            if i%2==0:
                gamerefresh(obstacles)
            if i>3:
                refresh_my_spaceship(beginningcor)
                
            showobstacles(obstacles,beginningcor)
            a=detectcollide(obstacles,beginningcor)
            point+=a
            sleep(400/level)
            if point>=10:
                gamestate=5
                break
        else:
            if point>=10:
                gamestate=5
            else:
                gamestate=4

