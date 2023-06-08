# Your new file!
from microbit import *
from math import *
import time
import music
import speech
import random

#璃奈板

#歌曲部分
tunes=["A4:2","B4:2","C5:4","D5:2",'B4:4','A4:2','G4:8','R:4',
        'A4:2','B4:2','C5:2','A4:4','G4:2','G5:4','G5:2','D5:4','E5:2','D5:2','C5:2','R:4',
        'A4:2','B4:2','C5:2','A4:2','C5:2','D5:4','B4:2','A4:2','G4:6','R:6',
        'A4:2','B4:2','C5:2','A4:4','G4:4','D5:2','E5:2','D5:6','R:4',
        'C5:10','D5:2','E5:2','C5:2','D5:2','D5:2','D5:2','E5:2','D5:2','G4:4','R:4',
        'A4:2','B4:2','C5:2','A4:2','G4:1','R:1','D5:1','E5:2','D5:6','R:2'
        "G4:1","A4:1","C5:1","A4:1","E5:3","E5:3","D5:6",
        "G4:1","A4:1","C5:1","A4:1","D5:3","D5:3","C5:1","B4:1","A4:4",
        "G4:1","A4:1","C5:1","A4:1","C5:4","D5:2","B4:2","A4:2","G4:2","R:2","G4:2","D5:4","C5:4","R:4"
        "G4:1","A4:1","C5:1","A4:1","E5:3","E5:3","D5:6",
        "G4:1","A4:1","C5:1","A4:1","G5:4","B4:2","D5:6",
        "G4:1","A4:1","C5:1","A4:1","C5:4","D5:2","B4:2","A4:2","G4:2","R:2","G4:2","D5:4","C5:4","R:4"]
music.play(tunes)

#璃奈板表情设置
Image1 = Image("00000:"
                "09090:"
                "00000:"
                "90009:"
                "09990")
ImageX = Image("00000:"
                "09090:"
                "00000:"
                "09990:"
                "90009")
Image2 = Image("09090:"
                "00000:"
                "00900:"
                "09090:"
                "00900")
Image3 = Image("00000:"
                "99099:"
                "00000:"
                "90009:"
                "09990")
Image4 = Image("09090:"
                "00000:"
                "09990:"
                "09090:"
                "00900")
Image5 = Image("09009:"
                "09090:"
                "00009:"
                "09090:"
                "00900")
Image7 = Image("00000:"
                "09090:"
                "00000:"
                "99099:"
                "00000")
Image6 = Image("90009:"
                "09090:"
                "90009:"
                "00000:"
                "00000")
#通过随机数控制随机表情生成及时长
while True:
    i=random.randint(1,6)
    j=random.random()
    if i==1:
        display.show(Image1)
        time.sleep(j)
        display.show(Image7)
        time.sleep(j)
    if i==2:
        display.show(Image2)
        time.sleep(j)
    if i==3:
        display.show(Image3)
        time.sleep(j)
    if i==4:
        display.show(Image4)
        time.sleep(j)
    if i==5:
        display.show(Image5)
        time.sleep(j)
    if i==6:
        display.show(Image6)
        time.sleep(j)
        
        
        
#俄罗斯方块部分

# 判断移动操作是否合法
def no_conflict(lst, rec):
    for k in lst:
        i, j = k
        if rec[i][j] != 0:
            return False  # 冲突
    return True  # 不冲突


# 把一个俄罗斯方块显示出来
def show(lst, bri):
    for k in lst:
        i, j = k
        display.set_pixel(i, j, bri)


# 俄罗斯方块下移
def down(lst):
    max_line = max([k[1] for k in lst])
    if max_line < 4:
        lst = [(k[0], k[1] + 1) for k in lst]
    return lst


# 俄罗斯方块左移
def left(lst):
    min_col = min([k[0] for k in lst])
    if min_col > 0:
        lst = [(k[0] - 1, k[1]) for k in lst]
    return lst


# 俄罗斯方块右移
def right(lst):
    max_col = max([k[0] for k in lst])
    if max_col < 4:
        lst = [(k[0] + 1, k[1]) for k in lst]
    return lst


# 俄罗斯方块不能再下落时更改record
def modify(lst, rec):
    for k in lst:
        i, j = k
        rec[i][j] = 1


# 点亮某两个点
def light_up(lst):
    for k in lst:
        x, y = k
        display.set_pixel(x, y, 9)
    sleep(100)
    for k in lst:
        x, y = k
        display.set_pixel(x, y, 4)


