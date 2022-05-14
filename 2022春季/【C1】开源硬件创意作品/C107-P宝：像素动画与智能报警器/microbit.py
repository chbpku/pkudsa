from microbit import *
import time
import music

# DDL警报器 
display.show(Image.HAPPY)
time.sleep(2)
time_left = 15
while time_left >= 10:
    time.sleep(1)
    time_left -= 1
    while time_left % 10 == 0:
        display.scroll('%d' % time_left)
        time.sleep(1)
        time_left -= 1
while time_left > 0:
    display.show('%d' % time_left)
    time.sleep(0.5)
    display.show(Image.SAD)
    time.sleep(0.5)
    time_left -= 1
display.show(Image.ASLEEP)


# 摸鱼，疯狂星期四警报器（简单更改时间即可）
def alarm(hours, minutes=0):
    display.show(Image.CONFUSED)
    time_left = hours * 3600 + minutes * 60
    while time_left > 0:
        time.sleep(1)
        time_left -= 1
    while True:
        music.play(music.JUMP_UP)


alarm(17, 30)

# 跳动的心
while True:
    display.show(Image.HEART)
    time.sleep(0.5)
    display.show(Image.HEART_SMALL)
    time.sleep(0.5)
# 早八警报器
while True:
    if display.read_light_level() > 1:
        display.show(Image.SKULL)
        music.play(music.POWER_DOWN)
    time.sleep(0.1)

# 芭蕾像素图
Image1 = Image("90900:"
               "09999:"
               "00990:"
               "00909:"
               "00900")

Image2 = Image("00909:"
               "99990:"
               "09900:"
               "90900:"
               "00900")

Image3 = Image("90909:"
               "09990:"
               "00900:"
               "09090:"
               "90009")

Image4 = Image("00900:"
               "99999:"
               "00900:"
               "09090:"
               "90090")

Image5 = Image("00009:"
               "00999:"
               "00009:"
               "99990:"
               "00000")

Image6 = Image("00900:"
               "99999:"
               "00900:"
               "00900:"
               "00900")

Image7 = Image("90000:"
               "99900:"
               "90000:"
               "09999:"
               "00000")

Image8 = Image("00900:"
               "99999:"
               "00900:"
               "09090:"
               "09009")

Image9 = Image("00009:"
               "00999:"
               "00009:"
               "00090:"
               "00900")
Image10 = Image("90000:"
                "99900:"
                "90000:"
                "09000:"
                "00900")

# 单人芭蕾
while True:
    display.show(Image6)
    time.sleep(2)
    for i in range(4):
        display.show(Image1)
        time.sleep(0.7)
        display.show(Image2)
        time.sleep(0.7)
    display.show(Image3)
    time.sleep(5)

# 双人芭蕾（另一个单片机基本对称）
while True:
    display.show(Image4)
    time.sleep(2)
    display.show(Image5)
    time.sleep(2)
    display.show(Image9)
    time.sleep(4)

# 奔跑者系列图（代码重复度高，略去）
image1 = Image("00090:"
               "09999:"
               "00090:"
               "00909:"
               "09009")

image2 = Image("00000:"
               "09009:"
               "99909:"
               "09090:"
               "90900")

image3 = Image("90000:"
               "90000:"
               "09000:"
               "09900:"
               "09090")

image4 = Image("00000:"
               "00000:"
               "00000:"
               "00000:"
               "00000")

image5 = Image("00009:"
               "00999:"
               "00009:"
               "00090:"
               "00900")

image6 = Image("00000:"
               "90000:"
               "00000:"
               "90000:"
               "90000")

image7 = Image("90000:"
               "99000:"
               "90000:"
               "09000:"
               "09000")

image8 = Image("00000:"
               "00099:"
               "00000:"
               "00009:"
               "00090")

image9 = Image("09000:"
               "99900:"
               "09000:"
               "90900:"
               "00900")

image10 = Image("00000:"
                "00009:"
                "00000:"
                "00000:"
                "00009")
