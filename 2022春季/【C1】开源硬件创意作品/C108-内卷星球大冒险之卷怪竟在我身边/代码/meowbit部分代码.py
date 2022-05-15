from meowbit import *
#开始界面
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99d99bbbbbcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99ddbdd66168bcccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999ddbbbd66888111ccccccb99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966ddbbbb6688811818ccccccbbc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdd69dddbbb66618881888818818cccccbe9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddd96dd6b6dbd68888888888888888cccccc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbd9666666dbb668886888888cccccccccccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb99666966d68866888888cccccccccccccccccc69ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666888888888ccccbbbcc8bcccccccccc9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999666666666888888888cbbcbe8bbbcbcccccbbcccb9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff9bbb999666666666688888888bccb888888bbbbb88888bcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666866888868bbbbb8888888ccc888b88bbc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffdbbb9d99ddd666668868888688bbcb888888888bc888bcc8bc886c9fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbddd966666888688888888888888b88888888888cc8ccc886c9ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffdbbbbbbdd6966666666868888888888bbdbbebb8888888888bcc8c86c9fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff9bbdbddd6666666666888688868888ddddddddde8888888888bccbbccccfffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff9dbb9dd666666666668868888888bddddddbdbbddcccccd88b8ebccbbbbc9ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffdd99999666666666668868888888bdddddbbbbbdbbbccccccb8bbbccc8bbb9fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9dd99996696966666666668888bbbdddddbbbddbbbbbbbbbcccc8bcccbb8bbcfffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9d999996666966666668688888bbdddbbbbdbbbbbbbbbbbcccccc8bbccc88bc9ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99999999666996696668868868bbdddddbbbdbbbbbbbbbbbbcbccc88bcccc88c6ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff999996696669666966d8868666bddbbbddbbdbbbbbbbbbbbbcccccc88bbccc8869fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999996699669666666d6688668bddbbdbbbbbbbbbbbbbbbbbccccccc88bcccc866fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9dd999669966666666666688668bdddbbbbbbbbbbbbbbbbbbbccccccc888bbccc669ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff999999669d69666666666688868bddbbbdbbbbbbbbbbbbbbbbcccccccc888bbcc869ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999996ddd69666666688888868ddbddbbbbbbbbbbbbbbbbbbccccccccc888888866ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999999969ddd6669666688688888bbbbbbbbbbbbbbbbbbbbbbbbccbccccc8888888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999966ddddd669666688888888bbbbbbbbbbbbbbbbbbbbbbbcbccccccccc88888869fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff999bb99666dddd6666666668886888bbbbbbbbbbbbbbbbbbbbbbcccccccccccc8888889fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbb966696666666666888886888bbbbbbbbbbbbbbbbbbbbbbcbccccccccccc888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbdbb666969666666668888868888bbbbbbbbbbbbbbbbbbbbccbccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99dbbbbb6696966666666668886868888bbbbeb888bbbbbbbbbcccccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbe6969666666666888888888888888888888bbbbbbbbccccccccccccc88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccbc66966666666688888688888888888d888ebbbbbbbcccccccccccbb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbcc69996666688668886888888dd88dbbd88bbbbbbbccccccccccceb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbccc999966668868888888888ddddbbbbd88cbbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9ebbbbcccccccc9966666688888888888888ddbbbb888bbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccccccccc666666888866888888888dddddbdd88bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffbbbbbbcccccccccc6666688888888888888888d8888888bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbccbbccccccb666688868888888888888888888888bbbbbccccccccc888888888b9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbbbbbcccccbb66666688888888888888888888888bbbbccccccccccc88888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbcccccccb666666688888888888888888888888bbbbcccccccccc888888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbccccccbb666666688888888888888888888888bbbbcccccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbbbccccb6666668888888888888888888888888bbbbcbcccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcbbccccb6666668888888888888888888888888bbbbbccccccccc888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcccccccc6666668688688888888888888888888bbbbccccccccc8888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999bbbbbccccbc6666666688688888888888888888888bbbbcccccccc88888dd88886ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff969bbbbbbcccc69666666668688868888888888888888bbbbccccccc88888bd888886ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff99bbbbcccccc696bb668888888868888888888888888bbbcccccccc8888bbd888869ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999bbbcccc9666dbbb8888888888888888888888888ccbcccccccc8888bc888886fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff699bbbbccc966966bbb8888888888888888888888888bbbbccccc88888bcc88869fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9999bbcccc666666dbbdd88888888688888888888888bbcccccc88888888888669fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9699dbcccc66666666bb6d8888888688888888888888bbcccccc8888888888869ffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9696bbbcc66666666dbbd6886868888888888888888bbcbccc8888888888d669ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff999ebbccc666666666dbb8868888688888888888888bbbccc8888888889b69fffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff969ccbcc66996666666bbb868888888888888888888bbbc888888888888b6ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff96ccccc966966666666bb8688666888888888888888b8888888888888699ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff99ccbc996666666666dbb6888668888888888888888888888888888869fffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff969ccb9666666666666dbb88866888888888888888888888888888869ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff969ccc6696666666666dd8888668888888888888888888888888866fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff969cc9669666966d66dd8888868888888888888888888bb8888669fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff96ccc66699669dddd888868888888888888888888888be888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff96c66669966666dd88886666668888888888888888dd888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff96966669966ddd686886868888888888888888888d888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff969666696666666688686888888888888888888888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966966966666666886888888888888886888888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9699996666666888888888888888888118888699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff969996666668888881188888888881888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff996999666688881818888888881886669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9961161186618811188886116699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99161111611118111666699fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999661166669999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999999999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
game.splash("!!! BIG NEWS !!!")
game.splash("人类发现一类新物种")
game.splash("学名为：大卷怪")
game.splash("此类生物因为过于内卷")
game.splash("给摆烂人类造成了极大压力")
game.splash("影响恶劣，危害巨大！")
game.splash("经全人类一致决定")
game.splash("将他们发射到内卷星！")
game.splash("人类永不与大卷怪为伍！")
game.splash("消息传来，普天同庆")
game.splash("而你却不太高兴")
game.splash("因为你也是大卷怪")
game.splash("~~~嗖~~~")
flash2 = sprites.create(img("""
    . . . . . . . c d . . . . . . .
    . . . . . . . c d . . . . . . .
    . . . . . . . c d . . . . . . .
    . . . . . . . c b . . . . . . .
    . . . . . . . f f . . . . . . .
    . . . . . . . c 4 . . . . . . .
    . . . . . . . f f . . . . . . .
    . . . . . . . e 4 . . . . . . .
    . . . . . . e e 5 2 . . . . . .
    . . . . . . e 4 5 2 . . . . . .
    . . . . . c c c 2 2 2 . . . . .
    . . . . e e 4 4 4 5 2 2 . . . .
    . . e f f f c c 2 2 f f 2 2 . .
    . e e e e 2 2 4 4 4 4 5 4 2 2 .
    e e e e e e 2 2 4 4 4 5 4 4 2 2
    e e e e e e 2 2 4 4 4 4 5 4 2 2
"""),
    SpriteKind.player)
