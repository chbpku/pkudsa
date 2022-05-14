import os
import math
import time
import copy
import Data
from collections import deque
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

dataread = True
advmodel = True
econtrol = False
observer = False
pd = 0.08 #使用此项调节瞳距

#导入世界的物理常数
TICKS_PER_SEC = 24
WALKING_SPEED = 3
FLYING_SPEED = -15
GRAVITY = 20.0
MAX_JUMP_HEIGHT = 1.0
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 50
PLAYER_HEIGHT = 2
headhight = {2:0.1,1:0.4}

path = os.path.join(os.path.dirname(__file__),'filesave.txt')
TEXTURE_PATH = 'texture.png'
MAN_PATH = 'man.png'
holyland={1:-1,2:-1,3:-1,4:-1,5:-1}
message=""

def cube_vertices(x, y, z, n, alpha=0):
    #通过定义每个方块的位置返回方块的6个面贴图位置
    if alpha ==0:
        return [
            x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,
            x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,
            x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,
            x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,
            x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,
            x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n
        ]
    elif alpha ==1:
        return [
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n
        ]
    elif alpha ==2:
        return [
            x-n,y+n,z, x+n,y+n,z, x+n,y-n,z, x-n,y-n,z,
            x-n,y+n,z, x+n,y+n,z, x+n,y-n,z, x-n,y-n,z,
            x-n,y+n,z, x+n,y+n,z, x+n,y-n,z, x-n,y-n,z,
            x-n,y+n,z, x+n,y+n,z, x+n,y-n,z, x-n,y-n,z,
            x-n,y+n,z, x+n,y+n,z, x+n,y-n,z, x-n,y-n,z,
            x-n,y+n,z, x+n,y+n,z, x+n,y-n,z, x-n,y-n,z
        ]
    elif alpha ==3:
        n=0.0001
        return [
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n,
            x,y+n,z-n, x,y+n,z+n, x,y-n,z+n, x,y-n,z-n
        ]
    elif alpha ==4:
        return [
            x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,
            x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,
            x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,
            x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,
            x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,
            x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n
        ]
    else:
        #(+,+,+)
        a=[x,y,z, x+n,y,z, x+n,y+n,z, x,y+n,z,
           x,y,z, x+n,y,z, x+n,y,z+n, x,y,z+n,
           x,y,z, x,y+n,z, x,y+n,z+n, x,y,z+n,
           x,y,z+n, x+n,y,z+n, x+n,y+n,z+n, x,y+n,z+n,
           x,y+n,z, x+n,y+n,z, x+n,y+n,z+n, x,y+n,z+n,
           x+n,y,z, x+n,y+n,z, x+n,y+n,z+n, x+n,y,z+n]
        #(-,+,+)
        b=[x,y,z, x-n,y,z, x-n,y+n,z, x,y+n,z,
           x,y,z, x-n,y,z, x-n,y,z+n, x,y,z+n,
           x,y,z, x,y+n,z, x,y+n,z+n, x,y,z+n,
           x,y,z+n, x-n,y,z+n, x-n,y+n,z+n, x,y+n,z+n,
           x,y+n,z, x-n,y+n,z, x-n,y+n,z+n, x,y+n,z+n,
           x-n,y,z, x-n,y+n,z, x-n,y+n,z+n, x-n,y,z+n]
        #(-,+,-)
        c=[x,y,z, x-n,y,z, x-n,y-n,z, x,y-n,z,
           x,y,z, x-n,y,z, x-n,y,z-n, x,y,z-n,
           x,y,z, x,y+n,z, x,y+n,z-n, x,y,z-n,
           x,y,z-n, x-n,y,z-n, x-n,y+n,z-n, x,y+n,z-n,
           x,y+n,z, x-n,y+n,z, x-n,y+n,z-n, x,y+n,z-n,
           x-n,y,z, x-n,y-n,z, x-n,y+n,z-n, x-n,y,z-n]
        #(+,+,-)
        d=[x,y,z, x+n,y,z, x+n,y+n,z, x,y+n,z,
           x,y,z, x+n,y,z, x+n,y,z-n, x,y,z-n,
           x,y,z, x,y+n,z, x,y+n,z-n, x,y,z-n,
           x,y,z-n, x+n,y,z-n, x+n,y+n,z-n, x,y+n,z-n,
           x,y+n,z, x+n,y+n,z, x+n,y+n,z-n, x,y+n,z-n,
           x+n,y,z, x+n,y+n,z, x+n,y+n,z-n, x+n,y,z-n]
        #(0,-,0)
        e=[x+n,y,z+n, x-n,y,z+n, x-n,y,z-n, x+n,y,z-n,
           x+n,y-n,z+n, x-n,y-n,z+n, x-n,y-n,z-n, x+n,y-n,z-n,
           x+n,y,z+n, x+n,y,z-n, x+n,y-n,z-n, x+n,y-n,z+n,
           x-n,y,z+n, x-n,y,z-n, x-n,y-n,z-n, x-n,y-n,z+n,
           x+n,y,z-n, x-n,y,z-n, x-n,y-n,z-n, x+n,y-n,z-n,
           x+n,y,z+n, x-n,y,z+n, x-n,y-n,z+n, x+n,y-n,z+n]
        if alpha ==-1:
            return a+b+e
        elif alpha ==-2:
            return b+c+e
        elif alpha ==-3:
            return c+d+e
        elif alpha ==-4:
            return d+a+e
                   
                   
                   
                   
            
            
    
