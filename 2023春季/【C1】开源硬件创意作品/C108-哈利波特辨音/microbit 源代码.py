# Imports go at the top
import random
from microbit import *
import music
import speech

speech.say("Welcome to the magical world of Harry Potter! ",pitch=64,mouth=128,throat=128)
speech.say("Voldemort is tending to attack Hogwarts with his dark army",pitch=64,mouth=128,throat=128)
speech.say("You can beat him by the force of music notes",pitch=64,mouth=128,throat=128)
speech.say("If you can tell which note it is for three times, you can beat the Dark Lord",pitch=64,mouth=128,throat=128)
speech.say("Now, let the game begin",pitch=64,mouth=128,throat=128)

display.on()

music.set_tempo(bpm=86)
sleep(1000)
music.play(['b3:2', 'e4:3', 'g4:1', 'f#4:2','e4:4', 'b4:2', 'a4:6', 'f#4:6','e4:3', 'g4:1', 'f#4:2', 'd#4:4','f4:2', 'b3:10'])
sleep(100)
music.play(['b3:2', 'e4:3', 'g4:1', 'f#4:2','e4:4', 'b4:2', 'd5:4', 'c#5:2','c5:4', 'ab4:2', 'c5:3', 'b4:1','a#4:2', 'a#3:4','g4:2', 'e4:10'])

score=0

for round in range(0,3):
    note_reg = random.randint(0, 6)
    notelis = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    note = notelis[note_reg]
    note_range = random.randint(5, 6)
    music.play([note+str(note_range)+':12'])
    t=-1
    while True:
        if button_a.was_pressed():
            t+=1
            display.show(notelis[t%7])
        if button_b.was_pressed():
            break
    display.show(notelis[t])
    sleep(500)
    display.clear()
    sleep(500)
    display.show(notelis[t])
    sleep(500)
    display.clear()
    sleep(500)
    display.show(notelis[t])
    sleep(500)
    if t%7==note_reg:
        display.show(Image('00000:'
                           '00009:'
                           '00090:'
                           '90900:'
                           '09000'))
        music.play(['c4:4', 'g4:4', 'g4:4', 'g4:4','f4:4', 'c5:4', 'e5:4', 'c5:4','e4:4', 'e4:4', 'd4:8'])
        score+=1
    else:
        display.show(Image('90009:'
                           '09090:'
                           '00900:'
                           '09090:'
                           '90009'))
        music.play(['a3:8', 'c4:8', 'g#3:8'])
        score-=1
    sleep(1500)
if score>0:
    display.scroll('Succeed')
    speech.say("You have beaten Lord Voldemort!",pitch=64,mouth=128,throat=128)
else:
    display.scroll('Fail')
    speech.say("We feel sorry for you.",pitch=64,mouth=128,throat=128)
