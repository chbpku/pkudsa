from microbit import *
import radio
N0=Image("06660:06060:06060:06060:06660")
N1=Image("00600:06600:00600:00600:06660")
N2=Image("06660:00060:06660:06000:06660")
N3=Image("06660:00060:06660:00060:06660")
N4=Image("06060:06060:06660:00060:00060")
N5=Image("06660:06000:06660:00060:06660")
N6=Image("06000:06000:06660:06060:06660")
N7=Image("06660:00060:00060:00060:00060")
N8=Image("06660:06060:06660:06060:06660")
N9=Image("06660:06060:06660:00060:00060")
Stop=Image("60006:06060:00600:06060:60006")
Nlst=[N0,N1,N2,N3,N4,N5,N6,N7,N8,N9,Stop]

lst1=[(0,0),(0,3),(3,3),(3,0)]
lst2=[(1,0),(0,2),(2,3),(3,1)]
lst3=[(2,0),(0,1),(1,3),(3,2)]
lst4=[(1,1),(1,2),(2,2),(2,1)]

def nextt(x):
    for lst in [lst1,lst2,lst3,lst4]:
        if x in lst:
            return lst[lst.index(x)-1]

def turn(lst):
    return [nextt(x) for x in lst]

def shuru():
    cin=""
    curN=0
    stop=False
    while not stop:
        if button_b.was_pressed():
            display.clear()
            curN=(curN+1)%11
        display.show(Nlst[curN])
        if button_a.was_pressed():
            if curN==10:
                stop=True
            else:
                cin+=str(curN)
                curN=0
    return cin

def Ten_To_Four(n):
    out=""
    while n!=0:
        out=str(n%4)+out
        n=n//4
    return out
def Four_To_Ten(s):
    out=0
    for i in range(len(list(s))):
        out+=int(list(s)[-i-1])*(4**i)
    return out
def pulse():
        for i in range(5):
            display.set_pixel(i,4,8)
            sleep(10)

        for j in range(4):
            display.set_pixel(4,3-j,8)
            sleep(10)
        for i in range(5):
            display.set_pixel(i,4,0)
            sleep(10)

        for j in range(4):
            display.set_pixel(4,3-j,0)
            sleep(10)

#按a键留空，按b键不空
def choose_pos():
    pos=[]
    cur=0
    for x in [lst1,lst2,lst3,lst4]:
        display.set_pixel(x[0][0],x[0][1],5)
        display.set_pixel(x[1][0],x[1][1],5)
        display.set_pixel(x[2][0],x[2][1],5)
        display.set_pixel(x[3][0],x[3][1],5)
        while not button_b.was_pressed():
            pulse()
            display.set_pixel(x[cur][0],x[cur][1],9)
            sleep(50)
            display.set_pixel(x[cur][0],x[cur][1],0)
            sleep(50)
            if button_a.was_pressed():
                display.set_pixel(x[cur][0],x[cur][1],5)
                cur=(cur+1)%4
        display.set_pixel(x[0][0],x[0][1],0)
        display.set_pixel(x[1][0],x[1][1],0)
        display.set_pixel(x[2][0],x[2][1],0)
        display.set_pixel(x[3][0],x[3][1],0)
        pos.append(x[cur])
    pos=sorted(pos)
    return pos

def showw(pos):
    for x in range(4):
        for y in range(4):
            if (x,y) not in pos:
                display.set_pixel(x,y,7)

#s长为4
def tick(pos,s):
    for i in range(5):
        display.set_pixel(i,4,0)

    if len(s)==1:
        display.set_pixel(0,4,int(s[0]))
        sleep(1000)
        display.set_pixel(0,4,0)
        display.set_pixel(pos[0][0],pos[0][1],int(s[0]))
        sleep(1000)
    else:
        for i in range(len(s)):
            display.set_pixel(i,4,int(s[i]))
        sleep(1000)
        display.set_pixel(pos[0][0],pos[0][1],int(s[0]))
        tick(pos[1:],s[1:])


def Encrypt(cin4,pos):
    mingwen=cin4+"0"*(16-len(cin4))
    display.show(Image("00000:00000:00000:00000:00000"))

    for i in range(4):
        for j in range(4):
            display.set_pixel(i,j,3*int(mingwen[4*i+j]))
            sleep(400)

    sleep(4000)
    #装饰
    display.show(Image(
        "00000:"
        "00900:"
        "09990:"
        "00900:"
        "00000"))
    sleep(1000)
    display.show(Image(
        "00000:"
        "09990:"
        "09990:"
        "09990:"
        "00000"))
    sleep(1000)
    display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
    sleep(1000)

    display.show(Image("00000:00000:00000:00000:00000"))
    sleep(500)
    dic={}
    curpos=pos
    for i in range(4):
        showw(curpos)
        sleep(1000)
        s=[3*int(x) for x in mingwen[4*i:4*i+4]]
        tick(curpos,s)
        for x in curpos:
            dic[x]=display.get_pixel(x[0],x[1])
        curpos=turn(curpos)
        display.clear()
        sleep(200)

    sleep(1000)

    miwen=""
    for x in range(4):
        for y in range(4):
            miwen+=str(dic[(x,y)]//3)
            sleep(30)
    miwen=miwen+"_"+str(len(str(cin4)))
    return miwen

def Decrypt(miwen,pos):
    l=int(miwen[17])
    dic={(x,y):0 for x in range(4)
                    for y in range(4)}
    for x in range(4):
        for y in range(4):
            dic[(x,y)]=int(miwen[4*x+y])
    mingwen=""
    curpos=pos
    for i in range(4):
        for x in curpos:
            mingwen+=str(dic[x])
        curpos=turn(curpos)
    return mingwen[0:l]

def A():#加密
    cin=int(shuru())
    cin4=Ten_To_Four(cin)
    display.clear()
    pos=choose_pos()
    miwen=Encrypt(cin4,pos)
    display.scroll(miwen)
    sleep(3000)
    display.scroll("sending")
    radio.on()
    radio.send(miwen[miwen.index("_")+1:])
    recive=None
    while not recive:
        display.show(Stop)
        recive=radio.receive()
        sleep(500)
        display.clear()
    display.show(Image("00000:00009:00090:90900:09000"))
    sleep(1000)
    for x in miwen[:miwen.index("_")]:
        display.show(x)
        radio.send(x)
        sleep(1000)
        display.clear()
        sleep(100)

    display.clear()

def B():
    radio.on()
    pos=choose_pos()
    while True:
        countt=radio.receive()
        if countt:
            display.show(Image("00000:00009:00090:90900:09000"))
            sleep(500)
            radio.send("hello")

            miwen=""
            c=1
            while c<=16:
                x=radio.receive()
                if x:
                    display.show(x)
                    sleep(1000)
                    display.clear()
                    sleep(100)
                    miwen+=x
                    c+=1
            mingwen=Four_To_Ten(Decrypt(miwen+"_"+countt,pos))
            display.scroll(mingwen)
            sleep(10000)
            break
        else:
            showw(pos)



while True:
    if button_a.was_pressed():
        A()
    if button_b.was_pressed():
        B()
