from microbit import *
#############################
#INVERSE
#关卡：一个嵌套列表，列表的每一个元素是从上往下的行，每一个元素的元素是行内从左到右的组件
#空地——0；终点——3；球——6；墙体——9
#当前位置：一个含两个元素的列表
#standard：倾斜角度的标准值，可调
#level_index：当前关卡
#############################
standard = 300
level_index = 0
#清空函数，清空屏幕
def clear():
    display.show(Image("00000:00000:00000:00000:00000"))
#展示函数，输入一个关卡列表和当前位置，在屏幕上展示当前的状况
def present(input_level, input_current_position):
    current_map = []
    for row in input_level:
        current_map.append([])
        for number in row:
            current_map[-1].append(number)
    current_map[input_current_position[0]][input_current_position[1]] = 6
    y = input_current_position[0]
    x = input_current_position[1]
    if x <= 1:
        x = 2
    if x >= len(current_map[0]) - 2:
        x = len(current_map[0]) - 3
    if y <= 1:
        y = 2
    if y >= len(current_map) - 2:
        y = len(current_map) - 3
    image = "".join(map(str,current_map[y - 2][x - 2:x + 3])) + ":" +\
            "".join(map(str,current_map[y - 1][x - 2:x + 3])) + ":" +\
            "".join(map(str,current_map[y][x - 2:x + 3])) + ":" +\
            "".join(map(str,current_map[y + 1][x - 2:x + 3])) + ":" +\
            "".join(map(str,current_map[y + 2][x - 2:x + 3]))
    display.show(Image(image))
    return

#移动函数，当倾斜方向没有墙体或不是边缘时移动，可反转
def move(inversed):
    if inversed == 0:
        if current_position[0] < len(level) - 1 and \
           level[current_position[0] + 1][current_position[1]] != 9:
            current_position[0] = current_position[0] + 1
        if standard <= accelerometer.get_x():
            if current_position[1] < len(level[0]) - 1 and \
               level[current_position[0]][current_position[1] + 1] != 9:
                current_position[1] = current_position[1] + 1
        elif accelerometer.get_x() <= -standard:
            if current_position[1] > 0 and \
               level[current_position[0]][current_position[1] - 1] != 9:
                current_position[1] = current_position[1] - 1
    else:
        if current_position[0] > 0 and \
           level[current_position[0] - 1][current_position[1]] != 9:
            current_position[0] = current_position[0] - 1
        if -standard >= accelerometer.get_x():
            if current_position[1] < len(level[0]) - 1 and \
               level[current_position[0]][current_position[1] + 1] != 9:
                current_position[1] = current_position[1] + 1
        elif accelerometer.get_x() >= standard:
            if current_position[1] > 0 and \
               level[current_position[0]][current_position[1] - 1] != 9:
                current_position[1] = current_position[1] - 1
    sleep(300)
    present(level, current_position)
#反转函数，反转关卡内的墙体和空地
def inverse():
    for row_index in range(len(level)):
        for column_index in range(len(level[0])):
            if level[row_index][column_index] == 0:
                level[row_index][column_index] = 9
            elif level[row_index][column_index] == 9:
                level[row_index][column_index] = 0
#颠倒函数，颠倒关卡的上下
def invert():
    global level
    global current_position
    global destination
    level = level[::-1]
    destination[0] = len(level) - 1 - destination[0]
    current_position[0] = len(level) - 1 - current_position[0]
#过关时展示过关动画，关卡+1
def win():
    global level_index
    level_index = level_index + 1
    display.show(Image.YES)
    sleep(1000)
    clear()
    sleep(1000)
#bug函数，展示bug动画
def bug():
    display.show(Image("99909:09990:90009:99090:90999"))
    sleep(100)
    display.show(Image("00099:90999:99000:99099:00090"))
    sleep(300)
    display.show(Image("90099:00090:99909:09909:90990"))
    sleep(100)
    display.show(Image("99909:09990:90009:99090:90999"))
    sleep(300)
    display.show(Image("99909:09990:90009:99090:90999"))
    sleep(200)
    display.show(Image("00099:90999:99000:99099:00090"))
    sleep(300)
    display.show(Image("90099:00090:99909:09909:90990"))
    sleep(200)
    display.show(Image("99909:09990:90009:99090:90999"))
    sleep(400)
    
