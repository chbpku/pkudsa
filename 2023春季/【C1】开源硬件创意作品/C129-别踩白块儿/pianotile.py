# Imports go at the top
from microbit import *
import music
import random
import time

# nyan cat
nyan = ['e5', 'f5', 'g5', 'c6', 'f5', 'e5', 'f5', 'g5', 'c6', 'e6', 
       'f6', 'e6', 'b5', 'c6', 'g5', 'e5', 'f5', 'g5', 'c6', 'd6', 
       'b5', 'c6', 'd6', 'f6', 'e6', 'f6', 'd6', 'g', 'a', 'd#', 
       'e', 'd', 'd#', 'd', 'c', 'c', 'd', 'd#', 'd#', 'd', 'c', 
       'd', 'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd', 'c', 'e', 
       'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd#', 'e', 'd#', 'd', 'c', 
       'd', 'd#', 'c', 'd', 'e', 'g', 'd', 'd#', 'd', 'c', 'd', 'c', 
       'd', 'g', 'a', 'd#', 'e', 'd', 'd#', 'd', 'c', 'c', 'd', 'd#', 
       'd#', 'd', 'c', 'd', 'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 
       'd', 'c', 'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd#', 'e', 
       'd#', 'd', 'c', 'd', 'd#', 'c', 'd', 'e', 'g', 'd', 'd#', 'd', 
       'c', 'd', 'c', 'c', 'c5', 'g4', 'a4', 'c5', 'c5', 'd5', 'e5', 
       'c5', 'g4', 'a4', 'g4', 'c5', 'c5', 'b4', 'c5', 'f5', 'e5', 'f5', 
       'g5', 'c5', 'b4', 'c5', 'g4', 'a4', 'c5', 'g4', 'a4', 'c5', 'd5', 
       'e5', 'c5', 'f5', 'e5', 'f5', 'g5', 'c5', 'c5', 'g4', 'a4', 'c5', 
       'g4', 'f5', 'e5', 'd5', 'c5', 'f4', 'e4', 'f4', 'g4', 'c5', 'g4', 
       'a4', 'c5', 'g4', 'a4', 'c5', 'c5', 'd5', 'e5', 'c5', 'g4', 'a4', 
       'g4', 'c5', 'c5', 'b4', 'c5', 'f5', 'e5', 'f5', 'g5', 'c5', 'b5',
       'g', 'a', 'd#', 'e', 'd', 'd#', 'd', 'c', 'c', 'd', 'd#', 'd#', 
       'd', 'c', 'd', 'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd', 'c', 
       'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd#', 'e', 'd#', 'd', 'c', 
       'd', 'd#', 'c', 'd', 'e', 'g', 'd', 'd#', 'd', 'c', 'd', 'c', 'd', 
       'g', 'a', 'd#', 'e', 'd', 'd#', 'd', 'c', 'c', 'd', 'd#', 'd#', 'd', 
       'c', 'd', 'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd', 'c', 'e', 'g', 
       'a', 'e', 'g', 'd', 'e', 'c', 'd#', 'e', 'd#', 'd', 'c', 'd', 'd#', 
       'c', 'd', 'e', 'g', 'd', 'd#', 'd', 'c', 'd', 'c', 'c', 'c5', 'g4', 
       'a4', 'c5', 'c5', 'd5', 'e5', 'c5', 'g4', 'a4', 'g4', 'c5', 'c5', 
       'b4', 'c5', 'f5', 'e5', 'f5', 'g5', 'c5', 'b4', 'c5', 'g4', 'a4', 
       'c5', 'g4', 'a4', 'c5', 'd5', 'e5', 'c5', 'f5', 'e5', 'f5', 'g5', 
       'c5', 'c5', 'g4', 'a4', 'c5', 'g4', 'f5', 'e5', 'd5', 'c5', 'f4', 
       'e4', 'f4', 'g4', 'c5', 'g4', 'a4', 'c5', 'g4', 'a4', 'c5', 'c5', 
       'd5', 'e5', 'c5', 'g4', 'a4', 'g4', 'c5', 'c5', 'b4', 'c5', 'f5', 
       'e5', 'f5', 'g5', 'c5', 'b5']

