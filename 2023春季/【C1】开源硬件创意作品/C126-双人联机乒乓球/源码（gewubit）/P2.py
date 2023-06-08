import gewu
import network
import time
import ujson
from umqtt import MQTTClient
#网络连接初始化
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    gewu.display.fill(OLED.BLACK)
    gewu.display.text('connecting...', 0, 0, 6)
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
gewu.display.text(str('wait for p1 to start'),0,38, 6)
gewu.display.show()

ssid='c1phyf'
passwd='c1phyf'
client_id='usersnamef'
mserver = 'mq.tongxinmao.com'
port=18830
topic_ctl = b'/public/TEST/jwebcli'
topic_sta = b'/public/TEST/jwebcli'

def sub_callback(topic,msg):
    global x
    global wl
    str_msg=msg.decode()
    bxp,byp,dxp,dyp,wl=str(str_msg).split('#')
    if wl=='b':
        gewu.display.fill(OLED.BLACK)
        gewu.display.text(str('wait for p1 to start'),0,38, 6)
        gewu.display.show()
    
    if wl=='f':
        bx=133-int(bxp)
        by=-int(byp)
        dx=-int(dxp)
        dy=-int(dyp)
        location=str(bx)+'#'+str(by)+'#'+str(dx)+'#'+str(dy)+'#'+wl
        if gewu.button_b.is_pressed():
            x+=2
        if gewu.button_a.is_pressed():
            x-=2
        gewu.display.fill(OLED.BLACK)
        gewu.display.text(str('__'),x%113,38, 11)
        gewu.display.text(location,0,0,6)
        if 0<=by<=38:
            gewu.display.text(str('.'),bx,by, 11)
        gewu.display.show()
    if wl=='t':
        gewu.display.fill(OLED.BLACK)
        gewu.display.text('you win',0,0,6)
        gewu.display.text(str('wait for p1 to restart'),0,38, 6)
        gewu.display.show()
        str_msg=msg.decode()
        bxp,byp,dxp,dyp,wl=str(str_msg).split('#')
        
        

client = MQTTClient(client_id,mserver,port)
client.set_callback(sub_callback)
client.connect()
client.subscribe(topic_ctl)

x=0
wl='b'
while True:
    client.check_msg()