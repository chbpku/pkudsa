from random import randint, choice
import time
import music
from microbit import *


WIDTH = 15
HEIGHT = 15 
def resetMap(map, value):
    for y in range(WIDTH):
        for x in range(HEIGHT):
            map[x][y] = value

def setMap(map, x, y, value):
    map[y][x] = value


def isVisited(map, x, y):
    return map[y][x] != 9

def showMap(self):
    for row in self:
        s = ''
        for entry in row:
            if entry == 0:
                s += '  '
            elif entry == 9:
                s += ' #'
            else:
                s += ' X'
        print(s)


# find unvisited adjacent entries of four possible entris
# then add random one of them to checklist and mark it as visited
def checkAdjacentPos(map, x, y, width, height, checklist):
    directions = []
    if x > 0:
        if not isVisited(map, 2 * (x - 1) + 1, 2 * y + 1):
            directions.append(0)

    if y > 0:
        if not isVisited(map, 2 * x + 1, 2 * (y - 1) + 1):
            directions.append(1)

    if x < width - 1:
        if not isVisited(map, 2 * (x + 1) + 1, 2 * y + 1):
            directions.append(2)

    if y < height - 1:
        if not isVisited(map, 2 * x + 1, 2 * (y + 1) + 1):
            directions.append(3)

    if len(directions):
        direction = choice(directions)
        print("(%d, %d) => %s" % (x, y, str(direction)))
        if direction == 0:
            setMap(map,2 * (x - 1) + 1, 2 * y + 1, 0)
            setMap(map,2 * x, 2 * y + 1, 0)
            checklist.append((x - 1, y))
        elif direction == 1:
            setMap(map,2 * x + 1, 2 * (y - 1) + 1, 0)
            setMap(map,2 * x + 1, 2 * y, 0)
            checklist.append((x, y - 1))
        elif direction == 2:
            setMap(map,2 * (x + 1) + 1, 2 * y + 1, 0)
            setMap(map,2 * x + 2, 2 * y + 1, 0)
            checklist.append((x + 1, y))
        elif direction == 3:
            setMap(map,2 * x + 1, 2 * (y + 1) + 1, 0)
            setMap(map,2 * x + 1, 2 * y + 2, 0)
            checklist.append((x, y + 1))
        return True
    else:
        # if not find any unvisited adjacent entry
        return False


# random prim algorithm
def randomPrim(map, width, height):
    startX, startY = (randint(0, width - 1), randint(0, height - 1))
    print("start(%d, %d)" % (startX, startY))
    map[2 * startY + 1][2 * startX + 1] = 0

    checklist = []
    checklist.append((startX, startY))
    while len(checklist):
        # select a random entry from checklist
        entry = choice(checklist)
        if not checkAdjacentPos(map, entry[0], entry[1], width, height, checklist):
            # the entry has no unvisited adjacent entry, so remove it from checklist
            checklist.remove(entry)


def doRandomPrim(map):
    # set all entries of map to wall
    resetMap(map, 9)
    randomPrim(map, (WIDTH - 1) // 2, (HEIGHT - 1) // 2)

def generate_image(matrix, x, y):
    image = []
    for row in matrix[5*y:5*y+5]:
        line = "".join(map(str,row[5*x:5*x+5]))
        image.append(line)
    image = ':'.join(image)
    return Image(image)

def getOP(cursor, map):
    while True:
        if button_a.was_pressed():
            if map[cursor[1]][cursor[0]-1] == 0:
                cursor[0]=cursor[0]-1
                music.play('e6:1')
            else:
                music.play('c3:1')
            break
        if button_b.was_pressed():
            if map[cursor[1]][cursor[0]+1] == 0:
                cursor[0]=cursor[0]+1
                music.play('e6:1')
            else:
                music.play('c3:1')
            break
        if pin_logo.is_touched():
            if map[cursor[1]-1][cursor[0]] == 0:
                cursor[1]=cursor[1]-1
                music.play('e6:1')
            else:
                music.play('c3:1')
            break
        if pin2.is_touched():
            if map[cursor[1]+1][cursor[0]] == 0:
                cursor[1]=cursor[1]+1
                music.play('e6:1')
            else:
                music.play('c3:1')
            break

def maze_game(max_score):
    main_map = [[9 for i in range(WIDTH)] for j in range(HEIGHT)]
    doRandomPrim(main_map)
    while True:
        main_map[13][14] = 0
        showMap(main_map)
        cursor = [1,1]
        display.show(generate_image(main_map, 0, 0))
        display.set_pixel(cursor[0]%5, cursor[1]%5, 6)
        start_time = None
        while True:
            if cursor[0] == 14 and cursor[1]==13:
                stop_time = time.ticks_ms()
                break   
            getOP(cursor, main_map)
            if start_time is None:
                start_time = time.ticks_ms()
            display.show(generate_image(main_map, cursor[0]//5, cursor[1]//5))
            display.set_pixel(cursor[0]%5, cursor[1]%5, 6)
            sleep(200)
        music.play(music.BA_DING)
        time_cost = time.ticks_diff(stop_time, start_time)/1000
        display.scroll('{}s'.format(time_cost), delay=100,wait=False,loop=True)
        max_score = min(max_score,time_cost)
        while True:
            if pin_logo.is_touched():
                break
            if button_b.is_pressed():
                return max_score
                
        

if __name__ == "__main__":
    maze_game(0)
