import serial
import serial.tools.list_ports as list_ports
from pykeyboard import PyKeyboard
from time import sleep
import requests

key = PyKeyboard()

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1

def find_comport(pid, vid, baud):
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None

def process(line):
    if "left" in line:
        key.press_key(key.left_key)
        sleep(0.010)
        key.release_key(key.left_key)
    if "right" in line:
        key.press_key(key.right_key)
        sleep(0.010)
        key.release_key(key.right_key)
    if "up" in line:
        key.press_key(key.up_key)
        sleep(0.010)
        key.release_key(key.up_key)
    if "down" in line:
        key.press_key(key.down_key)
        sleep(0.010)
        key.release_key(key.down_key)
    if "enter" in line:
        key.tap_key(key.enter_key)

def main():
    print('looking for microbit')
    ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
    if not ser_micro:
        print('microbit not found')
        return
    print('opening and monitoring microbit port')
    ser_micro.open()
    while True:
        line = ser_micro.readline().decode('utf-8')
        if line:  # If it isn't a blank line
            process(line)
        now = int(requests.get("http://127.0.0.1:8000/data").text)
        if now != 0:
            print(now)
            ser_micro.write((str(now)+'\n').encode('utf-8'))
    ser_micro.close()

main()