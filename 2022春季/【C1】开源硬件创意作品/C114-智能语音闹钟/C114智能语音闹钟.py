# 在这里写上你的代码 :-)
def on_button_pressed_a():
    global buttonA_down
    buttonA_down = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global buttonAB_down
    buttonAB_down = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

value = 0
buttonAB_down = False
buttonA_down = False
serial.set_baud_rate(BaudRate.BAUD_RATE115200)
if True:
    Asr_V3.Asr_Clear_Buffer()
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Set_Mode(Asr_V3.Mode.PASSWORD_MODE)
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(0, "xiao bei")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(1, "kai deng")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(2, "guan deng")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(3, "nao zhong")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(4, "ban xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(5, "yi xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(6, "liang xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(7, "san xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(8, "si xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(9, "wu xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(10, "liu xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(11, "qi xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(12, "ba xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(13, "jiu xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(14, "shi xiao shi")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(15, "wu miao zhong")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(16, "guan bi nao zhong")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(17, "kai zhong")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(18, "xiao deng")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(19, "kai bei")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(20, "ban bei")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(21, "wu bei")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(22, "xiao zhu")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(23, "xiao xiao")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(24, "xiao niao")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(25, "da bei")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(26, "xia beng")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(27, "mao sui")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(28, "xiao shi zhong")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(29, "wu bei xiao")
    Asr_V3.Wait_Asr_Busy()
    Asr_V3.Asr_Add_Words(30, "xiao miao sui")
    Asr_V3.Wait_Asr_Busy()
    serial.write_number(Asr_V3.Asr_NUM_Cleck())
    Asr_V3.Cleck_Asr_Num(31)
Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.WHITE)
Asr_V3.Asr_Buzzer(Asr_V3.Buzzer_State.ON)
basic.pause(1000)
Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
Asr_V3.Asr_Buzzer(Asr_V3.Buzzer_State.OFF)

def on_forever():
    global value, buttonA_down, buttonAB_down
    value = Asr_V3.Asr_Result()
    serial.write_number(value)
    if value == 1:
        Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.RED)
    if value == 2:
        Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
    if value == 3:
        Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.GREEN)
    if value == 4:
        basic.show_string("0.5h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(1800000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 5:
        basic.show_string("1h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(3600000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 6:
        basic.show_string("2h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(7200000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 7:
        basic.show_string("3h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(10800000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 8:
        basic.show_string("4h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(14400000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 9:
        basic.show_string("5h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(18000000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 10:
        basic.show_string("6h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(21600000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 11:
        basic.show_string("7h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(25200000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 12:
        basic.show_string("8h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(28800000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 13:
        basic.show_string("9h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(32400000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 14:
        basic.show_string("10h")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(36000000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
    if value == 15:
        basic.show_string("5s")
        basic.pause(5000)
        if buttonA_down:
            basic.show_string("Done")
            Asr_V3.Asr_Set_RGB2(Asr_V3.enColor.OFF)
            basic.pause(5000)
            music.start_melody(music.built_in_melody(Melodies.POWER_UP),
                MelodyOptions.FOREVER)
            buttonA_down = False
    if value == 16 or buttonAB_down:
        music.stop_all_sounds()
        buttonAB_down = False
    basic.pause(500)
basic.forever(on_forever)
