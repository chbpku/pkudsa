# Imports go at the top
from microbit import *
status = Image.DIAMOND
cnt = 1
# Code in a 'while True:' loop repeats forever
while True:
    n = uart.readline()
    if n:
        if n.decode()=="1\n":
            status = Image.SMILE
        elif n.decode()=="2\n":
            status = Image.HEART
        elif n.decode()=="3\n":
            status = Image.SAD
            display.show(status)
            sleep(1000)
        elif n.decode()=="4\n":
            status = Image.ANGRY
        cnt = 1
    cnt+=1
    if cnt % 150 ==0:
        status = Image.DIAMOND
        cnt = 1
    display.show(status)
    if accelerometer.is_gesture('up'):
        display.show(Image.ARROW_S)
        print("down")
    if accelerometer.is_gesture('down'):
        print("up")
        display.show(Image.ARROW_N)
    if button_a.is_pressed():
        display.show(Image.ARROW_W)
        print("left")
    if button_b.is_pressed():
        display.show(Image.ARROW_E)
        print("right")
    if pin_logo.is_touched() and accelerometer.was_gesture('shake'):
        display.show(Image.HAPPY,delay=1500)
        print("enter")
    sleep(20)