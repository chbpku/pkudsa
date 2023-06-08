# Imports go at the top
from microbit import display, button_a, button_b, sleep, Image
from random import randint
CONFIG = {
    'scale': 9, 
    'TICK': 110, 
    'ENEMY_DOWN_FREQ': 3, 
    'ACTION_DELAY': 5, 
}
VARS = {}    
def new_enemy():
    VARS['enemy_level'] = 0
    VARS['enemy'] = randint(0, CONFIG['scale']-1)
    VARS['arrow_stat'] = True    
def play():
    clock = 0
    while VARS['life'] > 0:
        clock += 1
        sleep( CONFIG['TICK'] )
        display.clear()
        VARS['player'] -= button_a.get_presses()
        VARS['player'] += button_b.get_presses()
        sleep( CONFIG['ACTION_DELAY'] )
        relpos = VARS['enemy'] - VARS['player']
        if not clock % CONFIG['ENEMY_DOWN_FREQ']:
            VARS['enemy_level'] += 1
            if VARS['enemy_level'] > 3:
                if VARS['enemy'] == VARS['player']:
                    VARS['score'] += 1
                    clock = 0
                    new_enemy()
                elif VARS['enemy_level'] > 4:
                    VARS['life'] -= 1
                    new_enemy()
                    if abs(relpos) < 2:
                        display.set_pixel(1+relpos,4,4)
                        display.set_pixel(2+relpos,4,6)
                        display.set_pixel(3+relpos,4,4)
                        display.set_pixel(2+relpos,3,4)
                        sleep( CONFIG['TICK'] )
                    elif abs(relpos) < 3:
                        display.set_pixel(2+relpos,3,4)
                        display.set_pixel(2+relpos,4,6)
                        if relpos > 0:
                            display.set_pixel(1+relpos,4,4)
                        else:
                            display.set_pixel(3+relpos,4,4)
                        sleep( CONFIG['TICK'] )
        sleep( CONFIG['ACTION_DELAY'] )
        for i in range(5):
            display.set_pixel(i,1,0)
        display.set_pixel(1,0,0)
        display.set_pixel(1,2,0)
        display.set_pixel(3,0,0)
        display.set_pixel(3,2,0)
        relpos = VARS['enemy'] - VARS['player']
        if abs(relpos) < 3 and VARS['enemy_level'] < 5:
            display.set_pixel(2+relpos, VARS['enemy_level'], 6)
        elif relpos < -2:
            for i in range(5):
                display.set_pixel(i,1,4)
            display.set_pixel(1,0,4)
            display.set_pixel(1,2,4)
        elif relpos > 2:
            for i in range(5):
                display.set_pixel(i,1,4)
            display.set_pixel(3,0,4)
            display.set_pixel(3,2,4)
        display.set_pixel(2, 4, 9)
    display.scroll("GAME OVER", delay=50)
    display.scroll("SCORE: ", delay=100)
    display.scroll(VARS['score'], delay=250)
    button_a.was_pressed()
    button_b.was_pressed()
def restart():
    while True:
        display.scroll("A:retry ", delay=50)
        display.scroll("B:quit ", delay=50)
        for i in range(12):
            i = 2 - ( i % 3 )
            l = ['0', '0']
            l.insert(i, '9')
            l = ''.join(l)
            display.show(Image('00000:00000:00000:0{}0:00000'.format(l)))
            sleep(200)
            if button_a.was_pressed():
                return True
            if button_b.was_pressed():
                return False
while True:
    VARS['score'] = 0
    VARS['life'] = 3
    VARS['player'] = CONFIG['scale']//2
    new_enemy()
    play()
    if not restart():
        break
display.scroll('Good bye ~~', delay=75)
display.show(Image.HAPPY)