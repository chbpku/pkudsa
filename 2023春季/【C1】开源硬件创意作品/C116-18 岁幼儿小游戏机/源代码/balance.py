from microbit import *
import random
import time
import music

def play_note(note):
    if note == 0:
        music.stop()
        return
            
    # A 440hz
    f = 440.0 * pow(2, ((note - 58)/12.0));
    target_freq = int(f)
    music.pitch(target_freq)

    print(note)

def updateAccelPosition(originX,originY):
    accelX = 0;
    accelY = 0;
    basenote = 52
 
    if (accelerometer.get_x() > 600):
        accelX+=1
    if (accelerometer.get_x() > 250):
        accelX+=1
    if (accelerometer.get_x() > -250):
        accelX+=1
    if (accelerometer.get_x() > -600):
        accelX+=1
 
    if (accelerometer.get_y() > 600):
        accelY+=1
    if (accelerometer.get_y() > 250):
        accelY+=1
    if (accelerometer.get_y() > -250):
        accelY+=1
    if (accelerometer.get_y() > -600):
        accelY+=1
    if originX != accelX or originY != accelY:
        play_note(basenote - 12 + (12 * accelX) + (3 * accelY))
    else:
        play_note(0)
    

    return accelX, accelY


def insertNewTarget():

    targetX = random.randint(0,4);
    targetY = random.randint(0,4);
    if targetX == 0 and targetY == 0 : targetY+=1
    elif targetX == 0 and targetY == 4: targetY-=1
    elif targetX == 4 and targetY == 0: targetY+=1
    elif targetX == 4 and targetY == 4: targetY-=1

    return targetX,targetY

 
def balance_game(max_score):
    display.scroll('TILT!')
    while True:
        score = 0
        toggle = 0
        toggleCount = 0
        targetX,targetY = insertNewTarget()
        accelX,accelY = 2,2
        end_time = time.ticks_add(time.ticks_ms(), 30000)
        while True:
            if time.ticks_ms() > end_time:
                max_score = max(max_score,score)
                break
            if toggleCount % 5 == 0:
                toggle = 9-toggle
                toggleCount = 0
            
            accelX,accelY = updateAccelPosition(accelX,accelY)
            
            display.clear()
            display.set_pixel(accelX, accelY, 9);
            display.set_pixel(targetX, targetY, toggle);
            
            if targetX == accelX and targetY == accelY:
                music.play(music.BA_DING)
                targetX,targetY = insertNewTarget()
                score+=1
            sleep(100);
            toggleCount+=1
        display.scroll("score:{}".format(score),loop=True,wait=False)
        while True:
            if pin_logo.is_touched():
                break
            if button_b.is_pressed():
                return max_score
    
    


if __name__ == '__main__':
    balance_game(0)