def man_verticles(x, y, z, n, rotx):
    c = math.cos(math.radians(rotx+90))*n
    s = math.sin(math.radians(rotx+90))*n
    A=c-s
    B=c+s
    C=s-c
    D=-s-c
    a= [x+C,y+n,z+D, x+D,y+n,z+A, x+A,y+n,z+B, x+B,y+n,z+C,
        x+C,y-n,z+D, x+B,y-n,z+C, x+A,y-n,z+B, x+D,y-n,z+A,
        x+C,y-n,z+D, x+D,y-n,z+A, x+D,y+n,z+A, x+C,y+n,z+D,
        x+A,y-n,z+B, x+B,y-n,z+C, x+B,y+n,z+C, x+A,y+n,z+B,
        x+D,y-n,z+A, x+A,y-n,z+B, x+A,y+n,z+B, x+D,y+n,z+A,
        x+B,y-n,z+C, x+C,y-n,z+D, x+C,y+n,z+D, x+B,y+n,z+C
    ]
    return a

def man_body(x, y, z, n, rotx, op):
    c = math.cos(math.radians(rotx+90))*n
    s = math.sin(math.radians(rotx+90))*n
    A=c-s
    B=c+s
    C=s-c
    D=-s-c
    
    [x+C,y+n,z+D, x+D,y+n,z+A, x+A,y+n,z+B, x+B,y+n,z+C,
        x+C,y-n,z+D, x+B,y-n,z+C, x+A,y-n,z+B, x+D,y-n,z+A,
        x+C,y-n,z+D, x+D,y-n,z+A, x+D,y+n,z+A, x+C,y+n,z+D,
        x+A,y-n,z+B, x+B,y-n,z+C, x+B,y+n,z+C, x+A,y+n,z+B,
        x+D,y-n,z+A, x+A,y-n,z+B, x+A,y+n,z+B, x+D,y+n,z+A,
        x+B,y-n,z+C, x+C,y-n,z+D, x+C,y+n,z+D, x+B,y+n,z+C
    ]
    
    if op == 0:
        a=[x+(D+A)/2,y-n,z+(A+B)/2, x+(B+C)/2,y-n,z+(D+C)/2,
           x+(B+C)/2,y+n,z+(D+C)/2,x+(D+A)/2,y+n,z+(A+B)/2]*6
        
    if op == 1:
        a=[x+(C+D)/2,y-n,z+(A+D)/2, x+(A+B)/2,y-n,z+(B+C)/2,
           x+(A+B)/2,y+n,z+(B+C)/2,x+(C+D)/2,y+n,z+(A+D)/2]*6
    return a
    

#贴图函数
imagefunc={1:[0.75, 0.0, 1.0, 0.0, 1.0, 0.25, 0.75, 0.25, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75,4],
           2:[0.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.0, 0.5, 0.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.0, 0.5, 0.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.0, 0.5, 0.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.0, 0.5, 0.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.0, 0.5, 0.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.0, 0.5],
           3:[0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 1],
           4:[0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.0, 0.5, 0.0, 0.5, 0.25, 0.25, 0.25, 2],
           5:[0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 1],
           6:[0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 0.0, 0.75, 0.25, 0.75, 0.25, 1.0, 0.0, 1.0, 2],
           7:[0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5],
           18:[0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75],
           8:[0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25],
           9:[0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75, 0.5, 0.5, 0.75, 0.5, 0.75, 0.75, 0.5, 0.75],
           10:[0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75],
           11:[0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5],
           12:[0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5],
           13:[0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 1],
           14:[0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 0.25, 0.75, 0.5, 0.75, 0.5, 1.0, 0.25, 1.0, 2],
           15:[0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 1],
           16:[0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 0.5, 0.75, 0.75, 0.75, 0.75, 1.0, 0.5, 1.0, 2],
           17:[0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.25, 0.0, 0.25, 3],
           19:[0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75,-1],
           20:[0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75,-2],
           21:[0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75,-3],
           22:[0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75,-4],
          }



