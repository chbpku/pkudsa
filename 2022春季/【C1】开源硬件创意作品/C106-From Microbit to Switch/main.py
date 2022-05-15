#this program is made up of three parts:
#1.a mechanical watch that indicates time and show the movement of gear
#2.build_in small games
#3.Just_Dance

from microbit import *
import music,speech,random


#main
def button_judge():
    global buttonA,buttonB,pinZero,pinOne,pinTwo
    
    if button_a.is_pressed():
        buttonA=1
    if button_b.is_pressed():
        buttonB=1
    if pin0.is_touched():
        pinZero=1
    if pin1.is_touched():
        pinOne=1
    if pin2.is_touched():
        pinTwo=1

def control_center():
    global buttonA,buttonB,pinZero,pinOne,pinTwo
    
    buttonA=0#compass
    buttonB=0#triquestion
    pinZero=0#dont_touch_whiteblock
    pinOne=0#Just_Dance
    pinTwo=0
    
    while True:
        watch_run()
        
        #进入这一阶段说明watch_run()已经结束了
        if buttonA==1 and max(buttonB,pinZero,pinOne,pinTwo)==0:
            use_compass()
        elif buttonB==1 and max(buttonA,pinZero,pinOne,pinTwo)==0:
            triquestion()
        elif pinZero==1 and max(buttonA,buttonB,pinOne,pinTwo)==0:
            dont_touch_whiteblock()
        elif pinOne==1 and max(buttonA,buttonB,pinZero,pinTwo)==0:
            Just_Dance()
        elif pinTwo==1 and max(buttonA,buttonB,pinZero,pinOne)==0:
            pass#remain to be chosen
        


def get_GPA(score,full_score,magic=True):#this returns a strType object
    return str(4-(3*((100-((100*score/full_score)**(0.5 if magic else 1)*(10 if magic else 1)))**2)/1600))


#part 1:
def watch_run():
    global buttonA,buttonB,pinZero,pinOne,pinTwo
    
    stop=1
    while stop:
        up=0
        down=0
        for i in range(0,5):
            if accelerometer.current_gesture()!='face down':#泛向上
                up=1
                display.show(Image.ALL_CLOCKS[3*i:3*i+3],delay=200,wait=False,loop=False,clear=False)
            elif accelerometer.current_gesture()!='face up':#泛向下
                up=1
                display.show(Image.ALL_ARROWS[2*i:2*i+2],delay=200,wait=False,loop=False,clear=False)
            if up==1:
                sleep(600)
            elif down==1:
                sleep(400)
            up=0
            down=0
            stop=0
            button_judge()
            if max(buttonA,buttonB,pinZero,pinOne,pinTwo)!=0:
                break
            else:
                stop=1