# nyan cat abridged version
nyanShort = ['g5', 'a', 'd#', 'e', 'd', 'd#', 'd', 'c', 'c', 'd', 'd#', 'd#',
        'd', 'c', 'd', 'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd', 'c',
        'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd#', 'e', 'd#', 'd', 'c',
        'd', 'd#', 'c', 'd', 'e', 'g', 'd', 'd#', 'd', 'c', 'd', 'c', 'd',
        'g', 'a', 'd#', 'e', 'd', 'd#', 'd', 'c', 'c', 'd', 'd#', 'd#',
        'd', 'c', 'd', 'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd', 'c',
        'e', 'g', 'a', 'e', 'g', 'd', 'e', 'c', 'd#', 'e', 'd#', 'd', 'c',
        'd', 'd#', 'c', 'd', 'e', 'g', 'd', 'd#', 'd', 'c', 'd', 'c', 'c']

# Prelude in C (recommended, all notes are same length)
prelude = [
    'c4:1', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',
    'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5', 'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5',
    'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5', 'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',
    'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',
    'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5', 'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5',
    'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5', 'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5',
    'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5', 'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5',
    'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
    'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
    'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5', 'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5',
    'g3', 'b', 'd4', 'g', 'b', 'd', 'g', 'b', 'g3', 'b3', 'd4', 'g', 'b', 'd', 'g', 'b'
]

# abridged version of Prelude
preludeShort = [
    'c4:1', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',
    'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5', 'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5',
    'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5', 'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',
]

# contains string name, note list, and bpm for each music
musicList = [('PRELUDE', prelude, 80), ('SHORT PRELUDE', preludeShort, 80),
            ('NYAN CAT', nyan, 300), ('SHORT NYAN CAT', nyanShort, 300)]

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

class Game:
    # initialize board (5x5 grid)
    def __init__(self):
        self.screen = [0,0,0,0,0] * 5

    # "shift" the grid down by removing bottom row and adding new row to the top
    def add_line(self, list):
        self.screen = list + self.screen[:20]

    def get_screen(self):
        return self.screen

class Line:
    # line (containing "piano tile") with a key value associated to it
    def __init__(self):
        self.line = []
        self.key = -1

    # generate a random "piano tile" and associated key
    # key: 1 = left tile; 2 = right tile; 0 = both tiles
    def gen_line(self):
        x = random.randint(0,100)
        if x <= 49:
            self.line = [0,9,0,0,0]
            self.key = 1
        elif x >= 50 and x <= 99:
            self.line = [0,0,0,9,0]
            self.key = 2
        elif x == 100:
            self.line = [9,9,9,9,9]
            self.key = 0

    # same as gen_line(), except no double tiles (for SPEED mode to remove rng)
    def gen_line2(self):
        x = random.randint(0,1)
        if x == 0:
            self.line = [0,9,0,0,0]
            self.key = 1
        elif x == 1:
            self.line = [0,0,0,9,0]
            self.key = 2
            

    def get_line(self):
        return self.line
    def get_key(self):
        return self.key

# on a filled grid (tiles in all rows), "shifts" the tiles down, creating a new one in the process
# uses a Queue to keep track of keys for each line of tiles
def cont():
    line.gen_line()
    game.add_line(line.get_line())
    keyQ.enqueue(line.get_key())
    display.show(Image(5,5,bytearray(game.get_screen())))

# for SPEED mode, no 'shakes' to remove rng
def cont2():
    line.gen_line2()
    game.add_line(line.get_line())
    keyQ.enqueue(line.get_key())
    display.show(Image(5,5,bytearray(game.get_screen())))

# start up
display.show(Image.MUSIC_QUAVER)
music.set_tempo(bpm=60)
music.play(music.POWER_UP)

