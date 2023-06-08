from microbit import *
import music
from symmetric import symmetric_game
from maze import maze_game
from timer import timer_game
from balance import balance_game
from tap import tap_game
import struct


games = (symmetric_game, maze_game, timer_game,balance_game,tap_game)
try:
    with open('data', 'rb') as data:
        max_scores = list(struct.unpack('hffhh', data.readline()))
        
except:
    with open('data', 'wb') as data:
        max_scores =[0,0,0,0,0]
        data.write(struct.pack('hffhh',*max_scores))
        

idx = 0

while True:
    if idx == 0:      # symmetric_game
        display.show(Image('90000:'
                           '00000:'
                           '09090:'
                           '99994:'
                           '90909'))
    elif idx == 1:
        display.show(Image('09000:'
                           '99999:'
                           '00999:'
                           '90000:'
                           '90999'))
    elif idx == 2:
        display.show(Image('00900:'
                           '00009:'
                           '00090:'
                           '00900:'
                           '00900'))
    elif idx == 3:
        display.show(Image('00090:'
                           '00000:'
                           '00900:'
                           '99999:'
                           '00000'))
    elif idx == 4:
        display.show(Image('00009:'
                           '00000:'
                           '09990:'
                           '09990:'
                           '00000'))

    if button_a.was_pressed():
        idx=(idx-1)%5
    if button_b.was_pressed():
        idx=(idx+1)%5
    if pin_logo.is_touched():
        display.scroll('best:{}'.format(max_scores[idx]),wait=False,loop=True)
        sleep(500)
        while not pin_logo.is_touched():
            continue
        display.clear()
        max_scores[idx]=games[idx](max_scores[idx])
        music.stop()
        with open('data', 'wb') as data:
            data.write(struct.pack('hffhh',*max_scores))
    

    