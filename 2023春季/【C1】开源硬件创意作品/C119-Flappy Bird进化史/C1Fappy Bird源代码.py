from microbit import *
import random
import music
import speech

def generate():
    global level, index
    level = random.randint(0, 1)
    index = random.randint(0, level + 3)
    
def toString(level, index, cur):
    s = ''
    for i in range(5):
        s += ''.join(['0' if (x + cur != 4 or index <= i <= index - level + 1) else '8' for x in range(5)])
        if i != 4:
            s += ':'
    return s

speech.say("Welcome to Flappy Bird!")
sleep(1000)

def scroll(string):
    while True:
        for s in string:
            display.scroll(s)
            if button_a.was_pressed():
                return 'a'
            if button_b.was_pressed():
                return 'b'
def countdown(n):
    for i in range(n, -1, -1):
        display.show(i)
        sleep(1000)

first = True
while True:
    choice = scroll("PressBtoStart" if first else "PressBtoRestart")
    hp = 1
    if choice == 'a':
        hp = 0
        while True:
            if pin_logo.is_touched():
                hp += 1
            if button_a.was_pressed():
                break
            sleep(400)
        if hp == 0:
            hp = 23333333333333333
    countdown(3)
    first = False
    cur = 0
    score = 0
    generate()
    y = 2
    while True:
        screen = toString(level, index, cur)
        display.show(Image(screen))
        if y == -1 or y == 5 or screen[y * 6 + 1] == '8':
            hp -= 1
        y = max(min(y, 4), 0)
        if hp <= 0:
            if hp == 0:
                for i in range(3):
                    display.set_pixel(1, y, 9)
                    sleep(500)
                    display.set_pixel(1, y, 0)
                    sleep(500)
                music.play(music.POWER_DOWN)
                sleep(500)
            while True:
                scroll("score" + str(score))
                break
            break
        display.set_pixel(1, y % 5, 6)
        sleep(max(1000 - 100 * (score // 5), 200))
        if button_a.was_pressed():
            hp = -2333
        if button_b.was_pressed():
            y -= 1
        elif button_b.is_pressed():
            pass
        else:
            y += 1
        cur = (cur + 1) % 5
        if cur == 0:
            generate()
        if cur == 4:
            score += 1