flash1 = sprites.create(img("""
        . . . . . . f f f f . . . . . .
            . . . . f f f 2 2 f f f . . . .
            . . . f f f 2 2 2 2 f f f . . .
            . . f f f e e e e e e f f f . .
            . . f f e 2 2 2 2 2 2 e e f . .
            . . f e 2 f f f f f f 2 e f . .
            . . f f f f e e e e f f f f . .
            . f f e f b f 4 4 f b f e f f .
            . f e e 4 1 f d d f 1 4 e e f .
            . . f e e d d d d d d e e f . .
            . . . f e e 4 4 4 4 e e f . . .
            . . e 4 f 2 2 2 2 2 2 f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
flash1.set_position(25, 79)
flash2.set_position(15, 108)
animation.run_movement_animation(flash1,
    animation.animation_presets(animation.fly_to_center),
    500,
    False)
pause(1000)
music.ba_ding.play()
pause(500)
game.splash("410号大卷怪发射成功！")
music.beam_up.play()
game.splash("你在内卷星的生活即将开始！")
game.splash("内卷星球大冒险之——", "卷怪竟在在我身边！")
effects.confetti.start_screen_effect(500)

#初遇
def on_on_overlap(sprite, otherSprite):
    game.set_dialog_text_color(9)
    game.set_dialog_frame(img("""
        ..bbabbaabbaabbaabbbbb..
                .bddbaddbaddbaddbabbddb.
                addddbaddbaddbaddbadddda
                addddbbaabbaabbaabbdddda
                abddb11111111111111bddba
                bbab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111babb
                abddb11111111111111bddba
                addddbbaabbaabbaabbdddda
                addddabddabddabddabdddda
                .addbbabddabddabddabdda.
                ..aaabbaabbaabbaabbaaa..
    """))
    game.set_dialog_cursor(img("""
        . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f f f c c f f f c .
                f f f c f f f f f f f c .
                c c c f f f e e f f c c .
                f f f f f e e f f c c f .
                f f f b f e e f b f f f .
                . f 4 1 f 4 4 f 1 4 f . .
                . f e 4 4 4 4 4 4 e f . .
                . f f f e e e e f f f . .
                f e f b 7 7 7 7 b f e f .
                e 4 f 7 7 7 7 7 7 f 4 e .
                e e f 6 6 6 6 6 6 f e e .
                . . . f f f f f f . . . .
                . . . f f . . f f . . . .
    """))
    game.show_long_text("你好，大卷怪410号", DialogLayout.BOTTOM)
    game.show_long_text("在这颗星球上，不是卷死别人，就是被别人卷死", DialogLayout.CENTER)
    game.show_long_text("大卷怪410号，准备好开卷了吗！", DialogLayout.CENTER)
    game.set_dialog_cursor(img("""
        . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
    """))
    game.set_dialog_text_color(9)
    game.set_dialog_frame(img("""
        ..bbabbaabbaabbaabbbbb..
                .bddbaddbaddbaddbabbddb.
                addddbaddbaddbaddbadddda
                addddbbaabbaabbaabbdddda
                abddb11111111111111bddba
                bbab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111babb
                abddb11111111111111bddba
                addddbbaabbaabbaabbdddda
                addddabddabddabddabdddda
                .addbbabddabddabddabdda.
                ..aaabbaabbaabbaabbaaa..
    """))
    game.show_long_text("卷，都可以卷！", DialogLayout.BOTTOM)
    game.set_dialog_frame(img("""
        ..bbabbaabbaabbaabbbbb..
                .bddbaddbaddbaddbabbddb.
                addddbaddbaddbaddbadddda
                addddbbaabbaabbaabbdddda
                abddb11111111111111bddba
                bbab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111babb
                abddb11111111111111bddba
                addddbbaabbaabbaabbdddda
                addddabddabddabddabdddda
                .addbbabddabddabddabdda.
                ..aaabbaabbaabbaabbaaa..
    """))
    game.set_dialog_text_color(9)
    game.set_dialog_cursor(img("""
        . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f f f c c f f f c .
                f f f c f f f f f f f c .
                c c c f f f e e f f c c .
                f f f f f e e f f c c f .
                f f f b f e e f b f f f .
                . f 4 1 f 4 4 f 1 4 f . .
                . f e 4 4 4 4 4 4 e f . .
                . f f f e e e e f f f . .
                f e f b 7 7 7 7 b f e f .
                e 4 f 7 7 7 7 7 7 f 4 e .
                e e f 6 6 6 6 6 6 f e e .
                . . . f f f f f f . . . .
                . . . f f . . f f . . . .
    """))
    game.show_long_text("在这颗星球上，我们卷的方式就是不断捕捉更强的神兽", DialogLayout.CENTER)
    game.show_long_text("不断培养我们的神兽，并让自己的神兽击败别人的神兽", DialogLayout.CENTER)
    game.show_long_text("而对于你来说，第一步，便是捕捉属于你自己的神兽。", DialogLayout.CENTER)
    game.set_dialog_text_color(9)
    game.set_dialog_frame(img("""
        ..bbabbaabbaabbaabbbbb..
                .bddbaddbaddbaddbabbddb.
                addddbaddbaddbaddbadddda
                addddbbaabbaabbaabbdddda
                abddb11111111111111bddba
                bbab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111babb
                abddb11111111111111bddba
                addddbbaabbaabbaabbdddda
                addddabddabddabddabdddda
                .addbbabddabddabddabdda.
                ..aaabbaabbaabbaabbaaa..
    """))
    game.set_dialog_cursor(img("""
        . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f f f c c f f f c .
                f f f c f f f f f f f c .
                c c c f f f e e f f c c .
                f f f f f e e f f c c f .
                f f f b f e e f b f f f .
                . f 4 1 f 4 4 f 1 4 f . .
                . f e 4 4 4 4 4 4 e f . .
                . f f f e e e e f f f . .
                f e f b 7 7 7 7 b f e f .
                e 4 f 7 7 7 7 7 7 f 4 e .
                e e f 6 6 6 6 6 6 f e e .
                . . . f f f f f f . . . .
                . . . f f . . f f . . . .
    """))
    game.show_long_text("请收下开卷利器，捕捉神兽的法宝，内卷星球的圣物！", DialogLayout.CENTER)
    game.show_long_text("MICROBIT", DialogLayout.FULL)
    tiles.set_current_tilemap(tilemap("""
        级别10
    """))
    scene.set_background_image(img("""
        555555555555555555555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555555555555555f555555555555555555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555555555555555ff555555555555555555555ff555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555555555555ffff55555555555555555555fff55555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555555555555ffff5555555555555555555ffff55555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555555555555fffff55555555555555555ffffff5555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555555555555555555555555555ffffff5555555555555555fffffff5555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555555555fffffff555555555555555ffffffff555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555555555fffffff5555555555555ffffffffff5555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555555555ffffffff555555555555fffffffffff555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555555555555555555555555fffffffff55555555555ffffffffffff55ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555555ffffffffff5555555555fffffffffffff5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555555fffffffffff55555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555555fffffffffff55555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555555555555555555555ffffffffffff5555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555555fffffffffffff555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555555ffffffffffffff555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555555555555555555fffffffffffffff55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555ffffffffffffffff5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555555ffffffffffffffff5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555555555fffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555555555555555ffffffffffffffffff555ffffffffffffffffffffffff5555555555555555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555555fffffffffffffffffff55fffffffffffffffff55555555555555555555555555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555555555555fffffffffffffffffffff55ffffffffffffff555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555555555fffffffffffffffffffffffffffffffff555555555555555555ffffffffffffffffffffffffffffffff5555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555555ffffffffffffffffffffffffffffffff555555555555ffffffffffffffffffffffffffffffffffffffffff555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555555555fffffffffffffffffffffffffffffffff555555555ffffffffffffffffffffffffffffffffffffffffffffff55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555555fffffffffffffffffffffffffffffffffff55555fffffffffffffffffffffffffffffffffffffffffffffffffff5555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55555fffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                5555ffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                555fffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                55ffffffffffffffffffffffffffffffffffffffff555fffffffffff555fffffffffffffffffffffffffff555ffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff555fffffffffff555fffffffffffffffffffffffffff555ffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff555fffffffffff555fffffffffffffffffffffffffff555ffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff5555fffffffffffffffffffffffffffffffffffffffffffffffffffff555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff55555fffffffffffffffffffffffffffffffffffffffffffffffffff5555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff555555fffffffffffffffffffffffffffffffffffffffffffffffff55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff555555ffffffffffffffffffffffffffffffffffffffffffffff5555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffff555555fffffffffffffffffffffffffffffffffffffffffff55555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff55555555fff55555555555fffffffffffffff555555555555555555ffffffffffffffffffffffff55555555555555555fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff5555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffff5555555555555555ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffff555fff555555555fffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff55555555ffffff555555555555555555555fffffffffffffffffffffffffffffffffffffff55f55f5555555fffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55ffff555555ffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55ffff55555fffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55f55ff555ffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55f555f55fffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55fffff5ffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ff55555ffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5555555fffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55555fffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5555ffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555fffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5fffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddbbbddddddbbbddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddbbbddddddbbbddddffffffffffffffffffffffffff
                fffffffffffddddbbbddddddbbbddddfffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffddddbbbddddddbbbddddffffffffffffffffffffffffff
                fffffffffffddddbbbddddddbbbddddfffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffddddbbbddddddbbbddddffffffffffffffffffffffffff
                fffffffffffdddddddffffffdddddddfffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffdddddddffffffdddddddffffffffffffffffffffffffff
                fffffffffffdddddddffffffdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddffffffdddddddffffffffffffffffffffffffff
                fffffffffffdddddddffffffdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddffffffdddddddffffffffffffffffffffffffff
                fffffffffffdddddddffffffdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddffffffdddddddffffffffffffffffffffffffff
                fffffffffffdddddddffffffdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddffffffdddddddffffffffffffffffffffffffff
                fffffffffffddddbbbddddddbbbddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddbbbddddddbbbddddffffffffffffffffffffffffff
                fffffffffffddddbbbddddddbbbddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddbbbddddddbbbddddffffffffffffffffffffffffff
                fffffffffffddddbbbddddddbbbddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddbbbddddddbbbddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                fffffffffffddddddddddddddddddddfffffffff444fffffffffff444ffffffffff444fffffffffff444fffffffffffff444ffffffffffffffddddddddddddddddddddffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffff55fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffff555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffff555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffff5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffff55555fffffffffffffffff444fffffffffff444ffffffffff444ffffffffffff444ffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffff5555555fffffffffffffffff444fffffffffff444ffffffffff444ffffffffffff444ffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffff55555555fffffffffffffffff444fffffffffff444ffffffffff444ffffffffffff444ffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffff555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffff5555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffff55555ff55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffff55555ffff5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffff555555f55f5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffff555555fffff5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffff5555555f555f5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffff55555555f555f5555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffff55555555555555555fffffffffffffffff444fffffffffff444ffffffffff444ffffffffffff444ffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff444fffffffffff444ffffffffff444ffffffffffff444ffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff444fffffffffff444ffffffffff444ffffffffffff444ffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffff555555555ffffffffffffffff555555555fffffffffffffff555555555fffffffffffffffff555555555ffffffffffffffffffff555555555fffffffffffffffffffffffffffffff
                ffffffffffffffff5.......5ffffffffffffffff5.......5fffffffffffffff5.......5fffffffffffffffff5.......5ffffffffffffffffffff5.......5fffffffffffffffffffffffffffffff
                ffffffffffffffff5.......5ffffffffffffffff5.......5fffffffffffffff5.......5fffffffffffffffff5.......5ffffffffffffffffffff5.......5fffffffffffffffffffffffffffffff
                ffffffffffffffff5.......5ffffffffffffffff5.......5fffffffffffffff5.......5fffffffffffffffff5.......5ffffffffffffffffffff5.......5fffffffffffffffffffffffffffffff
                ffffffffffffffff5.......5ffffffffffffffff5.......5fffffffffffffff5.......5fffffffffffffffff5.......5ffffffffffffffffffff5.......5fffffffffffffffffffffffffffffff
                ffffffffffffffff5.......5ffffffffffffffff5.......5fffffffffffffff5.......5fffffffffffffffff5.......5ffffffffffffffffffff5.......5fffffffffffffffffffffffffffffff
                ffffffffffffffff5.......5ffffffffffffffff5.......5fffffffffffffff5.......5fffffffffffffffff5.......5ffffffffffffffffffff5.......5fffffffffffffffffffffffffffffff
                ffffffffffffffff5.......5ffffffffffffffff5.......5fffffffffffffff5.......5fffffffffffffffff5.......5ffffffffffffffffffff5.......5fffffffffffffffffffffffffffffff
                ffffffffffffffff555555555ffffffffffffffff555555555fffffffffffffff555555555fffffffffffffffff555555555ffffffffffffffffffff555555555fffffffffffffffffffffffffffffff
    """))
    npc1.set_flag(SpriteFlag.INVISIBLE, True)
    player1.set_flag(SpriteFlag.INVISIBLE, True)
    pause(2000)
    tiles.set_current_tilemap(tilemap("""
        级别9
    """))
    tiles.set_tile_at(tiles.get_tile_location(6, 8), sprites.dungeon.button_orange)
    npc1.set_flag(SpriteFlag.INVISIBLE, False)
    player1.set_flag(SpriteFlag.INVISIBLE, False)
    game.show_long_text("你可以用microbit捕捉宠物，用microbit培养宠物", DialogLayout.FULL)
    game.set_dialog_text_color(9)
    game.set_dialog_cursor(img("""
        . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f f f c c f f f c .
                f f f c f f f f f f f c .
                c c c f f f e e f f c c .
                f f f f f e e f f c c f .
                f f f b f e e f b f f f .
                . f 4 1 f 4 4 f 1 4 f . .
                . f e 4 4 4 4 4 4 e f . .
                . f f f e e e e f f f . .
                f e f b 7 7 7 7 b f e f .
                e 4 f 7 7 7 7 7 7 f 4 e .
                e e f 6 6 6 6 6 6 f e e .
                . . . f f f f f f . . . .
                . . . f f . . f f . . . .
    """))
    game.set_dialog_frame(img("""
        ..bbabbaabbaabbaabbbbb..
                .bddbaddbaddbaddbabbddb.
                addddbaddbaddbaddbadddda
                addddbbaabbaabbaabbdddda
                abddb11111111111111bddba
                bbab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111badb
                abda1111111111111111adda
                adda1111111111111111adba
                bdab1111111111111111bbab
                babb1111111111111111babb
                abddb11111111111111bddba
                addddbbaabbaabbaabbdddda
                addddabddabddabddabdddda
                .addbbabddabddabddabdda.
                ..aaabbaabbaabbaabbaaa..
    """))
    game.show_long_text("我先卷一步了，拜拜，祝你好运！", DialogLayout.CENTER)
    npc1.destroy(effects.bubbles, 1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap)

npc1: Sprite = None
player1: Sprite = None
tiles.set_current_tilemap(tilemap("""
    级别9
"""))
player1 = sprites.create(img("""
        . . . . . . f f f f . . . . . .
            . . . . f f f 2 2 f f f . . . .
            . . . f f f 2 2 2 2 f f f . . .
            . . f f f e e e e e e f f f . .
            . . f f e 2 2 2 2 2 2 e e f . .
            . . f e 2 f f f f f f 2 e f . .
            . . f f f f e e e e f f f f . .
            . f f e f b f 4 4 f b f e f f .
            . f e e 4 1 f d d f 1 4 e e f .
            . . f e e d d d d d d e e f . .
            . . . f e e 4 4 4 4 e e f . . .
            . . e 4 f 2 2 2 2 2 2 f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(player1)
tiles.place_on_random_tile(player1, sprites.dungeon.green_inner_south_east)
player1.say_text(":头好晕啊，这是哪里？得赶紧找个人问一问", 2000, False)
controller.move_sprite(player1)
npc1 = sprites.create(img("""
        . . . . f f f f . . . . .
            . . f f f f f f f f . . .
            . f f f f f f c f f f . .
            f f f f f f c c f f f c .
            f f f c f f f f f f f c .
            c c c f f f e e f f c c .
            f f f f f e e f f c c f .
            f f f b f e e f b f f f .
            . f 4 1 f 4 4 f 1 4 f . .
            . f e 4 4 4 4 4 4 e f . .
            . f f f e e e e f f f . .
            f e f b 7 7 7 7 b f e f .
            e 4 f 7 7 7 7 7 7 f 4 e .
            e e f 6 6 6 6 6 6 f e e .
            . . . f f f f f f . . . .
            . . . f f . . f f . . . .
    """),
    SpriteKind.player)
tiles.place_on_random_tile(npc1, sprites.dungeon.purple_inner_south_west)

def on_update_interval():
    if controller.left.is_pressed():
        player1.set_image(img("""
            . . . . . . . . . . . . . . . .
                        . . . . f f f f f f . . . . . .
                        . . . f 2 f e e e e f f . . . .
                        . . f 2 2 2 f e e e e f f . . .
                        . . f e e e e f f e e e f . . .
                        . f e 2 2 2 2 e e f f f f . . .
                        . f 2 e f f f f 2 2 2 e f . . .
                        . f f f e e e f f f f f f f . .
                        . f e e 4 4 f b e 4 4 e f f . .
                        . . f e d d f 1 4 d 4 e e f . .
                        . . . f d d d d 4 e e e f . . .
                        . . . f e 4 4 4 e d d 4 . . . .
                        . . . f 2 2 2 2 e d d e . . . .
                        . . f f 5 5 4 4 f e e f . . . .
                        . . f f f f f f f f f f . . . .
                        . . . f f f . . . f f . . . . .
        """))
    if controller.up.is_pressed():
        player1.set_image(img("""
            . . . . . f f f f . . . . . . .
                        . . . f f e e e e f f . . . . .
                        . . f e e e f f e e e f . . . .
                        . f f f f f 2 2 f f f f f . . .
                        . f f e 2 e 2 2 e 2 e f f . . .
                        . f e 2 f 2 f f 2 f 2 e f . . .
                        . f f f 2 2 e e 2 2 f f f . . .
                        f f e f 2 f e e f 2 f e f f . .
                        f e e f f e e e e f e e e f . .
                        . f e e e e e e e e e e f . . .
                        . . f e e e e e e e e f . . . .
                        . e 4 f f f f f f f f 4 e . . .
                        . 4 d f 2 2 2 2 2 2 f d 4 . . .
                        . 4 4 f 4 4 4 4 4 4 f 4 4 . . .
                        . . . . f f f f f f . . . . . .
                        . . . . f f . . f f . . . . . .
        """))
    if controller.down.is_pressed():
        player1.set_image(img("""
            . . . . . . f f f f . . . . . .
                        . . . . f f f 2 2 f f f . . . .
                        . . . f f f 2 2 2 2 f f f . . .
                        . . f f f e e e e e e f f f . .
                        . . f f e 2 2 2 2 2 2 e e f . .
                        . . f e 2 f f f f f f 2 e f . .
                        . . f f f f e e e e f f f f . .
                        . f f e f b f 4 4 f b f e f f .
                        . f e e 4 1 f d d f 1 4 e e f .
                        . . f e e d d d d d d e e f . .
                        . . . f e e 4 4 4 4 e e f . . .
                        . . e 4 f 2 2 2 2 2 2 f 4 e . .
                        . . 4 d f 2 2 2 2 2 2 f d 4 . .
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                        . . . . . f f f f f f . . . . .
                        . . . . . f f . . f f . . . . .
        """))
    if controller.right.is_pressed():
        player1.set_image(img("""
            . . . . . . . . . . . . . . . .
                        . . . . . f f f f f f . . . . .
                        . . . f f e e e e f 2 f . . . .
                        . . f f e e e e f 2 2 2 f . . .
                        . . f e e e f f e e e e f . . .
                        . . f f f f e e 2 2 2 2 e f . .
                        . . f e 2 2 2 f f f f e 2 f . .
                        . f f f f f f f e e e f f f . .
                        . f f e 4 4 e b f 4 4 e e f . .
                        . f e e 4 d 4 1 f d d e f . . .
                        . . f e e e e e d d d f . . . .
                        . . . . f 4 d d e 4 e f . . . .
                        . . . . f e d d e 2 2 f . . . .
                        . . . f f f e e f 5 5 f f . . .
                        . . . f f f f f f f f f f . . .
                        . . . . f f . . . f f f . . . .
        """))
    if player1.tile_kind_at(TileDirection.CENTER, sprites.dungeon.button_orange):
        if game.ask("是否传送到主地图继续探索？"):
            game.show_long_text("即将传送到内卷星主地图", DialogLayout.BOTTOM)
    if player1.tile_kind_at(TileDirection.CENTER, sprites.dungeon.hazard_lava0):
        game.show_long_text("你刚来到内卷星就挂了，死于 【被岩浆烧死】", DialogLayout.CENTER)
        game.over(False, effects.dissolve)
game.on_update_interval(100, on_update_interval)

#主地图画面
@namespace
class SpriteKind:
    egg = SpriteKind.create()
    zidan = SpriteKind.create()
time2 = 0
time1 = 0
a4 = 0
a2 = 0
a3 = 0
a1 = 0
transit = ""
transform = 0
man: Sprite = None
egg2: Sprite = None
zhu: Sprite = None
tree: Sprite = None
car: Sprite = None
actor = [img("""
        . . . . . f f 4 4 f f . . . . . 
            . . . . f 5 4 5 5 4 5 f . . . . 
            . . . f e 4 5 5 5 5 4 e f . . . 
            . . f b 3 e 4 4 4 4 e 3 b f . . 
            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
            . f 3 3 e b 3 e e 3 b e 3 3 f . 
            . f 3 3 f f e e e e f f 3 3 f . 
            . f b b f b f e e f b f b b f . 
            . f b b e 1 f 4 4 f 1 e b b f . 
            f f b b f 4 4 4 4 4 4 f b b f f 
            f b b f f f e e e e f f f b b f 
            . f e e f b d d d d b f e e f . 
            . . e 4 c d d d d d d c 4 e . . 
            . . e f b d b d b d b b f e . . 
            . . . f f 1 d 1 d 1 d f f . . . 
            . . . . . f f b b f f . . . . .
    """),
    img("""
        . f f f . f f f f . f f f . 
            f f f f f c c c c f f f f f 
            f f f f b c c c c b f f f f 
            f f f c 3 c c c c 3 c f f f 
            . f 3 3 c c c c c c 3 3 f . 
            . f c c c c 4 4 c c c c f . 
            . f f c c 4 4 4 4 c c f f . 
            . f f f b f 4 4 f b f f f . 
            . f f 4 1 f d d f 1 4 f f . 
            . . f f d d d d d d f f . . 
            . . e f e 4 4 4 4 e f e . . 
            . e 4 f b 3 3 3 3 b f 4 e . 
            . 4 d f 3 3 3 3 3 3 c d 4 . 
            . 4 4 f 6 6 6 6 6 6 f 4 4 . 
            . . . . f f f f f f . . . . 
            . . . . f f . . f f . . . .
    """),
    img("""
        . . . . f f f f . . . . . 
            . . f f f f f f f f . . . 
            . f f f f f f c f f f . . 
            f f f f f f c c f f f c . 
            f f f c f f f f f f f c . 
            c c c f f f e e f f c c . 
            f f f f f e e f f c c f . 
            f f f b f e e f b f f f . 
            . f 4 1 f 4 4 f 1 4 f . . 
            . f e 4 4 4 4 4 4 e f . . 
            . f f f e e e e f f f . . 
            f e f b 7 7 7 7 b f e f . 
            e 4 f 7 7 7 7 7 7 f 4 e . 
            e e f 6 6 6 6 6 6 f e e . 
            . . . f f f f f f . . . . 
            . . . f f . . f f . . . .
    """),
    img("""
        . . . . . f f f f . . . . . 
            . . . f f 5 5 5 5 f f . . . 
            . . f 5 5 5 5 5 5 5 5 f . . 
            . f 5 5 5 5 5 5 5 5 5 5 f . 
            . f 5 5 5 d b b d 5 5 5 f . 
            f 5 5 5 b 4 4 4 4 b 5 5 5 f 
            f 5 5 c c 4 4 4 4 c c 5 5 f 
            f b b f b f 4 4 f b f b b f 
            f b b 4 1 f d d f 1 4 b b f 
            . f b f d d d d d d f b f . 
            . f e f e 4 4 4 4 e f e f . 
            . e 4 f 6 9 9 9 9 6 f 4 e . 
            . 4 d c 9 9 9 9 9 9 c d 4 . 
            . 4 f b 3 b 3 b 3 b b f 4 . 
            . . f f 3 b 3 b 3 3 f f . . 
            . . . . f f b b f f . . . .
    """),
    img("""
        . . . . . . c c c . . . . . . . 
            . . . . . . c 5 b c . . . . . . 
            . . . . c c c 5 5 c c c . . . . 
            . . c c c c 5 5 5 5 c b c c . . 
            . c b b 5 b 5 5 5 5 b 5 b b c . 
            . c b 5 5 b b 5 5 b b 5 5 b c . 
            . . c 5 5 5 b b b b 5 5 5 f . . 
            . . f f 5 5 5 5 5 5 5 5 f f . . 
            . . f f f b f e e f b f f f . . 
            . . f f f 1 f b b f 1 f f f . . 
            . . . f f b b b b b b f f . . . 
            . . . e e f e e e e f e e . . . 
            . . e b f b 5 b b 5 b c b e . . 
            . . e e f 5 5 5 5 5 5 f e e . . 
            . . . . c b 5 5 5 5 b c . . . . 
            . . . . . f f f f f f . . . . .
    """),
    img("""
        . . . . f f f f . . . . 
            . . f f e e e e f f . . 
            . f f e e e e e e f f . 
            f f f f 4 e e e f f f f 
            f f f 4 4 4 e e f f f f 
            f f f 4 4 4 4 e e f f f 
            f 4 e 4 4 4 4 4 4 e 4 f 
            f 4 4 f f 4 4 f f 4 4 f 
            f e 4 d d d d d d 4 e f 
            . f e d d b b d d e f . 
            . f f e 4 4 4 4 e f f . 
            e 4 f b 1 1 1 1 b f 4 e 
            4 d f 1 1 1 1 1 1 f d 4 
            4 4 f 6 6 6 6 6 6 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . .
    """),
    img("""
        . . . . . . 5 . 5 . . . . . . . 
            . . . . . f 5 5 5 f f . . . . . 
            . . . . f 1 5 2 5 1 6 f . . . . 
            . . . f 1 6 6 6 6 6 1 6 f . . . 
            . . . f 6 6 f f f f 6 1 f . . . 
            . . . f 6 f f d d f f 6 f . . . 
            . . f 6 f d f d d f d f 6 f . . 
            . . f 6 f d 3 d d 3 d f 6 f . . 
            . . f 6 6 f d d d d f 6 6 f . . 
            . f 6 6 f 3 f f f f 3 f 6 6 f . 
            . . f f d 3 5 3 3 5 3 d f f . . 
            . . f d d f 3 5 5 3 f d d f . . 
            . . . f f 3 3 3 3 3 3 f f . . . 
            . . . f 3 3 5 3 3 5 3 3 f . . . 
            . . . f f f f f f f f f f . . . 
            . . . . . f f . . f f . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . c c c c . . . . 
            . . . . . . c c d d d d c . . . 
            . . . . . c c c c c c d c . . . 
            . . . . c c 4 4 4 4 d c c . . . 
            . . . c 4 d 4 4 4 4 4 1 c . c c 
            . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
            . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
            f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
            f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
            f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
            . f 4 4 4 4 1 c 4 f 4 d f f f f 
            . . f f 4 d 4 4 f f 4 c f c . . 
            . . . . f f 4 4 4 4 c d b c . . 
            . . . . . . f f f f d d d c . . 
            . . . . . . . . . . c c c . . .
    """),
    img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ............cccc................
            ...........cbbbbc...............
            .........cbbdbbfbf..............
            ..........ffdbbfbf..............
            ............bbbbbb..............
            ............bbbbbbf.............
            ...........fbbbbb63dcc..........
            ..........cd666663dddddc........
            ..........cdd333dbddddbc........
            ..........cddddddbdddbbdc.......
            ..........cddddddbddbbddb.......
            ...........cddddddbdbdddbccc....
            ............cdddddddddddcffff...
            ............cccddcbdddbbf.......
            ............c33bb33cbfff........
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
    """),
    img("""
        ....................
            ....................
            ....................
            ....................
            ....................
            ...........444......
            ..........4eee4.....
            ..........44444.....
            ...........444......
            .....444....7.......
            ....4eee4...7.......
            ....44444..77.7.....
            .....444...7766.....
            ......7....766......
            .......7...76.......
            .....7777..7........
            ......6667.6........
            .........666........
            ....................
            ....................
    """)]
plant = [img("""
        ................86..................
            ...........6688867886...............
            ...........8666877688868............
            ............868777767768............
            .........688667777776688............
            ........67767777777778666...........
            .........6776667767666868...........
            ..........866667667677688...........
            .........8666666666667778...........
            ........667766666666666676..........
            .......67766667666776667776.........
            ......886667776676777666688.........
            .....67766777667767777666768........
            ....6776666666777667776666776.......
            .....8667776667766676677776776......
            ......8777666666667776777776688.....
            ....6887766776677677777777776776....
            ..8866666677767777777777766666778...
            .86666666777667767777766666776668...
            ..88677666666777677677666667776668..
            ..86776677666666666666667776666668..
            886666677766667666666776677766668...
            6668666676667766767767766677666668..
            88866666666777677677667666666776668.
            .86668866666766776776666667766666668
            .86688666666666776666667667776666688
            .668866666666666666666677666666688..
            ..8866686666666666677667776666668...
            ...866886666666666677667776666668...
            ...86886668666666667666666666888....
            ....88866886686666666666666668......
            ......86886668666866668666868.......
            ......88866688668866688866888.......
            ........8888888688888ce868..........
            ..............e88e88.ec.8...........
            ...............eeee..e..............
            ...............ceef.ce..............
            ...............ceefcec..............
            ...............feefce...............
            ...............fceeec...............
            ...............ffceec...............
    """),
    img("""
        ...............cc...............
            ............ccc65c66............
            ............c6c55c76............
            ...........6cc7557c66...........
            ..........cc77777577c6..........
            .........666c677776cc66.........
            ........c7776c7c67657576........
            ........ccc666c666655666........
            ......c66cc7666667777c6766......
            .....c777c77667667767767776.....
            .....cc66cccc77c677cc666666.....
            ....c6766666c7c6767677777766....
            ...cc777666666677767777667c66...
            .666cc6677666667777777776677666.
            .67776677c676677777776677677776.
            cc6666ccc67767776777776cc7767666
            c666777667766776c776777c67776c66
            .c6777666ccc667c676cc666667776c.
            .cc6666766666cc66666666776cc666.
            ...66776c666666666677667766cccc.
            ...cc76c66766666667677667776c...
            ...6cccc677666666776777c77666...
            ......6ccc7c67767776c776cc......
            ........ccc6777c67776cc6........
            ...........cc77c67766...........
            .............6c6666.............
            ............ffeeeef.............
            ..........ffeeeeeeeef...........
            .............feeeffe............
            ..............fef...............
            ..............fef...............
            ...............f................
    """),
    img("""
        . . . . . . . . 
            . . . . . . . . 
            . . . . . . . . 
            . . . . . . . . 
            . b b d d b b . 
            b 1 1 3 3 1 1 b 
            b 1 3 5 5 3 1 b 
            b d 3 5 5 3 d b 
            c 1 1 d d 1 1 c 
            c d 1 d d 1 d c 
            . c c 7 6 c c . 
            . . 6 7 6 . . . 
            . . 6 6 8 8 8 6 
            . . 6 8 7 7 7 6 
            . . 8 7 7 7 6 . 
            . . 8 8 8 6 . .
    """),
    img("""
        ........................
            ...........66...........
            ..........6776..........
            ..........6776..........
            .........877778.........
            ........86777768........
            .......6777777776.......
            ......677677776776......
            ......866777777668......
            .....86677677677668.....
            ....8668866766888668....
            ....8888668886686888....
            .....86868868868668.....
            ....866888668888868.....
            ....8688886888888888....
            ....8886688888866888....
            ....8676888868886768....
            ...87778868678688776....
            ..8777767767787767778...
            .877767777777677776778..
            .8866777777777777776778.
            .8667776776767776777688.
            ..887766768668776667668.
            ..8688668886688686688668
            .86688688686866888688888
            8668868866888866888868..
            88886686688888868688668.
            .8688888888888888668868.
            .8878888868868878868788.
            .87768776788778777667788
            877677767787776767776778
            88877787766777777877788.
            ..88886786777667768888..
            .....86887786668868.....
            ......8886888668888.....
            .........88ee88.........
            .........feeeef.........
            .........feeeef.........
            ........feeefeef........
            ........fefeffef........
    """),
    img("""
        .....79....797....97..7.....77..
            ..9.99999.977779..799.7..7797...
            ..93377.969747.766777766779e777.
            ...1379.73377317677636776763377.
            99.797.73176777777731767c77137..
            7e9494777733769967776766677677.7
            ..73397773777966667676966777677.
            .9.3197977779917777667677766766.
            .7777674376767377676677673776767
            ..733.77777977777713973313767c67
            ..379799777799777737973777731777
            799997799.7967777777677777996.66
            .997777ee7633367767767767667677.
            .931377777731767767e67776767....
            .9337377.779777776776776676777.6
            9..777777.77777773776367767766..
            9.997...77737777316731767667.66.
            ..999.7737.77.796367cc667631676.
            ...7...71377.777676697317773776.
            .....77....7.9977e7669.7...666..
            .....97....7799666767..7.6......
            .....7..........4eeee.6.........
            ................46ee6...........
            ................4eeec...........
            ................4eeec...........
            ...............e4eece...........
            ...............eeeece...........
            ..............44eeecce..........
            ............444eeeeccc..........
            .........eee44ee.ececccec.......
            .......eeee.4ee..ece.cccec......
            ....eee....e......e...eee.ccee..
    """),
    img("""
        ....................
            ....................
            .........1..........
            ......661d1.........
            .....177717766......
            ....1d177777677.....
            ..6.717777c77177....
            ...7c77767771d17....
            ...77677766771777...
            ..1777766677777767..
            .1d1776717676777c7..
            .7177661d176777777..
            .77767771777777176..
            .677c77777c7671d17..
            .77777777777767176..
            .667776776777777767.
            ...76776766676766...
            ....................
            ....................
            ....................
    """),
    img("""
        ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            .......9............
            ......999...9.......
            ......919..919..9...
            ...9...9...999.999..
            ..919..7....9..919..
            ..999..77...7...9...
            ...9..77....7...77..
            ...7...7.7.777..7...
            .7...7.........7..7.
            ....................
    """),
    img("""
        .........ccc........
            ......cccc3cc.......
            .....cc3c3c3c.......
            .....c33ccbcc.......
            .....cb3cb3b3c......
            .....ccccccc3c......
            .....c33bbc33c......
            .....cc333cccc......
            ......ccccc7..6.....
            ...........7666.....
            .......5..766.......
            .......7776.........
            ........76..........
            ........6...........
            ........6...........
            ........6...........
            ........66..........
            .........6..........
            ....................
            ....................
    """)]
tiles.set_current_tilemap(tilemap("""
    级别1
"""))
for index in range(randint(5, 8)):
    car = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 2 2 2 2 2 2 2 2 . . 
                    . . . . . 2 c 2 2 2 2 2 2 4 2 . 
                    . . . . 2 c c 2 2 2 2 2 2 4 c 2 
                    . . d 2 4 c c 2 4 4 4 4 4 4 c c 
                    . d 2 2 4 c b e e e e e e e 2 c 
                    . 2 2 2 4 b e e b b b e b b e 2 
                    . 2 2 2 2 2 e b b b b e b b b e 
                    . 2 2 2 2 e 2 2 2 2 2 e 2 2 2 e 
                    . 2 d d 2 e f e e e f e e e e e 
                    . d d 2 e e e f e e f e e e e e 
                    . e e e e e e e f f f e e e e e 
                    . e e e e f f f e e e e f f f f 
                    . . . e f f f f f e e f f f f f 
                    . . . . f f f f . . . . f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    tiles.place_on_random_tile(car, sprites.dungeon.dark_ground_center)
for index2 in range(randint(20, 30)):
    tree = sprites.create(plant[randint(0, len(plant) - 1)], SpriteKind.projectile)
    tiles.place_on_random_tile(tree, sprites.dungeon.dark_ground_center)
for index3 in range(randint(1, 2)):
    zhu = sprites.create(img("""
            .......bbbbbbbbbbbbbbbbbb.......
                    ......bddddddddddddddddddb......
                    .....bddddddddddddddddddddb.....
                    ....bddddddddddddddddddddddb....
                    ...bddddddddddddddddddddddddb...
                    ..bddddddddddddddddddddddddddb..
                    ..c11111111111111111111111111c..
                    ..c11111111111111111111111111c..
                    .bccccccccccccccccccccccccccccb.
                    bb11111dd11dbbbbbbbbd11dd11111bb
                    c11bbcc11dd11dbbbbd11dd11ccbb11c
                    c1bbddbcb11dd111111dd11bcbddbb1c
                    c1bbbddbdbd11dddddd11dbdbddbbb1c
                    c11bbddcddbbd111111dbbddcddbb11c
                    cb1111dcbd11bbbbbbbb11dbcd1111bc
                    .cb111ccbdd1111111111ddbcc111bc.
                    ..cccc.cbdbb1bb11bb1bbdbc.cccc..
                    .......cbdbb1db11bd1bbdbc.......
                    .......cbdbd1dd11dd1dbdbc.......
                    .......cbdbd1dd11dd1dbdbc.......
                    ......ccbdbd1dd11dd1dbdbcc......
                    .....cbbbdbd1dd11dd1dbdbbbc.....
                    .....cdbbdbd1dd11dd1dbdbbdc.....
                    .....c11bbbd1dd11dd1dbbb11c.....
                    .....cd111bbbbbbbbbbbb111dc.....
                    ....cccd1111111111111111dccc....
                    ...cbddbbb111111111111bbbddbc...
                    ..cbddddddbbbbbbbbbbbbddddddbc..
                    ..c11111111111111111111111111c..
                    ..c11111111111111111111111111c..
                    ..c11111111111111111111111111c..
                    ..cbbbbbbbbbbbbbbbbbbbbbbbbbbc..
        """),
        SpriteKind.projectile)
    tiles.place_on_random_tile(zhu, assets.tile("""
        myTile14
    """))
for index4 in range(1):
    egg2 = sprites.create(img("""
            . . . b b b b b b b b b . . . . 
                    . . b 1 d d d d d d d 1 b . . . 
                    . b 1 1 1 1 1 1 1 1 1 1 1 b . . 
                    . b d b c c c c c c c b d b . . 
                    . b d c 6 6 6 6 6 6 6 c d b . . 
                    . b d c 6 d 6 6 6 6 6 c d b . . 
                    . b d c 6 6 6 6 6 6 6 c d b . . 
                    . b d c 6 6 6 6 6 6 6 c d b . . 
                    . b d c 6 6 6 6 6 6 6 c d b . . 
                    . b d c c c c c c c c c d b . . 
                    . c b b b b b b b b b b b c . . 
                    c b c c c c c c c c c c c b c . 
                    c 1 d d d d d d d d d d d 1 c . 
                    c 1 d 1 1 d 1 1 d 1 1 d 1 1 c . 
                    c b b b b b b b b b b b b b c . 
                    c c c c c c c c c c c c c c c .
        """),
        SpriteKind.egg)
    tiles.place_on_random_tile(egg2, sprites.dungeon.dark_ground_center)
for index5 in range(randint(15, 20)):
    man = sprites.create(actor[randint(0, len(actor) - 1)], SpriteKind.projectile)
    tiles.place_on_random_tile(man, sprites.dungeon.dark_ground_center)
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
bullet = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 4 4 . . . . . . . 
            . . . . . . 4 5 5 4 . . . . . . 
            . . . . . . 2 5 5 2 . . . . . . 
            . . . . . . . 2 2 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.zidan)
bullet2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 2 2 . . . . . . . 
            . . . . . . 3 1 1 3 . . . . . . 
            . . . . . 2 1 1 1 1 2 . . . . . 
            . . . . . 2 1 1 1 1 2 . . . . . 
            . . . . . . 3 1 1 3 . . . . . . 
            . . . . . . . 2 2 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.zidan)
tiles.place_on_tile(bullet, tiles.get_tile_location(14, 42))
tiles.place_on_tile(bullet2, tiles.get_tile_location(15, 42))
animation.run_image_animation(bullet2,
    [img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . 2 2 . . . . . . . 
                . . . . . . 3 1 1 3 . . . . . . 
                . . . . . 2 1 1 1 1 2 . . . . . 
                . . . . . 2 1 1 1 1 2 . . . . . 
                . . . . . . 3 1 1 3 . . . . . . 
                . . . . . . . 2 2 . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . 2 2 . . . . . . . 
                . . . . . . 3 1 1 3 . . . . . . 
                . . . . . 2 1 1 1 1 2 . . . . . 
                . . . . . 2 1 1 1 1 2 . . . . . 
                . . . . . . 3 1 1 3 . . . . . . 
                . . . . . . . 2 2 . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . 3 3 . . . . . . . . 
                . . . . . . 3 1 3 . . . . . . . 
                . . 3 3 . . 3 1 3 . . 3 3 . . . 
                . . 3 1 3 . 3 1 3 2 3 1 3 . . . 
                . . . 3 1 3 3 1 3 2 1 3 . . . . 
                3 3 3 3 2 1 3 1 1 1 3 . . . . . 
                3 1 1 1 1 1 1 1 1 2 3 3 3 3 3 3 
                . 3 3 3 2 3 1 1 1 1 1 1 1 1 1 3 
                . . . . . 2 1 1 1 3 3 2 3 3 3 . 
                . . . . 3 1 3 1 3 1 2 . . . . . 
                . . . 3 1 3 2 1 3 3 1 3 . . . . 
                . . 3 1 3 . 2 1 3 . 3 1 3 . . . 
                . . 3 3 . . 3 1 3 . . 3 3 . . . 
                . . . . . . 3 1 3 . . . . . . . 
                . . . . . . 3 1 3 . . . . . . . 
                . . . . . . 3 3 . . . . . . . .
        """),
        img("""
            . . 3 3 . . . 3 3 . . . . . . . 
                . 3 1 1 2 . . 3 1 3 . . 3 3 3 . 
                . 3 1 1 2 . . 3 1 3 . 3 1 1 3 . 
                . . 3 2 2 . . 2 1 2 . 2 1 1 3 . 
                . 3 3 . . . . . 2 2 . 2 2 2 . . 
                3 1 1 2 2 . . . . . . . 3 3 . . 
                3 1 1 1 2 . . . . . . 2 1 1 3 3 
                3 1 1 2 . . . . . . 3 1 1 1 1 3 
                . 3 2 2 . . . . . . . 2 1 1 3 . 
                . . . . . . . 2 . . . . 3 3 . . 
                . . 2 2 2 . 2 1 2 . . 2 2 2 . . 
                . 3 1 1 2 2 3 1 1 2 . 2 1 1 3 3 
                3 1 1 1 2 2 1 1 1 2 . 2 1 1 1 3 
                3 1 1 3 . . 3 1 3 . . . 3 1 1 3 
                3 3 3 . . . . 3 3 . . . . 3 3 . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . 3 . . . . . 
                . . . . . 3 . . . . 3 3 . . . . 
                . . . . 3 3 . . . . . 3 . . . . 
                . . . . 3 . . . 3 . . . . . . . 
                . . . . . . . . 3 . . . . . . . 
                . 3 . . . . . . . . . . 3 . . . 
                3 3 . . . . . . . . . . 3 3 . . 
                3 . . . . . . . . . . . . 3 . . 
                . . . . . . . . . . . . . . . . 
                . . . 3 . . . 3 . . . . . 3 . . 
                . . 3 3 . . . 3 . . . . . 3 3 . 
                . . 3 . . . . 3 . . . . . . 3 .
        """)],
    400,
    True)
