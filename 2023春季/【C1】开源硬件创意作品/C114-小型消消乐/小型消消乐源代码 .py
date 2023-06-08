from microbit import *
import random
import music

score = 0
end = False
button_a.was_pressed()
button_b.was_pressed()
while not end:
    pixel = random.choice([3,6,9])
    x = random.randrange(0,5)
    y = 0
    stop = False
#产生的新的随机像素点位置已经有了像素点，结束整个游戏
    if display.get_pixel(x,y) != 0:
        end = True
    else:
        display.set_pixel(x,y,pixel)
    sleep(500)
    while not stop:
        #清除之前位置的亮度
        display.set_pixel(x,y,0)
        #循环中A被按下
        if button_a.was_pressed():
            left = 0
            if x > 0:
                for i in range(x-1,-1,-1):
                    if display.get_pixel(i,y) != 0:
                        left = i+1#右边一格是左边界
                        break
                x = max(left,x-button_a.get_presses())#设定最小边界
        #循环中B被按下
        if button_b.was_pressed():
            right = 4
            if x < 4:
                for i in range(x+1,5):
                    if display.get_pixel(i,y) != 0:
                        right = i-1#左边一格是右边界
                        break
                x = min(right,x+button_b.get_presses())#设定最大边界
        #如果y达到最大边界，或者下面已经有像素点，结束
        if y == 4 or display.get_pixel(x,y+1) != 0:
            display.set_pixel(x,y,pixel)
            stop = True
        #没有达到最大边界，下面也没有像素点
        elif y < 4 and display.get_pixel(x,y+1) == 0:
            y = y + 1
        display.set_pixel(x,y,pixel)
        sleep(500)
    judge_stop = False
    #判断可消除的方块
    while not judge_stop:
        judge_stop = True
        for j in range(5):
            clear = True
            for i in range(4):
                if display.get_pixel(i,j) != 9:
                    clear = False
                #当有两个相同亮度的方块左右相邻时，合并为一个更大亮度的方块
                if display.get_pixel(i,j) == display.get_pixel(i+1,j) and display.get_pixel(i,j)>0:
                    if display.get_pixel(i,j) < 9:
                        judge_stop = False
                        light=display.get_pixel(i,j) + 3
                        display.set_pixel(i,j,light)
                        for k in range(j,0,-1):
                            display.set_pixel(i+1,k,display.get_pixel(i+1,k-1))
                        display.set_pixel(i+1,0,0)
            if display.get_pixel(4,j) != 9:
                clear = False
            #当一行全为最大亮度的方块时，整行消除，分数加500
            if clear:
                music.play(['c4:2','c4:2','d4:2','a4:2','b4:2'])
                judge_stop = False
                for l in range(5):
                    display.set_pixel(l,j,0)
                    for m in range(j,0,-1):
                        display.set_pixel(l,m,display.get_pixel(l,m-1))
                    display.set_pixel(l,0,0)
                score += 500
        sleep(500)
        
#游戏结束时，清算剩余方块
for j in range(5):
    for i in range(5):
        score += display.get_pixel(i,j)*0.7
        
#显示得分
music.play(['c4:4','g4:4','f4:3','d4:4','g4:2','b4:4','f4:3','g4:2','d4:1'])
display.scroll('score:'+str(score))