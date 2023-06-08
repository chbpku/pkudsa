# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
# 我们要实现以下的一些功能：
# 1.可视化，具体而言是图像的显示
# 2.声音的载入，并与图像建立一一对应的关系
# 3.对按键进行识别，并通过相应的输入检测是否正确触发
import music




Sheet_music = {"fstline":[('0',None),('0',None),('0',None),#1
                          ('9','d4'),('9','e4'),('0',None),
                          ('0',None),('0',None),('0',None),
                          ('9','d5'),('7','c5'),('5','a4'),
                          ('0',None),('0',None),('0',None),#5
                          ('9','a4'),('8','g4'),('7','f4'),
                          ('6','e4'),('0',None),('0',None),
                          ('0',None),('7','g4'),('0',None),
                          ('0',None),('0',None),('0',None),
                          ('9','e4'),('9','d4'),('0',None),#10
                          ('0',None),('9','e4'),('9','d4'),
                          ('0',None),('0',None),
                          
                          ('5','d4'),('7','e4'),('9','f4'),#1
                          ('0',None),('9','a4'),('0',None),
                          ('9','d5'),('0',None),('5','a4'),
                          ('0',None),('0',None),('0',None),
                          ('9','a4'),('7','g4'),('5','f4'),#5
                          ('0','e4'),('0',None),('0',None),
                          ('0',None),('7','g4'),('9','a4'),
                          ('0',None),('9','g4'),('0',None),
                          ('9','e4'),('0',None),('9','f4'),
                          ('0',None),('9','g4'),('0',None),#10
                          ('9','a4'),('0',None),
                          
                          ('7','c5'),('9','d5'),('0',None),#1
                          ('7','g4'),('0',None),('0',None),
                          ('5','g4'),('0',None),('7','c5'),
                          ('0',None),('7','a4'),('5','g4'),
                          ('0',None),('0',None),('7','g4'),#5
                          ('9','a4'),('0',None),('0',None),
                          ('5','e4'),('0',None),('7','d4'),
                          ('0',None),('0',None),('7','d4'),
                          ('0',None),('7','f4'),('0',None),
                          ('9','a4'),('7','d4'),('0',None),#10
                          ('0',None),('9','c5'),
                          
                          ('7','c5'),('9','d5'),('0',None),#1
                          ('7','g4'),('0',None),('0',None),
                          ('5','g4'),('0',None),('7','c5'),
                          ('0',None),('7','a4'),('5','g4'),
                          ('0',None),('0',None),('7','g4'),#5
                          ('9','a4'),('0',None),('0',None),
                          ('5','e4'),('0',None),('7','d4'),
                          ('0',None),('0',None),('7','d4'),
                          ('0',None),('7','f4'),('0',None),
                          ('9','a4'),('7','d4'),('0',None),#10
                          ('0',None),('9','c5'),
                          
                          ('7','c5'),('9','d5'),('0',None),#1
                          ('7','g4'),('0',None),('0',None),
                          ('5','g4'),('0',None),('7','c5'),
                          ('0',None),('7','a4'),('5','g4'),
                          ('0',None),('0',None),('7','g4'),#5
                          ('9','a4'),('0',None),('0',None),
                          ('5','e4'),('0',None),('7','d4'),
                          ('0',None),('0',None),('7','d4'),
                          ('0',None),('7','f4'),('0',None),
                          ('9','a4'),('7','d4'),('0',None),#10
                          ('0',None),('9','c5'),
                          
                          ('7','c5'),('9','d5'),('0',None),#1
                          ('7','g4'),('0',None),('0',None),
                          ('5','g4'),('0',None),('7','c5'),
                          ('0',None),('7','a4'),('5','g4'),
                          ('0',None),('0',None),('5','d5'),#5
                          ('7','e5'),('9','f5'),('7','e5'),
                          ('6','d5'),('5','c5'),('0',None),
                          ('0',None),('6','g4'),('7','a4'),
                          ('0',None),('0',None),('0',None),
                          ('5','c4'),('7','d4'),('0',None),#10
                          ('0',None),('0',None),('0',None),
                          ('0',None),('0',None),('0',None)],
               "scdline":[('0',None),('0',None),('0',None),#1
                          ('0',None),('0',None),('9','f4'),
                          ('5','g4'),('9','a4'),('0',None),
                          ('0',None),('0',None),('0',None),
                          ('0',None),('7','d4'),('0',None),#5
                          ('0',None),('0',None),('0',None),
                          ('0',None),('5','d4'),('7','e4'),
                          ('9','f4'),('0',None),('7','a4'),
                          ('0',None),('9','g4'),('9','f4'),
                          ('0',None),('0',None),('9','e4'),#10
                          ('9','f4'),('0',None),('0',None),
                          ('9','c4'),('9','e4'),
                          
                          ('0',None),('0',None),('0',None),#1
                          ('9','g4'),('0',None),('0',None),
                          ('0',None),('7','c5'),('0',None),
                          ('0',None),('9','d4'),('0',None),
                          ('0',None),('0',None),('0',None),#5
                          ('0',None),('5','d4'),('6','e4'),
                          ('8','f4'),('0',None),('0',None),
                          ('0',None),('0',None),('7','f4'),
                          ('9','e4'),('0',None),('9','f4'),
                          ('0',None),('9','g4'),('0',None),#10
                          ('9','a4'),('0',None),
                          
                          ('0',None),('0',None),('7','a4'),#1
                          ('0',None),('8','a4'),('0',None),
                          ('0',None),('7','a4'),('0',None),
                          ('9','d5'),('0',None),('0',None),
                          ('7','a4'),('0',None),('0',None),#5
                          ('0',None),('7','g4'),('5','f4'),
                          ('0',None),('5','c4'),('7','d4'),
                          ('0',None),('7','c4'),('0',None),
                          ('7','e4'),('0',None),('7','g4'),
                          ('0',None),('7','d4'),('0',None),#10
                          ('7','a4'),('0',None),
                          
                          ('0',None),('0',None),('7','a4'),#1
                          ('0',None),('8','a4'),('0',None),
                          ('0',None),('7','a4'),('0',None),
                          ('9','d5'),('0',None),('0',None),
                          ('7','a4'),('0',None),('0',None),#5
                          ('0',None),('7','g4'),('5','f4'),
                          ('0',None),('5','c4'),('7','d4'),
                          ('0',None),('7','c4'),('0',None),
                          ('7','e4'),('0',None),('7','g4'),
                          ('0',None),('7','d4'),('0',None),#10
                          ('7','a4'),('0',None),
                          
                          ('0',None),('0',None),('7','a4'),#1
                          ('0',None),('8','a4'),('0',None),
                          ('0',None),('7','a4'),('0',None),
                          ('9','d5'),('0',None),('0',None),
                          ('7','a4'),('0',None),('0',None),#5
                          ('0',None),('7','g4'),('5','f4'),
                          ('0',None),('5','c4'),('7','d4'),
                          ('0',None),('7','c4'),('0',None),
                          ('7','e4'),('0',None),('7','g4'),
                          ('0',None),('7','d4'),('0',None),#10
                          ('7','a4'),('0',None),
                          
                          ('0',None),('0',None),('7','a4'),#1
                          ('0',None),('8','a4'),('0',None),
                          ('0',None),('7','a4'),('0',None),
                          ('9','d5'),('0',None),('0',None),
                          ('7','a4'),('0',None),('0',None),#5
                          ('0',None),('9','f5'),('0',None),
                          ('0',None),('0',None),('5','a4'),
                          ('0',None),('0',None),('0',None),
                          ('7','g4'),('6','f4'),('5','e4'),
                          ('0',None),('7','d4'),('0',None),#10
                          ('0',None),('0',None),('0',None),
                          ('0',None),('0',None),('0',None)],

               "beats":[],
               "music_length":0}