animation.run_image_animation(bullet,
    [img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . 4 4 . . . . . . . 
                . . . . . . 4 5 5 4 . . . . . . 
                . . . . . . 2 5 5 2 . . . . . . 
                . . . . . . . 2 2 . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . 4 . . . . . 
                . . . . 2 . . . . 4 4 . . . . . 
                . . . . 2 4 . . 4 5 4 . . . . . 
                . . . . . 2 4 d 5 5 4 . . . . . 
                . . . . . 2 5 5 5 5 4 . . . . . 
                . . . . . . 2 5 5 5 5 4 . . . . 
                . . . . . . 2 5 4 2 4 4 . . . . 
                . . . . . . 4 4 . . 2 4 4 . . . 
                . . . . . 4 4 . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . 3 . . . . . . . . . . . 4 . . 
                . 3 3 . . . . . . . . . 4 4 . . 
                . 3 d 3 . . 4 4 . . 4 4 d 4 . . 
                . . 3 5 3 4 5 5 4 4 d d 4 4 . . 
                . . 3 d 5 d 1 1 d 5 5 d 4 4 . . 
                . . 4 5 5 1 1 1 1 5 1 1 5 4 . . 
                . 4 5 5 5 5 1 1 5 1 1 1 d 4 4 . 
                . 4 d 5 1 1 5 5 5 1 1 1 5 5 4 . 
                . 4 4 5 1 1 5 5 5 5 5 d 5 5 4 . 
                . . 4 3 d 5 5 5 d 5 5 d d d 4 . 
                . 4 5 5 d 5 5 5 d d d 5 5 4 . . 
                . 4 5 5 d 3 5 d d 3 d 5 5 4 . . 
                . 4 4 d d 4 d d d 4 3 d d 4 . . 
                . . 4 5 4 4 4 4 4 4 4 4 4 . . . 
                . 4 5 4 . . 4 4 4 . . . 4 4 . . 
                . 4 4 . . . . . . . . . . 4 4 .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . b b . b b b . . . . . 
                . . . . b 1 1 b 1 1 1 b . . . . 
                . . b b 3 1 1 d d 1 d d b b . . 
                . b 1 1 d d b b b b b 1 1 b . . 
                . b 1 1 1 b . . . . . b d d b . 
                . . 3 d d b . . . . . b d 1 1 b 
                . b 1 d 3 . . . . . . . b 1 1 b 
                . b 1 1 b . . . . . . b b 1 d b 
                . b 1 d b . . . . . . b d 3 d b 
                . b b d d b . . . . b d d d b . 
                . b d d d d b . b b 3 d d 3 b . 
                . . b d d 3 3 b d 3 3 b b b . . 
                . . . b b b d d d d d b . . . . 
                . . . . . . b b b b b . . . . .
        """)],
    500,
    True)
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile11
"""))
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
神兽1 = sprites.create(img("""
        .........ccc............
            .........cccccccc.......
            ......cc..cc55555cc.....
            ......cccc555555555c....
            ......ccb55555555555c...
            ...cc..b55555ff155555c..
            ...cccb5555555ff55d55c..
            ....ccb55555d55555555c..
            .....b55555d5555d5555c..
            ..cc.b555ddd55555bbbbc..
            ..cccd55ddddd5555d555c..
            ...ccdd5dbdddbbbd555c...
            ....bdddb555bbbbbccc....
            ..cccdddb555cbbbbbbc....
            ...ccddddb555cbbbbbbc...
            ....cdddddb555cbbbbbc...
            ...ccddddddb55cbbbbbcc..
            ..ccbddddd55bcbbbbbbcc..
            ccdddddddd5555bbbbbbc...
            cdddddddbdd555bbbbbc....
            .ccddddbbbdd55cbbccc....
            ...cccbbcbddddccdddcc...
            ......cccdd555dcccccc...
            ........cccccccc........
    """),
    SpriteKind.player)
神兽2 = sprites.create(img("""
        . . f f f . . . . . . . . f f f 
            . f f c c . . . . . . f c b b c 
            f f c c . . . . . . f c b b c . 
            f c f c . . . . . . f b c c c . 
            f f f c c . c c . f c b b c c . 
            f f c 3 c c 3 c c f b c b b c . 
            f f b 3 b c 3 b c f b c c b c . 
            . c b b b b b b c b b c c c . . 
            . c 1 b b b 1 b b c c c c . . . 
            c b b b b b b b b b c c . . . . 
            c b c b b b c b b b b f . . . . 
            f b 1 f f f 1 b b b b f c . . . 
            f b b b b b b b b b b f c c . . 
            . f b b b b b b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . .
    """),
    SpriteKind.player)
tiles.place_on_random_tile(神兽1, assets.tile("""
    myTile9
"""))
tiles.place_on_random_tile(神兽2, assets.tile("""
    myTile13
"""))
animation.run_image_animation(神兽1,
    [img("""
            ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb555555ff155555c
                ......cb55555555ff55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb13bbc.
                ...cccd55ddddd555b3335c.
                .....bdddddddddd55b335c.
                ..cccdddddb55bbddd5555c.
                ..cccdddddb555bbbbcccc..
                ...ccddddddb5555cbcdc...
                ccccbdddddd5cb55cbcc....
                cddddddddd5555ccbbc.....
                .cddddddbdd555bbbcc.....
                ..ccdddbbbdd55cbcdc.....
                ....ccbbcbddddccdddcc...
                ......cccdd555dcccccc...
                ........cccccccc........
        """),
        img("""
            .........ccc............
                .........cccccccc.......
                ......cc..cc55555cc.....
                ......cccc555555555c....
                ......ccb55555555555c...
                ...cc..b55555ff155555c..
                ...cccb5555555ff55d55c..
                ....ccb55555d55555555c..
                .....b55555d5555d5555c..
                ..cc.b555ddd55555bbbbc..
                ..cccd55ddddd5555d555c..
                ...ccdd5dbdddbbbd555c...
                ....bdddb555bbbbbccc....
                ..cccdddb555cbbbbbbc....
                ...ccddddb555cbbbbbbc...
                ....cdddddb555cbbbbbc...
                ...ccddddddb55cbbbbbcc..
                ..ccbddddd55bcbbbbbbcc..
                ccdddddddd5555bbbbbbc...
                cdddddddbdd555bbbbbc....
                .ccddddbbbdd55cbbccc....
                ...cccbbcbddddccdddcc...
                ......cccdd555dcccccc...
                ........cccccccc........
        """),
        img("""
            ........ccc.............
                ........cccccccc........
                .....cc..cc55555cc......
                .....cccc555555555c.....
                .....ccb55555555555c....
                ...cc.b5555bcc555555c...
                ...ccb55555555c55d55c...
                ....cb5555dd55555555c...
                .....5555dd5555d5555c...
                ..cc.555dd555555dbbbc...
                ..ccc55ddd555555d555c...
                ...ccd5dbdd5555d555c....
                ....bdddb555bbbbbccc....
                ..cccdddb555cbbbbbbbc...
                ...ccddddb555cbbbbbbbc..
                ....cdddddb555cbbbbbbc..
                ...ccddddddb55cbbbbbbcc.
                ...cbddddd55bcbbbbbbbcc.
                ..cbdddddd5555bbbbbbbc..
                .cddddddbdd555bbbbbbc...
                cddddddbbbdd55cbbccc....
                ccccccbbcbddddccdddcc...
                ......cccdd555dcccccc...
                ........cccccccc........
        """),
        img("""
            ........................
                ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb55555bcc555555c
                ......cb555555555c55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb1bbbc.
                ....ccd55ddddd5bbbb335c.
                ...ccbdddddddd5bbbb335c.
                .ccccddddddddd55bbb335c.
                cdcccdddddb55bb5bb3335c.
                cddbddddddb555bb5b3335c.
                cddddddddddb5555b53335c.
                ccddddddbd55bb55c5555c..
                .ccddddbbbdd55cccbccc...
                ...ccbbbcbddddccdddc....
                .....ccccdd555dccccc....
                ........cccccccc........
        """),
        img("""
            ........................
                ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb55555bcc555555c
                ......cb555555555c55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb1bbbc.
                ....ccd55ddddd5bbbb335c.
                ...ccbdddddddd5bbbb335c.
                .ccccddddddddd55bb3335c.
                cdcccdddddb55bb55b3335c.
                cddbddddddb555bb553335c.
                cddddddddddb5555b5555c..
                ccddddddbd55bb55cbccc...
                .ccddddbbbdd55ccbbc.....
                ...ccbbbcbddddccdddc....
                .....ccccdd555dccccc....
                ........cccccccc........
        """),
        img("""
            ........................
                ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb55555bcc555555c
                ......cb555555555c55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb1bbbc.
                ....ccd55ddddd55bbb335c.
                ...ccbddddddddd5bb3335c.
                .ccccdddddddddd55b3335c.
                cdcccdddddb55bbd553335c.
                cddbddddddb555bb55555c..
                cddddddddddb5555bbccc...
                ccddddddbd55bb55cbc.....
                .ccddddbbbdd55ccbdc.....
                ...ccbbbcbddddccdddc....
                .....ccccdd555dccccc....
                ........cccccccc........
        """)],
    500,
    True)
animation.run_image_animation(神兽2,
    [img("""
            . . f f f . . . . . . . . f f f 
                . f f c c . . . . . . f c b b c 
                f f c c . . . . . . f c b b c . 
                f c f c . . . . . . f b c c c . 
                f f f c c . c c . f c b b c c . 
                f f c 3 c c 3 c c f b c b b c . 
                f f b 3 b c 3 b c f b c c b c . 
                . c 1 b b b 1 b c b b c c c . . 
                . c 1 b b b 1 b b c c c c . . . 
                c b b b b b b b b b c c . . . . 
                c b 1 f f 1 c b b b b f . . . . 
                f f 1 f f 1 f b b b b f c . . . 
                f f 2 2 2 2 f b b b b f c c . . 
                . f 2 2 2 2 b b b b c f . . . . 
                . . f b b b b b b c f . . . . . 
                . . . f f f f f f f . . . . . .
        """),
        img("""
            . . f f f . . . . . . . . . . . 
                f f f c c . . . . . . . . f f f 
                f f c c c . c c . . . f c b b c 
                f f c 3 c c 3 c c f f b b b c . 
                f f c 3 b c 3 b c f b b c c c . 
                f c b b b b b b c f b c b c c . 
                c c 1 b b b 1 b c b b c b b c . 
                c b b b b b b b b b c c c b c . 
                c b 1 f f 1 c b b c c c c c . . 
                c f 1 f f 1 f b b b b f c . . . 
                f f f f f f f b b b b f c . . . 
                f f 2 2 2 2 f b b b b f c c . . 
                . f 2 2 2 2 2 b b b c f . . . . 
                . . f 2 2 2 b b b c f . . . . . 
                . . . f f f f f f f . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . c c . c c . . . . . . . . 
                . . f 3 c c 3 c c c . . . . . . 
                . f c 3 b c 3 b c c c . . . . . 
                f c b b b b b b b b f f . . . . 
                c c 1 b b b 1 b b b f f . . . . 
                c b b b b b b b b c f f f . . . 
                c b 1 f f 1 c b b f f f f . . . 
                f f 1 f f 1 f b c c b b b . . . 
                f f f f f f f b f c c c c . . . 
                f f 2 2 2 2 f b f b b c c c . . 
                . f 2 2 2 2 2 b c c b b c . . . 
                . . f 2 2 2 b f f c c b b c . . 
                . . . f f f f f f f c c c c c . 
                . . . . . . . . . . . . c c c c
        """),
        img("""
            . f f f . . . . . . . . f f f . 
                f f c . . . . . . . f c b b c . 
                f c c . . . . . . f c b b c . . 
                c f . . . . . . . f b c c c . . 
                c f f . . . . . f f b b c c . . 
                f f f c c . c c f b c b b c . . 
                f f f c c c c c f b c c b c . . 
                . f c 3 c c 3 b c b c c c . . . 
                . c b 3 b c 3 b b c c c c . . . 
                c c b b b b b b b b c c . . . . 
                c 1 1 b b b 1 1 b b b f c . . . 
                f b b b b b b b b b b f c c . . 
                f b c b b b c b b b b f . . . . 
                . f 1 f f f 1 b b b c f . . . . 
                . . f b b b b b b c f . . . . . 
                . . . f f f f f f f . . . . . .
        """)],
    500,
    True)