#part2
def use_compass():
    global buttonA
    
    button_a.was_pressed()
    button_b.was_pressed()
    
    compass.calibrate()
    while True:
        display.show(Image.ALL_CLOCKS[((15-compass.heading())//30)%12])
        sleep(25)
    
        if button_a.was_pressed() and button_b.was_pressed():
            break
    buttonA=0


def triquestion():
    global buttonB
    
    hour=random.randint(1,12)
    quarter=random.randint(0,3)
    minute=random.randint(0,14)
    
    for i in ['D5']*hour + ['B2']*quarter + ['C4']*minute:
        music.play(i)
        sleep(360)
    
    buttonB=0



def dont_touch_whiteblock():
    key_press=[]
    key_light=[]
    tune=['C','C','G','G','A','A','G','F','F','E','E','D','D','C']
    tune_count=0
    #生成初始的
    for i in range(5):
        key_press.append(random.randint(1,5))
    #亮度是3和9
    for i in range(5):
        key_light.append(random.randint(0,1)*6+3)
    button_press_a=0
    button_press_b=0
    button_press_pin0=0
    button_press_pin1=0
    
    music.play(music.PYTHON)
    t=running_time()
    score=0
    while tune_count<len(tune):
        music.play(tune[tune_count])
        image_present=' '
        for i in range(5):
            if key_press[i]==1:
                image_present=image_present+str(key_light[i])+'0000:'
            elif key_press[i]==2:
                image_present=image_present+'0'+str(key_light[i])+'000:'
            elif key_press[i]==3:
                image_present=image_present+'00'+str(key_light[i])+'00:'
            elif key_press[i]==4:
                image_present=image_present+'000'+str(key_light[i])+'0:'
            elif key_press[i]==5:
                image_present=image_present+'0000'+str(key_light[i])+':'
        image_present=image_present[1:-1:]#去掉定义时的空格和最后的冒号
        #以上，完成生成一个此时的方块
        #然后其实我们关心最下面一层是什么
        
        music_image=Image(image_present)
        display.show(music_image)
        
        #按键反馈
        #如果奇数行按左，偶数行/空着按右
        #1.5秒没反应就miss
        reaction_start=running_time();
        while running_time()-reaction_start<1500:
            if button_a.is_pressed():
                button_press_a=1
                break
            if button_b.is_pressed():
                button_press_b=1
                break
            if pin0.is_touched():
                button_press_pin0=1
                break
            if pin1.is_touched():
                button_press_pin1=1
                break
        #写个循环把剩余按键时间卡住,按着就卡住
        while button_a.is_pressed() or button_b.is_pressed() or pin0.is_touched() or pin1.is_touched():
            press=1
            
        if (button_press_a==1 and key_press[4]%2==1 and key_light[4]==9)\
        or(button_press_b==1 and key_press[4]%2==0 and key_light[4]==9)\
        or (button_press_pin0==1 and key_press[4]%2==1 and key_light[4]==3)\
        or (button_press_pin0==1 and key_press[4]%2==0 and key_light[4]==3):
            score+=1
        
        #update
        button_press_a==0
        button_press_b==0
        button_press_pin0=0
        button_press_pin1=0
        key_press.pop(4)
        key_press.insert(0,random.randint(1,5))
        key_light.pop(4)
        key_light.insert(0,random.randint(0,1)*6+3)
        tune_count+=1
        
    display.scroll(get_GPA(score,len(tune),magic=True))



#part3
def Just_Dance():
    

    compass.calibrate()
    
    
    def get_movement(time):
        facing=compass.heading()
        lst=[]
        t=running_time()
        while running_time()-t<=time:
            deviate_facing=compass.heading()-facing
            lst.append((accelerometer.current_gesture(),deviate_facing))
            sleep(100)
        return lst
    
    
    
    def compare_movement(lst1,lst2):
        score=0
        for i in range(min(len(lst1),len(lst2))):
            angle_score=1-abs(lst1[i][1]-lst2[i][1])/360
            score+=angle_score
            if lst1[i][0]==lst2[i][0]:
                score+=2
        return score,i*3
    
    
    def start_game():
        music_list=['1.PYTHON']
        music_time=['12499']
        
        mu_str=' '.join(music_list)
        while not (button_a.is_pressed() and button_b.is_pressed()):
            display.scroll(mu_str,loop=False,delay=100,wait=True)
        display.scroll('choose one!',wait=True,loop=False)
        button_a.get_presses()
        button_b.get_presses()
        sleep(3000)
        choice=button_a.get_presses()
        music.play(eval('music'+music_list[choice-1][1:]),wait=False)
        
        lst1=get_movement(12499)
        
        display.show(Image.SMILE)
        while True:
            if button_a.is_pressed():
                break
        display.clear()
        sleep(500)
        music.play(eval('music'+music_list[choice-1][1:]),wait=False)
        
        lst2=get_movement(12499)
        
        AllScore=compare_movement(lst1,lst2)
        display.scroll(get_GPA(AllScore[0],AllScore[1],magic=True))


control_center()