from microbit import *
import random
import music
import time

#准备开始，倒计时三下后提示障碍物移动方向
display.show(3,delay=2000)
music.play(['c:7','r:3'])
display.show(2,delay=2000)
music.play(['c:6','r:3'])
display.show(1,delay=2000)
music.play(['c:6','r:3'])
display.show(Image('00900:'
                   '90909:'
                   '09990:'
                   '00900:'
                   '00000')) #屏幕上显示下箭头，代表障碍物移动方向
music.play(['c5:8'])
display.clear()

#参数设定、显示初始位置
waittime=500 #每一步操作的等待时间
current=random.choice([0,1,2,3,4]) 
display.set_pixel(current,4,9)
time.sleep_ms(2*waittime) 
display.clear() #随机选择初始位置，在屏幕上显示一段时间后消失
score=0
level=20 #总关卡数

#主程序，每一关进行一次循环
for i in range(level):
#每一关生成一个障碍物,生成对应障碍物的障碍位置列表和空位置列表，空位置可能有1或2个
    blocklist=[0,1,2,3,4]
    blanklist=[random.choice(blocklist) for _ in \
                                       range(random.randint(1,2))]
    blocklist=list(set(blocklist)-set(blanklist))
    
    #障碍物在第一行生成并不断下落
    y=0
    while y<=4:
        for block in blocklist:
            display.set_pixel(block,y,9)
        time.sleep_ms(waittime)
        for block in blocklist:
            display.set_pixel(block,y,0)
        time.sleep_ms(waittime)
        y+=1
        
    #检测按键次数左右移动位置，若在一关之内总位移超出了范围，会被墙壁挡住，位置停在0或4，防止index out of range报错。
    current -= (button_a.get_presses()-button_b.get_presses())
    current=min(4,current)
    current=max(0,current)

    #每次显示当前位置，若增加难度，可将代码删去
    display.set_pixel(current,4,9)
    time.sleep_ms(waittime)
    display.clear()
    
    #检测是否发生碰撞，若是则游戏结束，播放失败语音；若否则游戏进入下一关，+1分并播放得分语音。
    if current in blanklist:
        score+=1
        music.play(['c:1','e:1','g:1','c5:1'])
    else:
        display.set_pixel(current,4,9)
        time.sleep_ms(500)
        display.clear()
        display.show(Image.NO)
        music.play(['c5:1','g4:1','e:1','c:1'])
        sleep(1000)
        display.scroll('GAME OVER')    
        display.scroll('SCORE:')  
        display.show(score)
        break
    
    #增加游戏难度，每5关之后下落速度增加
    waittime=500-50*(score//5)

#检测是否通关，通关播放胜利音乐，显示分数
if score==level:
    sleep(1000)
    display.show(Image.YES)
    music.play(music.RINGTONE)
    sleep(1000)
    display.scroll('YOU WIN')    
    display.scroll('SCORE:')  
    display.show(score)
