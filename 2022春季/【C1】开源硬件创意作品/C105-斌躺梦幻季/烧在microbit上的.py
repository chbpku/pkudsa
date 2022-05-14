from microbit import *
from music import *
from random import *
import radio
import speech

radio.on()
radio.config(length=64,
             queue=10,
             channel=29,
             power=7,
             data_rate=radio.RATE_1MBIT) # initialze radio
uart.init(115200) # initialize serial port
def check_button_and_show():
    while True:
        if button_a.is_pressed():
            try:
        # on every received packet
                uart.write("a")
            except:
                continue
        elif button_b.is_pressed():
            try:
                uart.write("b")
            except:
                continue
        elif accelerometer.is_gesture("shake"):
            try:
                uart.write("c")
            except:
                continue
        elif button_a.is_pressed() and button_b.is_pressed():
            try:
                uart.write("d")
            except:
                continue
x = 2
y = 0
k = 0
t = 0
startpicture = Image("99099:90009:00000:90009:99099")



#可以根据实际的歌曲来做一些块，可以定义它们的形状，生成的位置以及移动的速度及方向。
note1 = [[9,9,9],[0,0,9],[0,0,9]]
note2 = [[9,9,9]]
note3 = [[9,0],[9,0]]
note4=[[9],[9],[9]]
note5=[[9,9],[9,9]]
note6=[[9]]

note_lst1 = [note1, note2, note3]
note_lst2=[note1, note2,note3,note4,note6,note6, note2,note3,note4,note6,note5,note1, note2, note3,note4,note5,note1, note2, note3,note4,note5, note2,note3,note4]
spawnPos_lst = [[2,0],[2,0],[1,0]]
speed_lst = [[0,1],[0,1],[1,1]]


#用来绘制一帧。
def draw_note(note):
    global x, y
    display.clear()
    r = len(note)
    c = len(note[0])
    for i in range(r):
        for j in range(c):
            if -1<x-c+1+j<5 and -1<y-r+1+i<5:
                display.set_pixel(x-c+1+j, y-r+1+i, note[i][j])

#根据块的尺寸来随机生成块的位置，在zen mode里用到。
def random_spawn(note):
    global x
    c = len(note[0])
    x = randint(c-1,4)



#此处的both和shake是为了后面check_bottom里描述之便
def both():
    return button_a.is_pressed() and button_b.is_pressed
def shake():
    return accelerometer.is_gesture('shake')




#根据底端五个灯珠的亮起方式来决定玩家如何做出反应，具体是：仅亮一个灯，且此灯是第一个或第二个，玩家的响应方式是摁a键，若此灯是第四个或第五个，相应方式是摁b键，若此灯是中间一个，玩家应按电容键；
#亮起两个灯，玩家同时按a、b键；
#亮其三个灯，玩家摇动microbit。
def check_bottom():
    bottom = [1 if display.get_pixel(i, 4) != 0 else 0 for i in range(5)]
    #print(bottom)
    if bottom.count(1) == 0:
        return 0
    elif bottom.count(1) == 1:
        if bottom.index(1) < 2:
            return button_a.is_pressed
        elif bottom.index(1) == 2:
            return pin_logo.is_touched
        else:
            return button_b.is_pressed
    elif bottom.count(1) == 2:
        return both
    else:
        return shake



#在设定好的位置生成，并按设定好的速度移动。
def spawn_note(pos):
    global x, y
    x = pos[0]
    y = pos[1]
def move(speed):
    global x, y
    x += speed[0]
    y += speed[1]



#定义一些变量
gameOn = True
zenMode = True
zenScore = 0
challengeMode = True
display.scroll("Press A for zen mode, B for challenge mode, A and B to quit.", delay = 65)



#玩家在这个循环内选定游戏模式
while True:
    sleep(100)
    display.show(startpicture)
    if pin_logo.is_touched():
        display.scroll("Good bye!")
        gameOn = False
        break
    elif button_a.is_pressed():
        display.scroll("zen mode")
        zenMode = True
        challengeMode = False
        break
    elif button_b.is_pressed():
        display.scroll("challenge mode")
        print(2)
        challengeMode = True
        zenMode = False
        break

display.clear()

note = choice(note_lst1)
random_spawn(note)
aflag=False
bflag=False
cflag=False
dflag=False