def on_update_interval():
    global transit, transform, a1, a3, a2, a4, time1, time2
    if controller.left.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 2 2 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
        """))
    if controller.up.is_pressed():
        mySprite.set_image(img("""
            . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . f f f f f 2 2 f f f f f . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e 2 f 2 f f 2 f 2 e f . . . 
                        . f f f 2 2 e e 2 2 f f f . . . 
                        f f e f 2 f e e f 2 f e f f . . 
                        f e e f f e e e e f e e e f . . 
                        . f e e e e e e e e e e f . . . 
                        . . f e e e e e e e e f . . . . 
                        . e 4 f f f f f f f f 4 e . . . 
                        . 4 d f 2 2 2 2 2 2 f d 4 . . . 
                        . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . f f . . f f . . . . . .
        """))
    if controller.down.is_pressed():
        mySprite.set_image(img("""
            . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
        """))
    if controller.right.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 2 2 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
        """))
    if mySprite.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile3
    """)):
        if game.ask("是否要传送到出生点"):
            game.show_long_text("即将传送到出生点", DialogLayout.BOTTOM)
            mySprite.start_effect(effects.cool_radial, 1000)
            tiles.place_on_random_tile(mySprite, sprites.dungeon.purple_outer_south_west)
    while mySprite.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile4
    """)):
        if game.ask("是否要传送到角斗场"):
            game.show_long_text("即将传送到角斗场", DialogLayout.BOTTOM)
            mySprite.start_effect(effects.cool_radial, 1000)
            tiles.place_on_random_tile(mySprite, assets.tile("""
                myTile10
            """))
    while mySprite.tile_kind_at(TileDirection.CENTER, sprites.dungeon.button_teal):
        if game.ask("是否要传送到禁林"):
            game.show_long_text("即将传送到禁林", DialogLayout.BOTTOM)
            mySprite.start_effect(effects.cool_radial, 1000)
            tiles.place_on_random_tile(mySprite, sprites.castle.tile_dark_grass3)
    while mySprite.tile_kind_at(TileDirection.CENTER, sprites.dungeon.button_pink):
        if game.ask("是否要传送到未名湖"):
            game.show_long_text("即将传送到未名湖", DialogLayout.BOTTOM)
            mySprite.start_effect(effects.cool_radial, 1000)
            tiles.place_on_random_tile(mySprite, sprites.castle.tile_grass1)
    if transform == 0 and mySprite.tile_kind_at(TileDirection.CENTER, sprites.dungeon.button_orange):
        game.show_long_text("请输入内卷星之王的密令", DialogLayout.BOTTOM)
        transit = game.ask_for_string("", 2)
        if transform == 0 and transit == "cb":
            transform = 1
            game.show_long_text("密令正确，即将传送到内卷星之王的宫殿！", DialogLayout.BOTTOM)
            scene.camera_shake(6, 1000)
            mySprite.destroy(effects.cool_radial, 2000)
    if mySprite.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile16
    """)):
        if game.ask("我是传送门", "您确定要离开吗？"):
            game.show_long_text("即将离开该场景", DialogLayout.BOTTOM)
            tiles.place_on_random_tile(mySprite, assets.tile("""
                myTile11
            """))
    if mySprite.tile_kind_at(TileDirection.CENTER, sprites.dungeon.chest_open) and a1 == 0:
        game.show_long_text("发现一个宝箱", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            ....................
                        ....................
                        ....................
                        .....7977777777.....
                        .....7777777777.....
                        .....7777777777.....
                        ......66666666......
                        ......77777777......
                        .....7797777777.....
                        .....7977777777.....
                        .....7977777777.....
                        .....7977777777.....
                        .....7777777777.....
                        .....7777777777.....
                        .....7777777776.....
                        .....7777777776.....
                        .....7777777776.....
                        ......76666666......
                        ....................
                        ....................
        """))
        game.show_long_text("得到神秘绿色药剂", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
        a1 = 1
    if mySprite.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile17
    """)) and a3 == 0:
        game.show_long_text("发现一个宝箱", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            ....................
                        ....................
                        ....................
                        ....................
                        ....................
                        ....................
                        ........dd55........
                        ........5555........
                        .........44.........
                        ........5555........
                        ........5d55........
                        .......5d5555.......
                        .......d55555.......
                        .......555555.......
                        .......555555.......
                        .......555555.......
                        .......555555.......
                        ........5555........
                        ........4444........
                        ....................
        """))
        game.show_long_text("得到神秘黄色药剂", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
        a3 = 1
    if mySprite.tile_kind_at(TileDirection.CENTER, sprites.dungeon.chest_closed) and a2 == 0:
        game.show_long_text("发现一个宝箱", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            ....................
                        ....................
                        ....................
                        ....79777777777.....
                        ....77777777777.....
                        ....77777777777.....
                        .....666666666......
                        .....777777777......
                        ....77977777777.....
                        ....79777777777.....
                        ....79777777777.....
                        ....79777777777.....
                        ....77777777777.....
                        ....77777777777.....
                        ....77777777776.....
                        ....77777777776.....
                        ....77777777776.....
                        .....766666666......
                        ....................
                        ....................
        """))
        game.show_long_text("里面有残破的字条，上面隐约有字迹【cb】", DialogLayout.CENTER)
        a2 = 1
    if mySprite.tile_kind_at(TileDirection.CENTER, sprites.swamp.swamp_tile13):
        game.show_long_text("你在禁林误入毒气池，结局是【毒死】", DialogLayout.BOTTOM)
        game.over(False, effects.slash)
    if mySprite.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile15
    """)) and a4 == 0:
        game.show_long_text("你发现了一处破损的墙壁，打算进去看看", DialogLayout.BOTTOM)
        a4 = 1
    if mySprite.tile_kind_at(TileDirection.CENTER, sprites.vehicle.road_intersection2):
        time1 += 1
        if time1 >= 20:
            game.show_long_text("没想到这都被你发现了！", DialogLayout.BOTTOM)
            game.set_dialog_cursor(img("""
                ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                ........4eee........
                                .......eeeeee.......
                                .........cc.........
                                .........4c.........
                                ........4444........
                                .......444444.......
                                ......44444444......
                                .....4444444444.....
                                .....4444444444.....
                                .....4444444444.....
                                ......44444444......
                                .......eeeeee.......
                                ....................
                                ....................
            """))
            game.show_long_text("恭喜你获得了神秘橙色药剂", DialogLayout.BOTTOM)
            game.set_dialog_cursor(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
            """))
            time1 = 0
    if mySprite.overlaps_with(bullet):
        time2 += 1
        if time2 >= 20:
            game.set_dialog_cursor(img("""
                ....................
                                ....................
                                ........4eee........
                                .......eeeeee.......
                                .......eeeeee.......
                                .........cc.........
                                .........ec.........
                                ........eeee........
                                ........eeee........
                                .......ee4eee.......
                                ......ee4eeeee......
                                .....ee4eeeeeee.....
                                .....ee4eeeeeee.....
                                .....eeeeeeeeee.....
                                .....eeeeeeeecc.....
                                ......eeeeeecc......
                                ......eeeeeecc......
                                .......eccccc.......
                                ....................
                                ....................
            """))
            time2 = 0
            game.show_long_text("你收集了卷卷怪和旧冠蝠的子弹，并配置了一份棕色药剂", DialogLayout.BOTTOM)
            game.set_dialog_cursor(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
            """))
    if mySprite.overlaps_with(zhu):
        game.set_dialog_cursor(img("""
            .......bbbbbbbbbbbbbbbbbb.......
                        ......bddddddddddddddddddb......
                        .....bddddddddddddddddddddb.....
                        ....bddddddddddddddddddddddb....
                        ...bddddddddddddddddddddddddb...
                        ..bddddddddddddddddddddddddddb..
                        ..c11111111111111111111111111c..
                        ..c11111111111111111111111111c..
                        .bccccccccccccccccccccccccccccb.
                        bb11111dd11dbbbbbbbbd11dd11111bb
                        c11bbcc11dd11dbbbbd11dd11ccbb11c
                        c1bbddbcb11dd111111dd11bcbddbb1c
                        c1bbbddbdbd11dddddd11dbdbddbbb1c
                        c11bbddcddbbd111111dbbddcddbb11c
                        cb1111dcbd11bbbbbbbb11dbcd1111bc
                        .cb111ccbdd1111111111ddbcc111bc.
                        ..cccc.cbdbb1bb11bb1bbdbc.cccc..
                        .......cbdbb1db11bd1bbdbc.......
                        .......cbdbd1dd11dd1dbdbc.......
                        .......cbdbd1dd11dd1dbdbc.......
                        ......ccbdbd1dd11dd1dbdbcc......
                        .....cbbbdbd1dd11dd1dbdbbbc.....
                        .....cdbbdbd1dd11dd1dbdbbdc.....
                        .....c11bbbd1dd11dd1dbbb11c.....
                        .....cd111bbbbbbbbbbbb111dc.....
                        ....cccd1111111111111111dccc....
                        ...cbddbbb111111111111bbbddbc...
                        ..cbddddddbbbbbbbbbbbbddddddbc..
                        ..c11111111111111111111111111c..
                        ..c11111111111111111111111111c..
                        ..c11111111111111111111111111c..
                        ..cbbbbbbbbbbbbbbbbbbbbbbbbbbc..
        """))
        game.show_long_text("我是孤独的湖心岛神柱，由内卷之力化成", DialogLayout.BOTTOM)
        game.show_long_text("只有集齐七瓶药剂，才能见到我", DialogLayout.BOTTOM)
        game.show_long_text("千百年来你是唯一一个", DialogLayout.BOTTOM)
        game.show_long_text("我将赐予你卷王之力", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
        game.show_long_text("【隐藏结局】：你获得了卷王之力，把cb赶出了卷王的宫殿，直接成为下一任卷王！", DialogLayout.FULL)
        game.over(True, effects.confetti)
    if mySprite.tile_kind_at(TileDirection.CENTER, sprites.dungeon.hazard_lava1):
        time1 += 1
        if time1 >= 20:
            game.set_dialog_cursor(img("""
                ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                .........bb.........
                                ........cccc........
                                ........cccc........
                                .........ff.........
                                .........cf.........
                                .........cc.........
                                ........cccc........
                                .......cbbccc.......
                                .......cbcccc.......
                                .......cccccc.......
                                .......cccccf.......
                                ........cfff........
                                ....................
                                ....................
            """))
            time1 = 0
            game.show_long_text("震惊，你从岩浆里捞出来一瓶神秘紫色药剂", DialogLayout.BOTTOM)
            game.set_dialog_cursor(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
            """))
    if mySprite.overlaps_with(egg2):
        game.show_long_text("你发现了大卷王用过的电脑，只不过被废弃了", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            ....................
                        ....................
                        ....................
                        ....................
                        ....................
                        ....................
                        .........888........
                        .........888........
                        ......888888888.....
                        ........fffff.......
                        .......9999999......
                        .......9999999......
                        .......9999999......
                        .......9999999......
                        .......9999999......
                        .......9999999......
                        ......888888888.....
                        ......fffffffff.....
                        ....................
                        ....................
        """))
        game.show_long_text("你从电脑柜里发现一瓶蓝色药剂", DialogLayout.BOTTOM)
        game.set_dialog_cursor(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
game.on_update_interval(200, on_update_interval)

#神兽图鉴
scene.set_background_image(img("""
    eeeee2222222222222222222222222222222222ee2222ee2222ee2222222eeeee2222222222222222222222222222222222ee22222eeee222ee2eeeee2222222222222222222222222222222222ee222
        222eeeee22222222222222222222222222222eee2222eeee2222ee222222222eeeee22222222222222222222222222222eee2222eeeee222ee22222eeeee22222222222222222222222222222eee2222
        222222eeeeeee222222222222222222222eeee22222eeeeee2222eee2222222222eeeeeee222222222222222222222eeee22222eeee2222ee222222222eeeeeee222222222222222222222eeee22222e
        222222222eeeeeeeeeeeeee2222222eeeee222222eeee22eee2222eeee22222222222eeeeeeeeeeeeee2222222eeeee222223eeee22222eeee22222222222eeeeeeeeeeeeee2222222eeeee222222eee
        e222222222222222222222222222eeee2222222eeee22222eef22222eeeee222222222222222222222222222eeee2333333eeee22222efe2eeeee222222222222222222222222222eeee2222222eeee2
        eeeeeeee22222222222222222222222222222eee2222222eeeefe222222eeeeeeeee22222222222222333333333333322eee2222222efe22222eeeeeeeee22222222222222222222222222222eee2222
        2222eeeeeeeee222222222222222222222eeee2222222eeeeeeeffe222222222eeeeeeeee222223333333333322222eeee2223322effeee222322222eeeeeeeee222222222222222222222eeee222222
        2223322222222222222222222222222eeee2222222eeeeeeee222efffe222222222222222222222222222222222eeee2233332efffe22eeeee233333222222222222222222222222222eeee2222222ee
        2222233332222222222222222222222222222222eeeeeeeee22222eefffe2222222222222222222222222222222233333332efffee22222eeeee2233333333333333333332222222222222222222eeee
        eeee22233333333333333332222222222222eeeeee222222222eeeee22ffffee22222222223333333333333333333332eeffff22eeeee22222eeeeee23333333333333222222222222222222eeeeeeee
        eeeeeeeeee233333333332222222222eeeeeee2222222222eeeee2222ffeefffffffee2222222222223333333332fffffffeeff2222eeeee222222eeeeeeee222222222222222222222eeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee22eeeeeeee2222eee222222ffeeeeeeeeeeffffffffffffffffffffffffeeeeeeeeeeff222222eee2222eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeee22222222222222ee22222222222222222222222222effeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffe22222222222222222222222222ee22222222222222eeeeeeeeeee
        eeeeeeeeee22222222222222222eeee2222222222222222222efffeeeeeeeeeeeeeeeeee2eeeeeeeeeeeeeeeeee2eeeeeeeeeeeeeefffe2222222222222222222eeee22222222222222222eeeeeeeeee
        eeeeeeeeee222222222222222222eeeeeeee222222222eeefffeeeeeeeeeeeeeeeeeeeee222222eeeeeeeeee2222eeeeeeeeeeeeeeeeefffeee222222222eeeeeeee222222222222222222eeeeeeeeee
        eeeeeeeee2222222222222222222eeeeeeeeeeeeeeeeffffeeeeeeeeeeeeeeeeeeeeeeee22222222222222222222ee2eeeeeeeeeeeeeeeeeffffeeeeeeeeeeeeeeee2222222222222222222eeeeeeeee
        eeeeeeeee2222222222222222222ee2222effffffffffffeeeeeeeeeeeeeeeeeeeeeeeee22222222222222222222ee22eeeeeeeeeeeeeeeefffffffffffffe2222ee2222222222222222222eeeeeeeee
        eeeeeeee22e22222222222222222ee2222eeee2efffffffeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeeffffffffe2eeee2222ee22222222222222222e22eeeeeeee
        eeeeeeee2222222222222222222ee22222ee22eeffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeeffffffffee22ee22222ee2222222222222222222eeeeeeee
        eeeeeeee2e2222222222222222eee22222ee22efffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeefffffffffe22ee22222eee2222222222222222e2eeeeeeee
        eeeeeee22e2222222222222222ee222222e22eefffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeefffffffffee22e222222ee2222222222222222e22eeeeeee
        eeeeeee22e222222222222222ee222222ee22effffffffeeeeeeeeeeeeeeeeee2eee22ee22222222222222222222e222eeee2eeeeeeeeeeeefffffffffe22ee222222ee222222222222222e22eeeeeee
        eeeeee22e2222222222222222ee222222e22eeffffffffeeeeeeeeeeeeeeeeee2eee22ee22222222222222222222e2222eee2eeeeeeeeeeeefffffffffee22e222222ee2222222222222222e22eeeeee
        eeeeee22e222222222222222ee222222ee2eeeffffffffeeeeeeeeeeeeeeeeee2ee222e222222222222222222222e2222eee2eeeeeeeeeeeefffffffffe3e2ee222222ee222222222222222e22eeeeee
        eeeee22ee222222222222222ee22222ee22eefffffffffeeeeeeeeeeeeeeeeee2ee222e2222222222222222222222e222eee2eeeeeeeeeeeeffffffffffe322ee22222ee222222222222222ee22eeeee
        eeeee22e222222222222222ee222222ee2eeeffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eee2eeeeeeeeeeeeffffffffffe3e2ee222222ee222222222222222e22eeeee
        eeee22ee222222222222222e222222ee22eefffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eee22eeeeeeeeeeeeffffffffffe322ee222222e222222222222222ee22eeee
        eeee22ee22e22222222222ee22222ee22eeffffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eeee2eeeeeeeeeeeefffffffffff3322ee22222ee22222222222e22ee22eeee
        eeee2ee222222222222222e222222ee32eeffffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeefffffffffffe332ee222222e222222222222222ee2eeee
        eee22ee22e22222222222e222222ee32eeffffffeffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeffffffffffff3322ee222222e22222222222e22ee22eee
        eee2ee222e22222222222e22222ee23eeeffffffeffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeffffffffffffe3322ee22222e22222222222e222ee2eee
        ee22ee22e22222222222e222222ee32eefffffffefffeeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeeffffffffffffe332ee222222e22222222222e22ee22ee
        ee2eee2ee2222222222e222222ee33eeefffffffefffeefeeeeeeeeeeeeeee222ee22ee2222222222222222222222e2222eee22eeeeeeeeeeeeffffffffffffe3322ee222222e2222222222ee2eee2ee
        eeeee22ee2222222222e22222ee33eeeffffffffffffeefeeeeeeeeeeeeeee22eee22ee2222222222222222222222e2222eee22eeeeeeeeeeeefffffffffffffe3322ee22222e2222222222ee22eeeee
        eeeee2ee2222222222222222eee33eeffffffffeffffeefeeeeeeeeeeeeeee22eee22ee2222222222222222222222e2222eee22eeeeeeeeeeeefeffffffffffffe332eee2222222222222222ee2eeeee
        eeee22ee2222222222222222ee33eeeffffffffeffffeefeeeeeeeeeeeeeee22ee222ee2222222222222222222222e2222eee22eeeeeeeeeeeefeffffefffffffe3332ee2222222222222222ee22eeee
        eeee2ee2222222222222222ee33eeefffffffffeffffeefeeeeeeeeeeeeeee22ee222e22222222222222222222222e2222eee22eeeeeeeeeeeeeeffffeffffffffe3322ee2222222222222222ee2eeee
        eeee2ee222222222222222ee333eeffffffffffefffeeeeeeeeeeeeeeeeeee22ee222e22222222222222222222222e2222eee22eeeeeeeeeeeeeeefffefffffffffe3322ee222222222222222ee2eeee
        eee2ee2222222222222222ee33eeeffffffffffefffeeeeeeeeeeeeeeeeeee22ee222e22222222222222222222222e22222ee22eeeeeeeeeeeeeeefffefffffffffee332ee2222222222222222ee2eee
        eee2ee222222222222222ee33eeefffffffffffefffeefeeeeeeeeeeeeeeee22ee222e22222222222222222222222ee2222eee2eeeeeeeeeeeeeeefffeffffffffffe3332ee222222222222222ee2eee
        ee2ee2222222222222222e33eeefffffffffffeefffeefeeeeeeeeeeeeeee222ee222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeffffeffffffffffe3322e2322222222222222ee2ee
        ee2ee222222222222232e333eeffffffffffffeefffeefeeeeeeeeeeeeeee22eee222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffe3322e322222222222222ee2ee
        e2ee2222222222222322e33eeeffffffffffffeefffeefeeeeeeeeeeeeeee22ee2222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffee332e2322222222222222ee2e
        e2ee222222222222332e33eeefffffffffffffeefffeefeeeeeeeeeeeeeee22ee2222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffeffffffffffffe3322e322222222222222ee2e
        eee222222222222332e33eeeffffffffffffffeeffeeeeeeeeeeeeeeeeeee22ee2222222222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffffe3322e322222222222222eee
        eee222222222222322332eefffffffffffffffefffeefeeeeeeeeeeeeeeee22ee2222222222222222222222222222ee2222eee22eeeeeeeeeeeeeeeeffeefffffffffffffe3322322222222222222eee
        ee222222222222332333eeeffffffffffffffeefffeefeeeeeeeeeeeeeee222ee22222222222222222222222222222e2222eee22eeeeeeeeeeeeeeeeffeefffffffffffffee3223322222222222222ee
        ee22222222222332233eeefffffffffffffffeefffeefeeeeeeeeee2eeee222ee22222222222222222222222222222e2222eee22eeeeeeeeeeeeeeeeffeeffffffffffffffee322322222222222222ee
        e22222222222332233eeeffffffffffffffffeefffeefeeeeeeeeee2eeee22eee22222222222222222222222222222e2222eee22eeeeeeeeeeeeeeeefffefffffffffffffffe3323322222222222222e
        e22222222222332332eefffffffffffffffffeefffeefeeeeeeeeeeeeeee22eee22222222222222222222222222222e2222eeee2eeeeeeeeeeeeeeeefffeefffffffffffffffe322322222222222222e
        22222e22222332232eeefffffffffffffffffeefffeefeeeeeeeee2eeeee22ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeeffeefffffffffffffffeee23322222222e22222
        22222e2222332232eeeffffffffffffffffffeeffeefeeeeeeeeee2eeeee22ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeeffeeffffffffffffffffeee2322222222e22222
        222222222332222eeeffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeeffeefffffffffffffffffeee332222222222222
        2222e222233222eeefffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeefffeffffffffffffffffffeee322222222e2222
        2222e222332222eeefffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeefffeefffffffffffffffffeee332222222e2222
        222e222332222eeeffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeefffeeffffffffffffffffffeee322222222e222
        222e22232e22eeefffffffffffffffffffffeefffeefeeeeeeeee2eeeee22eee222222222222222222222222222222222222eee22eeeeeeeeeeeeeeeeeffeefffffffffffffffffffee332e22222e222
        222e22222e2eeeffffffffffffffffffffffeefffefeeeeeeeeee2eeeee22ee2222222222222222222222222222222222222eee22eeeeeeeeeeeeeeeeeffeeffffffffffffffffffffee32e22222e222
        22ee2222e2eeeffffffffffffffffffffffeeffffefeeeeeeeeee2eeee222ee2222222222222222222222222222222222222eee22eeeeeeeeeeeeeeeeefffefffffffffffffffffffffee32e2222ee22
        22e22222e2eeeffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222222222222222222222222222222222222eee222eeeeeeeeeeeeeeeefffeeffffffffffffffffffffee32e22222e22
        22e2222eeeeefffffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee2222222222222222222222222222222222222eee222eeeeeeeeeeeeeeeefffeefffffffffffffffffffffeeeee2222e22
        2ee2222eeeeffffffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee2222222222222222222222222222222222222eeee22e2eeeeeeeeeeeeeefffeeffffffffffffffffffffffeeee2222ee2
        2e2222eeeefffffffffffffffffffffffffeefffefeeeeeeeeee2eeeee222ee2222222222222222222222222222222222222eeee22eeeeeeeeeeeeeeeeeffeefffffffffffffffffffffffeeee2222e2
        2e222eee2effffffffffffffffffffffffeeefffefeeeeeeeeee2eeee222eee222e222222222222222222222222222222222eeee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eee222e2
        2e222eee2effffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222e222222222222222222222222222222222eeee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eee222e2
        ee22eeee2effffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222e2222222222222222222222222222e22222eee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eeee22ee
        ee22eee22effffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222e2222222222222222222222222222e22222eee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe22eee22ee
        eeeeee22eeffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee222ee2222e2222222222222222222222222222e22222eee22ee2eeeeeeeeeeeeeeeffeeffffffffffffffffffffffee22eeeeee
        eeeee222efffffffffffffffffffffffffeeffffeeeeeeeeeee2eeeee222ee2222e2222222222222222222222222222e22222eee222e22eeeeeeeeeeeeeefffeeffffffffffffffffffffffe222eeeee
        2222222eeffffffffffffffffffffffffeeefffeeeeeeeeeee22eeee2222ee2222e2222222222222222222222222222e22222eee222e22eeeeeeeeeeeeeefffeeffffffffffffffffffffffee2222222
        222222eefffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee2222e22222e2222222222222222222222222222e22222eee222ee2eeeeeeeeeeeeeefffeefffffffffffffffffffffffee222222
        22222eeefffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee222ee22222e2222222222222222222222222222e22222eeee22ee2eeeeeeeeeeeeeeeffeefffffffffffffffffffffffeee22222
        222eeeeefffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee222ee22222e2222222222222222222222222222e22222eeee22ee2eeeeeeeeeeeeeeefffeeffffffffffffffffffffffeeeee222
        eeee2eeeeffffffffffffffffffffffffeeffffeeeeeeeeee22eeeee222ee2222ee2222222222222222222222222222e22222eeee22ee2eeeeeeeeeeeeeeefffeefffffffffffffffffffffeeee2eeee
        222e2ee2effffffffffffffffffffffffeeffffeeeeeeeeee22eeee2222ee2222ee2222222222222222222222222222e22222eeee22ee22eeeeeeeeeeeeeefffeefffffffffffffffffffffe2ee2e222
        222e2ee2efffffffffffffffffffffffeeeffffeeeeeeeeee22eeee2222ee2222ee2222222222222222222222222222e22222eeee22ee22eeeeeeeeeeeeeefffeefffffffffffffffffffffe2ee2e222
        222e2ee2efffffffffffffffffffffffeefffffeeeeeeeeee22eeee2222ee2222ee2222222222222222222222222222e22222eeee222e22eeeeeeeeeeeeeeffffeeffffffffffffffffffffe2ee2e222
        222e2ee2efffffffffffffffffffffffeefffffeeeeeeeee22eeeee2222ee2222ee2222222222222222222222222222e22222eeee222e22eeeeeeeeeeeeefffffeeffffffffffffffffffffe2ee2e222
        222e2ee22effffffffffffffffffffffeefffffeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeee222ee2eeeeeeeeeeeeeeffffeefffffffffffffffffffe22ee2e222
        222e2ee22effffffffffffffffffffffeeffffeeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeeee22ee2eeeeeeeeeeeeeefffffefffffffffffffffffffe22ee2e222
        222e2eee2effffffffffffffffffffffeeffffeeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeefffffefffffffffffffffffffe2eee2e222
        222e22ee2eefffffffffffffffffffffefffffeeeeeeeee222eee22222ee22222ee2222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeeffffffffffffffffffffffffee2ee22e222
        222e22ee22efffffffffffffffffffffefffffeeeeeeeee22eeee22222ee22222ee2222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
        222e22ee22efffffffffffffffffffffefffffeeeeeeeee22eeee22222ee22222e22222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
        222e22ee22efffffffffffffffffffffffffffeeeeeeeee22eee222222ee22222e22222222222222222222222222222ee22222eeee222e22eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
        222e22ee222effffffffffffffffffffffffffeeeeeeeee22eee222222ee22222e22222222222222222222222222222ee22222eeee222ee2eeeeeeeeeeeeeeefffffffffffffffffffffe222ee22e222
        222e22eee22effffffffffffffffffffffffffeeeeeeee22eeee222222e222222e22222222222222222222222222222ee22222eeee222ee22eeeeeeeeeeeeeefffffffffffffffffffffe22eee22e222
        222e222ee22effffffffffffffffffffffffffeeeeeeee22eeee222222e222222e22222222222222222222222222222ee22222eeee222ee22eeeeeeeeeeeefffffffffffffffffffffffe22ee222e222
        222e222ee22eeffffffffffffffffffffffffeeeeeeeee22eee2222222e222222ee22222eeee222eeee222eeee22222ee222222eeee22222eeeeeeeeeeeeeffffffffffffffffffffffee22ee222e222
        222e222ee222efffffffbffffffffbbbfffffbbeeeeebeeeeeeee222eebeeeeeeddeeeeeeedeeeeeeeeeeeedeeeeeeeddeeeeeebeee22eeeeeeeebeeeeebbfffffbbbffffffffbfffffe222ee222e222
        222e222ee222ebbfffbbbbbfffffbbbbbbbbbbbbbbbbbbeebbbbeeeeedddeeeedddddeeeddddeeeeddeeeeddddeeedddddeeeedbbbbeeebbbbeebbbbbbbbbbbbbbbbbbfffffbbbbbfffe222ee222e222
        222ee22ee222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee222ee22ee222
        222ee22ee2222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2222ee22ee222
        2222e222e2222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222e222e2222
        2222e222ee2222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2222ee222e2222
        2222e222ee2222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2222ee222e2222
        2222e222ee2222eebbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbee2222ee222e2222
        2222e2222e22e22ebbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbe22e22e2222e2222
        222222222e22e22eebbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbee22e22e222222222
        222222222e22e222ebbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbe222e22e222222222
        2222222222e22e22eebbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbee22e22e2222222222
        222222e222e22e222ebbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbe222e22e222e222222
        222222e222222e222eebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbee222e222222e222222
        222222e2222222e222ebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbe222e2222222e222222
        222222ee222222e222eebbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbee222e222222ee222222
        2222222e222222e2222ebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbe2222e222222e2222222
        22222e2e2222222e222eebbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbee222e2222222e2e22222
        22222e2e2222222e222eebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbee222e2222222e2e22222
        22222e2e22222222e22ebbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbe22e22222222e2e22222
        22222e2ee2222222e22ebbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbe22e2222222ee2e22222
        22222e2ee2222222eeeebbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbeeee2222222ee2e22222
        22222e22e2222222eeebbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbeee2222222e22e22222
        22222ee2e2222222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222222e2ee22222
        22222ee2e222222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee222222e2ee22222
        222222e2ee22222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe22222ee2e222222
        222222e22e2222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222e22e222222
        222222e22e22eeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeee22e22e222222
        222222e2eeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeee2e222222
        222222e2ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2e222222
        222222eeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeee222222
"""))
a1 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
a1.set_position(75, 99)
actorlist = [img("""
        . . . . . . . . . . . . . . . .
            . . . . . . . . c c c c . . . .
            . . . . . . c c d d d d c . . .
            . . . . . c c c c c c d c . . .
            . . . . c c 4 4 4 4 d c c . . .
            . . . c 4 d 4 4 4 4 4 1 c . c c
            . . c 4 4 4 1 4 4 4 4 d 1 c 4 c
            . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c
            f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f
            f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f
            f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f
            . f 4 4 4 4 1 c 4 f 4 d f f f f
            . . f f 4 d 4 4 f f 4 c f c . .
            . . . . f f 4 4 4 4 c d b c . .
            . . . . . . f f f f d d d c . .
            . . . . . . . . . . c c c . . .
    """),
    img("""
        ..................................................
            ..................................................
            ..................................................
            ..................................................
            ......777777777777................................
            ......777777777777................................
            ......777777777777................................
            ......777777777777................................
            ......777777777777................................
            ......777777777777................................
            ......777ffff77777..............dddddddddddd......
            ......777ffff77777..............dddddddddddd......
            ......777ffff77777........dddddddddddddd..........
            ......777ffff77777........dddddddddddddd..........
            ......777ffff77777........dddddddddddddd..........
            ....55555777777777......ddddddddd.................
            ....55555777777777......ddddddddd.................
            ....55555777777777......ddddddddd.................
            .55555555bbbbbbbbbbbbbbbbbbbbbbbb.................
            .55555555bbbbbbbbbbbbbbbbbbbbbbbb.................
            .55555555bbbbbbbbbbbbbbbbbbbbbbbb.................
            .........bbbbbbbbbbbbbbbbbbb1111111111111111......
            .........bbbbbbbbbbbbbbbbbbb1111111111111111......
            .........bbbbbbbbbbbbbbbbbbb1111111111111.........
            .........bbbbbbbbbbbbbbbbbbb1111111111111.........
            .........bbbbbbbbbbbbbbbbb111111111111111.........
            .........bbbbbbbbbbbbbbbbb11111111111.............
            .........bbbbbbbbbbbbbbbbb11111111111.............
            .........bbbbbbbbbbbbbbbbb11111111111.............
            .........bbbbbbbbbbbbbbbbbbbbbbbb.................
            .........bbbbbbbbbbbbbbbbbbbbbbbb.................
            .........bbbbbbbbbbbbbbbbbbbbbbbb.................
            .............bbb..........bbb.....................
            .............bbb..........bbb.....................
            .............444..........444444..................
            .............444..........444444..................
            .............444..........444444..................
            ..........444................444..................
            ..........444................444..................
            ..........444................444..................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
    """),
    img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ........ccccc...................
            ......ccbbbbbc..................
            ....ccddbbbbbbf.................
            ...cbbbddbbffbf.................
            ....ffffdbbffbff................
            .......fbbbbbbbf................
            .......fbbbbbbbff...............
            ......ffbbbbbbbbfff.............
            ......f6bbbbbb663ddcc...........
            .....cc66bbbb666dddddc..........
            .....cd36666663dddddddc.........
            .....cddd3333dbddddddbcc........
            .....cddddddddbdddddbbddc.......
            .....cddddddddbbdddbbdddbc......
            ......cddddddddbbdbbddddbbccc...
            ......ccddddddddbbbbcccccbbbcc..
            .......ccddddddddddddddbccffff..
            ........cccbddccbddddbbfff......
            ........c333bb333cbbfff.........
            ........c33cc33cc3fff...........
    """),
    img("""
        bbbb........bbbb.................
            c99bb......bb99b.................
            c999bb....bb999c.................
            c9b99bccccb99b9c.................
            c9bb99bccb99bb9c.................
            c93b99999999b39c.................
            c93399999999339c.................
            c99399999999399c.................
            c99999991199999c.................
            c999ff91119ff99c........bbbbbb...
            c999ff91111ff99c.......c999999bb.
            c99991111111999c......c99999999b.
            c9991111fff1199c.....c9991119999b
            c999c11fff1199bc.....c9911111999b
            c999cc111111c9bc.....c911dd11199b
            c99999bb33cc99bcc....cbddbbd1199c
            c999999b33c99999bbccccbbdbbb1199c
            c9999999bb9999999999999999bb1999c
            c999911119999999999999999999b999c
            c999111111999999999999999999999c.
            c99911111119999999999999999999cc.
            c99111111119999999999999999999c..
            c99111111111999999999999999999c..
            cb9111111111999999999999999999c..
            .f9111111111999999999999999999c..
            .ff111111111999999999999999999c..
            ..fb11111111999999999999999999c..
            ...fb1111119999999111111999999c..
            ...fbbb11119999991111111199999c..
            ....fbbfffb9999ccccccccccb9999c..
            ....fbbf..f999c.....fbbf.c9999c..
            ....fbbf..f999c.....fbbf.cc9999c.
            ....fbbf..f99c.......fbf..cc999c.
            ....fbbf..f99c.......fbbf..cc99c.
            ....fbbf..f99c.......fbbf...c99c.
            ....fbbf..f99c......fbbbf...c99c.
            ...fbbbf..f99c......ffff....cb9c.
            ...fbbf..f999c.............c999c.
            ...ffff..f99cc.............c999c.
            .........fffc..............cccc..
    """),
    img("""
        . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . . . . b c . . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            b d d d b b d 5 5 5 4 4 4 4 4 b
            b b d 5 5 5 b 5 5 4 4 4 4 4 b .
            b d c 5 5 5 5 d 5 5 5 5 5 b . .
            c d d c d 5 5 b 5 5 5 5 5 5 b .
            c b d d c c b 5 5 5 5 5 5 5 b .
            . c d d d d d d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
    """),
    img("""
        ..............ccccccccc........
            ............cc555555555cc......
            ...........c5555555555555c.....
            ..........c55555555555555dc....
            .........c555555555555b5bdc....
            .........555bc1555555555bdcccc.
            ........c555ccc55555555bbdccddc
            ........c555bcb5555555ccddcdddc
            .......c555555555551ccccddbdddc
            .......c555555b555c1cccbddbbdbc
            .......c5555555bbc33333ddddbcc.
            .......c555555555bc333555ddbc..
            .......c5555555555555555555c...
            .......cd555555555555cccc555c..
            .......cd55555555555c555c555c..
            .......cdd555555555b5555b555c..
            .......cddd55555ddbb555bb555c..
            .......cdddd55555555555b5555c..
            .......cddddd5555555ddb5555dc..
            c......cdddddd555555555555dcc..
            cc...ccddddddd555555555555dc...
            cdccccdddddd555555d55555ddcc...
            cdddddddddbd5555555ddddddccccc.
            ccdddddddbb55555555bddddccbddc.
            .ccddddddbd55555555bdddccdddc..
            ..cccddddbd5555555cddcccddbc...
            ....ccccccd555555bcccc.cccc....
            .........cc555555bc............
            .........cc55555555c...........
            ..........cccccccccc...........
    """),
    img("""
        . f f f . . . . . . . . f f f .
            f f c . . . . . . . f c b b c .
            f c c . . . . . . f c b b c . .
            c f . . . . . . . f b c c c . .
            c f f . . . . . f f b b c c . .
            f f f c c . c c f b c b b c . .
            f f f c c c c c f b c c b c . .
            . f c 3 c c 3 b c b c c c . . .
            . c b 3 b c 3 b b c c c c . . .
            c c b b b b b b b b c c . . . .
            c b 1 b b b 1 b b b b f c . . .
            f b b b b b b b b b b f c c . .
            f b c b b b c b b b b f . . . .
            . f 1 f f f 1 b b b c f . . . .
            . . f b b b b b b c f . . . . .
            . . . f f f f f f f . . . . . .
    """),
    img("""
        ..................................................
            ..................................................
            .................55555............................
            .................55555............................
            .................55555............................
            ......................555.........................
            ......................555.........................
            ......................555.........................
            .................55555555.........................
            .................55555555.........................
            ....................5555555555555.................
            ....................5555555555555.................
            ....................5555555555555.................
            .................5555555555555555.................
            .................5555555555555555.................
            ............55555555555555555555555...............
            ............55555555555555555555555...............
            ............55555555555555555555555...............
            ..........5555555555555555555555555...............
            ..........5555555555555555555555555...............
            ..........5555555555555555555555555555............
            ..........5555555555555555555555555555............
            ..........5555555555555555555555555555............
            .......5555555555fff55555555ff5555555555..........
            .......5555555555fff55555555ff5555555555..........
            .......5555555555fff55555555ff5555555555555.......
            .......5555555555fff55555555ff5555555555555.......
            .......5555555555fff55555555ff5555555555555.......
            .......555555555555555555555555555555555555.......
            .......555555555555555555555555555555555555.......
            .......555555555555555555555555555555555555.......
            .......555555555555555444444555555555555555555....
            .......555555555555555444444555555555555555555....
            ..........555555555555555444555555555555555.......
            ..........555555555555555444555555555555555.......
            ..........555555555555555444555555555555555.......
            ............5555555555555555555555555555..........
            ............5555555555555555555555555555..........
            ...............55555555555555555555555............
            ...............55555555555555555555555............
            ...............55555555555555555555555............
            .................555555555555555555...............
            .................555555555555555555...............
            ..................................................
            ..................................................
    """),
    img("""
        .................88888888888888...................
            ..........8888888888777777777778888888............
            ..........8888888888777777777778888888............
            ..........8888888888777777777778888888............
            ...88888887777888888888888888887777777888.........
            ...88888887777888888888888888887777777888.........
            ...88888887777888888888888888887777777888.........
            888888855588885558887777888555588888888888888.....
            888888855588885558887777888555588888888888888.....
            888888855588885558887777888555588888888888888.....
            888555555555555555558888555555555555558888888.....
            888555555555555555558888555555555555558888888.....
            888555555555555555558888555555555555558888888.....
            888555555555555555558888555555555555558888888.....
            888555555555555555555555555555555555555558888.....
            888555555555555555555555555555555555555558888.....
            888555555555555555555555555555555555555558888.....
            888555555555555555555555555555555555555558888.....
            5555555555fffffff5555555555fffffff55555555555555..
            5555555555fffffff5555555555fffffff55555555555555..
            5555555555fffffff5555555555fffffff55555555555555..
            555555555555555555555555555555555555555555555555..
            555555555555555555555555555555555555555555555555..
            555555555555555555555555555555555555555555555555..
            55555555555555555ffffffffff555555555555555555555..
            55555555555555555ffffffffff555555555555555555555..
            55555555555555555ffffffffff555555555555555555555..
            55555555555555555ffffffffff555555555555555555555..
            77755555555555555555555555555555555555555555555577
            77755555555555555555555555555555555555555555555577
            77755555555555555555555555555555555555555555555577
            77788885558888888555555555588888888888555888877777
            77788885558888888555555555588888888888555888877777
            77788885558888888555555555588888888888555888877777
            77788885558888888555555555588888888888555888877777
            77788888888888888888888888888888888888888888877777
            77788888888888888888888888888888888888888888877777
            77788888888888888888888888888888888888888888877777
            77788888888888888888888888888888888888888888877777
            77777777777777888888888888888888887777777777777777
            77777777777777888888888888888888887777777777777777
            77777777777777888888888888888888887777777777777777
            777777777777777777778888888777777777777777777.....
            777777777777777777778888888777777777777777777.....
            777777777777777777778888888777777777777777777.....
            ...77777777777888888888888888888887777777.........
            ...77777777777888888888888888888887777777.........
            ...77777777777888888888888888888887777777.........
    """),
    img("""
        ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            .......................999........................
            ......................99999.......................
            ....................999999999.....................
            ..................9999999999999...................
            ..................9999999999999...................
            ..................9999999999999...................
            ................8888888888888888888...............
            ............88888881111111111188888888............
            ............88888811111111111118888888............
            ............88881111111111111111188888............
            ...............1111111111111111111................
            ..............1111fff1111111fff1111...............
            ..............1111111f11111f1111111...............
            .......111...11111111111111111111111...111........
            ......11111.11111111f1111111f11111111.11111.......
            .......11111111111111111111111111111111111........
            ........111111111111111111111111111111111.........
            .........11111113311111fff11111331111111..........
            ............1111111111111111111111111.............
            ............1111111111111111111111111.............
            ............1111111111111111111111111.............
            ............1111111111111111111111111.............
            ............1111111111111111111111111.............
            ............1111111111111111111111111.............
            ............1111111111111111111111111.............
            .............11111111111111111111111..............
            ..............111111111111111111111...............
            ..............111111111111111111111...............
            ...............1111111111111111111................
            ................11111111111111111.................
            ................111111111111111...................
            ..............1111.11111111111111.................
            .............11111............1111................
            ............11111..............1111...............
            ................................11................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
    """),
    assets.image("""
        myImage0
    """),
    assets.image("""
        myImage
    """)]
wordlist = ["名称：钓钓鱼；属性：普通；介绍：擅长在摆打树洞钓鱼问答，数量极多，常见于未名湖",
    "名称：绿帽烤鸭；属性：普通；介绍：长相粗糙，天生绿帽，擅长烹饪烤鸭，喜欢吃钓鱼",
    "名称：闭卷鸟；属性：普通；介绍：鸟类中的卷王，不喜欢飞行，最喜欢在未名湖湖心岛开卷",
    "名称：你真狗；属性：稀有；介绍：一只特别"狗"的狗，一般都躲起来开卷，只有很小的概率被发现",
    "名称：学术垃鸡：属性：普通；介绍：摆打大学常见生物，内卷星球的异类，内卷星人正在思考要不要把这类生物送到地球去",
    "名称：卷卷怪；属性：超稀有；介绍：内卷星最卷的神兽，成长极快，完全体有极大破坏力，难以驯服",
    "名称：旧冠蝠；属性：超稀有；介绍：很少人见到过这类生物，唯一一次目击是在摆打大学45乙宿舍楼",
    "名称：识数鸡；属性：史诗；介绍：摆打大学数院最强实力的生物，用实力让数院绩点卷到飞起",
    "名称：地小空；属性：史诗；介绍：地球派遣到内卷星的大使，现被抓去做摆打地空学院吉祥物",
    "名称：费米子；属性；史诗；介绍；明明可以靠颜值萌化别人，偏偏要靠内卷卷倒别人",
    "名称：搬砖狗；属性：史诗；介绍：默默搬砖，渴望逃离内卷星，但不幸被摆打大学生科同学抓去做研究",
    "名称：未知；属性：神话；介绍：内卷星球实力最强的生物，隐藏在在卷王的城堡，无人见过它的真面目"]
order = 0

def on_update_interval():
    global order
    if controller.B.is_pressed():
        order += 1
        order = order % len(actorlist)
    if controller.A.is_pressed() and order > 0:
        order += -1
        order = order % len(actorlist)
    a1.set_position(75, 99)
    a1.set_image(actorlist[order])
    a1.say_text(wordlist[order])
game.on_update_interval(100, on_update_interval)


#未名湖宠物捕获部分

@namespace
class SpriteKind:
    npc = SpriteKind.create()
    npc3 = SpriteKind.create()
    npc1 = SpriteKind.create()
    npc2 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    game.set_dialog_cursor(img("""
        . . . . . . c c c . . . . . . .
                . . . . . . c 5 b c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f f b b b b b b f f . . .
                . . . e e f e e e e f e e . . .
                . . e b f b 5 b b 5 b c b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
    """))
    game.show_long_text("据说唯一的传说神兽就藏在卷王的宫殿，但还没有人见过它", DialogLayout.CENTER)
    pause(500)
    npc32.set_kind(SpriteKind.projectile)
sprites.on_overlap(SpriteKind.player, SpriteKind.npc3, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.set_dialog_cursor(img("""
        . . . . f f f f . . . .
                . . f f e e e e f f . .
                . f f e e e e e e f f .
                f f f f 4 e e e f f f f
                f f f 4 4 4 e e f f f f
                f f f 4 4 4 4 e e f f f
                f 4 e 4 4 4 4 4 4 e 4 f
                f 4 4 f f 4 4 f f 4 4 f
                f e 4 d d d d d d 4 e f
                . f e d d b b d d e f .
                . f f e 4 4 4 4 e f f .
                e 4 f b 1 1 1 1 b f 4 e
                4 d f 1 1 1 1 1 1 f d 4
                4 4 f 6 6 6 6 6 6 f 4 4
                . . . f f f f f f . . .
                . . . f f . . f f . . .
    """))
    game.show_long_text("我今天运气真好，捕获了稀有动物【你真狗】", DialogLayout.BOTTOM)
    pause(500)
    npc12.set_kind(SpriteKind.projectile)
sprites.on_overlap(SpriteKind.player, SpriteKind.npc1, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    game.set_dialog_cursor(img("""
        . . . . . f f f f . . . . .
                . . . f f 5 5 5 5 f f . . .
                . . f 5 5 5 5 5 5 5 5 f . .
                . f 5 5 5 5 5 5 5 5 5 5 f .
                . f 5 5 5 d b b d 5 5 5 f .
                f 5 5 5 b 4 4 4 4 b 5 5 5 f
                f 5 5 c c 4 4 4 4 c c 5 5 f
                f b b f b f 4 4 f b f b b f
                f b b 4 1 f d d f 1 4 b b f
                . f b f d d d d d d f b f .
                . f e f e 4 4 4 4 e f e f .
                . e 4 f 6 9 9 9 9 6 f 4 e .
                . 4 d c 9 9 9 9 9 9 c d 4 .
                . 4 f b 3 b 3 b 3 b b f 4 .
                . . f f 3 b 3 b 3 3 f f . .
                . . . . f f b b f f . . . .
    """))
    game.show_long_text("你好，这里是摆打大学未名湖", DialogLayout.BOTTOM)
    pause(500)
    npc22.set_kind(SpriteKind.projectile)
sprites.on_overlap(SpriteKind.player, SpriteKind.npc2, on_on_overlap3)

mySprite: Sprite = None
npc32: Sprite = None
npc22: Sprite = None
npc12: Sprite = None
tiles.set_current_tilemap(tilemap("""
    级别1
"""))
npc12 = sprites.create(img("""
        . . . . f f f f . . . .
            . . f f e e e e f f . .
            . f f e e e e e e f f .
            f f f f 4 e e e f f f f
            f f f 4 4 4 e e f f f f
            f f f 4 4 4 4 e e f f f
            f 4 e 4 4 4 4 4 4 e 4 f
            f 4 4 f f 4 4 f f 4 4 f
            f e 4 d d d d d d 4 e f
            . f e d d b b d d e f .
            . f f e 4 4 4 4 e f f .
            e 4 f b 1 1 1 1 b f 4 e
            4 d f 1 1 1 1 1 1 f d 4
            4 4 f 6 6 6 6 6 6 f 4 4
            . . . f f f f f f . . .
            . . . f f . . f f . . .
    """),
    SpriteKind.npc1)
tiles.place_on_random_tile(npc12, sprites.castle.tile_grass3)
npc22 = sprites.create(img("""
        . . . . . f f f f . . . . .
            . . . f f 5 5 5 5 f f . . .
            . . f 5 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 f .
            . f 5 5 5 d b b d 5 5 5 f .
            f 5 5 5 b 4 4 4 4 b 5 5 5 f
            f 5 5 c c 4 4 4 4 c c 5 5 f
            f b b f b f 4 4 f b f b b f
            f b b 4 1 f d d f 1 4 b b f
            . f b f d d d d d d f b f .
            . f e f e 4 4 4 4 e f e f .
            . e 4 f 6 9 9 9 9 6 f 4 e .
            . 4 d c 9 9 9 9 9 9 c d 4 .
            . 4 f b 3 b 3 b 3 b b f 4 .
            . . f f 3 b 3 b 3 3 f f . .
            . . . . f f b b f f . . . .
    """),
    SpriteKind.npc2)
tiles.place_on_random_tile(npc22, sprites.castle.tile_grass1)
npc32 = sprites.create(img("""
        . . . . . . . c c c . . . . . .
            . . . . . . c b 5 c . . . . . .
            . . . . c c c 5 5 c c c . . . .
            . . c c b c 5 5 5 5 c c c c . .
            . c b b 5 b 5 5 5 5 b 5 b b c .
            . c b 5 5 b b 5 5 b b 5 5 b c .
            . . f 5 5 5 b b b b 5 5 5 c . .
            . . f f 5 5 5 5 5 5 5 5 f f . .
            . . f f f b f e e f b f f f . .
            . . f f f 1 f b b f 1 f f f . .
            . . . f f b b b b b b f f . . .
            . . . e e f e e e e f e e . . .
            . . e b c b 5 b b 5 b f b e . .
            . . e e f 5 5 5 5 5 5 f e e . .
            . . . . c b 5 5 5 5 b c . . . .
            . . . . . f f f f f f . . . . .
    """),
    SpriteKind.npc3)
tiles.place_on_random_tile(npc32, sprites.castle.tile_grass2)
player1 = sprites.create(img("""
        . . . . . . f f f f . . . . . .
            . . . . f f f 2 2 f f f . . . .
            . . . f f f 2 2 2 2 f f f . . .
            . . f f f e e e e e e f f f . .
            . . f f e 2 2 2 2 2 2 e e f . .
            . . f e 2 f f f f f f 2 e f . .
            . . f f f f e e e e f f f f . .
            . f f e f b f 4 4 f b f e f f .
            . f e e 4 1 f d d f 1 4 e e f .
            . . f e e d d d d d d e e f . .
            . . . f e e 4 4 4 4 e e f . . .
            . . e 4 f 2 2 2 2 2 2 f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(player1)
tiles.place_on_random_tile(player1, sprites.castle.tile_grass2)
scene.camera_follow_sprite(player1)
for index in range(randint(0, 3)):
    mySprite = sprites.create(img("""
            . . 7 7 7 7 7 7 . . . . . . . .
                    . . 7 7 7 7 7 7 . . . . . . . .
                    . . 7 7 f f 7 7 . . . . . . . .
                    . . 5 7 f f 7 7 . . . . . 1 1 1
                    . 5 5 5 7 7 7 7 . . . d d d d .
                    5 5 5 . d d d d d . 1 1 1 . . .
                    . . . d d d d d 1 1 1 d d d . .
                    . . . d d d d d d d d d d d d .
                    . . . d d d d d d d d d d d d 1
                    9 9 d d d d d d d d d d d d d 1
                    9 9 d d d d d d d d d d d 9 9 9
                    9 9 9 9 9 1 9 9 9 d d 1 9 9 9 9
                    9 9 9 9 4 9 9 9 9 9 9 4 9 9 9 9
                    9 9 9 4 9 9 9 9 9 9 9 4 9 9 9 9
                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
        """),
        SpriteKind.projectile)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile0
    """))
for index2 in range(randint(0, 5)):
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . c c c c . . . .
                    . . . . . . c c d d d d c . . .
                    . . . . . c c c c c c d c . . .
                    . . . . c c 4 4 4 4 d c c . . .
                    . . . c 4 d 4 4 4 4 4 1 c . c c
                    . . c 4 4 4 1 4 4 4 4 d 1 c 4 c
                    . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c
                    f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f
                    f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f
                    f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f
                    . f 4 4 4 4 1 c 4 f 4 d f f f f
                    . . f f 4 d 4 4 f f 4 c f c . .
                    . . . . f f 4 4 4 4 c d b c . .
                    . . . . . . f f f f d d d c . .
                    . . . . . . . . . . c c c . . .
        """),
        SpriteKind.projectile)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile0
    """))
for index3 in range(randint(0, 1)):
    mySprite = sprites.create(img("""
            .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    ...bbb.....bb....................
                    ...c9bb...b99....................
                    ...c999ccc9b9....................
                    ...c9b9999939....................
                    ...c939999939....................
                    ...c999911999....................
                    ...c99f911f99....c9999b..........
                    ...c9911ff199...c991999..........
                    ...c99c1ff19b...c911199..........
                    ...c999b33c9bc..cddb119..........
                    ...c9999bb999999999b199..........
                    ...c991111999999999999c..........
                    ...c991111999999999999c..........
                    ...c991111999999999999c..........
                    ....f11111199999999999...........
                    .....b1111199999999999...........
                    .....fb111999911119999...........
                    ......fbff999cccccc999...........
                    ......fb..99c...bf.c99c..........
                    ......fb..9c....fbf.c9c..........
                    ......fb..9c....fbf.c9c..........
                    .....fbb..9c....ff..cbc..........
                    .....fff.f9c........99c..........
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
                    .................................
        """),
        SpriteKind.projectile)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile8
    """))
