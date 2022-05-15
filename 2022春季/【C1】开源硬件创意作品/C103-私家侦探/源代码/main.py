from microbit import *
import os
import math
import music

g = 9.8


def track():
    dt = 0.001
    vN = 0
    vE = 0
    N, E = 0, 0
    dT = 0.01
    times = 1/dT
    compass.calibrate()
    with open("position.txt", "w", encoding="utf8") as f:
        f.write('track')
        f.write("\n")
        
        while True:
            if button_a.is_pressed():
                display.show('g')
                sleep(1000)
                atotal = 0
                for _ in range(int(1 / dt)):
                    a_x, a_y, a_z = accelerometer.get_values()
                    atotal += (a_x ** 2 + a_y ** 2 + a_z ** 2) ** (1 / 2)
                    sleep(dt * 1000)
                abar = atotal / int(1 / dt)
                display.show('d')
                break
        print(abar)
        
        
        while True:
            if button_a.is_pressed():
                display.show('R')
                sleep(1000)
                time = 0
                while True:
                    if time < times:
                        time += 1
                    else:
                        time = 0
                        print('a:',axy)
                        print('v:',vE,vN)
                        print('loc:',E, N)
                        f.write(str(N) + '/' + str(E))
                        f.write("\n")
                        needle = ((15 - compass.heading()) // 30) % 12
                        display.show(Image.ALL_CLOCKS[needle])

                    a2 = 0
                    cosum = 0
                    sinum = 0
                    aY=0
                    for _ in range(int(dT / dt)):
                        a_x, a_y, a_z = accelerometer.get_values()
                        aY+=a_y
                        direction = math.radians(compass.heading())
                        asq = (a_x ** 2 + a_y ** 2 + a_z ** 2 - abar ** 2)//100
                        a2 += asq
                        cosum += math.cos(direction)
                        sinum += math.sin(direction)
                        sleep(dt * 1000)

                    if a2 <= 0:
                        aH = 0
                    else:
                        aH = ((a2 / int(dT / dt)) ** (1 / 2))//10*10
                        if aY>0:
                            axy = aH * 0.001 * g
                        else:
                            axy =- aH * 0.001 * g
                    vN += axy * cosum / int(dT / dt) * dT
                    vE += axy * sinum / int(dT / dt) * dT
                    N += vN * dT
                    E += vE * dT

                    if button_b.is_pressed():
                        display.show('D')
                        break
                    if os.size('position.txt') > 25000:
                        display.show('D')
                        break
                break
    f.close()
    
def Compass():
    compass.calibrate()

    display.scroll("Hello! This is a compass")
    display.show(Image.HEART)
    music.play(music.ENTERTAINER)
    for i in range(3, 0, -1):
        display.show(Image.ALL_CLOCKS, loop=False, delay=i * 30)
    display.scroll("A=start <<<")
    while True:
        if button_a.is_pressed():
            music.play(music.POWER_UP)
            display.scroll("B=stop >>>")
            while True:
                sleep(100)
                needle = ((15 - compass.heading()) // 30) % 12
                display.show(Image.ALL_CLOCKS[needle])
                if button_b.is_pressed():
                    display.scroll("BYE~~")
                    music.play(music.POWER_DOWN)
                    break
            break

def Timer():
    
    display.scroll("Hello! This is a stopwatch")
    display.show(Image.DIAMOND)
    music.play(music.DADADADUM)

    display.scroll("A=start <<<")
    display.scroll("logo=see minutes ^^^")
    display.scroll("B=stop >>>")
    while True:
        if button_a.is_pressed():
            music.play(music.POWER_UP)
        
            time = 0
            while True:
                sleep(100)
                time += 0.1
                pointer = int(time / 5) % 12
                display.show(Image.ALL_CLOCKS[pointer])
                if pin_logo.is_touched():
                    display.show(str(int(time // 60)))
                    sleep(2000)
                    time += 2
                if button_b.is_pressed():
                    ms = str(int(time // 60)) + ':' + '%.1f'%(time % 60)
                    display.scroll(ms)
                    display.scroll("A=restart <<<")
                    display.scroll("B=finish >>>")
                    restart = False
                    while True:
                        if button_a.is_pressed():
                            restart = True
                            break
                        if button_b.is_pressed():
                            break
                    if restart:
                        time = 0
                        continue
                    else:
                        music.play(music.POWER_DOWN)
                        break
            break

def Step():
    display.scroll("Hello! This is a stepcounter")
    display.show(Image.SMILE)
    music.play(music.WEDDING)

    display.scroll("A=start <<<")
    while True:
        if button_a.is_pressed():
            display.scroll("logo=see steps ^^^")
            display.scroll("B=stop >>>")
            music.play(music.POWER_UP)
            for i in range(3, 0, -1):
                display.show(str(i))
                sleep(1000)
                display.clear()

            count = 0
            while True:
                if accelerometer.get_x() > 1500:
                    count += 1
                    sleep(700)
                if pin_logo.is_touched():
                    display.scroll(str(count))
                if button_b.is_pressed():
                    display.scroll(str(count))
                    display.scroll("BYE~")
                    music.play(music.POWER_DOWN)
                    break


mode=0
while True:
    if pin_logo.is_touched():
        track()
        break
    if button_b.is_pressed():
        if mode==0:
            break
        elif mode%3==1:
            Compass()
        elif mode%3==2:
            Timer()
        elif mode%3==3:
            Step()
    if button_a.is_pressed():
        mode+=1
