from microbit import *
import random
#按A开始，A键向右，B键向下，不按自动向前，长按logo增加难度
class trap:
    def __init__(self,dif):#难度参数
        self.difficulty = dif
    def map(self,snakelist):#随机生成，返回一个列表
        maplist=[["0","0","0","0","0"],["0","0","0","0","0"]\
               ,["0","0","0","0","0"]\
              ,["0","0","0","0","0"],["0","0","0","0","0"]]
        for i in range(5):
            for j in range(self.difficulty):
                p = random.randint(0,4)
                if snakelist[i][p] == '0':
                    maplist[i][p] = '5'
            
        return maplist
class snake:
    def __init__(self,x,y,a,b):
        self.location1=(x,y)
        self.location2=(a,b)
    def lit(self):
        alist=[["0","0","0","0","0"],["0","0","0","0","0"]\
               ,["0","0","0","0","0"]\
              ,["0","0","0","0","0"],["0","0","0","0","0"]]
        x,y=self.location1
        a,b=self.location2
        alist[x % 5][y % 5]="9"
        alist[a % 5][b % 5]="9"
        return alist
    def right(self):
        x,y=self.location1
        a,b=self.location2
        x,y=a,b
        a,b=a,b+1
        self.location1=(x,y)
        self.location2=(a,b)
    def down(self):
        x,y=self.location1
        a,b=self.location2
        x,y=a,b
        a,b=a+1,b
        self.location1=(x,y)
        self.location2=(a,b)
    def isright(self):
        x,y=self.location1
        a,b=self.location2
        return x==a and y==b-1
    def isdown(self):
        x,y=self.location1
        a,b=self.location2
        return x==a-1 and y==b
def attack(oldlist,newlist):#蛇与障碍重合时结束游戏
    for row in range(5):
        for col in range(5):
            if oldlist[row][col]!= '0' and \
            newlist[row][col] != '0':
                return True
    else:
        return False
def showmap(a,b):#将map和snake一起显示
    maplist = [["0","0","0","0","0"],["0","0","0","0","0"]\
               ,["0","0","0","0","0"]\
              ,["0","0","0","0","0"],["0","0","0","0","0"]]
    for i in range(5):
        for j in range(5):
            maplist[i][j] = str(int(a[i][j]) +int(b[i][j]))
            if int(maplist[i][j]) > 9:
                maplist[i][j] = '9'
    mapstr = "".join(maplist[0])+":"+"".join(maplist[1])+\
                    ":"+"".join(maplist[2])+":"+"".join(maplist[3])+\
                    ":"+"".join(maplist[4])
    return mapstr
while True:
    display.show('press A')
    if button_a.was_pressed():
        break
display.show(Image('90000:'
                   '00000:'
                   '00000:'
                   '00000:'
                   '00000'))
while True:
    if button_a.was_pressed():
        asnake=snake(0,0,0,1)#按钮a代表向右
        asnake.lit()
        break
    elif button_b.was_pressed():
        asnake=snake(0,0,1,0)#按钮b代表向下
        asnake.lit()
        break
x = 1
difficulty = 1
time = 1000
while True:
    tra = trap(difficulty)
    if button_a.was_pressed() and asnake.isdown()\
    or button_b.was_pressed() and asnake.isright():
        if asnake.isdown():
            asnake.right()
            lit = asnake.lit()
            if x >0:#new_set a map
                map = tra.map(asnake.lit())
            display.show(Image(showmap(lit,map)))
            sleep(time)
        else:
            asnake.down()
            lit = asnake.lit()
            if x >0:#new_set a map
                map = tra.map(asnake.lit())
            display.show(Image(showmap(lit,map)))
            sleep(time)
    else:
        if asnake.isright():
            asnake.right()
            lit = asnake.lit()
            if x >0:#new_set a map
                map = tra.map(asnake.lit())
            display.show(Image(showmap(lit,map)))
            sleep(time)
        elif asnake.isdown():
            asnake.down()
            lit = asnake.lit()
            if x >0:#new_set a map
                map = tra.map(asnake.lit())
            display.show(Image(showmap(lit,map)))
            sleep(time)
    if attack(lit,map):
        display.show(Image(showmap(lit,map)))
        sleep(2000)
        break
    if pin_logo.is_touched():#加多
        difficulty += 1 
    if pin_logo.is_touched() and button_b.was_pressed():#加速
        time -= 100 
    x = -x   
    
display.show('lose')    
while True:#结束
    if pin_logo.is_touched():
        display.show(Image.HAPPY)