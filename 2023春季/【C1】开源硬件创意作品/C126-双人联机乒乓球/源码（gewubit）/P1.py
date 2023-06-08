import gewu
import network
import time
import ujson
from umqtt import MQTTClient
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    gewu.display.fill(OLED.BLACK)
    gewu.display.text(str('connecting...'),1,0,6)
    gewu.display.show()
    wlan.connect('yyb','12345678')
    while not wlan.isconnected():
        pass
while (wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
gewu.display.fill(OLED.BLACK)
string='network config[0]:',wlan.ifconfig()[0]
gewu.display.text(str('OK'),1,0,6)
gewu.display.show()
time.sleep(1)

gewu.display.fill(OLED.BLACK)
gewu.display.text(str('OK'),1,0,6)
gewu.display.show()

ssid='yybphy'
passwd='yybphy'
client_id='usersname'
mserver = 'mq.tongxinmao.com'
port=18830
topic_ctl = b'/public/TEST/jwebcli'
topic_sta = b'/public/TEST/jwebcli'

def sub_callback(topic,msg):
    pass

    
#消息发送  
client = MQTTClient(client_id,mserver,port)
client.set_callback(sub_callback)
client.connect()
client.subscribe(topic_ctl)

x=0
bx,by=2,2
dx,dy=1,1
s=0
while True:
    gewu.display.fill(OLED.BLACK)
    gewu.display.text(str('press a to switch'),0,0,6)
    gewu.display.text(str('press b to confirm'),0,8,6)
    gewu.display.text(str('easy'),0,16,6)
    gewu.display.text(str('mild'),0,24,6)
    gewu.display.text(str('hard'),0,32,6)
    gewu.display.text(str('<--'),50,16+s*8,6)
    if gewu.button_a.is_pressed():
        s+=1
        s=s%3
    if gewu.button_b.is_pressed():
        if s==0:
            dx,dy=1,1
            delta_x=1
        if s==1:
            dx,dy=2,2
            delta_x=2
        if s==3:
            dx,dy=3,3
            delta_x=3
        break
    gewu.display.show()
while True:
    while True:
        if gewu.button_b.is_pressed():
            x+=delta_x
        if gewu.button_a.is_pressed():
            x-=delta_x
        if bx<2 or bx>110:
            dx=-dx
        if by<-36:
            dy=-dy
        if (by>36):
            if (bx%133>=x%113-12 and bx%133<=x%113+12):
                dy=-dy
            else:
                break
        bx+=dx
        by+=dy
        location=str(bx)+'#'+str(by)+'#'+str(dx)+'#'+str(dy)+'#'+'f'
        client.publish(topic_sta,location,retain=True)
        client.check_msg()
        gewu.display.fill(OLED.BLACK)
        gewu.display.text(location,0,0,6)
        gewu.display.text(str('__'),x%113,38, 11)
        if 0<=by<=38:
            gewu.display.text(str('.'),bx,by, 11)
        gewu.display.show()

    while True:
        gewu.display.fill(OLED.BLACK)
        gewu.display.text(str('you lose'),1,1,6)
        gewu.display.text(str('press a to continue'),1,38,6)
        gewu.display.show()
        location=str(bx)+'#'+str(by)+'#'+str(dx)+'#'+str(dy)+'#'+'t'
        client.publish(topic_sta,location,retain=True)
        client.check_msg()
        if gewu.button_a.is_pressed():
            break