head1 =[0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.5, 1.0, 0.5, 1.0, 0.75, 0.75, 0.75, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5]
head2 =[0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.75, 1.0, 0.75, 1.0, 1.0, 0.75, 1.0, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5, 0.75, 0.25, 1.0, 0.25, 1.0, 0.5, 0.75, 0.5]
body1=[0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.25, 0.75, 0.5, 0.5, 0.5]
body2=[0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25, 0.5, 0.0, 0.75, 0.0, 0.75, 0.25, 0.5, 0.25]
body3=[0.75, 0.0, 1.0, 0.0, 1.0, 0.25, 0.75, 0.25, 0.75, 0.0, 1.0, 0.0, 1.0, 0.25, 0.75, 0.25, 0.75, 0.0, 1.0, 0.0, 1.0, 0.25, 0.75, 0.25, 0.75, 0.0, 1.0, 0.0, 1.0, 0.25, 0.75, 0.25, 0.75, 0.0, 1.0, 0.0, 1.0, 0.25, 0.75, 0.25, 0.75, 0.0, 1.0, 0.0, 1.0, 0.25, 0.75, 0.25]
transparent = {5, 6, 3, 4, 15, 16, 13, 14, 1, 9, 17}
playertangi = {7, 3, 4, 5, 6, 13, 14, 18, 8, 2, 10, 11, 12, 17, 13, 14}
playerupen={19, 20, 21, 22}
bullettangi = {7, 5, 6, 13, 14, 18, 8, 2, 10, 11, 12, 17, 19, 20, 21, 22}
boom =[0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75, 0.0, 0.5, 0.25, 0.5, 0.25, 0.75, 0.0, 0.75]

#查找和某个块相邻的6个块
FACES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]

def normalize(position):
    #对任意坐标返回其所属格
    x, y, z = position
    x, y, z = (int(round(x)), int(round(y)), int(round(z)))
    return (x, y, z)

def hit_test(position, num, vector):
    #通过给出三元组表示的人物位置和方向，整数射程，判断是否有被碰撞的方块
    if advmodel == True:
        max_distance = 99
        damage = 15
        m = 5
        x, y, z = position
        dx, dy, dz = vector
        previous = None
        for _ in range(max_distance * m):
            damage*=0.99
            key = normalize((x, y, z))
            for i in alive:
                x1,y1,z1 = i.pos
                if i.height == 2:
                    if ((x-x1)**2+(y-y1)**2+(z-z1)**2<=0.5 or(x-x1)**2+(y-y1-1)**2+(z-z1)**2<=0.5) and i.num != num:
                        return i.num, damage
                elif i.height == 1:
                    if (x-x1)**2+(y-y1)**2+(z-z1)**2<=0.5 and i.num != num:
                        return i.num, damage
            if key != previous and key in model.world and model.world[key] not in bullettangi:
                return None, key
            previous = key
            x, y, z = x + dx / m, y + dy / m, z + dz / m
        return None, None
    elif advmodel == False:
        max_distance = 5
        m = 5
        x, y, z = position
        dx, dy, dz = vector
        previous = None
        for _ in range(max_distance * m):
            key = normalize((x, y, z))
            if key != previous and key in model.world:
                return key, previous, 
            previous = key
            x, y, z = x + dx / m, y + dy / m, z + dz / m
        return None, None

default={1:100, 2:(25,2,25), 3:10, 4:(0, 0), 5:0, 6:0, 7:0, 8:[0,0], 9:False, 10:0}
pllist=[0,None,None]
alive=[]