#标题
display.scroll("INVERSE")
sleep(1000)

#教程：反转
while True:
    if button_a.is_pressed():
        break
    display.show(Image("00900:09000:99999:09000:00900"))
display.show(Image("22722:27222:77777:27222:22722"))
sleep(200)
display.show(Image("44644:46444:66666:46444:44644"))
sleep(200)
display.show(Image("66466:64666:44444:64666:66466"))
sleep(200)
display.show(Image("77277:72777:22222:72777:77277"))
sleep(200)
display.show(Image("99099:90999:00000:90999:99099"))
sleep(1000)
clear()
sleep(1500)
while True:
    if button_b.is_pressed():
        break
    display.show(Image("00900:00090:99999:00090:00900"))
display.show(Image("00000:00990:99999:00990:00000"))
sleep(200)
display.show(Image("00000:00000:99999:00000:00000"))
sleep(200)
display.show(Image("00000:00990:99999:00990:00000"))
sleep(200)
display.show(Image("00900:00090:99999:00090:00900"))
sleep(1000)
clear()
sleep(2000)

#正式开始游戏，第一轮
while True:
    if level_index == 0:
        level = [[0,0,0,0,0],[0,0,0,0,0],[0,0,3,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        current_position = [4,0]
        destination = [2,2]
    if level_index == 1:
        level = [[0,0,3,0,0],[0,0,0,0,0],[9,9,9,9,9],[0,0,0,0,0],[0,0,0,0,0]]
        current_position = [4,2]
        destination = [0,2]
    if level_index == 2:
        level = [[0,0,0,0,0,0,0,0,0,0,0,0,0],\
                 [0,9,9,9,9,9,9,9,9,9,9,9,0],\
                 [0,9,0,0,0,0,0,0,0,0,0,9,0],\
                 [0,9,0,9,9,9,9,9,9,9,0,9,0],\
                 [0,9,0,9,0,0,0,0,0,9,0,9,0],\
                 [0,9,0,9,0,9,9,9,0,9,0,9,0],\
                 [0,9,0,9,0,9,3,9,0,9,0,9,0],\
                 [0,9,0,9,0,9,9,9,0,9,0,9,0],\
                 [0,9,0,9,0,0,0,0,0,9,0,9,0],\
                 [0,9,0,9,9,9,9,9,9,9,0,9,0],\
                 [0,9,0,0,0,0,0,0,0,0,0,9,0],\
                 [0,9,9,9,9,9,9,9,9,9,9,9,0],\
                 [0,0,0,0,0,0,0,0,0,0,0,0,0]]
        current_position = [0,0]
        destination = [6,6]
    if level_index == 3:
        level = [[0,0,0,9,0,0,9,0,0,0,0,9,0,9,0],\
                 [0,9,9,9,0,0,9,9,9,9,0,9,0,0,0],\
                 [0,9,9,0,0,9,9,0,9,0,0,0,0,9,9],\
                 [0,0,0,0,0,0,0,0,9,0,9,0,0,9,0],\
                 [9,9,0,9,9,9,0,9,9,0,9,9,0,9,0],\
                 [9,9,0,9,9,0,0,9,0,0,0,9,0,9,0],\
                 [0,0,0,9,0,0,9,9,0,9,0,9,0,9,0],\
                 [0,9,9,9,0,9,9,0,0,9,0,0,0,9,0],\
                 [0,9,9,9,0,9,0,0,9,9,9,0,9,9,0],\
                 [0,0,0,0,0,9,0,9,9,9,9,0,9,0,0],\
                 [9,9,9,9,0,9,0,0,0,0,9,0,0,0,9],\
                 [9,9,9,0,0,9,9,9,9,0,9,0,9,0,0],\
                 [0,0,0,0,9,9,0,0,0,0,9,0,9,0,9],\
                 [0,9,9,9,9,9,0,9,9,0,9,9,9,0,0],\
                 [0,0,0,0,9,0,0,9,9,0,0,3,9,9,0]]
        current_position = [0,2]
        destination = [14,11]
    if level_index == 4:
        level = [[3,0,9,9,0],\
                 [0,9,0,9,0],\
                 [9,0,0,9,0],\
                 [9,9,9,9,9],\
                 [0,0,0,9,0]]
        current_position = [4,4]
        destination = [0,0]
    if level_index == 5:
        level = [[0,9,0,0,9,0,9,9,9,9,0,9,0,0,0,0,9,9,9,0,0,0,0,0,9,0,0,0,9,0,9,9,9,9,0],\
                 [0,9,0,0,9,0,9,0,0,0,0,9,0,0,0,0,9,0,0,9,0,0,0,0,9,9,0,9,9,0,9,0,0,0,0],\
                 [0,9,9,9,9,0,9,9,9,0,0,9,0,0,0,0,9,9,9,0,0,0,0,0,9,0,9,0,9,0,9,9,9,0,3],\
                 [0,9,0,0,9,0,9,0,0,0,0,9,0,0,0,0,9,0,0,0,0,0,0,0,9,0,0,0,9,0,9,0,0,0,0],\
                 [0,9,0,0,9,0,9,9,9,9,0,9,9,9,9,0,9,0,0,0,0,0,0,0,9,0,0,0,9,0,9,9,9,9,0]]
        current_position = [2,0]
        destination = [2,34]
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    if level_index == 6:
        level = [[0,9,0,0,9,0,9,9,9,9,0,9,0,0,0,0,9,9,9,0,0,0,0,0,9,0,9,9,9,9,9,9,9,9,9],\
                 [0,9,0,0,9,0,9,0,0,0,0,9,0,0,0,0,9,0,0,9,0,0,0,0,9,9,9,9,9,9,9,9,9,9,9],\
                 [0,9,9,9,9,0,9,9,9,0,0,9,0,0,0,0,9,9,9,0,0,0,0,0,9,0,9,9,9,9,9,9,9,9,3],\
                 [0,9,0,0,9,0,9,0,0,0,0,9,0,0,0,0,9,0,0,0,0,0,0,0,9,0,9,9,9,9,9,9,9,9,9],\
                 [0,9,0,0,9,0,9,9,9,9,0,9,9,9,9,0,9,0,0,0,0,0,0,0,9,0,9,9,9,9,9,9,9,9,9]]
        current_position = [2,0]
        destination = [2,34]
    if level_index == 7:
        level = [[0,9,0,0,9,0,9,9,9,9,0,9,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],\
                 [0,9,0,0,9,0,9,0,0,0,0,9,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],\
                 [0,9,9,9,9,0,9,9,9,0,0,9,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,3],\
                 [0,9,0,0,9,0,9,0,0,0,0,9,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],\
                 [0,9,0,0,9,0,9,9,9,9,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]]
        current_position = [2,0]
        destination = [2,34]
    if level_index == 8:
        level = [[0,0,0,0,0],\
                 [0,0,0,0,0],\
                 [0,0,0,0,0],\
                 [0,0,0,0,0],\
                 [0,0,0,0,0]]
        current_position = [2,2]
        destination = [-1,-1]
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    display.show(level_index)
    sleep(1000)
    clear()
    start_time = running_time()
    while True:
        present(level, current_position)
        #第八关没有过关条件，到达10秒后直接进剧情
        if level_index == 8 and running_time() >= start_time + 10000:
            break
        if current_position == destination:
            break
        elif button_a.was_pressed():
            inverse()
        elif button_b.was_pressed():
            invert()
        else:
            move(0)
    if level_index == 8:
        break
    win()
#第八关结束后，播放bug动画，进入第二轮
display.show(Image("99999:99999:99999:99999:99999"))
sleep(1000)
clear()
sleep(500)
display.show(Image("99999:99999:99999:99999:99999"))
sleep(800)
bug()
bug()
display.show(Image("99999:99999:99999:99999:99999"))
sleep(3000)
clear()
sleep(5000)

#第二轮教程开始，左右、上下、按钮反转
display.scroll("ESREVNI")
sleep(1000)
while True:
    if button_b.is_pressed():
        break
    display.show(Image("00900:09000:99999:09000:00900"))
display.show(Image("22722:27222:77777:27222:22722"))
sleep(200)
display.show(Image("44644:46444:66666:46444:44644"))
sleep(200)
display.show(Image("66466:64666:44444:64666:66466"))
sleep(200)
display.show(Image("77277:72777:22222:72777:77277"))
sleep(200)
display.show(Image("99099:90999:00000:90999:99099"))
sleep(1000)
clear()
sleep(1500)
while True:
    if button_a.is_pressed():
        break
    display.show(Image("00900:00090:99999:00090:00900"))
display.show(Image("00000:00990:99999:00990:00000"))
sleep(200)
display.show(Image("00000:00000:99999:00000:00000"))
sleep(200)
display.show(Image("00000:00990:99999:00990:00000"))
sleep(200)
display.show(Image("00900:00090:99999:00090:00900"))
sleep(1000)
clear()
sleep(2000)
level_index = 0

#第二轮游戏开始
while True:
    if level_index == 0:
        level = [[0,0,0,0,0],[0,0,0,0,0],[0,0,3,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        current_position = [4,0]
        destination = [2,2]
    if level_index == 1:
        level = [[0,0,3,0,0],[0,0,0,0,0],[9,9,9,9,9],[0,0,0,0,0],[0,0,0,0,0]]
        current_position = [4,2]
        destination = [0,2]
    if level_index == 2:
        level = [[0,0,9,3,0,9,0],[0,9,9,9,0,9,0],[0,0,0,9,0,0,0],[0,9,0,0,9,0,9],[0,0,9,0,9,0,0],[9,0,9,0,9,9,0],[9,0,0,0,9,0,0]]
        current_position = [6,5]
        destination = [0,3]
    if level_index == 3:
        level = [[0,0,0,9,0,0,9,0,0,0,0,9,0,9,0],\
                 [0,9,9,9,0,0,9,9,9,9,0,9,0,0,0],\
                 [0,9,9,0,0,9,9,0,9,0,0,0,0,9,9],\
                 [0,0,0,0,0,0,0,0,9,0,9,0,0,9,0],\
                 [9,9,0,9,9,9,0,9,9,0,9,9,0,9,0],\
                 [9,9,0,9,9,0,0,9,0,0,0,9,0,9,0],\
                 [0,0,0,9,0,0,9,9,0,9,0,9,0,9,0],\
                 [0,9,9,9,0,9,9,0,0,9,0,0,0,9,0],\
                 [0,9,9,9,0,9,0,0,9,9,9,0,9,9,0],\
                 [0,0,0,0,0,9,0,9,9,9,9,0,9,0,0],\
                 [9,9,9,9,0,9,0,0,0,0,9,0,0,0,9],\
                 [9,9,9,0,0,9,9,9,9,0,9,0,9,0,0],\
                 [0,0,0,0,9,9,0,0,0,0,9,0,9,0,9],\
                 [0,9,9,9,9,9,0,9,9,0,9,9,9,0,0],\
                 [0,0,0,0,9,0,0,9,9,0,0,3,9,9,0]]
        current_position = [0,2]
        destination = [14,11]
    if level_index == 4:
        level = [[9,0,0,0,9],\
                 [0,9,0,9,0],\
                 [0,0,9,0,0],\
                 [0,9,0,9,0],\
                 [9,0,3,0,9]]
        current_position = [0,2]
        destination = [4,2]
    display.show(level_index)
    sleep(1000)
    clear()
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    while True:
        present(level, current_position)
        if current_position == destination:
            break
        elif button_a.was_pressed():
            invert()
        elif button_b.was_pressed():
            inverse()
        else:
            move(1)
    if level_index == 3:
        clear()
        sleep(2000)
        bug()
        clear()
        sleep(1500)
    if level_index == 4:
        display.show(Image.SAD)
        sleep(2000)
        clear()
        break
    win()
    
#进入第三轮
sleep(10000)
display.scroll("INVERSE")
sleep(5000)
display.show(Image("99999:99999:99999:99999:99999"))
sleep(1500)
for _ in range(3):
    bug()
clear()
sleep(3000)
display.scroll("INVERSE")
sleep(5000)
#1
display.scroll("HELP ME")
display.show(1)
sleep(1000)
duration = 0
while True:
    if microphone.sound_level() < 20:
        duration = 0
        clear()
    elif microphone.sound_level() < 50:
        duration = 0
        display.show(Image("00000:00000:00900:00000:00000"))
    elif microphone.sound_level() < 80:
        duration = 0
        display.show(Image("00000:09990:09990:09990:00000"))
    else:
        duration = duration + 1
        display.show(Image("99999:99999:99999:99999:99999"))
        sleep(100)
    if duration >= 15:
        break
clear()
sleep(1000)
display.show(Image.YES)
sleep(1000)
clear()
sleep(3000)
sound_list = []
duration = 0
while True:
    if microphone.sound_level() < 30:
        if 1 < duration <= 10:
            sound_list.append(0)
        elif duration > 10:
            sound_list.append(1)
        clear()
        duration = 0
    else:
        duration = duration + 1
        if 1 < duration <= 10:
            display.show(Image("00000:00000:00900:00000:00000"))
        elif duration > 10:
            display.show(Image("00000:00000:99999:00000:00000"))
        sleep(100)
    if sound_list[-9:] == [0,0,0,1,1,1,0,0,0]:
        break
sleep(1000)
display.show(Image.YES)
sleep(1000)
clear()
sleep(3000)
#2
display.scroll("Before I played this game")
sleep(2000)
display.show(2)
sleep(1000)
while True:
    if button_a.is_pressed():
        break
    display.show(Image("00900:09000:99999:09000:00900"))
display.show(Image("22722:27222:77777:27222:22722"))
sleep(200)
display.show(Image("44644:46444:66666:46444:44644"))
sleep(200)
display.show(Image("66466:64666:44444:64666:66466"))
sleep(200)
display.show(Image("77277:72777:22222:72777:77277"))
sleep(200)
display.show(Image("99099:90999:00000:90999:99099"))
sleep(1000)
clear()
sleep(1500)
while True:
    if button_b.is_pressed():
        break
    display.show(Image("00900:00090:99999:00090:00900"))
display.show(Image("00000:00990:99999:00990:00000"))
sleep(200)
display.show(Image("00000:00000:99999:00000:00000"))
sleep(200)
display.show(Image("00000:00990:99999:00990:00000"))
sleep(200)
display.show(Image("00900:00090:99999:00090:00900"))
sleep(1000)
clear()
sleep(3000)
#3
display.scroll("a man was trapped in it")
display.show(3)
sleep(1000)
b = button_b.was_pressed()
level = [[0,0,9,9,9,0,0],[0,9,0,0,0,9,0],[0,9,3,0,0,0,0],[0,9,9,9,9,9,0],[0,9,9,9,9,9,0],[0,9,9,9,9,9,0],[0,0,0,0,0,0,0]]
current_position = [6,3]
destination = [2,2]
while True:
    present(level, current_position)
    if current_position == destination:
        break
    elif button_b.was_pressed():
        invert()
    else:
        move(0)
display.show(Image("09990:90009:96000:99999:99999"))
sleep(2000)
display.show(Image("09990:90009:96009:99999:99999"))
sleep(5000)
clear()
sleep(3000)
display.scroll("...and he deceived me")

display.show(4)
sleep(2000)
display.show(Image.SAD)
sleep(2000)
display.show(5)
sleep(1000)
display.show(Image.SAD)
sleep(1000)
display.show(6)
sleep(800)
display.show(Image.SAD)
sleep(800)
display.show(7)
sleep(500)
display.show(Image.SAD)
sleep(500)
display.show(8)
sleep(300)
display.show(Image.SAD)
sleep(300)
display.show(9)
sleep(100)
display.show(Image.SAD)
sleep(100)
clear()
sleep(3000)

while True:
    if pin_logo.is_touched():
        break
    else:
        display.show(Image("00900:00900:90909:09990:00900"))
clear()
sleep(1000)
display.scroll("I took his place.")
sleep(2000)
while True:
    if button_a.is_pressed():
        break
    display.show(Image.STICKFIGURE)
display.show(Image("99099:00000:99099:90909:09990"))
sleep(2000)
clear()
sleep(1000)
while True:
    if button_b.is_pressed():
        break
    display.show(Image.YES)
display.show(Image.NO)
sleep(2000)
clear()
sleep(1000)
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        break
    display.show(Image.HAPPY)
display.show(Image.SAD)
sleep(2000)
clear()
sleep(5000)
display.show("AND NOW YOU TAKE MINE",delay = 200)
a = button_a.was_pressed()
b = button_b.was_pressed()
level = [[9,9,0,9,9],[9,9,0,9,9],[9,9,0,9,9],[9,9,0,9,9],[9,9,3,9,9]]
current_position = [0,2]
destination = [4,2]
while True:
    present(level, current_position)
    if current_position == destination:
        clear()
        sleep(2000)
        display.show(Image("99099:00000:99099:90909:09990"))
        sleep(2000)
        display.show(Image("77277:22222:77277:72727:27772"))
        sleep(200)
        display.show(Image("66466:44444:66466:64646:46664"))
        sleep(200)
        display.show(Image("44644:66666:44644:46464:64446"))
        sleep(200)
        display.show(Image("22722:77777:22722:27272:72227"))
        sleep(200)
        display.show(Image("00900:99999:00900:09090:90009"))
        sleep(3000)
        clear()
        sleep(2000)
        display.scroll("ENDING:INVERSED")
        break
    elif current_position[0] == destination[0]:
        clear()
        sleep(3000)
        level = [[0,9,9,9,0,0],[9,0,0,0,9,0],[9,0,0,0,0,3],[9,9,9,9,9,0],[9,9,9,9,9,0]]
        current_position = [2,1]
        while True:
            present(level, current_position)
            if current_position[1] == 5:
                break
            else:
                move(0)
        display.scroll("ENDING:ESCAPED")
        sleep(2000)
        display.scroll("...TEMPORARILY")
        break
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(Image("99999:99999:99999:99999:99999"))
        sleep(5000)
        for _ in range(3):
            for i in range(0,10):
                line = [9 - i] * 5
                line = "".join(map(str,line))
                image = [line] * 5
                image = ":".join(image)
                display.show(Image(image))
                sleep(200)
        for _ in range(3):
            bug()
        display.show(Image("99999:99999:99999:99999:99999"))
        sleep(2000)
        clear()
        sleep(300)
        display.show(Image("99999:99999:99999:99999:99999"))
        sleep(200)
        display.show(Image("00000:99999:99999:99999:00000"))
        sleep(200)
        display.show(Image("00000:00000:99999:00000:00000"))
        sleep(200)
        display.show(Image("00000:00900:09990:00900:00000"))
        sleep(200)
        display.show(Image("00900:00900:00900:00900:00900"))
        sleep(200)
        display.show(Image("00000:00900:00900:00900:00000"))
        sleep(200)
        display.show(Image("00000:00000:00900:00000:00000"))
        sleep(200)
        clear()
        sleep(5000)
        display.scroll("ENDING:SUBVERT")
        break
    elif button_a.was_pressed():
        inverse()
    elif button_b.was_pressed():
        invert()
    else:
        move(0)