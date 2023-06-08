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
        sound_level += microphone.sound_level()  # 计算100次声音平均值
    return sound_level / 100

def blink_led(score):
    """控制LED灯带闪烁"""
    if score == 0:
        np.clear()  # 如果得分为零则熄灭所有LED灯
    else:
        for i in range(score):
            np[i] = (255, 0, 0)  # 根据得分数设置LED灯的颜色，这里设置为红色
        np.show()  # 显示LED灯效果
        sleep(BLINK_DELAY)  # 等待一定时间
        np.clear()  # 熄灭所有LED灯
        sleep(BLINK_DELAY)  # 再等待一定时间

# 启动游戏
display.show('Ready')  # 显示“Ready”提示
while not button_a.is_pressed():  # 等待用户按下A键开始游戏
    pass

score = 0  # 初始化得分为零
start_time = running_time()  # 记录游戏开始时间
while True:
    sound_level = get_sound_level()  # 获取当前声音强度
    if sound_level > 50:  # 如果声音强度大于50，则认为玩家移开了手指，此时得分加一
        score += 1
        if score >= MAX_SCORE:  # 如果得分达到最大值，则游戏胜利
            display.scroll('You win!')  # 显示“You win!”提示
            break
    else:  # 如果声音强度小于等于50，则认为玩家未能及时移开手指，此时得分减一
        if score > 0:
            score -= 1

    cur_time = running_time()  # 获取当前时间
    elapsed_time = (cur_time - start_time) // 1000  # 计算已经过去的时间
    if elapsed_time >= TIME_LIMIT:  # 如果时间超过规定时间，则游戏结束
        display.scroll('Time up! You lose!')  # 显示“Time up! You lose!”提示
        break

blink_led(score)  # 根据得分控制LED灯带闪烁