while True:
    # start the game by pressing gold logo (activates upon release)
    # the while loop for when the gold logo is touched is important, as it is considered held down
    # being held down will activate later gold logo condition checks
    stage = 0
    if stage == 0 and pin_logo.is_touched():
        while pin_logo.is_touched():
            pass
        stage = 1

    # stage 1: select music from list of available music
    # button get_presses() to reset counter when playing through a second time
    if stage == 1:   
        m = p = 0
        n = q = -1
        menu = musicSelection = True
        button_a.get_presses()
        button_b.get_presses()

        # display.scroll() works in background in loop, only want to call it once when necessary
        # otherwise will keep restarting in a while loop
        # this logic will be used a lot (m != n, p != q)
        while menu == True:
            if p != q:
                display.scroll('SELECT MUSIC', delay=65, loop=True, wait=False)
                q = p
            if button_a.get_presses() == 1 or button_b.get_presses() == 1:
                menu = False

        # select music from musicList, using m as index
        while musicSelection == True:
            if m != n:
                currentMusic = musicList[m]
                display.scroll(currentMusic[0], delay=65, loop=True, wait=False)
                n = m
            if button_b.get_presses() == 1:
                m = (m + 1) % 4
            if button_a.get_presses() == 1:
                m = (m + len(musicList) - 1) % 4
            if pin_logo.is_touched():
                while pin_logo.is_touched():
                    pass
                melody = currentMusic[1]
                musicSelection = False
                stage = 2

    # stage 2: selecting gamemode
    # two gamemodes: classic and speed
    # code is very similar to stage 1
    if stage == 2:
        m = p = 0
        n = q = -1
        menu = gamemodeSelection = True
        
        while menu == True:
            if p != q:
                display.scroll('SELECT GAMEMODE', delay=65, loop=True, wait=False)
                q = p
            if button_a.get_presses() == 1 or button_b.get_presses() == 1:
                menu = False
            
        while gamemodeSelection == True:
            if m == 0:
                if m != n:
                    display.scroll('CLASSIC', delay=65, loop=True, wait=False)
                    n = m
            if m == 1:
                if m != n:
                    display.scroll('SPEED', delay=65, loop=True, wait=False)
                    n = m
            if button_a.get_presses() == 1 or button_b.get_presses() == 1:
                m = (m + 1) % 2
            if pin_logo.is_touched():
                while pin_logo.is_touched():
                    pass
                if m == 0:
                    stage = 4
                else:
                    stage = 3
                gamemodeSelection = False

    # stage 3: time limit selection if chose SPEED gamemode
    # 6 available time limits: 5, 10, 15, 20, 25, 30 seconds
    # again, uses very similar code to previous two stages, here directly uses m
    if stage == 3:
        m = p = 0
        n = q = -1
        menu = timeSelection = True
        
        while menu == True:
            if p != q:
                display.scroll('SELECT TIME', delay=65, loop=True, wait=False)
                q = p
            if button_a.get_presses() == 1 or button_b.get_presses() == 1:
                menu = False
            
        while timeSelection == True:
            if m != n:
                display.scroll(str(m + 5), delay=65, loop=True, wait=False)
                n = m
            if button_b.get_presses() == 1:
                m = (m + 5) % 30
            if button_a.get_presses() == 1:
                m = (m + 25) % 30
            if pin_logo.is_touched():
                while pin_logo.is_touched():
                    pass
                timeLimit = m + 5
                timeSelection = False
                stage = 5
        
    # stage 4: begin playing CLASSIC gamemode for selected music
    if stage == 4:
        game = Game()
        line = Line()
        keyQ = Queue()
        c = 0
        # tempo set at 400 to allow quick gameplay while maintaining note length
        music.set_tempo(bpm=400)

        # initialize the board with the first 5 rows of tiles
        for i in range(5):
            cont()
            sleep(300)
            
        stop = False

        #iterate through each note in the music list
        for note in melody:
            if stop == True:
                break    
            key = keyQ.dequeue()
            while True:
                if key == 1:
                    if button_a.get_presses() == 1 and button_b.is_pressed() == 0:
                        music.play(note)

                        # prevent extra rows of tiles spawning after music ended
                        if c < len(melody) - 5:
                            cont()
                            c += 1
                            # print(c)
                            break
                        else:
                            game.add_line([0,0,0,0,0])
                            keyQ.enqueue(line.get_key())
                            display.show(Image(5,5,bytearray(game.get_screen())))
                            break
                    elif button_b.get_presses() != 0:
                        stop = True
                        break
                elif key == 2:
                    if button_b.get_presses() == 1 and button_a.get_presses() == 0:
                        music.play(note)
                        if c < len(melody) - 5:
                            cont()
                            c += 1
                            break
                        else:
                            game.add_line([0,0,0,0,0])
                            keyQ.enqueue(line.get_key())
                            display.show(Image(5,5,bytearray(game.get_screen())))
                            break
                    elif button_a.get_presses() != 0:
                        stop = True
                        break
                elif key == 0:
                    if accelerometer.was_gesture('shake') and button_a.get_presses() == 0 and button_a.get_presses() == 0:
                        music.play(note)
                        if c < len(melody) - 5:
                            cont()
                            c += 1
                            break
                        else:
                            game.add_line([0,0,0,0,0])
                            keyQ.enqueue(line.get_key())
                            display.show(Image(5,5,bytearray(game.get_screen())))
                            break
                    elif button_a.get_presses() != 0 or button_b.get_presses() != 0:
                        stop = True
                        break
                        
       # execute if failed midway through music 
        if stop == True:
            music.set_tempo(bpm=60)
            display.show(Image.SAD)
            music.play(music.POWER_DOWN)
        # execute if level completed successfully
        else:
            music.set_tempo(bpm=currentMusic[2])
            display.show(Image.HAPPY)
            music.play(melody)

    # stage 5: being playing SPEED gamemode for chosen music and time limit
    if stage == 5:
        game = Game()
        line = Line()
        keyQ = Queue()
        c = 0
        # tempo set at 400 to allow quick gameplay while maintaining note length
        music.set_tempo(bpm=400)

        # initialize the board with the first 5 rows of tiles
        for i in range(5):
            cont2()
            sleep(300)
            
        stop = False

        m = 0
        n = -1

        # set up variables for timing
        # timeElapsed indicates time passed after starting timer
        # timer indicates whether or not the timer is running
        # completed indicates whether or not the player has played through without failing
        # inGame indicates in the game (endless, so will repeat music lists)
        timeElapsed = 0
        timer = completed = False
        inGame = True
        while inGame == True:
            if stop == True:
                break
            # iterate through each note in the music list
            for note in melody:
                if stop == True:
                    break    
                # start timer after pressing first tile
                if m != n and c == 1:
                    start = time.ticks_ms()
                    timer = True
                    n = m
                
                key = keyQ.dequeue()

                #keep playing as long as time elapsed doesn't go over time limit
                while timeElapsed < timeLimit * 1000:
                    # once timer is activated, constantly keep track of time elapsed from while loop
                    if timer == True:
                        timeElapsed = time.ticks_ms() - start
                    if key == 1:
                        if button_a.get_presses() == 1 and button_b.is_pressed() == 0:
                            music.play(note)
                            cont2()
                            c += 1
                            break
                        elif button_b.get_presses() != 0:
                            stop = True
                            break
                    elif key == 2:
                        if button_b.get_presses() == 1 and button_a.get_presses() == 0:
                            music.play(note)
                            cont2()
                            c += 1
                            break
                        elif button_a.get_presses() != 0:
                            stop = True
                            break
                else:
                    stop = True
                    inGame = False
                    completed = True

                        
       # execute if failed midway through music 
        if completed == False:
            music.set_tempo(bpm=60)
            display.show(Image.SAD)
            music.play(music.POWER_DOWN)
        # execute if level completed successfully
        else:
            music.set_tempo(bpm=currentMusic[2])
            display.scroll(str(c), delay=65, loop=True, wait=False)
            music.play(melody)