def doset():
    yourbpm = 240
    chances = 10
    display.scroll('GOTO MODULE A JUST START B',delay = 50)
    while True:
        if button_a.is_pressed():
            display.scroll('BASIC A SELF DEFINE B',delay = 75)
            while True:
                if button_a.is_pressed():
                    display.scroll('SLOW A MIDDLE B FAST AB',delay = 75)
                    while True:
                        if button_a.is_pressed() and button_b.is_pressed():
                            yourbpm = 240
                        elif button_a.is_pressed():
                            yourbpm = 60
                        elif button_b.is_pressed():
                            yourbpm = 120
                        break
                    break
                if button_b.is_pressed():
                    display.scroll('SET bpm ADD A DECLINE B SET NEXT AB',delay = 75)
                    while True:
                        if button_a.is_pressed() and button_b.is_pressed():
                            display.scroll('bpm %d'%yourbpm, delay =75)
                            display.scroll('SET CHANCES ADD A DECLINE B END AB',delay = 75)
                            while True: 
                                if button_a.is_pressed() and button_b.is_pressed():
                                    display.scroll('CHANCES %d'%chances,delay = 75)
                                    break
                                elif button_a.is_pressed():
                                    chances += 1
                                elif button_b.is_pressed():
                                    if chances >= 2:
                                        chances -= 1
                            break
                        elif button_a.is_pressed():
                            if yourbpm <=290:
                                yourbpm = yourbpm +10
                        elif button_b.is_pressed():
                            if yourbpm >= 20:
                                yourbpm = yourbpm -10
                    break     
            break
        if button_b.was_pressed():
            break
    return yourbpm ,chances
