#mPythonType:0
#mPythonType:0
#mPythonType:0

from mpython import *
import time
from random import randint

_is_shaked = _is_thrown = False
_last_x = _last_y = _last_z = _count_shaked = _count_thrown = 0

class snowball():
    def __init__(self):                
        self.x = randint(0,127)        
        self.y = randint(0,10)
        self.r = randint(1,2)           
        self.vx = randint(-2,2)        
        self.vy = randint(1,3)         
 
    def refresh(self):                 
        self.x += self.vx              
        self.y += self.vy
        if self.x > 128 or self.x < 0:
            self.x = randint(0,127)
        if self.y > 63 or self.y < 0:
            self.y = 0
            
    def run(self):
            self.refresh()
            oled.fill_circle(self.x,self.y,self.r,1)     #画雪花
class bar():
    def __init__(self,mode,stack,rate,rang):
        self.mode=mode
        self.x=0
        self.y=16
        self.value=0
        self.stack=stack
        self.rate=rate
        self.rang=rang
    def set(self):
        if self.mode==0:
            self.x=randint(2,20)
        elif self.mode==1:
            self.x=randint(33,52)
        elif self.mode==2:
            self.x=randint(65,84)
        elif self.mode==3:
            self.x=randint(97,116)
        if self.rang==1:
            self.value=randint(60,75)
        elif self.rang==2:
            self.value=randint(70,90)
        
        self.stack[self.mode]=self.value

