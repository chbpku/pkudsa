from microbit import *
import neopixel

# 初始化LED灯
np = neopixel.NeoPixel(pin0, 8)

# 常量定义
TIME_LIMIT = 30  # 游戏时间限制（秒）
MAX_SCORE = 10  # 最大分数
BLINK_DELAY = 100  # 每次闪烁延时（毫秒）

def get_sound_level():
    """获取声音信号强度"""
    sound_level = 0
    for i in range(100):
        sound_level += microphone.sound_level()
    return sound_level / 100

def blink_led(score):
    """控制LED灯带闪烁"""
    if score == 0:
        np.clear()
    else:
        for i in range(score):
            np[i] = (255, 0, 0)
        np.show()
        sleep(BLINK_DELAY)
        np.clear()
        sleep(BLINK_DELAY)

# 启动游戏
display.show('Ready')
while not button_a.is_pressed():
    pass

score = 0
start_time = running_time()
while True:
    sound_level = get_sound_level()
    if sound_level > 50:
        score += 1
        if score >= MAX_SCORE:
            display.scroll('You win!')
            break
    else:
        if score > 0:
            score -= 1

    cur_time = running_time()
    elapsed_time = (cur_time - start_time) // 1000
    if elapsed_time >= TIME_LIMIT:
        display.scroll('Time up! You lose!')
        break

    blink_led(score)b