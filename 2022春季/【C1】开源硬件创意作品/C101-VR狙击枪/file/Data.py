import serial
import threading
import time

class Data:
    def __init__(self):

        # 初始化接口
        self.serialport = serial.Serial(
                                    port = 'COM4',
                                    baudrate = 115200,
                                    bytesize = 8,
                                    parity = serial.PARITY_NONE,
                                    stopbits = 1,
                                    timeout = 0.005
                                    )

        # 数据队列
        self.dataQueue = []

        # 踏板数据
        self.action = {
                    'w': False, # 前进
                    'a': False, # 左移
                    'd': False, # 右移
                    's': False, # 开枪
                    'f': False, # 手榴弹
                    }

        # 接口数据队列
        self.dataFromSerialQueue = ''

        # 数据获取状态
        self.dataGetting = False


    def beginGettingData(self):

        if not self.serialport.is_open:
            self.serialport.open() # 打开接口

        debug = False

        def gettingData():
            while True:
                time.sleep(0.02)
                # 读取串口发送数据
                self.dataFromSerialQueue += self.serialport.read_until(expected = b'\n').decode('utf-8')

                x = self.dataFromSerialQueue.find('/')

                if debug:
                    print('begin')
                    print(self.dataFromSerialQueue)
                    print('end')
                
                if x >= 0: # 找到数据结尾, 处理本组数据
                    if not self.dataGetting:    # 启动获取数据(可能意味着损失第一组数据)
                        self.dataGetting = True
                    else:
                        try :
                            pitch, roll, z, w, a, d, s, f = map(int,self.dataFromSerialQueue[:x].split(',')) # 数据协议
                        except ValueError:
                            print('ValueError')
                            self.dataFromSerialQueue = self.dataFromSerialQueue[x + 1:]
                            continue

                        if debug:
                            print('start')
                            print(pitch, roll, a) # debug
                            print('finish')
                        
                        self.dataQueue.append([pitch, roll, z, w, a, d, s, f])
                    self.dataFromSerialQueue = self.dataFromSerialQueue[x + 1:]
                
                if debug:
                    print(self.dataQueue)
        
        GetDataThread = threading.Thread(target = gettingData) # 创建线程
        GetDataThread.start()


    def getData(self):
        if self.dataQueue:
            return self.dataQueue.pop(0)
        else:
            return []


    def stopGettingData(self):
        self.dataQueue = [] # 清空数据队列
        self.dataFromSerialQueue = '' # 清空接口数据队列
        self.dataGetting = False # 停止接收数据
        if self.serialport.is_open:
            self.serialport.close() # 关闭端口


if __name__ == "__main__":
    import pybullet as p
    import keyboard
    import time
    import math
    import pandas as pd

    p.connect(p.GUI)
    boxId = p.createCollisionShape(p.GEOM_BOX, halfExtents = [1, 1.5, 0.2])
    boxMId = p.createMultiBody(
                            baseCollisionShapeIndex = boxId,
                            basePosition = [0, 0, 0],
                            baseOrientation = [0, 0, 0, 1]
                            )

    data = Data()
    data.beginGettingData()

    running = True
    while running:
        if data.dataQueue:
            pitch, roll, z, w, a, d, s, f = data.getData()
        else:
            time.sleep(0.01)
            continue
        
        p.resetBasePositionAndOrientation(
                                        boxId,
                                        posObj = [0, 0, 0],
                                        ornObj = p.getQuaternionFromEuler(list(map(lambda x : x*math.pi/180, [-roll, pitch, 0])))
                                        )