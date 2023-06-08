from microbit import *
import random

# 难度列表
DIFFICULTIES = {
    'easy': 3,
    'medium': 6,
    'hard': 9
}

# 选择难度函数
def select_difficulty():
    display.scroll("Select difficulty:")
    options = list(DIFFICULTIES.keys())
    index = 0
    display.show(options[index])
    while True:
        if button_a.was_pressed() and index > 0:
            index -= 1
            display.show(options[index])
        elif button_b.was_pressed() and index < len(options) - 1:
            index += 1
            display.show(options[index])
        elif pin_logo.is_touched():
            return DIFFICULTIES[options[index]]
        sleep(100)

# 获取难度并设置地雷数量
NUM_MINES = select_difficulty()


# 游戏区域大小
WIDTH = 5
HEIGHT = 5


# 周围8个方块的偏移量
OFFSETS = [(-1, -1), (0, -1), (1, -1),
           (-1, 0), (1, 0),
           (-1, 1), (0, 1), (1, 1)]

# 游戏区域状态：0表示未扫描，1表示已扫描，2表示地雷
board = [[0 for y in range(HEIGHT)] for x in range(WIDTH)]

# 随机生成地雷位置
mines = []
while len(mines) < NUM_MINES:
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    if (x, y) not in mines:
        mines.append((x, y))
        board[x][y] = 2

# 初始化光标位置和游戏状态
cursor_x = 0
cursor_y = 0
game_over = False


# 显示游戏区域函数
def display_board():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if cursor_x == x and cursor_y == y:
                # 光标所在位置
                display.set_pixel(x, y, 9)
            elif board[x][y] == 1:
                # 已扫描的方块
                display.set_pixel(x, y, 5)
            else:
                # 未扫描的方块
                display.set_pixel(x, y, 0)


# 显示地雷数量函数
def display_mine_count():
    if game_over:
        return
    count = sum(1 for (mx, my) in mines if abs(mx - cursor_x) <= 1 and abs(my - cursor_y) <= 1)
    display.scroll(str(count))


# 扫描周围方块函数
def reveal(x, y):
    global game_over
    if board[x][y] == 2:
        # 按中了地雷处理
        game_over = True
        display.set_pixel(x, y, 9)
        display.scroll('Game Over!')
    elif board[x][y] == 0:
        # 扫描周围8个方块
        mines_count = 0
        for off_x, off_y in OFFSETS:
            nx, ny = x + off_x, y + off_y
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and board[nx][ny] == 2:
                mines_count += 1
        board[x][y] = 1
        display.set_pixel(x, y, 5)
        if mines_count > 0:
            display.scroll(str(mines_count))
        else:
            for off_x, off_y in OFFSETS:
                nx, ny = x + off_x, y + off_y
                if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and board[nx][ny] == 0:
                    reveal(nx, ny)


while not game_over:
    # 显示游戏区域和地雷数量
    display_board()
    display_mine_count()

    # 按下按钮控制光标移动和扫描方块
    if button_a.was_pressed() and cursor_x > 0 and cursor_x < WIDTH - 1:
        cursor_x += 1
    elif button_a.was_pressed() and cursor_x >= WIDTH - 1:
        cursor_x = 0
    elif button_b.was_pressed() and cursor_y > 0 and cursor_y < HEIGHT - 1 :
        cursor_y += 1
    elif button_b.was_pressed() and cursor_y >= HEIGHT - 1:
        cursor_x = 0
    elif pin_logo.is_touched():
        reveal(cursor_x, cursor_y)
    elif accelerometer.was_gesture("shake"):
        # 重新开始游戏
        board = [[0 for y in range(HEIGHT)] for x in range(WIDTH)]
        mines = []
        while len(mines) < NUM_MINES:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            if (x, y) not in mines:
                mines.append((x, y))
                board[x][y] = 2
        cursor_x = 0
        cursor_y = 0
        game_over = False
        display.clear()

    sleep(100)