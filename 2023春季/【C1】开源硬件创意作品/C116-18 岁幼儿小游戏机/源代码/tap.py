from microbit import *
import time
import music

def tap_game(max_score):
    display.scroll("TAP!")
    while True:
        score = 0
        end_time = time.ticks_add(time.ticks_ms(), 10000)
        while time.ticks_ms() < end_time:
            if button_a.was_pressed() or button_b.was_pressed():
                score+=1
                music.pitch(440 + score * 10,duration=50,wait=False)
           
                if score != 0:
                    if score % 25 == 1:
                        display.clear()
                    display.set_pixel((score-1)%5,(score-1)%25//5,9)
        display.scroll(score,wait=False,loop=True)
        max_score = max(max_score,score)
        sleep(1000)
        while True:
                if pin_logo.is_touched():
                    break
                if button_b.is_pressed():
                    return max_score
                
            
        