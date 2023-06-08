from microbit import *
import speech
import music

global inputcache
global password
global status
global message
message="CRAZY THURSDAY V ME 50"
password="AB"
inputcache=""
status="atrest"
display.show("A")



# atrest inputing unlocked resetpassword
def check():
    display.show("C")
    global inputcache
    global password
    global status
    if inputcache==password:
        inputcache=""
        display.show(Image.YES)
        sleep(1000)
        display.show(Image('00000:'
                           '09090:'
                           '00000:'
                           '90009:'
                           '09990'))
        music.play(music.ENTERTAINER)
        sleep(200)
        display.scroll(message,delay=50)   
        status="unlocked"
        display.show("U")
        
    else:
        inputcache=""
        display.show(Image.NO)
        sleep(1000)
        display.show(Image.SAD)
        music.play(music.BADDY)
        sleep(200)
        status="atrest"
        display.show("A")


while True:

    if button_a.is_pressed():
        if status=="inputing":
            inputcache+="A"
            sleep(500)
        elif status=="resetpassword":
            password+="A"
            sleep(500)

    if button_b.is_pressed():
        if status=="inputing":
            inputcache+="B"
            sleep(500)
        elif status=="resetpassword":
            password+="B"
            sleep(500)

    if pin0.is_touched():
        if status=="inputing":
            inputcache+="0"
            sleep(500)
        elif status=="resetpassword":
            password+="0"
            sleep(500)
    if pin1.is_touched():
        if status=="inputing":
            inputcache+="1"
            sleep(500)
        elif status=="resetpassword":
            password+="1"
            sleep(500)
    if pin2.is_touched():
        if status=="inputing":
            inputcache+="2"
            sleep(500)
        elif status=="resetpassword":
            password+="2"
            sleep(500)


    if pin_logo.is_touched():
        if status=="atrest":
            status="inputing"
            display.show("I")
            sleep(300)
        elif status=="inputing":
            check()
            sleep(300)
        elif status=="unlocked":
            status="atrest"
            display.show("A")
            sleep(300)
        elif status=="resetpassword":
            status="atrest"
            display.show("A")
            sleep(300)
            
    if status=="unlocked" and microphone.current_event() == SoundEvent.LOUD:
        password=""
        status="resetpassword"
        display.show("R")
        sleep(300)
        




