from _serialconnection import *
import pgzrun
ser = serial.Serial()
ser.baudrate = 115200
ser.timeout = 1
ser.port = find_microbit_comport()

WIDTH=1000
HEIGHT=500
things=["real_black3","real_black"]
real_things=[]
def draw():
    screen.clear()
    screen.blit("bkgrd",(0,0))
    alien.draw()
    for r in real_things:
        r.draw()
def update():
    ser.open()
    text=ser.read()
    if "a" in text.decode("utf-8","ignore"):
        
        alien.left+=2
  
    if "b" in text.decode("utf-8","ignore"):
        alien.left-=2
    if "c" in text.decode("utf-8","ignore"):
        alien.y+=50
    if "d" in text.decode("utf-8","ignore"):
        set_cb_to_a_picapica()
        for t in things:
            real_things.append(Actor(t))
    for rr in real_things:
        rr.y+=5
        if rr.y>HEIGHT:
            rr.y=0
            
    if alien.left>WIDTH:
        alien.left=0
    if alien.left<0:
        alien.left=WIDTH
    if alien.y>HEIGHT:
        alien.y=0
    ser.close()
def set_cb_to_a_picapica():#彩蛋是cb变身！
    alien.image="real_cb_1"
alien=Actor("real_cb")
alien.topright=0,10
    

ser.close()
pgzrun.go()