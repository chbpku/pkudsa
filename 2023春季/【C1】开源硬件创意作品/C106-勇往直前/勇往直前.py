from microbit import *
import random
import music

score = 0
tick=0
pressed=False
player_pos = 2  # 玩家光点的初始位置，初始位置是屏幕中央
queue=[-1,-1,-1,-1,-1]
tune1=['G3:1','A3:1','C4:1','A3:1','E4:3','E4:3','D4:5',
      'G3:1','A3:1','C4:1','A3:1','D4:3','D4:3','C4:3','B3:1','A3:1',
      'G3:1','A3:1','C4:1','A3:1','C4:4','D4:2','B3:3','A3:2','G3:3','D4:4','C4:4']
music.play(tune1)
while True:
    if tick==40:
        tick=0
        # 随机生成光点的位置
        led_pos = random.randint(0, 4)
        queue.append(led_pos)
        queue.pop(0)
        
        #检测是否出现无解情况
        if led_pos==4:
            l=0
            for i in range(3,-1,-1):
                if queue[i]==4-i:
                    l+=1
                else:
                    break
            if l > 1:
                led_pos = random.randint(0, 3)
        if led_pos == 0:
            l=0
            for i in range(1,5):
                if queue[i]==i:
                    l+=1
                else:
                    break
            if l > 1:
                led_pos = random.randint(1, 4)
        
        # 移动光点
        for i in range(5):
            for j in range(5):
                if i == led_pos and j == 0:
                    display.set_pixel(i, j, 5)  # 新光点
                elif  i==player_pos and j == 4:
                    display.set_pixel(i, j, 9)  # 玩家光点
                else:
                    display.set_pixel(i, j, 0)  #清理屏幕 
        for i in range(5):
            if queue[i]>-1:
                display.set_pixel(queue[i], 4-i, 5)#设置旧的光点
        
        # 计分规则
        if score < 20:
            sleep(300)
            score += 1
        elif score < 80:
            sleep(100)
            score += 2
        else:
            sleep(0)
            score += 3
    
        #记录时间
        tick += 1
    else:
        # 移动玩家光点
        if button_a.is_pressed() and player_pos > 0:
            if pressed==False:
                player_pos -= 1
        elif button_b.is_pressed() and player_pos < 4:
            if pressed==False:
                player_pos += 1
        pressed=button_a.is_pressed() or button_b.is_pressed()
            
        # 碰撞检测
        if queue[0] == player_pos:
            for k in range(3):
                for i in range(5):
                    for j in range(5):
                        display.set_pixel(i, j, 0)
                sleep(500)
                for i in range(5):
                    for j in range(5):
                        display.set_pixel(i, j, 9)
                sleep(300)
            tune2=['A3:4','B3:2','E4:2','D4:4','C4:4','B3:4','B3:2','B3:2',
                'D4:4','C4:2','B3:2','A3:2','A3:1','C5:2','B4A3:2','C5:2',
                'B4A3:2','C5:2']
            music.play(tune2)
            display.scroll("SCOre:%d"%score )
            break              # 如果玩家光点和光点重合，游戏结束，并闪光提示，播放音乐
        
        # 保持原本光点不动
        for i in range(5):
            for j in range(5):
                if  i==player_pos and j == 4:
                    display.set_pixel(i, j, 9)  # 玩家光点
                else:
                    display.set_pixel(i, j, 0)  #清理屏幕 
        for i in range(5):
            if queue[i]>-1:
                display.set_pixel(queue[i], 4-i, 5)#设置旧的光点
                
        #记录时间
        tick += 1
        sleep(10)  