class Player():
    def __init__(self,num=0):
        self.num=num
        self.life=default[1]
        if self.num==1:
            self.pos=(38,2,32)
            pllist[1]=self
            alive.append(self)
        elif self.num==2:
            self.pos=(48,10,44)
            pllist[2]=self
            alive.append(self)
        else:
            self.pos=default[2]
            pllist.append(self)
            alive.append(self)
        self.bullet=default[3]
        self.rot=default[4]
        if self.num == 1:
            self.rot = (0, 0)
        elif self.num == 2:
            self.rot = (180, 0)
        self.load=default[5]
        self.hurt=default[6]
        self.inwater=default[7]
        self.speed=default[8]
        self.fly=default[9]
        self.dy=default[10]
        self.height=PLAYER_HEIGHT
        self.half=0
        self.watercount = 0
        self.message = ""
        self.boom1=0
        self.boom2=0
        
        
    def checklife(self,damage):
        self.life-=damage
        if self.life<=0:
            self.life=0
            if self in alive:
                alive.remove(self)
        else:
            self.hurt=60
        
    def shoot(self):
        if self.load==0:
            if self.bullet>0:
                self.bullet-=1
                vector = self.get_sight_vector()
                n,m=hit_test(self.pos, self.num, vector)
                if n:
                    pllist[n].checklife(m)
                elif m:
                    if model.world[m] == 5:
                        model.remove_block(m)
                        model.add_block(m, 13)
                    elif model.world[m] == 6:
                        model.remove_block(m)
                        model.add_block(m, 14)
            else:
                self.load = 600
                
    def load(self):
        if self.bullet != 10 and self.load == 0:
            self.load += 600
                
    def get_motion_vector(self):
        #计算三维的速度方向和各方向大小
        if any(self.speed):
            x, y = self.rot
            speed = math.degrees(math.atan2(*self.speed))
            y_angle = math.radians(y)
            x_angle = math.radians(x + speed)
            if self.fly or self.inwater:
                m = math.cos(y_angle)
                dy = math.sin(y_angle)
                if self.speed[1]:
                    dy = 0.0
                    m = 1
                if self.speed[0] > 0:
                    dy *= -1
                dx = math.cos(x_angle) * m
                dz = math.sin(x_angle) * m
            else:
                dy = 0.0
                dx = math.cos(x_angle)
                dz = math.sin(x_angle)
        else:
            dy = 0.0
            dx = 0.0
            dz = 0.0
        return (dx, dy, dz)

    def update(self, dt):
        x,y,z = self.pos
        player1.pos=(38,2,32)
        if (x-49)**2+(y-2)**2+(z-1)**2<1:
            if holyland[1] != self.num:
                self.message="Strategic Point 1 Got Occupied"
                holyland[1] = self.num
                self.life += 30
        if (x-1)**2+(y-2)**2+(z-49)**2<1:
            if holyland[2] != self.num:
                self.message="Strategic Point 2 Got Occupied"
                holyland[2] = self.num
                self.life += 30
        if (x-49)**2+(y-3)**2+(z-49)**2<1:
            if holyland[3] != self.num:
                self.message="Strategic Point 3 Got Occupied"
                holyland[3] = self.num
                self.life += 30
        if (x-1)**2+(y-12)**2+(z-1)**2<1:
            if holyland[4] != self.num:
                self.message="Strategic Point 4 Got Occupied"
                holyland[4] = self.num
                self.life += 30
        if (x-20)**2+(y-6)**2+(z-27)**2<1:
            if holyland[5] != self.num:
                self.message="Strategic Point 5 Got Occupied"
                holyland[5] = self.num
                self.life += 30
        if normalize(self.pos) in model.world and model.world[normalize(self.pos)] == 1:
            self.inwater = 1
        else:
            self.inwater = 0
        if self.inwater and self.watercount < 0:
            self.jump()
            self.watercount = 60
        else:
            self.watercount -= 1
                
        x,y,z = normalize(self.pos)
        speed = FLYING_SPEED if self.fly else WALKING_SPEED
        d = dt * (speed-self.inwater*2)
        if self.load:
            d=0
            self.load -= 1
            if self.load%60==0:
                if self.bullet == 10:
                    self.load = 0
                else:
                    self. bullet += 1
        if self.num == 2:
            if self.boom1>0:
                self.boom1-=1
            if self.boom2>0:
                self.boom2-=1
        if self.hurt:
            self.hurt -=1
        dx, dy, dz = self.get_motion_vector()
        dx, dy, dz = dx * d, dy * d, dz * d
        if not (self.fly or self.inwater): 
            self.dy -= dt * (GRAVITY-self.inwater*10)
            self.dy = max(self.dy, -TERMINAL_VELOCITY+30*self.inwater)
            dy += self.dy * dt
        x, y, z = self.pos
        x, y, z = self.collide((x + dx, y + dy, z + dz), self.height)
        p = (x,y-self.height+1,z)
        po = normalize(p)
        xn,yn,zn = po
        if po in model.world.keys() and model.world[po] in playerupen:
            y = max(yn+1.5, y)
            self.half = 1
        else:
            self.half = 0
        self.pos = (x,y,z)
        lis=[]
        for i in alive:
            x1, y1, z1 = i.pos
            if (x-x1)**2+(y-y1)**2+(z-z1)**2>0.1:
                lis.append(i.num)
        return lis
    
    def get_sight_vector(self):
        #从视角方向计算正余弦
        x, y = self.rot
        m = math.cos(math.radians(y))
        dy = math.sin(math.radians(y))
        dx = math.cos(math.radians(x - 90)) * m
        dz = math.sin(math.radians(x - 90)) * m
        return (dx, dy, dz)

    def collide(self, position, height):
        #pad值决定了碰撞的范围有多大
        if self.height == 1:
            pad = 0.25
            p = list(position)
            np = normalize(position)
            for face in FACES:
                for i in range(3):
                    if not face[i]:
                        continue
                    d = (p[i] - np[i]) * face[i]
                    if d < pad:
                        continue
                    for dy in range(height):  # check each height
                        op = list(np)
                        op[1] -= dy
                        op[i] += face[i]
                        if tuple(op) not in model.world or (model.world[tuple(op)] not in playertangi and model.world[tuple(op)] not in playerupen):
                            continue
                        p[i] -= (d - pad) * face[i]
                        if face == (0, -1, 0) or face == (0, 1, 0):
                            self.dy = 0
                        break
            return tuple(p)
        else:
            if self.half:
                x,y,z = position
                position = x,y+0.5,z
            pad = 0
            p = list(position)            
            np = normalize(position)
            for face in FACES:
                for i in range(3):
                    if not face[i]:
                        continue
                    d = (p[i] - np[i]) * face[i]
                    if d < pad:
                        continue
                    for dy in range(height):  # check each height
                        op = list(np)
                        op[1] -= dy
                        op[i] += face[i]
                        if tuple(op) not in model.world or  model.world[tuple(op)] not in playertangi:
                            continue
                        p[i] -= (d - pad) * face[i]
                        if face == (0, -1, 0) or face == (0, 1, 0):
                            self.dy = 0
                        break
            if self.half:
                p[1]-=0.5
            g = copy.deepcopy(p)
            g[1] -= 1
            posit = normalize(tuple(g))
            if posit in model.world.keys() and model.world[posit] in playertangi:
                p[1]+=0.5
            return tuple(p)
    
    def squat(self):
        if self.height == 1:
            self.height = 2
            x,y,z = self.pos
            self.pos = x,y+1,z
        elif self.height == 2:
            self.height = 1
            x,y,z = self.pos
            self.pos = x,y-1,z
            
    def jump(self):
        if self.inwater:
            self.dy =max(JUMP_SPEED,self.inwater+JUMP_SPEED)
        elif self.dy == 0:
            self.dy = JUMP_SPEED
    
    def boom(self):
        if self.num ==1 and player2.boom1==0:
            x,y,z = self.pos
            x1,y1,z1 = player2.pos
            if (x-x1)**2+(y-y1)**2+(z-z1)**2<20:
                player2.checklife(20)
                return 1
            else:
                return 0

        elif self.num ==2 and player2.boom2==0:
            x,y,z = self.pos
            x1,y1,z1 = player1.pos
            if (x-x1)**2+(y-y1)**2+(z-z1)**2<20:
                player1.checklife(20)
                return 1
            else:
                return 0
        
            