for index4 in range(randint(0, 2)):
    mySprite = sprites.create(img("""
            ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ...............ccc..............
                    ............ccdbbbbf............
                    ...........cbbddbfbf............
                    ..............fbbbbb............
                    ..............fbbbbbf...........
                    ..............6bbbb63dcc........
                    .............c66bb66dddd........
                    .............cdd33dbddddcc......
                    .............cdddddbdddbdd......
                    ..............ddddddbdbdddbcc...
                    ..............cdddddbbbcccbbcc..
                    ...............ccbdcbdddbff.....
                    ...............c33b33cbff.......
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
        """),
        SpriteKind.projectile)
    tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)

def on_update_interval():
    if controller.up.is_pressed():
        player1.set_image(img("""
            . . . . . . f f f f . . . . . .
                        . . . . f f e e e e f f . . . .
                        . . . f e e e f f e e e f . . .
                        . . f f f f f 2 2 f f f f f . .
                        . . f f e 2 e 2 2 e 2 e f f . .
                        . . f e 2 f 2 f f 2 f 2 e f . .
                        . . f f f 2 2 e e 2 2 f f f . .
                        . f f e f 2 f e e f 2 f e f f .
                        . f e e f f e e e e f e e e f .
                        . . f e e e e e e e e e e f . .
                        . . . f e e e e e e e e f . . .
                        . . e 4 f f f f f f f f 4 e . .
                        . . 4 d f 2 2 2 2 2 2 f d 4 . .
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                        . . . . . f f f f f f . . . . .
                        . . . . . f f . . f f . . . . .
        """))
    if controller.right.is_pressed():
        player1.set_image(img("""
            . . . . . . . . . . . . . . . .
                        . . . . . . f f f f f f . . . .
                        . . . . f f e e e e f 2 f . . .
                        . . . f f e e e e f 2 2 2 f . .
                        . . . f e e e f f e e e e f . .
                        . . . f f f f e e 2 2 2 2 e f .
                        . . . f e 2 2 2 f f f f e 2 f .
                        . . f f f f f f f e e e f f f .
                        . . f f e 4 4 e b f 4 4 e e f .
                        . . f e e 4 d 4 1 f d d e f . .
                        . . . f e e e e e d d d f . . .
                        . . . . . f 4 d d e 4 e f . . .
                        . . . . . f e d d e 2 2 f . . .
                        . . . . f f f e e f 5 5 f f . .
                        . . . . f f f f f f f f f f . .
                        . . . . . f f . . . f f f . . .
        """))
    if controller.left.is_pressed():
        player1.set_image(img("""
            . . . . . . . . . . . . . . . .
                        . . . . f f f f f f . . . . . .
                        . . . f 2 f e e e e f f . . . .
                        . . f 2 2 2 f e e e e f f . . .
                        . . f e e e e f f e e e f . . .
                        . f e 2 2 2 2 e e f f f f . . .
                        . f 2 e f f f f 2 2 2 e f . . .
                        . f f f e e e f f f f f f f . .
                        . f e e 4 4 f b e 4 4 e f f . .
                        . . f e d d f 1 4 d 4 e e f . .
                        . . . f d d d e e e e e f . . .
                        . . . f e 4 e d d 4 f . . . . .
                        . . . f 2 2 e d d e f . . . . .
                        . . f f 5 5 f e e f f f . . . .
                        . . f f f f f f f f f f . . . .
                        . . . f f f . . . f f . . . . .
        """))
    if controller.down.is_pressed():
        player1.set_image(img("""
            . . . . . . f f f f . . . . . .
                        . . . . f f f 2 2 f f f . . . .
                        . . . f f f 2 2 2 2 f f f . . .
                        . . f f f e e e e e e f f f . .
                        . . f f e 2 2 2 2 2 2 e e f . .
                        . . f e 2 f f f f f f 2 e f . .
                        . . f f f f e e e e f f f f . .
                        . f f e f b f 4 4 f b f e f f .
                        . f e e 4 1 f d d f 1 4 e e f .
                        . . f e e d d d d d d e e f . .
                        . . . f e e 4 4 4 4 e e f . . .
                        . . e 4 f 2 2 2 2 2 2 f 4 e . .
                        . . 4 d f 2 2 2 2 2 2 f d 4 . .
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                        . . . . . f f f f f f . . . . .
                        . . . . . f f . . f f . . . . .
        """))
