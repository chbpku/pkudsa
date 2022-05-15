from microbit import *
import random
import music

while True:
    display.show(Image.HEART)
    if button_a.is_pressed() and button_b.is_pressed():
        break

LEVEL_list=[1000,700,400]
win_list=[20,60,60]
egg_list=[50,70,40]

def transformer(matrix):
    s=''
    for i in range(5):
        for j in range(5):
            s+=str(matrix[i][j])
        s+=':'
    return s
def move(turn):
    if turn==0:
        dx=1
        dy=0
    elif turn==1:
        dx=0
        dy=1
    elif turn==2:
        dx=-1
        dy=0
    elif turn==3:
        dx=0
        dy=-1
    return dy,dx
def random_egg():
    return [random.randint(1,13),random.randint(1,13)]

class game :
    def __init__(self,eggs,wins):
        self.over=False
        self.body=[[0 for i in range(15)]for j in range(15)]
        self.body[7][7]=7
        self.body_list=[[7,7]]
        self.egg=[[0 for i in range(15)]for j in range(15)]
        self.egg_num=0
        self.egg_sum=eggs
        self.win_sum=wins
        while self.egg_num < self.egg_sum:
            l=random_egg()
            if self.egg[l[0]][l[1]] == 0:
                self.egg[l[0]][l[1]]=3
                self.egg_num+=1
        self.egg[7][7]=0
        self.win=False
        self.turn=0
        self.backgrd=[[0 for i in range(15)]for j in range(15)]
        for i in range(15):
            self.backgrd[0][i]=9
            self.backgrd[14][i]=9
            self.backgrd[i][0]=9
            self.backgrd[i][14]=9
        for i in range(15):
            for j in range(15):
                self.backgrd[i][j]+=self.body[i][j]+self.egg[i][j]
        self.showing=[[0 for i in range(5)]for j in range(5)]
        
    def update(self):
        if len(self.body_list)>self.win_sum:
            self.win=True
            return
        dx,dy=move(self.turn)
        head=self.body_list[0]
        new_pos=[head[0]+dx,head[1]+dy]
        if self.backgrd[new_pos[0]][new_pos[1]]==9 or self.body[new_pos[0]][new_pos[1]]!=0:
            self.over=True
        elif self.egg[new_pos[0]][new_pos[1]]!=0:
            self.body_list.insert(0,new_pos)
            self.egg[new_pos[0]][new_pos[1]]=0
            while True:
                l=random_egg()
                if self.egg[l[0]][l[1]] == 0 and self.body[l[0]][l[1]]==0:
                    self.egg[l[0]][l[1]]=3
                    break
            self.body[new_pos[0]][new_pos[1]]=7
            self.backgrd[new_pos[0]][new_pos[1]]=7
        else:
            old_pos=self.body_list.pop()
            self.body_list.insert(0,new_pos)
            self.body[new_pos[0]][new_pos[1]]=7
            self.backgrd[new_pos[0]][new_pos[1]]=7
            self.body[old_pos[0]][old_pos[1]]=0
            self.backgrd[old_pos[0]][old_pos[1]]=0
        self.show()
            
    def show(self):
        head=self.body_list[0]
        n=head[0]//5
        m=head[1]//5
        for i in range(5):
            for j in range(5):
                self.showing[i][j]=self.backgrd[i+n*5][j+m*5]
        display.show(Image(transformer(self.showing)))
      
win=False
for k in range(3):
    time_intrv=LEVEL_list[k]
    display.scroll('LV')
    display.scroll(str(k+1))
    s=game(egg_list[k],win_list[k])
    while s.over==False and s.win==False:
        t0=running_time()
        while running_time()<t0+time_intrv:
            if button_a.is_pressed():
                s.turn-=1
                if s.turn<0:
                    s.turn=3
                sleep(80)
                break
            elif button_b.is_pressed():
                s.turn+=1
                if s.turn>3:
                    s.turn=0
                sleep(80)
                break
            else:
                continue
        while running_time()<t0+time_intrv:
            sleep(10)
        s.update()
    if s.over==True:
        display.show(Image.SAD)
        music.play(music.WAWAWAWAA)
        
        break
    else:
        display.show(Image.SMILE)
        music.play(music.NYAN)
        
        if k == 2:
            win=True
if win :
    display.scroll('WIN')
else:
    display.scroll('LOSE')




