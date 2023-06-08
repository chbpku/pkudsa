from microbit import *
from random import randint
import music

diffusion =       {3:2, 6:4, 9:3}    #扩散系数，用于衡量无生命细胞诞生生命的生命力
competitiveness = {3:1, 6:3, 9:2}    #周边的竞争力和>6则该细胞死亡
dependence =      {3:4, 6:0, 9:2}    #周围细胞数少于这个数值则细胞死亡
reverse_competitiveness = {value:key for key,value in competitiveness.items()}


# 定义函数：画出当前宇宙的状态
def draw_universe(universe):
    for y in range(1, 6):
        for x in range(1, 6):
            display.set_pixel(x-1, y-1, universe[x + y * 7])

def draw_rev_universe(universe, xx, yy):
    for y in range(1, 6):
        for x in range(1, 6):
            if not (x == xx and y == yy):
                display.set_pixel(x-1, y-1, universe[x + y * 7])

def evolve_1(universe):
    next_universe = universe[:]
    for y in range(1, 6):
        for x in range(1, 6):
            count_neighbours = get_neighbours_count(universe, x, y)
            if not universe[x + 7 * y]:
                if count_neighbours == 3:
                    next_universe[x + 7 * y] = 9   # 新生命的诞生
            else:
                if count_neighbours < 2:
                    next_universe[x + 7 * y] = 0  # 生命因孤独而死亡
                elif count_neighbours > 3:
                    next_universe[x + 7 * y] = 0  # 生命因拥挤而死亡
                else:
                    pass

    return next_universe

def evolve_2(universe):
    # 细胞分为 4 种：0, 3, 6, 9
    next_universe = universe[:]
    for y in range(1, 6):
        for x in range(1, 6):
            if not universe[x + 7 * y]:
                next_universe[x + 7 * y] = get_neighbours_diff(universe, x, y)

            else:
                count_neighbours, compet_neighbours = get_neighbours_cc(universe, x, y)
                if count_neighbours < dependence[universe[x+7*y]]:
                    next_universe[x + 7 * y] = 0  # 生命因孤独而死亡
                elif compet_neighbours >= 6:
                    next_universe[x + 7 * y] = 0  # 生命因拥挤而死亡
                else:
                    pass

    return next_universe

def get_neighbours_count(universe, x, y):
    count_neighbours = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                pass
            elif universe[(x + dx) + 7 * (y + dy)] == 0:
                pass
            else:
                count_neighbours += 1    
    return count_neighbours

def get_neighbours_diff(universe, x, y):
    compet_values = [value for value in competitiveness.values()]
    compet_values.sort(reverse = True)
    for value in compet_values:
        key = reverse_competitiveness[value]
        diff_count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    pass
                elif not universe[(x + dx) + 7 * (y + dy)]:
                    pass
                elif universe[(x + dx) + 7 * (y + dy)] == key:
                    diff_count += 1
                else:
                    pass
        if diff_count >= diffusion[key]:
            return key
    return 0


def get_neighbours_cc(universe, x, y):
    count_neighbours, compet_neighbours = 0, 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                pass
            elif not universe[(x + dx) + 7 * (y + dy)]:
                pass
            else:
                cur = universe[(x + dx) + 7 * (y + dy)]
                count_neighbours += cur // 3
                compet_neighbours += competitiveness[cur]
    return count_neighbours, compet_neighbours
    
# 定义函数：让指定坐标的 LED 灯闪烁一下
def blink_pixel(x, y):
    display.set_pixel(x, y, 6)
    sleep(500)
    display.set_pixel(x, y, 0)
    sleep(500)


# 定义函数：对指定坐标的 LED 灯进行设置
def pixel_set_1(x, y, light):
    while not button_a.is_pressed():
        blink_pixel(x-1, y-1)
        light = (display.read_light_level() < 30)
        if button_b.is_pressed() or light:
            break
    else:
        is_pressed_a = True
        sleep(500)
        while is_pressed_a:
            cur = current_universe[x + 7 * y]
            current_universe[x + 7 * y] = 9 if cur == 0 else 0 if cur == 9 else cur     # 循环设置 0 与 9
            display.set_pixel(x-1, y-1, current_universe[x + 7 * y])
            sleep(500)
            while True:
                light = (display.read_light_level() < 30)       # 通过光线传感器来判断是否需要退出
                if button_b.is_pressed() or light:
                    is_pressed_a = False
                    sleep(500)
                    break
                if button_a.is_pressed():
                    is_pressed_a = True
                    sleep(500)
                    break
    return light

def pixel_set_2(x, y, light):
    while not button_a.is_pressed():
        blink_pixel(x-1, y-1)
        light = (display.read_light_level() < 30)
        if button_b.is_pressed() or light:
            break
    else:
        is_pressed_a = True
        sleep(500)
        press_a_count = 1       
        while is_pressed_a:
            press_a_count %= 4
            current_universe[x + 7 * y] = press_a_count * 3     # 通过统计 A 键按下的次数来确定当前 LED 灯的状态 
            display.set_pixel(x-1, y-1, current_universe[x + 7 * y])
            sleep(500)
            while True:
                light = (display.read_light_level() < 30)
                if button_b.is_pressed() or light:
                    is_pressed_a = False
                    sleep(500)
                    break
                elif button_a.is_pressed():
                    is_pressed_a = True
                    press_a_count += 1
                    sleep(500)
                    break
    return light
    

