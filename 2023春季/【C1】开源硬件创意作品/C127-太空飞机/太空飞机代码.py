from microbit import *
from random import randint
import time

class plane:
    def __init__(self):
        self.Light = 9
        self.Location = [2,4]
        self.wuDi = False
        self.outed = False
        self.count = 0
        self.wuDitime = 0
        self.temp = self.Light
        
    def wudiTime(self):
        if self.wuDi:
            self.wuDitime += 1
            self.Light = 0
        if self.wuDitime > 100:
            self.wuDi = False
            self.wuDitime = 0
            self.Light = self.temp
        
    def Left_go(self):
        if button_a.is_pressed():
            if self.Location[0] > 0:
               self.Location[0]-=1
        return self.Location[0]
    
    def Right_go(self):
        if button_b.is_pressed():
            if self.Location[0] < 4:
                self.Location[0]+=1
        return self.Location[1]
        
    def getHitted(self,razor):
        if not self.wuDi:
            if self.Location == [razor.x,razor.y]:
                self.Light -= 2
                razor.disappear()
            
    def Upwards(self):
        if pin_logo.is_touched():
            if self.Location[1] > 0:
                self.Location[1] -= 1
    
    def Downwards(self):
        if not pin_logo.is_touched():
            if self.Location[1] < 4:
                self.Location[1] += 1

    def get_buff(self,buff):
        if self.Location == buff.Location:
            choice_num = randint(0,2)
            if choice_num == 0:
                if self.Light != 9:
                    self.Light += 2
                else:
                    self.count += 5
            elif choice_num == 1:
                self.wuDi = True
                self.wuDitime = 0
            else:
                self.count += 5
            return True
        else:
            return False 
    
    def Out(self):
        if self.Light == 1:
            display.scroll('Out')
            display.scroll(self.count)
            self.outed = True
    
    def show(self):
        display.set_pixel(self.Location[0], self.Location[1],self.Light)

class razor:
    def __init__(self):
        self.x = randint(0,4)
        self.y = 0

    def show(self):
        if self.y <= 4:
            display.set_pixel(self.x,self.y,1)
        

    def disappear(self):
        display.set_pixel(self.x,self.y,0)

    def godown(self):
        self.y += 1
        
class plane_razor:
    def __init__(self,plane):
        self.x = plane.Location[0]
        self.y = plane.Location[1]
       

    def show(self):
        if self.y >= 0:
            display.set_pixel(self.x,self.y,3)
            
                
    def goup(self):
        self.y -= 1

    def disappear(self):
        display.set_pixel(self.x,self.y,0)

    def Hitted(self,razor):
        if self.x == razor.x and self.y <= razor.y :
            self.disappear()
            razor.disappear()
            return True
        else:
            return False
        
class Buff:
    def __init__(self):
        self.Location = [randint(0,4),0]

    def disappear(self):
        display.set_pixel(self.Location[0],self.Location[1],0)

    def godown(self):
        self.Location[1] += 1
            
    def show(self):
        if self.Location[1] <= 4:
            display.set_pixel(self.Location[0],self.Location[1],7)

Plane = plane()
i = 0
razor_lst = []
plane_razor_lst = []
Buff_lst = []
while not Plane.outed:
    Plane.Left_go()
    Plane.Right_go()
    Plane.Downwards()
    Plane.Upwards()
    i += 1
    if i % 3 == 0:
        pr = plane_razor(Plane)
        plane_razor_lst.append(pr)
    if i % 2 == 0:
        r = razor()
        razor_lst.append(r)
    buffnum = randint(0,200)
    
    if buffnum == 10:
        b = Buff()
        Buff_lst.append(b)
        
    if plane_razor_lst != []:
        for m in range(len(plane_razor_lst)-1,-1,-1):
            if plane_razor_lst[m].y == -1:
                plane_razor_lst.pop(m)
                
    if razor_lst != []:
        for m in range(len(razor_lst)-1,-1,-1):
            if razor_lst[m].y == 5:
                razor_lst.pop(m)
                
    if Buff_lst != []:
        for m in range(len(Buff_lst)-1,-1,-1):
            if Buff_lst[m].Location[1] == 5:
                Buff_lst.pop(m)
                
    if razor_lst and plane_razor_lst:
        for n in range(len(razor_lst)-1,-1,-1):
            for m in range(len(plane_razor_lst)-1,-1,-1):
                if plane_razor_lst[m].Hitted(razor_lst[n]):
                    plane_razor_lst.pop(m)
                    razor_lst.pop(n)
                    Plane.count += 1
                    break
                    
    if razor_lst != []:
        for m in range(len(razor_lst)-1,-1,-1):
            Plane.getHitted(razor_lst[m])
            if razor_lst[m].x == Plane.Location[0] and razor_lst[m].y == Plane.Location[1]:
                razor_lst.pop(m)
    
    if Buff_lst:
        for j in range(len(Buff_lst)-1,-1,-1):
            if Plane.get_buff(Buff_lst[j]):
                Buff_lst.pop(j)
    
    Plane.wudiTime()
            
    display.clear()
    
    for pr in plane_razor_lst:
        pr.show()
        
    for r in razor_lst:
        r.show()
        
    for b in Buff_lst:
        b.show()
        
    Plane.show()
    Plane.Out()
    if i <= 200:
        sleep(200)

    elif 200<i<400:
        sleep(100)
    else:
        sleep(50)
    
    for pr in plane_razor_lst:
        pr.goup()
        
    for r in razor_lst:
        r.godown()
        
    if i % 3 == 0:
        for b in Buff_lst:
            b.godown()
            
    
                
                
    



