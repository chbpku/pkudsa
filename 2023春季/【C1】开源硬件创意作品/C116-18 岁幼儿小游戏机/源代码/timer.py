from microbit import *
from random import randint
import music
from time import ticks_ms, ticks_diff
from math import ceil

def counter_down(time, start_time):
    while True:          #test for
        count = ceil((time - ticks_diff(ticks_ms(), start_time))/1000)
        print(count)
        display.scroll(count, delay=85)
        if count <2:     #test for
            break        #test for
    stop_time = ticks_ms()
    return stop_time
    
def timer_game(max_score):
    while True:
        time = randint(3,9)
        while not accelerometer.is_gesture('face down'):
            if button_b.was_pressed():
                return max_score
            display.show(time)
        time *= 1000
        display.clear()
        music.pitch(940, 100)
        start_time = ticks_ms()
        print(start_time)
        stop_time = counter_down(time, start_time)
        print(stop_time)
        music.pitch(940, 100)
        sleep(100)
        deviation = (time - ticks_diff(ticks_ms(), start_time))/1000
        display.scroll('{:.2f}s'.format(deviation), delay=100, loop=True, wait=False)
        max_score = min(abs(deviation), max_score)
        while True:
            if pin_logo.is_touched():
                break
            if button_b.is_pressed():
                return max_score
                
        
        
if __name__ == "__main__":
    timer_game(0)