current_universe = [0] * 49


# 主程序
display.scroll("Game of Life", wait = False)  # Game of Life
music.play(music.PYTHON, wait = False)
sleep(11000)
music.stop()
sleep(1000)
display.scroll("mod")
sleep(500)
display.show("1")
sleep(1000)
display.show(Image.ARROW_W)
sleep(1000)
display.show("2")
sleep(1000)
display.show(Image.ARROW_E)
sleep(1000)

while True:
    if button_a.is_pressed():
        game_mode = "mod1"
        display.show("1")
        sleep(1000)
        break
    elif button_b.is_pressed():
        game_mode = "mod2"
        display.show("2")
        sleep(1000)
        break

if game_mode == "mod1":
    mode = "SET"
    display.scroll(mode)
    while True:

        if mode == "RUN":
            if current_universe == [0] * 49:
                display.scroll("DEAD")
                mode = "SET"
                display.scroll(mode)
            
            current_universe = evolve_1(current_universe)
            draw_universe(current_universe)
            sleep(100)
            t_0 = running_time()
            while running_time() - t_0 < 1000:
                if button_a.is_pressed():
                    mode = "REV"
                    display.scroll(mode)
                    sleep(100)
                    break
                
                if button_b.is_pressed():
                    mode = "SET"
                    display.scroll(mode)
                    sleep(100)
                    break       # 按下 A 键，进入“修改”模式；按下 B 键，进入“设置”模式


        if mode == "SET":
            t_0 = running_time()
            while running_time() - t_0 < 10000:
                if accelerometer.current_gesture() == "shake":  
                    current_universe = [] 
                    current_universe.extend([0]*7)  
                    for i in range(5):
                        current_universe.append(0)
                        for _ in range(5):
                            current_universe.append(randint(0, 1) * 9)
                        current_universe.append(0)
                    current_universe.extend([0]*7) 
                    draw_universe(current_universe)
                    sleep(1000)    # 摇晃 Micro:bit，随机生成一个 5x5 的核心生命群落   

                if button_a.is_pressed():
                    sleep(1000)
                    light = False
                    current_universe = [0] * 49
                    for y in range(1, 6):
                        for x in range(1, 6):
                            light = pixel_set_1(x, y, light)
                            sleep(100)
                            if light:
                                break
                        if light:
                            break       # 用按键 A 设置初始生命群落
                    sleep(1000)

                if button_b.is_pressed():
                    mode = "RUN"
                    display.scroll(mode)
                    sleep(100)
                    draw_universe(current_universe)
                    sleep(1000)
                    break       # 用按键 B 开始运行

        if mode == "REV":
            light = False
            for y in range(1, 6):
                for x in range(1, 6):
                    draw_rev_universe(current_universe, x, y)
                    light = pixel_set_1(x, y, light)
                    sleep(100)
                    if light:
                        break
                if light:
                    break
            mode = "RUN"
            display.scroll(mode)        # 修改已有的生命群落

        draw_universe(current_universe)
        sleep(100)

if game_mode == "mod2":       
    mode = "SET"
    display.scroll(mode)
    while True:

        if mode == "RUN":
            if current_universe == [0] * 49:
                display.scroll("DEAD")
                mode = "SET"
                display.scroll(mode)

            current_universe = evolve_2(current_universe)
            draw_universe(current_universe)
            sleep(100)
            t_0 = running_time()
            while running_time() - t_0 < 1000:
                if button_a.is_pressed():
                    mode = "REV"
                    display.scroll(mode)
                    sleep(100)
                    break
                
                if button_b.is_pressed():
                    mode = "SET"
                    display.scroll(mode)
                    sleep(100)
                    break

        if mode == "SET":
            t_0 = running_time()
            while running_time() - t_0 < 10000:
                if accelerometer.current_gesture() == "shake":
                    current_universe = [] 
                    current_universe.extend([0]*7)  
                    for i in range(5):
                        current_universe.append(0)
                        for _ in range(5):
                            current_universe.append(randint(0, 3) * 3)
                        current_universe.append(0)
                    current_universe.extend([0]*7) 
                    draw_universe(current_universe)
                    sleep(1000)

                if button_a.is_pressed():
                    sleep(1000)
                    light = False
                    current_universe = [0] * 49
                    for y in range(1, 6):
                        for x in range(1, 6):
                            light = pixel_set_2(x, y, light)
                            sleep(100)
                            if light:
                                break
                        if light:
                            break
                    sleep(1000)

                if button_b.is_pressed():
                    mode = "RUN"
                    display.scroll(mode)
                    sleep(100)
                    draw_universe(current_universe)
                    sleep(1000)
                    break 

        if mode == "REV":
            light = False
            for y in range(1, 6):
                for x in range(1, 6):
                    draw_rev_universe(current_universe, x-1, y-1)
                    light = pixel_set_2(x, y, light)
                    sleep(100)
                    if light:
                        break
                if light:
                    break
            mode = "RUN"
            display.scroll(mode) 

        draw_universe(current_universe)
        sleep(100)