yourbpm , chances = doset()
def ourgame():
    gap = 0.01
    global chances
    music.set_tempo(bpm = yourbpm)
    score = 0
    isPass = False
    music_length = len(Sheet_music["fstline"])
    Sheet_music["music_length"] = music_length
    tick_sequence = 0
    tick = (60/yourbpm)-gap
    while chances and(not isPass):
        times = 0
        button_a.get_presses()
        button_b.get_presses()
        ispressed = False
        while times<2:
            #判断识别部分
            if times==1 :
                ka = button_a.get_presses()
                kb = button_b.get_presses()
                if ka == 1 and Sheet_music["fstline"][tick_sequence][0]!='0':
                    score = score + 1
                    ispressed = True
                elif ka !=1 and Sheet_music["fstline"][tick_sequence][0]!='0':
                    chances = chances - 1
                elif ka != 0 and Sheet_music["fstline"][tick_sequence][0]=='0':
                    chances = chances-1
                if kb == 1 and Sheet_music["scdline"][tick_sequence][0]!='0':
                    score = score + 1
                    ispressed = True
                elif kb !=1 and Sheet_music["scdline"][tick_sequence][0]!='0':
                    chances = chances - 1
                elif kb != 0 and Sheet_music["scdline"][tick_sequence][0]=='0':
                    chances = chances-1                
            
            #图像编辑部分
            line1 = '' 
            for i in range(5):
                line1 = line1 + Sheet_music["fstline"][tick_sequence+i][0]
            line1 = line1 + ':'
            if chances ==3:
                line3 = '09990:'
            elif chances == 2:
                line3 = '09900:'
            elif chances == 1:
                line3 = '09000:'
            else:
                line3 = '99999:'
                
            if ispressed:
                line2 = '99999:'
                line4 = '99999:'
            else:
                line2 = '00000:'
                line4 = '00000:'
                
            line5 = ''
            for i in range(5):
                line5 = line5 + Sheet_music["scdline"][tick_sequence+4-i][0]
            line5 = line5 + ''
            #图像与声音输出部分
            current = line1 + line2 + line3 + line4 +line5
            display.show(Image(current))
            if times == 0:
                first_symbol =  Sheet_music["fstline"][tick_sequence][1]
                second_symbol = Sheet_music["scdline"][tick_sequence][1]
                if (not first_symbol) and (not second_symbol) :
                    sleep(tick*1000)
                elif (first_symbol) and (not second_symbol):
                    music.play([first_symbol+':4'])
                elif (not first_symbol) and (second_symbol):
                    music.play([second_symbol+':4'])
                else:
                    music.play([first_symbol+':4'])
            elif times ==1:
                sleep(gap*1000)
            times = times+1
        tick_sequence = tick_sequence + 1
        if tick_sequence == music_length - 4:
            isPass = True
        ispressed = False
    
    if isPass:
        display.scroll('CONGRATULATIONS YOUR SCORE %d'%score,delay = 75)
    else:
        display.scroll('GAME OVER YOUR SCORE %d'%score,delay = 75) 
ourgame()