class Model(object):

    def __init__(self, path, op=0):
        self.batch1 = pyglet.graphics.Batch()
        self.batch2 = pyglet.graphics.Batch()
        self.group = TextureGroup(image.load(path).get_texture())
        self.world = {}
        self.shown = {}
        self._shown = {}
        self.op = op
        #定义正在等待的操作队列
        self.queue = deque()
        self._initialize()

    def _initialize(self):
        if self.op==0:
            if dataread ==False:
                #在游戏开始时放置方块,设定半边长，步长和初始海拔
                n = 50
                s = 1
                y = 0
                for x in range(0, n + 1, s):
                    for z in range(0, n + 1, s):
                        #放置地基
                        self.add_block((x, y - 2, z), 18, immediate=False)
                        self.add_block((x, y - 3, z), 18, immediate=False)
                        self.add_block((x, y - 1, z), 18, immediate=False)
                        self.add_block((x, y, z), 18, immediate=False)
                        if x in (0, n) or z in (0, n):
                            #放置围墙
                            for dy in range(-2, 13):
                                self.add_block((x, y + dy, z), 18, immediate=False)
            else:
                file = open(path,"r")
                dicti = eval(file.readline())
                file.close()
                for i in dicti.keys():
                    self.add_block(i, dicti[i], immediate=False)
                    
        for i in self.world.keys():
            self.check_neighbors(i)
            

    def exposed(self, position):
        #如果一个位置被六方向包围，则返回0，否则返回1
        x, y, z = position
        if self.world[(x, y, z)] == 1 and (x, y + 1, z) in self.world and self.world[(x, y + 1, z)] == 1:
            return False
        for dx, dy, dz in FACES:
            if (x + dx, y + dy, z + dz) not in self.world or self.world[(x + dx, y + dy, z + dz)] in transparent:
                return True
        return False

    def add_block(self, position, texture, immediate=True):
        #使用三元组的位置和材质，以及是否立即刷新来把块加入/移出世界
        if position in self.world:
            self.remove_block(position, immediate)
        self.world[position] = texture
        if immediate:
            if self.exposed(position):
                self.show_block(position)
            self.check_neighbors(position)

    def remove_block(self, position, immediate=True):
        #将目标位置的块移出世界
        del self.world[position]
        if immediate:
            if position in self.shown:
                self.hide_block(position)
            self.check_neighbors(position)

    def check_neighbors(self, position):
        #对给定位置周围的块进行刷新
        x, y, z = position
        for dx, dy, dz in FACES:
            key = (x + dx, y + dy, z + dz)
            if key not in self.world:
                continue
            if self.exposed(key):
                if key not in self.shown:
                    self.show_block(key)
            else:
                if key in self.shown:
                    self.hide_block(key)

    def show_block(self, position, immediate=True):
        #令目标位置的块显形
        texture = self.world[position]
        self.shown[position] = texture
        if immediate:
            self._show_block(position, texture)
        else:
            self._enqueue(self._show_block, position, texture)

    def _show_block(self, position, texture):
        #上一个函数的内置函数
        x, y, z = position
        texture_data = imagefunc[texture]
        if len(texture_data)%2:
            vertex_data = cube_vertices(x, y, z, 0.5, texture_data[-1])
            if texture_data[-1]<0:
                texture_data = texture_data[0:-1]*3
                self._shown[position] = self.batch1.add(int(len(vertex_data)/3), GL_QUADS, self.group,('v3f/static', vertex_data),('t2f/static', texture_data))
            else:
                self._shown[position] = self.batch2.add(int(len(vertex_data)/3), GL_QUADS, self.group,('v3f/static', vertex_data),('t2f/static', texture_data[0:-1]))
        elif texture == 9:
            vertex_data = cube_vertices(x, y, z, 0.5)
            self._shown[position] = self.batch2.add(int(len(vertex_data)/3), GL_QUADS, self.group,('v3f/static', vertex_data),('t2f/static', texture_data))
        else:
            vertex_data = cube_vertices(x, y, z, 0.5)
            self._shown[position] = self.batch1.add(int(len(vertex_data)/3), GL_QUADS, self.group,('v3f/static', vertex_data),('t2f/static', texture_data))

    def hide_block(self, position, immediate=True):
        #令目标位置的块隐形
        self.shown.pop(position)
        if immediate:
            self._hide_block(position)
        else:
            self._enqueue(self._hide_block, position)

    def _hide_block(self, position):
        #上一个函数的内置函数
        self._shown.pop(position).delete()

    def _enqueue(self, func, *args):
        #堆入下一个函数流程
        self.queue.append((func, args))

    def _dequeue(self):
        #执行下一个函数流程
        func, args = self.queue.popleft()
        func(*args)

    def process_queue(self):
        #队列在方块的刷新不是立刻的情况下进行
        start = time.perf_counter()
        while self.queue and time.perf_counter() - start < 1.0 / TICKS_PER_SEC:
            self._dequeue()

    def process_entire_queue(self):
        #将队列的操作全部释出
        while self.queue:
            self._dequeue()
            