class Game():
    def __init__(self,level):
        self.level=level
        self.state=0
        self.maxscore=self.read_high_score()
        self.score=0
    def write_high_score(self,n):
        f = open('fb_high_score.txt', 'w')
        f.write(str(n))
        f.close()

    # 读取最高分
    def read_high_score(self):
        if 'fb_high_score' in uos.listdir():
            f = open('fb_high_score.txt', 'r')
            high_score = f.read()
            f.close()
            return int(high_score)
        else:
            self.write_high_score(0)
            return 0
    def game_start(self):
        rgb.fill( (0, 0, 0) )
        rgb.write()
        time.sleep_ms(1)
        balls = []
        for x in range(20):              #生成20个雪花点
            balls.append(snowball())        
        t1=time.time()
        t2=time.time()
        
        while (t2-t1)<1.5:
            sleep_ms(50)                 #刷新时间
            oled.fill(0)                 #清屏
            for b in balls:              #雪花落下
                b.run()
            oled.show()                  #显示oled
            t2=time.time()
        
        
        
        rgb[0]=(25,25,25)
        rgb.write()
        time.sleep(1)
        rgb[1]=(25,25,25)
        rgb.write()
        time.sleep(1)
        rgb[2]=(25,25,25)
        rgb.write()
        time.sleep(1)
       
        oled.fill(0)
        oled.DispChar('重生之我是老师模拟器',0,0)
        oled.DispChar('按下B开始游戏',20,15)
        oled.DispChar('触摸H进入剧情', 20, 30)
        oled.DispChar('T最高分 O难度',20,45)
        oled.show() 
           
                 
        import music
        music.play(music.PYTHON)
        self.state=1
    def page(self):
        oled.fill(0)
        oled.DispChar('触摸H进入剧情', 20, 0)
        oled.DispChar('按下B开始游戏',22,15)
        oled.DispChar('按下A退出游戏', 20, 30)
        oled.DispChar('触摸T查看最高分',18,45)
        oled.show()
        self.state=1
    def check(self):
        while True:
            if button_a.is_pressed():
                oled.fill(0)
                oled.DispChar('下次再会', 50, 30)
                oled.show()
                time.sleep(2)
                oled.fill(0)
                image_picture = Image()
                oled.blit(image_picture.load('face/4.pbm', 0), 32, 0)
                oled.show()
                time.sleep(1)
                oled.fill(0)
                oled.show()
                self.state=2
                break
            elif button_b.is_pressed():
                self.state=3
                break
            elif touchpad_t.is_pressed():
                
                self.state=4
                break
            elif touchpad_h.is_pressed():
                self.state=7
                break
            elif touchpad_o.is_pressed():
                oled.fill(0)
                oled.DispChar(str(self.level), 60, 30)
                oled.show()
                while True:
                    if touchpad_p.is_pressed():
                        if self.level>0:
                            self.level-=1
                    if touchpad_n.is_pressed():
                        if self.level<5:
                            self.level+=1
                    elif button_b.is_pressed():
                        break
                    oled.fill(0)
                    oled.DispChar(str(self.level), 60, 30)
                    oled.show()
                self.state=5
    def run(self):
        while True:
            if self.state==0:
                self.game_start()
            elif self.state==1:
                self.check()
            elif self.state==2:
                while True:
                    if button_b.is_pressed():
                        self.game_start()
                        break
            elif self.state==3:
                self.game_running1() 
            elif self.state==4:
                oled.fill(0)
                oled.DispChar('最高得分为'+str(self.maxscore), 32, 15)
                oled.DispChar('按下B再来一次',20,30)
                oled.show()
                time.sleep(2)
                self.state=5
            elif self.state==5:
                self.page()
            elif self.state==6:
                self.game_running2()
            elif self.state==7:
                self.story()
            elif self.state==8:
                self.story2()
    def story(self):
        oled.fill(0)
        oled.DispChar('天黑请闭眼', 45, 29)
        oled.show()
        while True:
            oled.DispChar("亮度:",30,16)                    #显示亮度
            oled.DispChar("%d" % (light.read()), 60, 16)    #显示板载光线传感器
            oled.show()                                     #刷新
            sleep_ms(100)                                   #延时100ms
            if light.read() < 100 :                   
                rgb.fill((0,0,0))
                rgb.write()
                time.sleep(1)
                oled.fill(0)
                oled.show()
                break
            else:                                     
                rgb.fill((200,200,200))
                rgb.write()
                time.sleep(1)
        import music
        music.play(music.BLUES)
        music.play(music.POWER_UP)
        time.sleep(2)
        oled.fill(0)
        oled.DispChar('快醒醒！快醒醒', 30,28)
        oled.show()
        rgb.fill((20,200,0))
        rgb.write()
        stop=0
        from machine import Timer
        def on_shaked():pass
        def on_thrown():pass
        tim11 = Timer(11)
        def timer11_tick(_):
            global _is_shaked, _is_thrown, _last_x, _last_y, _last_z, _count_shaked, _count_thrown
            if _is_shaked:
                _count_shaked += 1
                if _count_shaked == 5: _count_shaked = 0
            if _is_thrown:
                _count_thrown += 1
                if _count_thrown == 10: _count_thrown = 0
                if _count_thrown > 0: return
            x=accelerometer.get_x(); y=accelerometer.get_y(); z=accelerometer.get_z()
            _is_thrown = (x * x + y * y + z * z < 0.25)
            if _is_thrown: on_thrown();return
            if _last_x == 0 and _last_y == 0 and _last_z == 0:
                _last_x = x; _last_y = y; _last_z = z; return
            diff_x = x - _last_x; diff_y = y - _last_y; diff_z = z - _last_z
            _last_x = x; _last_y = y; _last_z = z
            if _count_shaked > 0: return
            _is_shaked = (diff_x * diff_x + diff_y * diff_y + diff_z * diff_z > 1)
            if _is_shaked: on_shaked()
        
        tim11.init(period=100, mode=Timer.PERIODIC, callback=timer11_tick)
        while True:
            if _is_shaked:
                oled.fill(0)
                oled.DispChar('你发现了一些奇怪的变化', 10, 30)
                oled.show()
                time.sleep(1)
                oled.fill(0)
                oled.DispChar('等等..', 32, 30)
                oled.show()
                time.sleep(1)
                
                oled.fill(0)
                oled.DispChar('你变成了xx老师！！', 32, 30)
                oled.show()
                time.sleep(1) 
                shake=1
                break
        #import music
        #music.play(music.FUNK)
        rgb.fill((0,0,0))
        rgb.write()
        oled.fill(0)
        oled.DispChar('你来到了办公室！！', 20, 30)
        oled.show()
        rgb[0]=(0,200,0)
        rgb.write()
        time.sleep(1) 
        oled.fill(0)
        oled.DispChar('在你面前', 40, 20)
        oled.DispChar('有你刚刚考完的试卷！！', 30, 35)
        oled.show()
        rgb[1]=(0,200,0)
        rgb.write()
        time.sleep(1) 
        oled.fill(0)
        oled.DispChar('快捞捞你的同学！', 25, 30)
        oled.show()
        rgb[2]=(0,200,0)
        rgb.write()
        time.sleep(1) 
        oled.fill(0)
        oled.DispChar('操作说明：', 0, 0)
        oled.DispChar('P/T/H/N控制光标', 0, 15)
        oled.DispChar('A/B键捞捞', 0, 30)
        oled.DispChar('不同level有不同好评奖励', 0, 45)
        oled.show()
        time.sleep(3)
        self.state=3
    def story2(self):
        oled.fill(0)
        oled.DispChar('huhu~好累~', 32, 30)
        rgb.fill((0,0,200))
        rgb.write()
        oled.show()
        time.sleep(1) 
        oled.fill(0)
        oled.DispChar('现在', 55, 20)
        oled.DispChar('去鼓励一下那些成绩好的同学！',0 , 40)
        rgb.fill((0,200,0))
        rgb.write()
        oled.show()
        time.sleep(1) 
        oled.fill(0)
        oled.DispChar('操作说明：', 0, 0)
        oled.DispChar('P/T/H/N控制光标', 0, 15)
        oled.DispChar('A/B键鼓励', 0, 30)
        oled.DispChar('不同level有不同好评奖励', 0, 45)
        oled.show()
        time.sleep(2)
        self.state=6
    def game_running1(self):
        rgb.fill((0,64,64))
        rgb.write()
        
        nnl=[68, 63, 73, 78, 74, 75, 62, 66, 56, 67, 57, 76, 61, 69, 72, 65, 59, 79, 58, 64, 70, 71, 55, 77, 60]
        nnl+=[76, 72, 58, 62, 77, 67, 66, 64, 69, 59, 56, 57, 74, 61, 78, 79, 73, 63, 71, 70, 55, 75, 60, 68, 65]
        lx=16
        ly=62
        stack=[100,100,100,100]
        dl=133
        rate=4
        curnum=59
    
        mode=1
        timetool=randint(0,30)
        cnt=0
        tmp=0
        nownum=nnl[timetool]
        judge=0
        obj=bar(randint(0,3),stack,randint(3,5),1)
        obj.set()
        stop=0
        dydown=0
        timeonly=0
        
        stack=obj.stack
        error=0
        rightornot=1
        stop=0
        busy=1
        while True:
            if self.level==0:
                timetool=cnt//25
            else:
                timetool=cnt//(30-3*self.level)
            timetool=timetool%(len(nnl))
            if timetool!=tmp:
                nownum=nnl[timetool]
            tmp=timetool
            oled.fill(0)
            oled.vline(0,0,64,1)
            oled.vline(32,16,64,1)     
            oled.vline(64,16,64,1)
            oled.vline(96,16,64,1)
            oled.vline(127,0,64,1)
            oled.hline(0,16,128,1)
            oled.pixel(lx, ly, 1)
            oled.pixel(lx,ly+1,1)
            oled.pixel(lx-1, ly+1, 1)
            oled.pixel(lx+1, ly+1, 1)
            
            oled.DispChar(str(nownum)+str('捞捞')+'   '+'好评：'+str(self.score), 1, 0, 1)
            if timeonly==64//(obj.rate):
                busy=0
                if judge==obj.mode and stack[judge]<nownum:#没捞到还选中要扣分
                    self.score-=1
                    error+=1
                elif judge!=obj.mode and stack[judge]>nownum:#积极为学生服务，加分
                    self.score+=1
            if not busy:
                if self.level==0:
                    obj=bar(randint(0,3),stack,randint(3,5),1)
                else:
                    obj=bar(randint(0,3),stack,randint(self.level,5),1)
                obj.set()
                dydown=0
                stack=obj.stack
                busy=1
                stop=0
                rightornot=1
                timeonly=0
            if not stop:
                oled.DispChar(str(obj.value),obj.x,obj.y+dydown,1)
            else:
                pass
            #oled.DispChar(str(nownum)+' '+str(stack[judge]), 2, 50)

                
            oled.show()
            
            if button_a.value()==0 :
                
                if stack[judge]<nownum and judge==obj.mode:
                    stack[judge]=100
                    stop=1
                    if self.level==0:
                        self.score+=obj.rate
                    else:
                        self.score+=self.level
                    rightornot=0
                    busy=0
                elif stack[judge]>=nownum and judge==obj.mode:
                    stack[judge]=0
                    stop=1
                    self.score-=2
                    error+=1
                    rightornot=1
                    busy=0
        
                
            if touchpad_p.is_pressed():
                    lx = 16
                    judge=0
            elif touchpad_t.is_pressed():
                lx = 48
                judge=1
            elif touchpad_h.is_pressed():
                lx = 80
                judge=2
            elif touchpad_n.is_pressed():
                lx = 112
                judge=3
            
        
            if dydown<=63:
                dydown+=obj.rate
            
            if rightornot==1:
                if error==3:
                    for er in range(error) :
                        rgb[er]=(96,0,0)
                        rgb.write()
                    oled.fill(0)
                    image_picture = Image()
                    oled.blit(image_picture.load('face/11.pbm', 0), 32, 0)
                    oled.show()
                    time.sleep(1)
                    oled.fill(0)
                    oled.DispChar('第一个游戏结束', 32, 20)
                    oled.show()
                    if self.score>=self.maxscore:
                        self.maxscore=self.score
                        self.write_high_score(self.maxscore)
                        oled.fill(0)
                        oled.DispChar('干得漂亮！', 35, 15)
                        oled.DispChar('你获得了年度最佳好评！', 0, 30)
                        oled.DispChar(str(self.score)+'这个好评将被载入史册！', 0, 45)
                        oled.show()
                        import music 
                        music.play(music.POWER_UP)
                        while True:
                            if button_b.is_pressed():
                                break
                            
                    time.sleep(1)
                    self.state=8
                    break
                else:
                    for er in range(error) :
                        rgb[er]=(96,0,0)
                        rgb.write()
                
            cnt+=1
            timeonly+=1
    def game_running2(self):
        rgb.fill((0,64,64))
        rgb.write()
        
        nnl=[68, 63, 73, 78, 74, 75, 62, 66, 56, 67, 57, 76, 61, 69, 72, 65, 59, 79, 58, 64, 70, 71, 55, 77, 60]
        nnl+=[76, 72, 58, 62, 77, 67, 66, 64, 69, 59, 56, 57, 74, 61, 78, 79, 73, 63, 71, 70, 55, 75, 60, 68, 65]
        lx=16
        ly=62
        stack=[0,0,0,0]

        dl=133
        rate=4
        curnum=59
    
        mode=1
        timetool=randint(0,30)
        cnt=0
        tmp=0
        nownum=nnl[timetool]
        judge=0
        obj=bar(randint(0,3),stack,randint(3,5),2)
        obj.set()
        stop=0
        dydown=0
        timeonly=0
        
        stack=obj.stack
        error=0
        rightornot=1
        stop=0
        busy=1
        while True:
            if self.level==0:
                timetool=cnt//25
            else:
                timetool=cnt//(30-3*self.level)
            timetool=timetool%(len(nnl))
            if timetool!=tmp:
                nownum=nnl[timetool]
            tmp=timetool
            oled.fill(0)
            oled.vline(0,0,64,1)
            oled.vline(32,16,64,1)     
            oled.vline(64,16,64,1)
            oled.vline(96,16,64,1)
            oled.vline(127,0,64,1)
            oled.hline(0,16,128,1)
            oled.pixel(lx, ly, 1)
            oled.pixel(lx,ly+1,1)
            oled.pixel(lx-1, ly+1, 1)
            oled.pixel(lx+1, ly+1, 1)
            
            oled.DispChar(str(nownum)+str('鼓励')+'   '+'好评：'+str(self.score), 1, 0, 1)
            if timeonly==64//(obj.rate):
                busy=0
                if judge==obj.mode and stack[judge]>=nownum:#没鼓励还选中要扣分
                    self.score-=1
                    error+=1
                elif judge!=obj.mode and stack[judge]<nownum:#积极工作，加分
                    self.score+=1
            if not busy:
                if self.level==0:
                    obj=bar(randint(0,3),stack,randint(3,5),2)
                else:
                    obj=bar(randint(0,3),stack,randint(self.level,5),2)
                obj.set()
                dydown=0
                stack=obj.stack
                busy=1
                stop=0
                rightornot=1
                timeonly=0
            if not stop:
                oled.DispChar(str(obj.value),obj.x,obj.y+dydown,1)
            else:
                pass
            #oled.DispChar(str(nownum)+' '+str(stack[judge]), 2, 50)

                
            oled.show()
            
            if button_a.value()==0 :
                
                if stack[judge]>=nownum and judge==obj.mode:
                    stack[judge]=0
                    stop=1
                    if self.level==0:
                        self.score+=obj.rate
                    else:
                        self.score+=self.level
                    rightornot=0
                    busy=0
                elif stack[judge]<nownum and judge==obj.mode:
                    stack[judge]=100
                    stop=1
                    self.score-=2
                    error+=1
                    rightornot=1
                    busy=0
        
                
            if touchpad_p.is_pressed():
                    lx = 16
                    judge=0
            elif touchpad_t.is_pressed():
                lx = 48
                judge=1
            elif touchpad_h.is_pressed():
                lx = 80
                judge=2
            elif touchpad_n.is_pressed():
                lx = 112
                judge=3
            
        
            if dydown<=63:
                dydown+=obj.rate
            
            if rightornot==1:
                if error==3:
                    for er in range(error) :
                        rgb[er]=(96,0,0)
                        rgb.write()
                    oled.fill(0)
                    image_picture = Image()
                    oled.blit(image_picture.load('face/11.pbm', 0), 32, 0)
                    oled.show()
                    time.sleep(1)
                    oled.fill(0)
                    oled.DispChar('游戏结束', 32, 20)
                    oled.show()
                    if self.score>=self.maxscore:
                        self.maxscore=self.score
                        self.write_high_score(self.maxscore)
                        oled.fill(0)
                        oled.DispChar('干得漂亮！', 35, 15)
                        oled.DispChar('你获得了年度最佳好评！', 0, 30)
                        oled.DispChar(str(self.score)+'这个好评将被载入史册！', 0, 45)
                        oled.show()
                        import music 
                        music.play(music.POWER_UP)
                        while True:
                            if button_b.is_pressed():
                                break
                    time.sleep(1)
                    self.state=5
                    break
                else:
                    for er in range(error) :
                        rgb[er]=(96,0,0)
                        rgb.write()
                
            cnt+=1
            timeonly+=1
if __name__ == '__main__':
    game=Game(0)
    game.run()
        
        
        
        
        
        
        
        
        
        
        
        