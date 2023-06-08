from microbit import *
import random
import music
import speech

def selectdifficulty():
    speech.say('make your choice boy',speed=100)
    while True:
        if button_a.is_pressed():
            global diff 
            diff = 5
            speech.say('easy mode',speed=80)
            break
        elif button_b.is_pressed():
            global diff 
            diff = 7
            speech.say('common mode',speed=80)
            break
        elif pin_logo.is_touched():
            global diff
            diff = 10
            speech.say('hard mode,good luck boy',speed=80)
            break
        
def gen_pix(snk):
    x = random.randint(0,4)
    y = random.randint(0,4)
    
    while (x,y,6) in snk:
        x = random.randint(0,4)
        y = random.randint(0,4)
    else:
        display.set_pixel(x,y,9)
        return (x,y,6)

        

def greedy_snake(snk):
    backup = snk
    x,y,_ = snk[-1]
    direction = 1
    
    for i,j,_ in snk:
        display.set_pixel(i,j,6)
    
    while len(snk) <= 20:
        pixel = gen_pix(snk)
        while (x,y,6) != pixel:
            sleep(10000/diff)
            
            if button_a.is_pressed():
                direction = 4
            elif button_b.is_pressed():
                direction = 2
            elif accelerometer.was_gesture('left'):
                direction = 1
            elif accelerometer.was_gesture('right'):
                direction = 3
            
            if direction == 1:
                y -= 1
            elif direction == 2:
                x += 1
            elif direction == 3:
                y += 1
            elif direction == 4:
                x -= 1
                
            if 0 <= x <= 4 and 0 <= y <= 4 and (x,y,6) not in snk:
                backup = snk
                snk.append((x,y,6))
                temp = snk.pop(0)
                display.set_pixel(x,y,6)
                i,j,_ = temp
                display.set_pixel(i,j,0)
            else:
                display.clear()
                display.show(Image.ANGRY)
                sleep(400)
                display.clear()
                return False, backup
                
        else:
            snk.insert(0,temp)
            display.set_pixel(i,j,6)
    else:
        display.scroll('Win!')
        display.show(Image.HAPPY)
        sleep(400)
        return True, []
def beatbricks(wall):
    vx,vy = 0,1
    ball = (2,3)
    board = 1
    for bricks in wall:
        if bricks !=None:
            display.set_pixel(bricks[0],bricks[1],9)
    display.set_pixel(2,3,6)
    display.set_pixel(board,4,4)
    display.set_pixel(board+1,4,4)
    while ball[1]<4 and len(wall) != 0:
        sleep(8000/diff)       
        if ball[0]==0 or ball[0]==4:
            vx = -vx
        if button_a.is_pressed() and board>0:
            if ball[1] == 3 and (ball[0]+vx in (board,board+1)):
                vx -= 1
                vy = -vy
            display.set_pixel(board-1,4,4)
            display.set_pixel(board+1,4,0)
            board -= 1
        elif button_b.is_pressed() and board<3:
            if ball[1] == 3 and (ball[0]+vx in (board,board+1)):
                vx += 1
                vy = -vy
            display.set_pixel(board+2,4,4)
            display.set_pixel(board,4,0)
            board += 1
        if ball[1]==3 and (ball[0]+vx in (board,board+1))and vy == -1:
            vy = 1
        if vx < -1:vx=-1
        if vx > 1:vx=1

        if ball in wall:
            vy = -vy
            i = wall.index(ball)
            del wall[i]
        if ball[1]==0:
            vy = -1
        display.set_pixel(ball[0],ball[1],0)
        ball = ball[0]+vx,ball[1]-vy
        display.set_pixel(ball[0],ball[1],6)
            
    else:
        if ball[1] >= 4:
            return False, wall
        else:
            display.scroll('Win!')
            display.show(Image.HAPPY)
            sleep(400)
            return True, []
                        
        
    
