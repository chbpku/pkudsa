from microbit import *
import music

# 此版本未加注释，注释版请见实习报告

while True:
    if pin_logo.is_touched():
        display.show(Image.HAPPY)
        music.play(music.POWER_UP)
        sleep(500)
        display.show(1, delay=1000)
        player_1, player_2 = None, None
        loop_1, loop_2 = True, False

        while loop_1:
            if button_a.is_pressed():
                music.play(music.BA_DING)
                display.show(Image.YES, delay=2000)
                loop_1 = False
                loop_2 = True

                while loop_2:
                    if button_a.is_pressed():
                        loop_2 = False
                        music.play(music.BA_DING)
                        display.show(Image.YES)
                        player_1 = True
                    elif button_b.is_pressed():
                        loop_2 = False
                        music.play(music.BA_DING)
                        display.show(Image.NO)
                        player_1 = False

            elif button_b.is_pressed():
                loop_1 = False
                loop_2 = True
                music.play(music.BA_DING)
                display.show(Image.NO)

                while loop_2:
                    if button_b.is_pressed():
                        loop_2 = False
                        music.play(music.BA_DING)
                        display.show(Image.NO)
                        player_1 = False
                    elif button_a.is_pressed():
                        loop_2 = False
                        music.play(music.BA_DING)
                        display.show(Image.YES)
                        player_1 = True

        sleep(1000)
        display.show(2, delay=1000)
        loop_1 = True

        while loop_1:
            if button_a.is_pressed():
                loop_1 = False
                loop_2 = True
                music.play(music.BA_DING)
                display.show(Image.YES)

                while loop_2:
                    if button_a.is_pressed():
                        loop_2 = False
                        music.play(music.BA_DING)
                        display.show(Image.YES)
                        player_2 = True
                    elif button_b.is_pressed():
                        loop_2 = False
                        music.play(music.BA_DING)
                        display.show(Image.NO)
                        player_2 = False

            elif button_b.is_pressed():
                loop_1 = False
                loop_2 = True
                music.play(music.BA_DING)
                display.show(Image.NO)

                while loop_2:
                    if button_b.is_pressed():
                        loop_2 = False
                        display.show(Image.NO)
                        player_2 = False
                    elif button_a.is_pressed():
                        loop_2 = False
                        display.show(Image.YES)
                        player_2 = True

        if all([player_1, player_2]):
            sleep(1000)
            display.show(Image.HEART)
            music.play(music.WEDDING)

        else:
            sleep(1000)
            display.show(Image.SAD)
            music.play(music.WAWAWAWAA)




