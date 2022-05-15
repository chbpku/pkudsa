from microbit import *
import random, music


def play_music():
    """彩蛋！"""
    music.set_tempo(bpm=130)
    display.show(Image.MUSIC_QUAVERS)
    song = (
        "0:4 f4 e f:2 c:14 0:8 f:4 e f:2 a:14 0:4 "
        "a# a g f:2 a#:6 a:4 g f:3 0:1 f:6 g:1 0:1 g:20 0:4 "
        "0 f e f:2 c:14 0:8 f:4 e f:2 c5:14 0:4 "
        "a#4:1 0 a# 0 a# 0 a# 0 a# 0 a:2 g a#:10 0:2 g a a# a 0 a 0 a g f a:14 0:4 "
        "d e f g:2 d 0 d e 0 f g f c5:22 0:4 "
        "f4:2 g a a# c5 0 a4 f 0:4 c5 a#4 g 0 0 a# g:2 e 0:4 a# a f 0 0 "
        "0 d:4 f a# a c5:2 f4:6 0:2 a a# a a# a a# a f g:8 0:2 "
        "f4 g a a# c5 0 a4 f 0:4 c5 a#4 g 0 0 a# g:2 e 0:4 a# a f 0 0 "
        "d d5 c:2 a#4 a a# c5:8 f4:4 0:2 a a# a f a# a f d5 c:16 0:6 c4:1 0 c 0 a#:2 a g a f:16"
    )
    music.play(song.split())
    sleep(1000)
    start()


def show():
    """游戏界面与音效"""
    img = Image()
    for i in range(5):
        for j in obstacle[i]:
            img.set_pixel(j, 4 - i, wallbright)
    img.set_pixel(location, 4, playerbright)
    if coin:
        img.set_pixel(coin[1], 4 - coin[0], coinbright)
    display.show(img)
    music.play(tone)


def sample(nums):
    """random.sample(seq,k)的实现
    从box中选不重复的nums个数"""
    box = [0, 1, 2, 3, 4]
    ans = []
    ans.append(box.pop(box.index(location)))
    for i in range(nums - 1):
        ans.append(box.pop(random.randint(0, len(box) - 1)))
    return ans


def start():
    """开始界面与音效"""
    music.set_tempo(bpm=bpm)
    for i in range(3):
        display.show(str(3 - i))
        music.play("c5:10")
        sleep(750)
    if button_a.is_pressed() and button_b.is_pressed():  # 触发彩蛋方式
        play_music()
    button_a.was_pressed()  # 初始化按键a


def change_location():
    """控制玩家移动
    为了避免瞬移，每个tick内只能移动一格"""
    global location
    reading = accelerometer.get_x()
    if location == 4:
        if reading < 559:
            location -= 1
    elif location == 3:
        if reading > 574:  # 数值稍有差异，防止在边界剧烈抖动
            location += 1
        elif reading < 173:
            location -= 1
    elif location == 2:
        if reading > 190:
            location += 1
        elif reading < -190:
            location -= 1
    elif location == 1:
        if reading > -173:
            location += 1
        elif reading < -574:
            location -= 1
    else:
        if reading > -559:
            location += 1


def moveobstacle():
    """障碍物随时间的移动
    当玩家走过一定路程后，会加速并出现特殊障碍物"""
    global change, tone, bpm
    accelerate = distance % 100
    obstacle.pop(0)
    if accelerate < 90:
        if distance == change:
            if len(obstacle[-1]) > 0:
                obstacle.append([])
                change += random.choice((1, 2, 2, 2, 3))  # 空行数
            else:
                nums = random.choice((1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4))  # 障碍物所占列数
                obstacle.append(sample(nums))
                change = distance + random.choice((1, 1, 2, 2, 3, 4))  # 障碍物所占行数
        else:
            obstacle.append(obstacle[-1])
        return
    elif accelerate in (94, 96, 98):
        obstacle.append([0, 1, 3, 4])  # 特殊障碍物
    else:
        obstacle.append([])
        if accelerate == 99:
            change = distance + random.randint(2, 4)
            bpm += 200
            music.set_tempo(bpm=bpm)
        if accelerate > 94:
            tone = "c7"


def movecoin():
    """金币随时间的移动"""
    global coin
    if coin is not None:
        if coin[0] == 0:
            coin = None
        else:
            coin[0] -= 1


def refreshcoin():
    """新金币的生成"""
    global coin, coin_appear
    if distance == coin_appear:
        coin_appear += random.randint(7, 11)
        coin = [4, random.choice(list({0, 1, 2, 3, 4} - set(obstacle[-1])))]
        # coin代表金币的坐标


def ruin():
    """发射“炮弹”
    可摧毁所在列的障碍物"""
    global score, tone
    if score + distance >= 150:
        score -= 150  # 发射炮弹需要一定分数
        for j in obstacle:
            if location in j:
                j.remove(location)
        tone = "c3"


def fail():
    """结束界面与音效"""
    global tone, playerbright, coinbright
    tone = "0"
    for i in range(24):
        if i % 4 == 0:
            playerbright = 9 - playerbright
            tone = "c4"
        else:
            tone = "0"
        coinbright = 9 - coinbright
        show()
    display.scroll("SCORE:%d" % (score + distance))
    button_b.was_pressed()  # 初始化按键b
    sleep(1000)


while True:
    if button_b.was_pressed():  # 按b键开始游戏！
        # 初始化
        playerbright = 9
        wallbright = 6
        coinbright = 0

        obstacle = [[], [], [], [], []]  # 表示每行哪些位置有障碍物
        location = 2  # 玩家当前位置
        score = distance = time = 0
        tone = "c6:10"  # 当前播放的音效

        change = random.randint(6, 8)
        coin_appear = random.randint(13, 16)
        coin = None
        bpm = 600  # bpm控制音乐播放时间，也控制一个tick对应的实际时间

        # 游戏开始！
        start()
        while True:
            change_location()

            # 发射“炮弹”
            if button_a.was_pressed():
                ruin()

            # 碰到障碍物
            if location in obstacle[0]:
                fail()
                break

            # 吃到金币
            if coin is not None and coin[0] == 0 and coin[1] == location:
                score += 20
                tone = "g5"
                coin = None

            show()

            # 金币闪烁与音效
            coinbright = 9 - coinbright
            if tone == "g5":
                tone = "c6"
            elif tone == "c6" or "c3" or "c6:10":
                tone = "0"

            # 每4个tick，障碍物移动一步
            if time % 4 == 0:
                moveobstacle()
                movecoin()
                refreshcoin()
                distance += 1

            time += 1
    else:
        display.show(Image.ARROW_E)
        sleep(200)