def pac_man(location,score):
    player,enemy = location
    x,y = enemy
    i,j = player
    display.set_pixel(player[0],player[1],6)
    display.set_pixel(enemy[0],enemy[1],4)
    
    p,q = (player[0],player[1],6),(enemy[0],enemy[1],6)
    pixel = gen_pix([p,q])
    while p!=q:
        sleep(3500/diff)
        direction = random.randint(1,4)
        if direction == 1 and x!=0:
            display.set_pixel(x,y,0)
            x -= 1
            enemy = x,y
            display.set_pixel(x,y,4)
        elif direction == 2 and x!=4:
            display.set_pixel(x,y,0)
            x += 1
            enemy = x,y
            display.set_pixel(x,y,4)
        elif direction == 3 and y!=4:
            display.set_pixel(x,y,0)
            y += 1
            enemy = x,y
            display.set_pixel(x,y,4)
        elif direction == 4 and y!=0:
            display.set_pixel(x,y,0)
            y -= 1
            enemy = x,y
            display.set_pixel(x,y,4)
    
        if button_a.is_pressed() and i!=0:
                display.set_pixel(i,j,0)
                i -= 1
                player = i,j
                display.set_pixel(i,j,6)
        elif button_b.is_pressed() and i!=4:
                display.set_pixel(i,j,0)
                i += 1
                player = i,j
                display.set_pixel(i,j,6)
        elif accelerometer.was_gesture('left') and j!=0:
                display.set_pixel(i,j,0)
                j -= 1
                player = i,j
                display.set_pixel(i,j,6)
        elif accelerometer.was_gesture('right')and j!=4:
                display.set_pixel(i,j,0)
                j += 1
                player = i,j
                display.set_pixel(i,j,6)
        p,q = (i,j,6),(x,y,6)
        if p == pixel:
            score += 10
            sleep(500)
            pixel = gen_pix([p,q])
        if q == pixel:
            score -= 15
            sleep(500)
            pixel = gen_pix([p,q])
    location = [player,enemy]        
    return location,score
    
display.show(Image.HEART)
sleep(400)
speech.say('hello',speed=80)
sleep(400)
while True:
    music.play(music.ODE,loop=True,wait=False)
    display.show(Image.HAPPY)
    while True:    
        if button_a.is_pressed():
            speech.say('greedy snake',speed=100)
            sleep(1000)
            selectdifficulty()
            music.play(music.NYAN,loop=True,wait=False)
            sleep(400)
            display.show(Image.HAPPY)
            sleep(400)
            display.clear()
            res, backup = greedy_snake([(2,2,6)])
            if res == False:
                music.play(music.FUNERAL,loop=True,wait=False)
                display.scroll('Retry?',wait=True,loop=False)
                if pin_logo.is_touched():
                    music.play(music.NYAN,loop=True,wait=False)
                    sleep(2000)
                    res,snk = greedy_snake(backup)
                    if res == False:
                        music.play(music.FUNERAL,loop=False,wait=False)
                        display.scroll('Game Over %s!'%(len(snk)*5),loop=False,wait=True)
                        break
                    else:
                        break
                else:
                    display.scroll('Game Over %s!'%(len(backup)*5))
                    break
            else:
                break
        elif button_b.is_pressed():
            speech.say("lets beat bricks",speed=100)
            sleep(1000)
            selectdifficulty()
            music.play(music.NYAN,loop=True,wait=False)
            sleep(400)
            display.show(Image.HAPPY)
            sleep(400)
            display.clear()
            res, backup = beatbricks([(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2),(4,0),(4,1),(4,2)])
            if res == False:
                music.play(music.FUNERAL,loop=True,wait=False)
                display.scroll('Retry?',wait=True,loop=False)
                if pin_logo.is_touched():
                    music.play(music.NYAN,loop=True,wait=False)
                    sleep(1500)
                    res,backup = beatbricks(backup)
                    if res == False:
                        music.play(music.FUNERAL,loop=False,wait=False)
                        display.scroll('Game Over %s!'%((13-len(backup))*10),loop=False,wait=True)
                        break
                    else:
                        break
                else:
                    display.scroll('Game Over %s!'%((13-len(backup))*10))
                    break
            else:
                break
        elif pin_logo.is_touched():
            speech.say('the pac man',speed=100)
            sleep(1000)
            selectdifficulty()
            music.play(music.NYAN,loop=True,wait=False)
            sleep(400)
            display.show(Image.HAPPY)
            sleep(400)
            display.clear()
            location,score = pac_man([(0,4),(4,0)],0)
            music.play(music.FUNERAL,loop=True,wait=False)
            display.scroll('Retry?',wait=True,loop=False)
            if pin_logo.is_touched():
                music.play(music.NYAN,loop=True,wait=False)
                sleep(1500)
                _,score = pac_man([(2,2),(location[1])],score)
                music.play(music.FUNERAL,loop=False,wait=False)
                display.scroll('%s!'%score,loop=False,wait=True)
                break
            else:
                display.scroll('%s!'%score,loop=False,wait=True)
                break
        

