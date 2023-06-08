from microbit import *
from random import randint
from time import *
import music


def pixelFlash(loc):
    y, x = loc
    origin = display.get_pixel(x, y)
    display.set_pixel(x, y, (origin - 5) % 9)
    sleep_ms(200)
    display.set_pixel(x, y, origin)
    sleep_ms(200)


def imageGenerator():
    module = [str(randint(0, 1) * 9) for i in range(15)]
    wrong = [randint(0, 4), randint(0, 1) + randint(0, 1) * 3]
    image = []
    for i in range(5):
        row = module[3 * i:3 * i + 3]
        row.extend(row[-2::-1])
        if i == wrong[0]:
            if row[wrong[1]] == '9':
                row[wrong[1]] = "0"
            else:
                row[wrong[1]] = "9"
                wrong[1] = 4 - wrong[1]

        image.append(''.join(row))
    image = ':'.join(image)
    return (image, wrong)


def maingame(timelimit):
    image, wrong = imageGenerator()
    display.show(Image(image))
    display.set_pixel(wrong[1], wrong[0], 0)
    cursor = [0, 0]

    deadline = ticks_add(ticks_ms(), timelimit)
    while ticks_diff(deadline, ticks_ms()) > 0:
        print("剩余时间：", ticks_diff(deadline, ticks_ms()) / 1000, "s")
        if button_a.was_pressed():
            cursor[1] = (cursor[1] - 1) % 5
        if button_b.was_pressed():
            cursor[1] = (cursor[1] + 1) % 5
        if pin_logo.is_touched():
            cursor[0] = (cursor[0] - 1) % 5
        if pin2.is_touched():
            cursor[0] = (cursor[0] + 1) % 5
        if cursor == wrong:
            display.set_pixel(cursor[1], cursor[0], 9)
            music.play(music.BA_DING)
            music.play(music.PYTHON, wait=False, loop=True)
            return True
        pixelFlash(cursor)

    return False


def symmetric_game(max_score):
    while True:
        display.clear()
        score = 0
        timelimit = 5300
        music.play(music.PYTHON, wait=False, loop=True)
        while maingame(timelimit):
            score += 1
            timelimit -= 1000
        music.play(music.ODE, wait=False)
        max_score = max(max_score, score)
        display.scroll("score:{}".format(score), loop=True, wait=False)
        while True:
            if pin_logo.is_touched():
                break
            if button_b.is_pressed():
                return max_score
                


if __name__ == "__main__":
    symmetric_game(0)