model=Model(TEXTURE_PATH)
       

class Window(pyglet.window.Window):
    def __init__(self, player, cop, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.silent = cop
        self.num = player.num
        self.player = player
        self.exclusive = False
        self.reticle = None
        self.inventory = [i for i in range(23)]
        self.block = self.inventory[1]
        self.model = Model(MAN_PATH, 1)
        self.count = 0
        self.hist=[]
        self.waterconut = 0
        
        self.num_keys = [0,
            key._1, key._2, key._3, key._4, key._5,
            key._6, key._7, key._8, key._9, key._0,
            key.Z,  key.X,  key.C,  key.V,  key.B,
            key.N,  key.M,  key.G,  key.H,  key.J,
            key.K,  key.Y,  key.U,  key.I,  key.O]

        for i in range(len(pllist)):
            if i !=self.num and i:
                x1,y1,z1 = pllist[i].pos
                rotx,roty = pllist[i].rot
                vertex_data = man_verticles(x1, y1+headhight[pllist[i].height], z1, 0.15, rotx)
                self.model._shown[i] = self.model.batch1.add(24, GL_QUADS, self.model.group,('v3f/static', vertex_data),('t2f/static', head1))
                vertex_data = man_body(x1, y1, z1, 0.5, rotx,0)
                self.model._shown[i+0.1] = self.model.batch2.add(24, GL_QUADS, self.model.group,('v3f/static', vertex_data),('t2f/static', body1))
                vertex_data = man_body(x1, y1-1, z1, 0.5, rotx,0)
                self.model._shown[i+0.2] = self.model.batch2.add(24, GL_QUADS, self.model.group,('v3f/static', vertex_data),('t2f/static', body2))

                


        self.label = pyglet.text.Label('', font_name='Arial', font_size=18,
            x=10, y=self.height - 10, anchor_x='left', anchor_y='top',
            color=(0, 0, 0, 255))
        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)

    def set_exclusive_mouse(self, exclusive):
        #确认鼠标的有无
        super(Window, self).set_exclusive_mouse(exclusive)
        self.exclusive = exclusive


    
    def update(self, dt):
        #每隔一段时间进行界面刷新
        model.process_queue()
        m = 8
        dt = min(dt, 0.2)
        for _ in range(m):
            lis=self.player.update(dt / m)
            for i in range(len(pllist)):
                if i in self.model._shown.keys():
                    self.model._shown.pop(i).delete()
                if i+0.1 in self.model._shown.keys():
                    self.model._shown.pop(i+0.1).delete()
                if i+0.2 in self.model._shown.keys():
                    self.model._shown.pop(i+0.2).delete()
        for i in lis:
            x1,y1,z1 = pllist[i].pos
            rotx,roty = pllist[i].rot
            vertex_data = man_verticles(x1, y1+headhight[pllist[i].height], z1, 0.15, rotx)
            if pllist[i].hurt:
                head=head2
            else:
                head=head1
            self.model._shown[i] = self.model.batch1.add(24, GL_QUADS, self.model.group,('v3f/static', vertex_data),('t2f/static', head))
            if pllist[i].height == 2:
                if (player2.boom1>0 and self.player.num==1) or (player2.boom2>0 and self.player.num==2):
                    body=boom
                    bodyy=body2
                    vertex_data = man_body(x1, y1, z1, 2, rotx,0)
                else:
                    body=body1
                    bodyy=body2
                    vertex_data = man_body(x1, y1, z1, 0.5, rotx,0)
                self.model._shown[i+0.1] = self.model.batch2.add(24, GL_QUADS, self.model.group,('v3f/static', vertex_data),('t2f/static', body))
                vertex_data = man_body(x1, y1-1, z1, 0.5, rotx,0)
                self.model._shown[i+0.2] = self.model.batch2.add(24, GL_QUADS, self.model.group,('v3f/static', vertex_data),('t2f/static', bodyy))
            else:
                if (player2.boom1>0 and self.player.num==1) or (player2.boom2>0 and self.player.num==2):
                    body=boom
                    vertex_data = man_body(x1, y1, z1, 2, rotx,0)
                else:
                    body=body3
                    vertex_data = man_body(x1, y1, z1, 0.5, rotx,0)    
                self.model._shown[i+0.2] = self.model.batch2.add(24, GL_QUADS, self.model.group,('v3f/static', vertex_data),('t2f/static', body))


        if econtrol and self.num==1 and self.silent:
            file=data.getData()
            if file == []:
                file=copy.deepcopy(self.file)
            else:
                self.file=copy.deepcopy(file)
            an = float(file[2])
            pitch = float(file[0])
            roll = float(file[1])
            if pitch > 0:
                pitch = 180-pitch
            else:
                pitch = -pitch-180
            if roll > 0:
                roll = -180+roll
            else:
                roll = roll+180
            w = file[3]
            a = file[4]
            d = file[5]
            s = file[6]
            b = file[7]
            rotx, roty = player1.rot
            if len(self.hist)<5:
                self.hist.append(pitch)
            else:
                sum = 0
                for i in self.hist:
                    sum+=i
                sum/=5
                dif = 0
                for i in self.hist:
                    dif+=(sum-i)**2
                dif/=5
                if dif < 0:
                    pitch = sum
            if abs(roll) > 0:
                player1.rot = rotx + 0.1 * roll, pitch
            else:
                player1.rot = rotx, pitch
            if self.count ==0:
                if abs(an-1020)>200:
                    player1.squat()
                    print(a)
                    self.count = 15
            if b:
                print(123)
                bo=player1.boom()
                if bo:
                    player2.boom1=240
                    
            else:
                self.count -= 1
            player1.speed=[0,0]
            if player1.life > 0:
                if w:
                    player1.speed[0] -= 1
                if a:
                    player1.speed[1] -= 1
                if d:
                    player1.speed[1] += 1
            if s and player1.life > 0:
                player1.shoot()
                
                
                
                
                
    def on_mouse_press(self, x, y, button, modifiers):
        #鼠标点击的操作
        if self.exclusive:
            vector = self.player.get_sight_vector()
            if advmodel == False:
                block, previous = hit_test(self.player.pos, self.num, vector)
                if button == mouse.RIGHT:
                    if previous:
                        model.add_block(previous, self.block)
                elif button == pyglet.window.mouse.LEFT and block:
                    texture = model.world[block]
                    model.remove_block(block)
            if advmodel == True and button == mouse.LEFT and self.player.life > 0:
                self.player.shoot()          
        else:
            self.set_exclusive_mouse(True)

    def on_mouse_motion(self, x, y, dx, dy):
        #视角随鼠标移动旋转
        if self.exclusive and self.num== 2:
            m = 0.15
            x, y = self.player.rot
            x, y = x + dx * m, y + dy * m
            y = max(-90, min(90, y))
            self.player.rot = (x, y)

    def on_key_press(self, symbol, modifiers):
        if self.player.life > 0 and self.exclusive and self.num==2:
        #使用方向键移动，空格键跳跃，TAB键飞行，数字键切换方块
            if symbol == key.W:
                player2.speed[0] -= 1
            elif symbol == key.S:
                player2.speed[0] += 1
            elif symbol == key.A:
                player2.speed[1] -= 1
            elif symbol == key.D:
                player2.speed[1] += 1
            elif symbol == key.ESCAPE:
                self.set_exclusive_mouse(False)
            elif symbol == key.TAB and advmodel == False:
                player2.fly = not player2.fly
            elif symbol in self.num_keys and advmodel == False:
                index = self.num_keys.index(symbol)
                self.block = self.inventory[index]
            elif symbol == key.SPACE:
                if player2.dy == 0:
                    player2.dy = JUMP_SPEED
                if player2.inwater:
                    player2.dy =max(JUMP_SPEED,player2.inwater+JUMP_SPEED)
            elif symbol ==key.L:
                file = open(path, 'w').close()
                file = open(path,"r+")
                file.write(str(model.world))
                file.close()
                print("File Saved")

    def on_key_release(self, symbol, modifiers):
        if self.player.life > 0 and self.num== 2 and self.exclusive:
        #长按方向键来连续移动
            if symbol == key.W:
                player2.speed[0] += 1
            elif symbol == key.S:
                player2.speed[0] -= 1
            elif symbol == key.A:
                player2.speed[1] += 1
            elif symbol == key.D:
                player2.speed[1] -= 1
            elif symbol == key.B:
                player2.squat()
            elif symbol == key.H:
                bo=player2.boom()
                if bo:
                    player2.boom2=240
                

    def on_resize(self, width, height):
        #缩放游戏界面
        self.label.y = height - 10
        #控制十字准星
        if self.reticle:
            self.reticle.delete()
        x, y = self.width // 2, self.height // 2
        n = self.height//25
        m = self.height//200
        k = self.height//200
        self.reticle = pyglet.graphics.vertex_list( 12,
            ('v2i', (x - n, y + k, x - n, y - k, x - m, y, 
                     x + n, y + k, x + n, y - k, x + m, y,
                     x - k, y + n, x + k, y + n, x, y + m,
                     x - k, y - n, x + k, y - n, x, y - m
                     ))
        )

    def set_2d(self):
        #绘制2D画面
        width, height = self.get_size()
        glDisable(GL_DEPTH_TEST)
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set_3d(self):
        #绘制3D画面
        width, height = self.get_size()
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, width / float(height), 0.1, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        x, y = self.player.rot
        glRotatef(x, 0, 1, 0)
        glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
        x, y, z = self.player.pos
        rotx, roty = self.player.rot
        
        glTranslatef(-x+self.silent*math.cos(math.radians(rotx)), -y-0.3, -z-self.silent*math.sin(math.radians(rotx)))

    def on_draw(self):
        #调用整个绘制函数
        self.clear()
        glColor4d(1, 1, 1, 1)
        self.set_3d()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)
        model.batch1.draw()
        self.model.batch1.draw()
        self.draw_focused_block()
        glDepthMask(GL_FALSE)
        glColor4d(1, 1, 1, 0.5)
        model.batch2.draw()
        self.model.batch2.draw()
        glDepthMask(GL_TRUE)
        self.set_2d()
        self.draw_label()
        self.draw_reticle()

    def draw_focused_block(self):
        #绘制当前被选中的块的外围，此处还需认真研究
        if advmodel == False: 
            vector = self.player.get_sight_vector()
            block = hit_test(self.player.pos, self.num, vector)[0]
            if block:
                x, y, z = block
                vertex_data = cube_vertices(x, y, z, 0.51)
                glColor3d(0, 0, 0)
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                pyglet.graphics.draw(int(len(vertex_data)/3), GL_QUADS, ('v3f/static', vertex_data))
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def draw_label(self):
        #绘制文字描述
        if self.player.life > 0:
            x, y, z = self.player.pos
            if self.silent:
                s="L"
            else:
                s="R"
            self.label.text = s+self.player.message+'%02d (%.2f, %.2f, %.2f), %01d, %.01d, %01d' % (
                pyglet.clock.get_fps(), x, y, z, self.player.life, self.player.bullet, self.player.load)
            self.label.draw()

    def draw_reticle(self):
        #绘制十字准星
        glColor4d(1, 0, 0, 0.5)
        if self.silent:
            self.reticle.draw(GL_TRIANGLES)
        if normalize(self.player.pos) in model.world and model.world[normalize(self.player.pos)] == 1:
            glColor4d(0.5, 0.7, 1, 0.3)
            self.water = pyglet.graphics.vertex_list(4,
            ('v2i', (0, 0, 9999, 0, 9999, 9999, 0, 9999))
        )
            self.water.draw(GL_POLYGON)
        if 0 < self.player.life < 50:
            glColor4d(1, 0, 0, (50-self.player.life)/150)
            self.blood = pyglet.graphics.vertex_list(4,
            ('v2i', (0, 0, 9999, 0, 9999, 9999, 0, 9999))
        )
            self.blood.draw(GL_POLYGON)
        countit = 0
        for i in holyland.keys():
            if holyland[i]!=-1 and holyland[i]!=self.player.num:
                countit+=1
        if self.player.life <= 0 or countit >=4 :
            self.label.text = 'You Died!'
            self.label.draw()
            glColor4d(0.3, 0.3, 0.3, 0.5)
            self.blood = pyglet.graphics.vertex_list(4,
            ('v2i', (0, 0, 9999, 0, 9999, 9999, 0, 9999))
        )
            self.blood.draw(GL_POLYGON)
            
        
def setup():
    #配置天空背景颜色
    glClearColor(0.5, 0.69, 1.0, 1)
    #修正图像绘制的缩放问题
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

def main():
    #设定窗口和基本流程
    
    window2 = Window(player2, pd, width=800, height=800,resizable=True)
    window2.set_exclusive_mouse(True)
    window2.set_location( 100 , 100)
    setup()
    if advmodel == True:
        window4 = Window(player1, pd, width=1300, height=1300,resizable=True)
        window4.set_exclusive_mouse(False)
        window4.set_location( 2800 , 0 )
        setup()
        window1 = Window(player1, 0, width=1300, height=1300,resizable=True)
        window1.set_exclusive_mouse(False)
        window1.set_location( 4100 , 0 )
        setup()
        if observer == True:
            window3 = Window(player1, 0, width=800, height=800,resizable=True)
            window3.set_exclusive_mouse(False)
            window3.set_location( 800 , 100 )
            setup()
    
    pyglet.app.run()


if __name__ == '__main__':
    import threading
    import serial
    import keyboard
    
    player1=Player(1)
    player2=Player(2)
    #player3=Player(3)
    if econtrol:
        data=Data.Data()
        data.beginGettingData()
    hisp=[]
    main()
    if econtrol:
        ser.close()
