import serial
import serial.tools.list_ports as list_ports

def find_microbit_comport():
    ports = list(list_ports.comports())
    for p in ports:
        if (p.pid == 516) and (p.vid == 3368):
            return str(p.device)
def check_button_to_move_cb(s):
    if "a" in s:
        return "A"
    else:
        return "B"
def printtest():
    print("a")
if __name__ == '__main__':
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.timeout = 1
    ser.port = find_microbit_comport()
    ser.open()
    #ser.write(b'testing')
    text = ser.read()
   # while text != b'':
       # check_button_to_move_cb(text.decode('utf-8'))
        #text = ser.read()

    print("a")
    ser.close()