#这个是最主要的循环
while gameOn:
    if zenMode:#无尽模式，随机生成，玩家若不失误则游戏一直进行
        sleep(25)#调节sleep的时间来控制移动的快慢
        t += 1
        if t == 40:
            t = 0
            if y < 5 + len(note):
                y += 1
                draw_note(note)
                check_button_and_show()

            else:
                print(str(zenScore))
                y = 0
                note = choice(note_lst)
                random_spawn(note)
                draw_note(note)

            if check_bottom() != 0:
                tp = 0
                while tp < 15:
                    sleep(25)
                    tp += 1
                    if check_bottom()():
                        zenScore += 1
                        break
                else:
                    gameOn = False
                    display.clear()
                    display.scroll("Game over! Your score is: ")
                    for i in range(5):
                        display.clear()
                        sleep(500)
                        display.show(zenScore)
                    display.clear()

    elif challengeMode:#challenge mode
        sleep(25)
        t += 1
        #display.scroll("shake!")
        if t==20 and not aflag:#先进入第一个循环
            display.scroll("cb's show time!")
            print("\n")
            print("٩(｡・ω・｡)و")
            print("\n")
            print("\n")
            print("\n")
            speech.say("c b s show time")
            print("\n")
            print("<(￣︶￣)>")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("please shake")
            print("\n")
            print("\n")
            print("\n")
            start=running_time()
            while True and not aflag:

                now_time=running_time()
                if now_time-start>1000*25:#前25s通过shake来？？？画折线图 体现mu的优势
                    break
                check_button_and_show()
                if accelerometer.was_gesture("shake"):
                    print(accelerometer.get_values())
            aflag=True
        if t == 40 and not bflag and aflag: #25s后的 3s note 在 note_lst1里面 很可能有下标写错的地方））））
            display.clear()
            t = 0
            if y < 5 + len(note_lst1[k]) and x < 5 + len(note_lst1[k][0]):
                draw_note(note_lst1[k])
                move(speed_lst[k])
            else:
                y = 0
                k += 1
                if k < len(note_lst1):
                    spawn_note(spawnPos_lst[k])
                    draw_note(note_lst1[k])
                    t = 0
                else:
                    display.clear()
                    display.show(Image.HAPPY)
                    sleep(500)
                    bflag=True
                    display.clear()
            if check_bottom() != 0:
                tp = 0
                while tp < 15:
                    sleep(50)
                    tp += 1
                    if check_bottom()():
                        break
                else:
                    gameOn = False
                    display.clear()
                    display.scroll("You lose!")
        if t==20 and bflag and aflag and (not cflag): #下一个循环 大概12s 比较快 用notelst2
            k=0
            t=0
            if y < 5 + len(note_lst2[k]) and x < 5 + len(note_lst2[k][0]):
                draw_note(note_lst2[k])
                move(speed_lst[k])
            else:
                y = 0
                k += 1
                if k < len(note_lst2):
                    spawn_note(spawnPos_lst[k])
                    draw_note(note_lst2[k])
                    t = 0
                else:
                    display.clear()
                    display.show(Image.RABBIT)
                    sleep(500)
                    cflag=True
                    display.clear()

            if check_bottom() != 0:
                tp = 0
                while tp < 15:
                    sleep(50)
                    tp += 1
                    if check_bottom()():
                        break
                else:
                    gameOn = False
                    display.clear()
                    display.scroll("You lose!")
        if t==40 and cflag and aflag and bflag and (not dflag): #这个也应该是用1的Note 但是我好像里面有写错成Notelist的地方 而且还不少
            t = 0
            if y < 5 + len(note_lst1[k]) and x < 5 + len(note_lst1[k][0]):
                draw_note(note_lst[k])
                move(speed_lst[k])
            else:
                y = 0
                k += 1
                if k < len(note_lst1):
                    spawn_note(spawnPos_lst[k])
                    draw_note(note_lst1[k])
                    t = 0
                else:
                    display.clear()
                    display.show(Image.HAPPY)
                    sleep(500)
                    dflag=True
                    display.clear()
            if check_bottom() != 0:
                tp = 0
                while tp < 15:
                    sleep(50)
                    tp += 1
                    if check_bottom()():
                        break
                else:
                    gameOn = False
                    display.clear()
                    display.scroll("You lost!")
        if aflag and bflag and cflag and dflag: #放空 尽管如此我还是准备实现一下和pgzrun联动的彩蛋 彩蛋在"彩蛋.py"里面 我重新写了
            #彩蛋模式（？
            print("Congrats!!")
            print("\n")
            display.show(Image(
            "09090:"
            "90909:"
            "90009:"
            "90009:"
            "99999"))
            speech.say("meow")
            check_button_and_show()#隐藏剧情就是同时按ab（虽然这个设定很愚蠢
            while button_a.is_pressed():
                print(accelerometer.get_values())
            else:
                gameOn=False