game.on_update_interval(200, on_update_interval)

#角斗场部分
stage = 0
mySprite3: Sprite = None
attack = 0
effects.blizzard.start_screen_effect()
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999111199999999999999999999999999999999999999999999999999999999999999999999999999999911119999999999999999999999999999999999999999999999999999
        9999999999999999999991111119999999999999999999999999999999999999999999999999999999999999999999999999999111111999999999999999999999999999999999999999999999999999
        9999999999999999999991111119911999999999999999999999999999999999999999999999999999999999999999999999999111111991199999999999999999999999999999999999999999999999
        9999999999999999991111111119111119999999999999999999999999999999999999999999999999999999999999999999111111111911111999999999999999999999999999999999999999999999
        9999999999999999911111111111111119999999999999999999999999999999999999999999999999999999999999999991111111111111111999999999999999999999999999999999999999999999
        9999999999999999111111111111111111199999999999999999999999999999999999999999999999999999999999999911111111111111111119999999999999999999999999999999999999999999
        9999999999999999111111111111111111119999999999999999999999999999999999999999999999999999999999999911111111111111111111999999999999999999999999999999999999999999
        9999999999999999911111111111111111119991199999999999999999999999999999999999999999999999999999999991111111111111111111999119999999999999999999999999999999999999
        9999999999999111191111111111111111119911111999999999999999999999999999999999999999999999999999911119111111111111111111991111199999999999999999999999999999999999
        9999999999991111119111111111111111199911111999999999999999999999999999999999999999999999999999111111911111111111111119991111199999999999999999999999999999999999
        9999999999991111111111111111111111911111111199999999999999999999999999999999999999999999999999111111111111111111111191111111119999999999999999999999999999999999
        9999999999991111111111111111111111111111111199999999999999999999999999999999999999999999999999111111111111111111111111111111119999999999999999999999999999999999
        9999999999999111111111111111111111111111111199999999999999999999999999999999999999999999999999911111111111111111111111111111119999999999999999999999999999999999
        9911199991111911111111111111111111111111111991199999999999991111999999999999999999991119999111191111111111111111111111111111199119999999999999111199999999999999
        9111119911111111111111111111111111111111111911119999999999911111199999999999999999911111991111111111111111111111111111111111191111999999999991111119999999999999
        9111119111111111111111111111111111111111111911119999999999911111191119999999999999911111911111111111111111111111111111111111191111999999999991111119111999999999
        9911111111111111111111111111111111111111111111119999999999999111111111999999999999991111111111111111111111111111111111111111111111999999999999911111111199999999
        9111111111111111111111111111111111111111111111199999999911119111111111999999999999911111111111111111111111111111111111111111111119999999991111911111111199999999
        1111111111111111111111111111111111111111111111119999999111111111111119999999999199111111111dd1111111111111111111111111111111111111999999911111111111111999999999
        1111111111111111111111111111111111111111111111111911199111111111111111111999999ddd111111111ddd111111111111111111111111111111111111191119911111111111111111199999
        1111111111111111111111111111111111111111111111111111111111111111111111111199991ddd111111111ddd111111111111111111111111111111111111111111111111111111111111119999
        11111111111111111111111111111111111111111111111111111111111111111111111111999ddddddd111111ddddd11111111111111111111111111111111111111111111111111111111111119999
        11111111111111111111111111111111111111111ddddddddd111111111111111111111111111ddddddd111111ddddd111111111111111111111111111111111111111111dddddddddd1111111111111
        11111111111111111111111111111111111111111ddddddddd111111111111111111111111111ddddddd111111ddddd111111111111111111111111111111111111111111dddddddddd1111111111111
        1111111111111111111ddd1111111111111111111d11dddddd111111111111111111111111111d11dddd11111ddddddd11111111111111111111dd1111111111111111111dd1d1ddddd1111111111111
        111111111111111111ddddd111111111111111111ddddddd1d111111111111111111111111111ddddddd11111ddddddd1111111111111111111dddd111111111111111111dddddd11dd1111111111111
        11111111111111111dddddd111111111111111111ddddddddd1111111111d11111111ddddd111d1ddddd11111ddddddd11111111111111111dddddd111111111111111111dddddddddd1111111111111
        11111111111111111ddd1d111111d111111111111ddddddddd111111111dd11111111ddddd111ddddddd11111ddddddd11111111111111111ddd1d111111dd11111111111dddd1ddddd11111111dd111
        11111111111111111dddddd11111d111111111111ddddddd1d111111111dd11111111ddddd111ddddddd11111ddddddd11111111111111111dddddd11111dd11111111111ddddddd1dd11111111dd111
        11111111ddd111111dd11d11111ddd11111111111ddddddddd11dddddd1dd11111111ddddd111ddddddd11111ddddddd111111111dd111111ddd1d11111ddd11111111111dddddddddd1ddddddddd111
        d1dd1111ddddddddddd1ddd111ddddd1111111111ddddddd1d11d11ddd1dd111111111dd1dd11ddddddd111dddddddddd1dd1111ddddddddddddd1d1111dddd1111111111dddddd11dd1d11dddddd111
        dddd11111d1dd1ddddddddd111ddddd1111111111ddddddddd11dddd1d1dd11111111dddddd11dd1dddd111ddddddddddddd1111dd1ddd1dddddddd1111dddd1111111111dddddddddd1dddd1dddd111
        dd1d11111ddd1111ddddddd111ddddd1111111111ddddddddd11dddd1dddd11111111dddddd11ddddddd111ddddddddddd1d1111dddd1d11ddddddd1111dddd1111111111dddddddddd1dddd1dddd111
        dddd1111dddddddddddddddd11dddddd11dd1dd1ddddddddddd1d11dddddd11111111dddddd11ddddddd111ddddddddddddd1111dddddddddddddddd11dddddd111d11ddddddddddddd1d11dddddd111
        dd1d1111dddddddddddddddd11dddddd11ddddddddddddddddd1ddddddddd11d11d11dddddd11ddddddd111ddddddddddd1d1111dddddddddddddddd11dddddd111dddddddddddddddd1ddddddddd111
        ddddd1dd1d1ddddddddddddd11ddddddd1dddd11ddddddddddddd11bbddddddd1ddd11dd1dd11ddddddd111ddddddddddddddd1ddd1ddddddddddddd11ddddddd111d11ddddddbddddddd11bbbddd1dd
        ddddd1dddddddddddddddddddd1dddddd1dddddddddbbbdddddddddbbbdddddd1ddd1dddddd11ddddddd111ddddddddddddddd1dddddddddddddddddddddddddd1ddddddddddbbdddddddddbbbddd1dd
        ddddd1ddddddddddddddddddddddddddd1dddddddddbbbdddddddddbbbdddddddddddddddddddddddddd111ddddddddddddddd1dddddddddddddddddddddddddd1ddddddddddbbdddddddddbbbdddddd
        ddddd1ddddddddddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddd1dddddddddddddddddddddddddd1d1ddddddbbbbbbbdddddbbbbbddddd
        dddddbbbbbbbbbddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddd1ddddddddbbbbbbbdddddbbbbbddddd
        dddddbbbbbbbbbddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddd1ddddddddbbbbbbbdddddbbbbbddddd
        dddddbddbbbbbbddddddddddddddddddd1dddddddbddbbbbdddddbbbbbbbdd111dddddddddddddddbbdddd1ddddddddddddddbbdbdbbbbbdddddddddddddddddd1ddddddddbbbbbbbddddbbbbbbbb11d
        dddddbbbbbbbdbddddddddddddddddddd1dddddddbbbbbbbdddddbbbbbbbddd11ddddddddddddddbbbbddd1ddddddddddddddbbbbbbddbbdddddddddddddddddd1ddddddddbbbbbbbddddbbbbbbbbddd
        dddddbbbbbbbbbddddddddddbddddddddbbbbbdddbdbbbbbdddddbbbbbbbddddddddddd1dddddbbbbbbddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddddbbbbddddbbbdbbbddddbbbbbbbbddd
        dddddbbbbbbbbbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd1ddddddddddddddbbbdbddddddbbdddddddddddbbbbdbbbbbddddddddbbdddddddddbbbbddddbbbdbbbddddbbbbbbbbd1d
        dddddbbbbbbbdbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd111ddddddddddddbbbbbbdddddbbdddddddddddbbbbbbbdbbddddddddbbddddddddbbbbbbdddbbbbbbbddddbbbbbbbb11d
        dddddbbbbbbbbbddbbbbbbdbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdddddddddbb1dddddbbbdbdddddbbbdddddddddddbbbbbbbbbbdbbbbbbbbbddddddddbbbbbbdddbbbdbbbddddbbbbbbbbddd
        dddddbbbbbbbdbddbddbbbdbbdddddddddbbdbbddbbbbbbbdddbbbbbbbbbbdbbddddbbbbbbbbbbbbbdbddddbbbbddddddddddbbbbbbddbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        dddddbbbbbbbbbddbbbbdbdbbddddddddbbbbbbddbbdbbbbdddbbbbbbbbbbbbbddddbbdbbbdbbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
        dddddbbbbbbbbbddbbbbdbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbdbddbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        dbbdbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbbbddddbbbbbbbbbbbbbbbbddbbbbbbdddbddbbbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbdbbbbbbbbbddbddbddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbbbbbbbbbbbbbddbbbbbbdddbbbbbbbbbbbbbbbbdbbbbbbbbbdddddbddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbddbbbbbbbbbbbbbddddbbbbbbbdbbbddbbdbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbdbbbbbbbbbbbbbddbbbbbbbdddbddbbbbbbbbbbbbbbddbdbbbbdbbdbbbdbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbdbbbbbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbdbbbbbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbb
        bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7
        bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77
        bb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777b
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))
mySprite = sprites.create(img("""
        . . . . . . . . . . b 5 b . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 d 1 f 5 5 d f . . 
            . . . . b 5 5 1 f f 5 d 4 c . . 
            . . . . b 5 5 d f b d d 4 4 . . 
            . b b b d 5 5 5 5 5 4 4 4 4 4 b 
            b d d d b b d 5 5 4 4 4 4 4 b . 
            b b d 5 5 5 b 5 5 5 5 5 5 b . . 
            c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
            c b d c d 5 5 b 5 5 5 5 5 5 b . 
            . c d d c c b d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite2 = sprites.create(img("""
        . . f f f . . . . . . . . . . . 
            f f f c c . . . . . . . . f f f 
            f f c c . . c c . . . f c b b c 
            f f c 3 c c 3 c c f f b b b c . 
            f f b 3 b c 3 b c f b b c c c . 
            . c b b b b b b c f b c b c c . 
            . c b b b b b b c b b c b b c . 
            c b 1 b b b 1 b b b c c c b c . 
            c b b b b b b b b c c c c c . . 
            f b c b b b c b b b b f c . . . 
            f b 1 f f f 1 b b b b f c c . . 
            . f b b b b b b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(20, 90)
mySprite2.set_position(140, 90)
list2 = [746, 100, 30]
list22 = [398, 200, 35]
info.player1.set_life(list2[0])
info.player2.set_life(list22[0])
op = 0
turn = 1

def on_on_update():
    global turn
    if turn == 9 and op == 2 and game.runtime() - attack >= 200:
        turn = 10
        mySprite3.destroy()
game.on_update(on_on_update)

def on_on_update2():
    global attack, turn
    if turn == 8 and op == 2 and game.runtime() - attack >= 2200:
        attack = game.runtime()
        turn = 9
        mySprite3.set_velocity(0, 0)
        animation.run_image_animation(mySprite3,
            [img("""
                    . . . . . . c c c . . . . . . . 
                                . . . . . a a a c c c . . . . . 
                                . . . c a c f a a a a c . . . . 
                                . . c a c f f f a f f a c . . . 
                                . c c a c c f a a c f f a c . . 
                                . a b a a c 6 a a c c f a c c c 
                                . a b b b 6 a b b a a c a f f c 
                                . . a b b a f f b b a a c f f c 
                                c . a a a c c f c b a a c f a c 
                                c c a a a c c a a a b b a c a c 
                                a c a b b a a 6 a b b 6 b b c . 
                                b a c b b b 6 b c . c c a c . . 
                                b a c c a b b a c . . . . . . . 
                                b b a c a b a a . . . . . . . . 
                                a b 6 b b a c . . . . . . . . . 
                                . a a b c . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 2 3 3 3 3 3 2 . . . . 
                                . . . . 3 1 1 1 1 1 1 1 3 . . . 
                                . . . . 1 1 1 1 1 1 1 1 1 . . . 
                                . . . 2 1 1 1 1 1 1 1 1 1 2 . . 
                                . . . 2 3 1 1 1 1 1 1 3 3 2 . . 
                                . . . . . . 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 4 4 4 4 4 . . . . . . 
                                . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                                . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                                . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                                . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                                . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                                . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                                . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                                . . . 2 2 4 d 5 5 d d 4 4 . . . 
                                . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                                . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                                . . . . . 2 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                                . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                                . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                                . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                                . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                                2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                                2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                                4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                                . . b b b b 2 4 4 2 b b b b . . 
                                . b d d d d 2 4 4 2 d d d d b . 
                                b d d b b b 2 4 4 2 b b b d d b 
                                b d d b b b b b b b b b b d d b 
                                b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                                . . b b d d 1 1 3 d d 1 b b . . 
                                . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                                . . . 2 2 4 4 4 4 4 2 2 2 . . .
                """),
                img("""
                    . . . . . . . . b b . . . . . . 
                                . . . . . . . . b b . . . . . . 
                                . . . b b b . . . . . . . . . . 
                                . . b d d b . . . . . . . b b . 
                                . b d d d b . . . . . . b d d b 
                                . b d d b . . . . b b . b d d b 
                                . b b b . . . . . b b . . b b . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . b b b d d d d d d b b b . . 
                                . b d c c c b b b b c c d d b . 
                                b d d c b . . . . . b c c d d b 
                                c d d b b . . . . . . b c d d c 
                                c b d d d b b . . . . b d d c c 
                                . c c b d d d d b . c c c c c c 
                                . . . c c c c c c . . . . . . .
                """)],
            200,
            False)
game.on_update(on_on_update2)

def on_on_update3():
    global op, attack, turn, mySprite2, stage
    if turn == 10 and game.runtime() - attack >= 2600:
        op = 0
        attack = game.runtime()
        mySprite2.destroy()
        turn = -2
        animation.stop_animation(animation.AnimationTypes.ALL, mySprite2)
        mySprite2 = sprites.create(img("""
                . . f f f . . . . . . . . . . . 
                            f f f c c . . . . . . . . f f f 
                            f f c c . . c c . . . f c b b c 
                            f f c 3 c c 3 c c f f b b b c . 
                            f f b 3 b c 3 b c f b b c c c . 
                            . c b b b b b b c f b c b c c . 
                            . c b b b b b b c b b c b b c . 
                            c b 1 b b b 1 b b b c c c b c . 
                            c b b b b b b b b c c c c c . . 
                            f b c b b b c b b b b f c . . . 
                            f b 1 f f f 1 b b b b f c c . . 
                            . f b b b b b b b b c f . . . . 
                            . . f b b b b b b c f . . . . . 
                            . . . f f f f f f f . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player)
        mySprite2.set_position(140, 90)
        if Math.percent_chance(list2[2]):
            mySprite.say_text("Miss", 1000, False)
        else:
            stage = -1 * randint(list2[1] - 50, list2[1] + 50)
            info.player1.change_life_by(stage)
            mySprite.say_text(stage, 1000, False)
game.on_update(on_on_update3)

def on_on_update4():
    global turn, attack
    if op == 1 and turn == 6:
        turn = 7
        attack = game.runtime()
        animation.run_image_animation(mySprite2,
            [img("""
                    . . f f f . . . . . . . . f f f 
                                . f f c c . . . . . . f c b b c 
                                f f c c . . . . . . f c b b c . 
                                f c f c . . . . . . f b c c c . 
                                f f f c c . c c . f c b b c c . 
                                f f c 3 c c 3 c c f b c b b c . 
                                f f b 3 b c 3 b c f b c c b c . 
                                . c 1 b b b 1 b c b b c c c . . 
                                . c 1 b b b 1 b b c c c c . . . 
                                c b b b b b b b b b c c . . . . 
                                c b 1 f f 1 c b b b b f . . . . 
                                f f 1 f f 1 f b b b b f c . . . 
                                f f 2 2 2 2 f b b b b f c c . . 
                                . f 2 2 2 2 b b b b c f . . . . 
                                . . f b b b b b b c f . . . . . 
                                . . . f f f f f f f . . . . . .
                """),
                img("""
                    . . f f f . . . . . . . . . . . 
                                f f f c c . . . . . . . . f f f 
                                f f c c c . c c . . . f c b b c 
                                f f c 3 c c 3 c c f f b b b c . 
                                f f c 3 b c 3 b c f b b c c c . 
                                f c b b b b b b c f b c b c c . 
                                c c 1 b b b 1 b c b b c b b c . 
                                c b b b b b b b b b c c c b c . 
                                c b 1 f f 1 c b b c c c c c . . 
                                c f 1 f f 1 f b b b b f c . . . 
                                f f f f f f f b b b b f c . . . 
                                f f 2 2 2 2 f b b b b f c c . . 
                                . f 2 2 2 2 2 b b b c f . . . . 
                                . . f 2 2 2 b b b c f . . . . . 
                                . . . f f f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . c c . c c . . . . . . . . 
                                . . f 3 c c 3 c c c . . . . . . 
                                . f c 3 b c 3 b c c c . . . . . 
                                f c b b b b b b b b f f . . . . 
                                c c 1 b b b 1 b b b f f . . . . 
                                c b b b b b b b b c f f f . . . 
                                c b 1 f f 1 c b b f f f f . . . 
                                f f 1 f f 1 f b c c b b b . . . 
                                f f f f f f f b f c c c c . . . 
                                f f 2 2 2 2 f b f b b c c c . . 
                                . f 2 2 2 2 2 b c c b b c . . . 
                                . . f 2 2 2 b f f c c b b c . . 
                                . . . f f f f f f f c c c c c . 
                                . . . . . . . . . . . . c c c c
                """),
                img("""
                    . f f f . . . . . . . . f f f . 
                                f f c . . . . . . . f c b b c . 
                                f c c . . . . . . f c b b c . . 
                                c f . . . . . . . f b c c c . . 
                                c f f . . . . . f f b b c c . . 
                                f f f c c . c c f b c b b c . . 
                                f f f c c c c c f b c c b c . . 
                                . f c 3 c c 3 b c b c c c . . . 
                                . c b 3 b c 3 b b c c c c . . . 
                                c c b b b b b b b b c c . . . . 
                                c 1 1 b b b 1 1 b b b f c . . . 
                                f b b b b b b b b b b f c c . . 
                                f b c b b b c b b b b f . . . . 
                                . f 1 f f f 1 b b b c f . . . . 
                                . . f b b b b b b c f . . . . . 
                                . . . f f f f f f f . . . . . .
                """)],
            100,
            True)
        animation.run_movement_animation(mySprite2,
            animation.animation_presets(animation.ease_left),
            2000,
            False)
        mySprite2.say_text("新冠无影脚", 5000, False)
game.on_update(on_on_update4)

def on_on_update5():
    global turn, attack
    if op == 1 and turn == 1:
        turn = 2
        attack = game.runtime()
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . b 5 5 b . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . b b b b b 5 5 5 5 5 5 5 b . . 
                                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                                . . b d 5 5 b 1 f f 5 4 4 c . . 
                                b b d b 5 5 5 d f b 4 4 4 4 b . 
                                b d d c d 5 5 b 5 4 4 4 4 4 4 b 
                                c d d d c c b 5 5 5 5 5 5 5 b . 
                                c b d d d d d 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . b b b b b 5 5 5 5 5 5 5 b . . 
                                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                                . . b d 5 5 b 1 f f 5 4 4 c . . 
                                b b d b 5 5 5 d f b 4 4 4 4 4 b 
                                b d d c d 5 5 b 5 4 4 4 4 4 b . 
                                c d d d c c b 5 5 5 5 5 5 5 b . 
                                c b d d d d d 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . . . . b c . . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 5 d f . . 
                                . . . . b 5 5 1 f f 5 d 4 c . . 
                                . . . . b 5 5 d f b d d 4 4 . . 
                                b d d d b b d 5 5 5 4 4 4 4 4 b 
                                b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                                b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                                c d d c d 5 5 b 5 5 5 5 5 5 b . 
                                c b d d c c b 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 d 4 c . . 
                                . . . . b 5 5 1 f f d d 4 4 4 b 
                                . . . . b 5 5 d f b 4 4 4 4 b . 
                                . . . b d 5 5 5 5 4 4 4 4 b . . 
                                . . b d d 5 5 5 5 5 5 5 5 b . . 
                                . b d d d d 5 5 5 5 5 5 5 5 b . 
                                b d d d b b b 5 5 5 5 5 5 5 b . 
                                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                                c b b d 5 d c d 5 5 5 5 5 5 b . 
                                . b 5 5 b c d d 5 5 5 5 5 d b . 
                                b b c c c d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 d 4 c . . 
                                . . . . b 5 5 1 f f d d 4 4 4 b 
                                . . . . b 5 5 d f b 4 4 4 4 b . 
                                . . . b d 5 5 5 5 4 4 4 4 b . . 
                                . b b d d d 5 5 5 5 5 5 5 b . . 
                                b d d d b b b 5 5 5 5 5 5 5 b . 
                                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                                c b b d 5 d c d 5 5 5 5 5 5 b . 
                                c b 5 5 b c d d 5 5 5 5 5 5 b . 
                                b b c c c d d d 5 5 5 5 5 d b . 
                                . . . . c c d d d 5 5 5 b b . . 
                                . . . . . . c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 5 d f . . 
                                . . . . b 5 5 1 f f 5 d 4 c . . 
                                . . . . b 5 5 d f b d d 4 4 . . 
                                . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                                b d d d b b d 5 5 4 4 4 4 4 b . 
                                b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                                c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                                c b d c d 5 5 b 5 5 5 5 5 5 b . 
                                . c d d c c b d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            100,
            True)
        animation.run_movement_animation(mySprite,
            animation.animation_presets(animation.ease_right),
            2000,
            False)
        mySprite.say_text("暴风鸭力斩", 5000, False)
game.on_update(on_on_update5)

def on_on_update6():
    global turn, stage
    if turn == 3 and op == 2 and game.runtime() - attack >= 200:
        turn = -1
        mySprite3.destroy()
        if Math.percent_chance(list2[2]):
            mySprite2.say_text("Miss", 1000, False)
        else:
            stage = -1 * randint(list22[1] - 50, list22[1] + 50)
            info.player1.change_life_by(stage)
            mySprite2.say_text(stage, 1000, False)
game.on_update(on_on_update6)

def on_on_update7():
    global turn, attack
    if turn == 3 and op == 1 and game.runtime() - attack >= 1500:
        turn = 4
        attack = game.runtime()
        animation.run_movement_animation(mySprite,
            animation.animation_presets(animation.bobbing_left),
            500,
            False)
game.on_update(on_on_update7)

def on_update_interval():
    global op
    if turn == 1 and controller.A.is_pressed():
        game.show_long_text("技能1：暴风鸭力斩   技能2：夺命火球", DialogLayout.BOTTOM)
        op = game.ask_for_number("请选择你的技能", 1)
game.on_update_interval(100, on_update_interval)

def on_update_interval2():
    global turn, op
    if turn == 6 and controller.A.is_pressed():
        turn = 7
        game.show_long_text("技能1：新冠无影脚   技能2：混沌之力", DialogLayout.BOTTOM)
        op = game.ask_for_number("请选择你的技能", 1)
game.on_update_interval(100, on_update_interval2)

def on_on_update8():
    global attack, turn, mySprite3
    if op == 2 and turn == 7:
        attack = game.runtime()
        turn = 8
        mySprite3 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . c c . . . . . . 
                            . . . . . c a a a a . . . . . . 
                            . . . . . a a f f b a . . . . . 
                            . . . . c a b f f c b . . . . . 
                            . . . . c b b b a f c b . . . . 
                            . . . . c b a c a b b b . . . . 
                            . . . . . b b f f a a c . . . . 
                            . . . . . . a a b b c . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player)
        mySprite3.set_position(135, 87)
        mySprite3.set_velocity(-50, 0)
        animation.run_image_animation(mySprite2,
            [img("""
                    . . f f f . . . . . . . . f f f 
                                . f f c c . . . . . . f c b b c 
                                f f c c . . . . . . f c b b c . 
                                f c f c . . . . . . f b c c c . 
                                f f f c c . c c . f c b b c c . 
                                f f c 3 c c 3 c c f b c b b c . 
                                f f b 3 b c 3 b c f b c c b c . 
                                . c 1 b b b 1 b c b b c c c . . 
                                . c 1 b b b 1 b b c c c c . . . 
                                c b b b b b b b b b c c . . . . 
                                c b 1 f f 1 c b b b b f . . . . 
                                f f 1 f f 1 f b b b b f c . . . 
                                f f 2 2 2 2 f b b b b f c c . . 
                                . f 2 2 2 2 b b b b c f . . . . 
                                . . f b b b b b b c f . . . . . 
                                . . . f f f f f f f . . . . . .
                """),
                img("""
                    . . f f f . . . . . . . . . . . 
                                f f f c c . . . . . . . . f f f 
                                f f c c c . c c . . . f c b b c 
                                f f c 3 c c 3 c c f f b b b c . 
                                f f c 3 b c 3 b c f b b c c c . 
                                f c b b b b b b c f b c b c c . 
                                c c 1 b b b 1 b c b b c b b c . 
                                c b b b b b b b b b c c c b c . 
                                c b 1 f f 1 c b b c c c c c . . 
                                c f 1 f f 1 f b b b b f c . . . 
                                f f f f f f f b b b b f c . . . 
                                f f 2 2 2 2 f b b b b f c c . . 
                                . f 2 2 2 2 2 b b b c f . . . . 
                                . . f 2 2 2 b b b c f . . . . . 
                                . . . f f f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . c c . c c . . . . . . . . 
                                . . f 3 c c 3 c c c . . . . . . 
                                . f c 3 b c 3 b c c c . . . . . 
                                f c b b b b b b b b f f . . . . 
                                c c 1 b b b 1 b b b f f . . . . 
                                c b b b b b b b b c f f f . . . 
                                c b 1 f f 1 c b b f f f f . . . 
                                f f 1 f f 1 f b c c b b b . . . 
                                f f f f f f f b f c c c c . . . 
                                f f 2 2 2 2 f b f b b c c c . . 
                                . f 2 2 2 2 2 b c c b b c . . . 
                                . . f 2 2 2 b f f c c b b c . . 
                                . . . f f f f f f f c c c c c . 
                                . . . . . . . . . . . . c c c c
                """),
                img("""
                    . f f f . . . . . . . . f f f . 
                                f f c . . . . . . . f c b b c . 
                                f c c . . . . . . f c b b c . . 
                                c f . . . . . . . f b c c c . . 
                                c f f . . . . . f f b b c c . . 
                                f f f c c . c c f b c b b c . . 
                                f f f c c c c c f b c c b c . . 
                                . f c 3 c c 3 b c b c c c . . . 
                                . c b 3 b c 3 b b c c c c . . . 
                                c c b b b b b b b b c c . . . . 
                                c 1 1 b b b 1 1 b b b f c . . . 
                                f b b b b b b b b b b f c c . . 
                                f b c b b b c b b b b f . . . . 
                                . f 1 f f f 1 b b b c f . . . . 
                                . . f b b b b b b c f . . . . . 
                                . . . f f f f f f f . . . . . .
                """)],
            500,
            False)
        mySprite2.say_text("混沌之力", 2000, False)
game.on_update(on_on_update8)

def on_on_update9():
    global attack, turn, mySprite3
    if op == 2 and turn == 1:
        attack = game.runtime()
        turn = 2
        mySprite3 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . 2 2 2 2 . . . 
                            . . . . . . . 2 2 1 1 1 1 2 . . 
                            . . . . 2 2 3 3 1 1 1 1 1 1 . . 
                            . . 3 3 3 3 1 1 1 1 1 1 1 1 . . 
                            . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                            . . 3 3 2 2 3 1 1 1 1 1 1 1 . . 
                            . . . . . . 2 2 3 1 1 1 1 2 . . 
                            . . . . . . . . . 2 2 2 2 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player)
        mySprite3.set_position(25, 87)
        mySprite3.set_velocity(50, 0)
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . b 5 5 b . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . b b b b b 5 5 5 5 5 5 5 b . . 
                                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                                . . b d 5 5 b 1 f f 5 4 4 c . . 
                                b b d b 5 5 5 d f b 4 4 4 4 b . 
                                b d d c d 5 5 b 5 4 4 4 4 4 4 b 
                                c d d d c c b 5 5 5 5 5 5 5 b . 
                                c b d d d d d 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . b b b b b 5 5 5 5 5 5 5 b . . 
                                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                                . . b d 5 5 b 1 f f 5 4 4 c . . 
                                b b d b 5 5 5 d f b 4 4 4 4 4 b 
                                b d d c d 5 5 b 5 4 4 4 4 4 b . 
                                c d d d c c b 5 5 5 5 5 5 5 b . 
                                c b d d d d d 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . . . . b c . . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 5 d f . . 
                                . . . . b 5 5 1 f f 5 d 4 c . . 
                                . . . . b 5 5 d f b d d 4 4 . . 
                                b d d d b b d 5 5 5 4 4 4 4 4 b 
                                b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                                b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                                c d d c d 5 5 b 5 5 5 5 5 5 b . 
                                c b d d c c b 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 d 4 c . . 
                                . . . . b 5 5 1 f f d d 4 4 4 b 
                                . . . . b 5 5 d f b 4 4 4 4 b . 
                                . . . b d 5 5 5 5 4 4 4 4 b . . 
                                . . b d d 5 5 5 5 5 5 5 5 b . . 
                                . b d d d d 5 5 5 5 5 5 5 5 b . 
                                b d d d b b b 5 5 5 5 5 5 5 b . 
                                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                                c b b d 5 d c d 5 5 5 5 5 5 b . 
                                . b 5 5 b c d d 5 5 5 5 5 d b . 
                                b b c c c d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 d 4 c . . 
                                . . . . b 5 5 1 f f d d 4 4 4 b 
                                . . . . b 5 5 d f b 4 4 4 4 b . 
                                . . . b d 5 5 5 5 4 4 4 4 b . . 
                                . b b d d d 5 5 5 5 5 5 5 b . . 
                                b d d d b b b 5 5 5 5 5 5 5 b . 
                                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                                c b b d 5 d c d 5 5 5 5 5 5 b . 
                                c b 5 5 b c d d 5 5 5 5 5 5 b . 
                                b b c c c d d d 5 5 5 5 5 d b . 
                                . . . . c c d d d 5 5 5 b b . . 
                                . . . . . . c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 5 d f . . 
                                . . . . b 5 5 1 f f 5 d 4 c . . 
                                . . . . b 5 5 d f b d d 4 4 . . 
                                . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                                b d d d b b d 5 5 4 4 4 4 4 b . 
                                b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                                c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                                c b d c d 5 5 b 5 5 5 5 5 5 b . 
                                . c d d c c b d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            500,
            False)
        mySprite.say_text("夺命火球", 2000, False)
game.on_update(on_on_update9)

def on_on_update10():
    global attack, turn
    if turn == 2 and op == 2 and game.runtime() - attack >= 2200:
        attack = game.runtime()
        turn = 3
        mySprite3.set_velocity(0, 0)
        animation.run_image_animation(mySprite3,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 2 2 3 3 3 3 2 . . . . 
                                . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
                                . 1 1 1 1 1 1 1 1 1 1 1 2 . . . 
                                . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
                                . . . . . 2 2 2 3 3 3 2 . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 2 3 3 3 3 3 2 . . . . 
                                . . . . 3 1 1 1 1 1 1 1 3 . . . 
                                . . . . 1 1 1 1 1 1 1 1 1 . . . 
                                . . . 2 1 1 1 1 1 1 1 1 1 2 . . 
                                . . . 2 3 1 1 1 1 1 1 3 3 2 . . 
                                . . . . . . 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 4 4 4 4 4 . . . . . . 
                                . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                                . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                                . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                                . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                                . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                                . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                                . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                                . . . 2 2 4 d 5 5 d d 4 4 . . . 
                                . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                                . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                                . . . . . 2 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                                . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                                . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                                . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                                . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                                2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                                2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                                4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                                . . b b b b 2 4 4 2 b b b b . . 
                                . b d d d d 2 4 4 2 d d d d b . 
                                b d d b b b 2 4 4 2 b b b d d b 
                                b d d b b b b b b b b b b d d b 
                                b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                                . . b b d d 1 1 3 d d 1 b b . . 
                                . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                                . . . 2 2 4 4 4 4 4 2 2 2 . . .
                """),
                img("""
                    . . . . . . . . b b . . . . . . 
                                . . . . . . . . b b . . . . . . 
                                . . . b b b . . . . . . . . . . 
                                . . b d d b . . . . . . . b b . 
                                . b d d d b . . . . . . b d d b 
                                . b d d b . . . . b b . b d d b 
                                . b b b . . . . . b b . . b b . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . b b b d d d d d d b b b . . 
                                . b d c c c b b b b c c d d b . 
                                b d d c b . . . . . b c c d d b 
                                c d d b b . . . . . . b c d d c 
                                c b d d d b b . . . . b d d c c 
                                . c c b d d d d b . c c c c c c 
                                . . . c c c c c c . . . . . . .
                """)],
            200,
            False)
game.on_update(on_on_update10)

def on_on_update11():
    global turn, attack
    if turn == 2 and op == 1 and game.runtime() - attack >= 3000:
        turn = 3
        attack = game.runtime()
        animation.run_movement_animation(mySprite,
            animation.animation_presets(animation.bobbing_right),
            500,
            False)
game.on_update(on_on_update11)

def on_on_update12():
    global turn, attack
    if turn == 7 and op == 1 and game.runtime() - attack >= 3000:
        turn = 8
        attack = game.runtime()
        animation.run_movement_animation(mySprite2,
            animation.animation_presets(animation.bobbing_left),
            500,
            False)
game.on_update(on_on_update12)

def on_on_update13():
    global turn, attack
    if turn == 4 and op == 1 and game.runtime() - attack >= 1500:
        turn = 5
        attack = game.runtime()
        animation.run_movement_animation(mySprite,
            animation.animation_presets(animation.ease_left),
            2000,
            False)
game.on_update(on_on_update13)

def on_on_update14():
    global turn, attack
    if turn == 8 and op == 1 and game.runtime() - attack >= 1500:
        turn = 9
        attack = game.runtime()
        animation.run_movement_animation(mySprite2,
            animation.animation_presets(animation.bobbing_right),
            500,
            False)
game.on_update(on_on_update14)

def on_on_update15():
    global op, attack, turn, mySprite, stage
    if turn == 5 and op == 1 and game.runtime() - attack >= 2600:
        op = 0
        attack = game.runtime()
        mySprite.destroy()
        turn = -1
        animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
        mySprite = sprites.create(img("""
                . . . . . . . . . . b 5 b . . . 
                            . . . . . . . . . b 5 b . . . . 
                            . . . . . . b b b b b b . . . . 
                            . . . . . b b 5 5 5 5 5 b . . . 
                            . . . . b b 5 d 1 f 5 5 d f . . 
                            . . . . b 5 5 1 f f 5 d 4 c . . 
                            . . . . b 5 5 d f b d d 4 4 . . 
                            . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                            b d d d b b d 5 5 4 4 4 4 4 b . 
                            b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                            c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                            c b d c d 5 5 b 5 5 5 5 5 5 b . 
                            . c d d c c b d 5 5 5 5 5 d b . 
                            . . c b d d d d d 5 5 5 b b . . 
                            . . . c c c c c c c c b b . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player)
        mySprite.set_position(20, 90)
        if Math.percent_chance(list22[2]):
            mySprite2.say_text("Miss", 1000, False)
        else:
            stage = -1 * randint(list2[1] - 50, list2[1] + 50)
            info.player2.change_life_by(stage)
            mySprite2.say_text(stage, 1000, False)
game.on_update(on_on_update15)

def on_on_update16():
    global turn
    if turn == -1 and game.runtime() - attack >= 2000:
        turn = 6
        if info.player2.life() <= 0:
            turn = 0
            game.set_dialog_cursor(img("""
                . f f f . . . . . . . . f f f . 
                                f f c . . . . . . . f c b b c . 
                                f c c . . . . . . f c b b c . . 
                                c f . . . . . . . f b c c c . . 
                                c f f . . . . . f f b b c c . . 
                                f f f c c . c c f b c b b c . . 
                                f f f c c c c c f b c c b c . . 
                                . f c 3 c c 3 b c b c c c . . . 
                                . c b 3 b c 3 b b c c c c . . . 
                                c c b b b b b b b b c c . . . . 
                                c 1 1 b b b 1 1 b b b f c . . . 
                                f b b b b b b b b b b f c c . . 
                                f b c b b b c b b b b f . . . . 
                                . f 1 f f f 1 b b b c f . . . . 
                                . . f b b b b b b c f . . . . . 
                                . . . f f f f f f f . . . . . .
            """))
            game.splash("不....这不可能！")
            game.splash("莫非，你就是传说中的...")
game.on_update(on_on_update16)

def on_on_update17():
    global turn
    if turn == -2 and game.runtime() - attack >= 2000:
        turn = 1
        if info.player1.life() <= 0:
            game.set_dialog_cursor(img("""
                . . . b 5 b . . . . . . . . . . 
                                . . . . b 5 b . . . . . . . . . 
                                . . . . . c b . . . . . . . . . 
                                . . . . b b b b b b . . . . . . 
                                . . . b 5 5 5 5 5 b b . . . . . 
                                . . f d 5 5 f 1 d 5 b b . . . . 
                                . . c 4 d 5 f f 1 5 5 b . . . . 
                                . . 4 4 d d b f d 5 5 b . . . . 
                                b 4 4 4 4 4 5 5 5 d b b d d d b 
                                . b 4 4 4 4 4 5 5 b 5 5 5 d b b 
                                . . b 5 5 5 5 5 d 5 5 5 5 c d b 
                                . b 5 5 5 5 5 5 b 5 5 d c d d c 
                                . b 5 5 5 5 5 5 5 b c c d d b c 
                                . b d 5 5 5 5 5 d d d d d d c . 
                                . . b b 5 5 5 d d d d d b c . . 
                                . . . b b c c c c c c c c . . .
            """))
            game.splash("少年，我低估了你的实力")
            game.splash("去吧，去找那个叫cb的卷王")
            turn = 0
game.on_update(on_on_update17)

def on_on_update18():
    global turn, stage
    if turn == 9 and op == 2 and game.runtime() - attack >= 200:
        turn = -2
        mySprite3.destroy()
        if Math.percent_chance(list2[2]):
            mySprite.say_text("Miss", 1000, False)
        else:
            stage = -1 * randint(list2[1] - 50, list2[1] + 50)
            info.player1.change_life_by(stage)
            mySprite.say_text(stage, 1000, False)
game.on_update(on_on_update18)

def on_on_update19():
    global turn, attack
    if turn == 9 and op == 1 and game.runtime() - attack >= 1500:
        turn = 10
        attack = game.runtime()
        animation.run_movement_animation(mySprite2,
            animation.animation_presets(animation.ease_right),
            2000,
            False)
game.on_update(on_on_update19)


#卷王城堡部分
def on_b_pressed():
    global mySprite3
    scene.set_background_image(assets.image("""
        myImage30
    """))
    tiles.set_current_tilemap(tilemap("""
        级别10
    """))
    mySprite2.destroy()
    mySprite.destroy()
    effects.hearts.start_screen_effect(2000)
    mySprite3 = sprites.create(assets.image("""
        myImage22
    """), SpriteKind.player)
    mySprite.set_position(74, 123)
    controller.move_sprite(mySprite3)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

mySprite3: Sprite = None
mySprite: Sprite = None
mySprite2: Sprite = None
tiles.set_current_tilemap(tilemap("""
    级别6
"""))
mySprite2 = sprites.create(img("""
        . . . . . . f f f f . . . . . .
            . . . . f f e e e e f f . . . .
            . . . f e e e f f e e e f . . .
            . . f f f f f 2 2 f f f f f . .
            . . f f e 2 e 2 2 e 2 e f f . .
            . . f e 2 f 2 f f 2 f 2 e f . .
            . . f f f 2 2 e e 2 2 f f f . .
            . f f e f 2 f e e f 2 f e f f .
            . f e e f f e e e e f e e e f .
            . . f e e e e e e e e e e f . .
            . . . f e e e e e e e e f . . .
            . . e 4 f f f f f f f f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile8
"""))
tiles.place_on_random_tile(mySprite2, assets.tile("""
    myTile14
"""))
controller.move_sprite(mySprite2)
scene.camera_follow_sprite(mySprite2)
animation.run_image_animation(mySprite2,
    [img("""
            . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f f 2 f e f . .
                . . f f f 2 f e e 2 2 f f f . .
                . . f e 2 f f e e 2 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . . e f f f f f f f f 4 e . .
                . . . 4 f 2 2 2 2 2 e d d 4 . .
                . . . e f f f f f f e e 4 . . .
                . . . . f f f . . . . . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e f 2 f f f 2 f 2 e f . .
                . . f f f 2 2 e e f 2 f f f . .
                . . f e e f 2 e e f f 2 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f e . . .
                . . 4 d d e 2 2 2 2 2 f 4 . . .
                . . . 4 e e f f f f f f e . . .
                . . . . . . . . . f f f . . . .
        """)],
    500,
    True)

def on_update_interval():
    if mySprite2.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile17
    """)):
        game.splash("cb的第一重试炼")
        game.show_long_text("周三23:59前完成cb本周所有作业！【注意是本周】", DialogLayout.CENTER)
        tiles.set_tile_at(tiles.get_tile_location(8, 43),
            assets.tile("""
                myTile2
            """))
    if mySprite2.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile16
    """)):
        game.splash("cb的第二重试炼")
        game.show_long_text("在b站将cb的所有视频一键三连", DialogLayout.CENTER)
        tiles.set_tile_at(tiles.get_tile_location(8, 36),
            assets.tile("""
                myTile2
            """))
        tiles.set_wall_at(tiles.get_tile_location(0, 0), False)
    if mySprite2.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile
    """)):
        game.splash("cb的第三重试炼")
        game.show_long_text("不流口水地看cb吃完肯德基疯狂星期四", DialogLayout.CENTER)
        tiles.set_tile_at(tiles.get_tile_location(8, 29),
            assets.tile("""
                myTile2
            """))
    if mySprite2.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile15
    """)):
        game.set_dialog_text_color(8)
        game.set_dialog_frame(img("""
            ..ffffffffffffffffffff..
                        .f22ff22ff22ff22ff22fff.
                        fff22ff22ff22ff22ff22f2f
                        ff2ffffffffffffffffff22f
                        f22ff11111111111111ff2ff
                        f2ff1111111111111111ffff
                        ffff1111111111111111ff2f
                        ff2f1111111111111111f22f
                        f22f1111111111111111f2ff
                        f2ff1111111111111111ffff
                        ffff1111111111111111ff2f
                        ff2f1111111111111111f22f
                        f22f1111111111111111f2ff
                        f2ff1111111111111111ffff
                        ffff1111111111111111ff2f
                        ff2f1111111111111111f22f
                        f22f1111111111111111f2ff
                        f2ff1111111111111111ffff
                        ffff1111111111111111ff2f
                        ff2ff11111111111111ff22f
                        f22ffffffffffffffffff2ff
                        f2f22ff22ff22ff22ff22fff
                        .fff22ff22ff22ff22ff22f.
                        ..ffffffffffffffffffff..
        """))
        game.show_long_text("现在我还有最后一重考验。", DialogLayout.CENTER)
        game.show_long_text("你若能完成，我便赋予你卷王之力！让你在内卷星一切考试中高于90分！让你成为下一任",
            DialogLayout.CENTER)
        game.set_dialog_text_color(2)
        game.show_long_text("【卷王】", DialogLayout.CENTER)
        game.show_long_text("大卷怪410号，敢不敢接受我的考验！", DialogLayout.CENTER)
        game.set_dialog_text_color(15)
        game.set_dialog_cursor(img("""
            . . . . . . f f f f . . . . . .
                        . . . . f f f 2 2 f f f . . . .
                        . . . f f f 2 2 2 2 f f f . . .
                        . . f f f e e e e e e f f f . .
                        . . f f e 2 2 2 2 2 2 e e f . .
                        . . f e 2 f f f f f f 2 e f . .
                        . . f f f f e e e e f f f f . .
                        . f f e f b f 4 4 f b f e f f .
                        . f e e 4 1 f d d f 1 4 e e f .
                        . . f f f f d d d d d e e f . .
                        . f d d d d f 4 4 4 e e f . . .
                        . f b b b b f 2 2 2 2 f 4 e . .
                        . f b b b b f 2 2 2 2 f d 4 . .
                        . . f c c f 4 5 5 4 4 f 4 4 . .
                        . . . f f f f f f f f . . . . .
                        . . . . . f f . . f f . . . . .
        """))
        game.show_long_text("大卷怪向卷而生，从不畏惧，我接受！", DialogLayout.CENTER)
        game.set_dialog_cursor(img("""
            . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
        game.set_dialog_text_color(2)
        game.show_long_text("好，我的最后一重考验是——给本视频的小组投票！将选票砸向他们吧！", DialogLayout.FULL)
game.on_update_interval(200, on_update_interval)
