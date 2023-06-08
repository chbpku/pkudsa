from microbit import *
import random
import music

class Snake:
    def __init__(self,accel):
        self.accel = accel
        self.fscore = 3

    def new_food(self, snake):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        while [x, y] in snake:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
        food = [x, y]
        self.fscore = random.randint(3, 6)
        display.set_pixel(x, y, self.fscore)
        return food

    def move_snake(self, snake,food,score,direction):
        over = False
        head = snake[-1][:]
        if direction == 'right':
            head[0] += 1
        elif direction == 'left':
            head[0] -= 1
        elif direction == 'up':
            head[1] -= 1
        else:
            head[1] += 1
        if head in snake:  # 撞到自己
            over = True
        elif head[0] > 4 or head[0] < 0 or head[1] > 4 or head[1] < 0:  # 撞到墙
            over = True
        else:
            if head == food:  # 吃到食物
                music.play(["F5:1"])
                snake.append(head)
                display.set_pixel(snake[-1][0], snake[-1][1], 9)
                score += self.fscore
                # speed_up()
                food = self.new_food(snake)
            else:
                snake.append(head)
                display.set_pixel(snake[-1][0], snake[-1][1], 9)
                display.set_pixel(snake[0][0], snake[0][1], 0)  # 擦除尾部
                snake.pop(0)
        return over,snake,food,score

    def reset_game(self):
        global direction
        direction = 'right'
        display.clear()
        snake = [[2, 2]]
        display.set_pixel(snake[-1][0], snake[-1][1], 9)
        food = self.new_food(snake)
        score = 0
        bmp = 800
        over = False
        if self.accel == False:
            while not over:
                for _ in range(100):
                    if pin0.is_touched() and direction != "right":
                        direction = "left"
                    if pin1.is_touched() and direction != "left":
                        direction = "right"
                    if pin2.is_touched() and direction != "up":
                        direction = "down"
                    if pin_logo.is_touched() and direction != "down":
                        direction = "up"
                    sleep(bmp//100)
                over,snake,food,score = self.move_snake(snake,food,score,direction)
        else:
            x0 = accelerometer.get_x()
            y0 = accelerometer.get_y() * 1.2
            while not over:
                sleep(bmp)
                x = (accelerometer.get_x()-x0)
                y = (accelerometer.get_y()*1.2-y0)
                if abs(x) > abs(y):
                    if x > 0 and direction != "left":
                        direction = "right"
                    if x < 0 and direction != "right":
                        direction = "left"
                if abs(x) < abs(y):
                    if y > 0 and direction != "down":
                        direction = "up"
                    if y < 0 and direction != "up":
                        direction = "down"
                over,snake,food,score = self.move_snake(snake,food,score,direction)
        music.play(music.POWER_UP)
        display.scroll("Score: " + str(score))

class Dino:
    def __init__(self,accel):
        self.accel = accel

    def casechange(self,case1,case2,stren):
        for x in case1:
            display.set_pixel(x[0], x[1], 0)
        for x in case2:
            display.set_pixel(x[0], x[1], stren)

    def block(self,contin, blockstep,blockcase,dinodic,dinocase):
        if blockcase == 0:
            if blockstep < 8:
                blockstep += 1
            else:
                if random.randint(1,5) == 1:
                    blockcase = random.randint(1,3)
                    blockstep = 0
        elif blockcase == 1 or blockcase == 2:
            oldblocklis = [[[5-blockstep,1],[5-blockstep,2]],[[5-blockstep,2],[5-blockstep,3]]]
            newblocklis = [[[4-blockstep,1],[4-blockstep,2]],[[4-blockstep,2],[4-blockstep,3]]]
            if blockstep == 0:
                for x in newblocklis[blockcase-1]:
                    if x in dinodic[dinocase]:
                        return False,blockstep,blockcase
                    display.set_pixel(x[0], x[1], 6)
            elif blockstep < 5:
                for x in newblocklis[blockcase-1]:
                    if x in dinodic[dinocase]:
                        return False,blockstep,blockcase
                self.casechange(oldblocklis[blockcase-1],newblocklis[blockcase-1],6)
            else:
                blockset = oldblocklis[blockcase-1]
                for x in blockset:
                    display.set_pixel(x[0], x[1], 0)
                blockcase = 0
            blockstep += 1
        else:
            if blockstep < 8:
                if blockstep < 5:
                    if [4-blockstep, 3] in dinodic[dinocase]:
                        return False,blockstep,blockcase
                    display.set_pixel(4-blockstep, 3, 6)
                if blockstep > 2:
                    display.set_pixel(7-blockstep, 3, 0)
            else:
                blockcase = 0
            blockstep += 1
        return contin,blockstep,blockcase

    def move(self,bmp,dinocase,dinodic,contin,blockstep,blockcase,y0):
        for x in dinodic[dinocase]:
            display.set_pixel(x[0], x[1], 9)
        if dinocase == 0:
            if self.accel:
                sleep(bmp)
                y = accelerometer.get_y() - y0
                if y > 100:
                    dinocase = 1
                if y < -100:
                    dinocase = -1
            else:
                for __ in range(bmp//25):
                    if button_a.is_pressed():
                        dinocase = 1
                    if button_b.is_pressed():
                        dinocase = -1
                    sleep(25)
            if dinocase != 0:
                if dinocase == 1:
                    music.play(["F4:1"])
                else:
                    music.play(["F5:1"])
                self.casechange(dinodic[0],dinodic[dinocase],9)
        elif dinocase < 0:
            sleep(bmp)
            if dinocase == -4:
                self.casechange(dinodic[-4],dinodic[0],9)
                dinocase = 0
            else:
                self.casechange(dinodic[dinocase],dinodic[dinocase-1],9)
                dinocase -= 1
        else:
            sleep(bmp)
            if dinocase == 4:
                self.casechange(dinodic[4],dinodic[0],9)
                dinocase = 0
            else:
                self.casechange(dinodic[dinocase],dinodic[dinocase+1],9)
                dinocase += 1
        contin,blockstep,blockcase = self.block(contin, blockstep,blockcase,dinodic,dinocase)
        return dinocase,contin,blockstep,blockcase

    def inmain(self):
        display.clear()
        for i in range(5):
            display.set_pixel(i, 4, 3)
        dinolis = [[[0,3],[0,2]],[[0,3],[1,2]],[[0,3],[1,3]],[[0,2],[0,1]],[[0,1],[0,0]]]
        for x in dinolis[0]:
            display.set_pixel(x[0],x[1],9)
        bmp = 600
        dinocase = 0
        dinodic = {0:dinolis[0],1:dinolis[1],2:dinolis[2],3:dinolis[2],4:dinolis[1],
                  -1:dinolis[3],-2:dinolis[4],-3:dinolis[4],-4:dinolis[3]}
        contin = True
        score = 0
        blockstep = 0
        blockcase = 0
        music.play(["C5:1"])
        y0 = accelerometer.get_y()
        while contin:
            dinocase,contin,blockstep,blockcase = self.move(bmp,dinocase,dinodic,contin,blockstep,blockcase,y0)
            score += 1
            if score%50 == 0:
                if bmp > 250:
                    bmp -= 50
        music.play(music.POWER_UP)
        display.scroll("Score: " + str(score))

accel = False
prepare = True
gamenum = 0
while prepare:
    if pin_logo.is_touched():
        accel = not accel
        while pin_logo.is_touched():
            pass
    if accel:
        display.show(Image.SURPRISED)
    else:
        display.show(Image.HAPPY)
    if button_a.is_pressed():
        prepare = False
        gamenum = 1
        display.show("A")
        sleep(1000)
    if button_b.is_pressed():
        prepare = False
        gamenum = 2
        display.show("B")
        sleep(1000)
display.clear()
if gamenum == 1:
    snake = Snake(accel)
    snake.reset_game()
if gamenum == 2:
    dinoe = Dino(accel)
    dinoe.inmain()