# 六种备选俄罗斯方块
opptions = [[(2, 0)], [(2, 0), (3, 0)], [(2, 1), (3, 0)], [(2, 0), (3, 1)],
            [(2, 0), (2, 1), (3, 1)], [(3, 0), (2, 1), (3, 1)]]

# 开一个5*5表格记录每个点是否亮起
record = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# 点亮顺序的坐标
image = [(0, 0), (1, 0), (0, 1), (0, 2), (1, 1), (2, 0), (3, 0), (2, 1), (1, 2), (0, 3), (0, 4),
         (1, 3), (2, 2), (3, 1), (4, 0), (4, 1), (3, 2), (2, 3), (1, 4), (2, 4), (3, 3), (4, 2),
         (4, 3), (3, 4), (4, 4)]

# 数字-->英文
dic = {3: 'three', 6: 'six', 9: 'nine', 12: 'twelve', 15: 'fifteen', 18: 'eighteen', 21: 'twenty-one',
       25: 'twenty-five', 28: 'twenty-eight', 31: 'thirty-one', 34: 'thirty-four', 37: 'thirty-seven',
       40: 'forty', 43: 'forty-three', 47: 'forty-seven', 50: 'fifty', 53: 'fifty-three',
       56: 'fifty-six', 59: 'fifty-nine', 62: 'sixty-two', 65: 'sixty-five', 69: 'sixty-nine',
       72: 'seventy-two', 75: 'seventy-five', 78: 'seventy-eight'}

while True:
    # 1~4种生成概率较大，5~6种生成概率较小
    number = random.randint(1, 3)
    if number == 1:
        range = 6
    else:
        range = 4
    opption = opptions[0: range]
    tetris = random.choice(opption)
    color = random.randint(5, 9)
    show(tetris, color)
    sleep(1000)

    if not no_conflict(tetris, record):  # 不能再放置俄罗斯方块，游戏结束
        display.clear()
        display.scroll('Game Over', 100)
        fill = 0
        for times in [0, 0, 0]:  # 闪烁三次
            display.clear()
            sleep(500)
            for i in [0, 1, 2, 3, 4]:
                for j in [0, 1, 2, 3, 4]:
                    if record[i][j] != 0:
                        fill += 1
                        display.set_pixel(i, j, 9)
            sleep(500)

        display.clear()
        display.show(Image('44444:'
                           '44444:'
                           '44444:'
                           '44444:'
                           '44444'))
        stack = []
        for k in image:
            stack.append(k)
            if len(stack) == 3:
                stack.pop(0)
            light_up(stack)

        for times in [0, 0, 0]:
            display.show(Image('00000:'
                               '00000:'
                               '00900:'
                               '00000:'
                               '00000'))
            sleep(200)
            display.show(Image('00000:'
                               '09990:'
                               '09990:'
                               '09990:'
                               '00000'))
            sleep(200)
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))
            sleep(200)

        display.show(Image('06000:'
                           '69606:'
                           '06066:'
                           '00906:'
                           '00999'))

        money = int(fill // 3 * pi)
        if money == 50:
            display.clear()
            display.scroll('KFC! orz', 100)
            display.show(Image('04000:'
                               '49407:'
                               '04077:'
                               '00807:'
                               '00888'))
            music.set_tempo(bpm=280)
            music.play(['eb4:8', 'c4:4', 'c4:4', 'c4:8', 'c4:4', 'c4:4',
                        'c4:8', 'c4:8', 'c4:4', 'bb3:4', 'c4:4', 'd4:4'])
            music.play(['eb4:8', 'c4:4', 'c4:4', 'c4:8', 'c4:4', 'c4:4',
                        'bb3:4', 'c4:4', 'c4:8', 'g4:4', 'f4:4', 'eb4:4', 'f4:4'])
            speech.say('turn it up')
            sleep(400)
        speech.say('crazy Thursday v me %s.' % dic[money])
        break

    else:
        while True:
            times = 5
            while times > 0:
                if button_a.is_pressed() and no_conflict(left(tetris), record):
                    show(tetris, 0)
                    tetris = left(tetris)
                    show(tetris, color)
                if button_b.is_pressed() and no_conflict(right(tetris), record):
                    show(tetris, 0)
                    tetris = right(tetris)
                    show(tetris, color)
                times -= 1
                sleep(30)
            if no_conflict(down(tetris), record) and down(tetris) != tetris:  # 俄罗斯方块下移
                show(tetris, 0)
                tetris = down(tetris)
                show(tetris, color)
                sleep(1000)
            else:
                modify(tetris, record)  # 修改record，退出循环
                break
