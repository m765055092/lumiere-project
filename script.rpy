# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
#更改键位
init:
    $ config.underlay.append(renpy.Keymap(history = ShowMenu("history")))
    $ config.keymap["history"] = [ 'mousedown_4' ]
    $ config.keymap['dismiss'].append('mousedown_5')
    $ config.keymap['rollback']= ['K_PAGEUP']


define lloris = Character("洛里斯")
define eileen = Character("艾琳")
define ariel = Character("爱丽儿")
define kelly = Character("凯莉谱索")
define warfarin = Character("华芙琳")
define eberl = Character("埃布尔")
define marci = Character("麦瑞克")
define lilith = Character("莉莉丝")

define Alika = Character("Alika", image="Alika")

image black = "#000"
image white = '#fff'
image red = '#ff0000'

define MoveRight = ImageDissolve("images/rules/101.png", time=1.0,ramplen = 32)
define MoveDown = ImageDissolve("images/rules/02.jpg", time=1.0,ramplen = 32)
define QMoveup = ImageDissolve("images/rules/03.jpg", time=0.35,ramplen = 32)
define QMovedown = ImageDissolve("images/rules/03.jpg", time=0.35,ramplen = 32, reverse=True)
define slash = ImageDissolve("images/rules/06.jpg", time=0.35,ramplen = 32, reverse=True)
define slash_2 = ImageDissolve("images/rules/07.jpg", time=0.35,ramplen = 32)
define QMoveRight = ImageDissolve("images/rules/101.png", time=0.45,ramplen = 32)
define QMoveLeft = ImageDissolve("images/rules/101.png", time=0.45,ramplen = 32, reverse=True)
define MoveLeft = ImageDissolve("images/rules/101.png", time=1.0,ramplen = 32, reverse=True)
define CloseDoor = ImageDissolve("images/rules/11.jpg", time=1.0,ramplen = 32)
define OpenDoor = ImageDissolve("images/rules/11.jpg", time=1.0,ramplen = 32, reverse=True)
define ccirclewipe = ImageDissolve("images/rules/circlewipe-ccw.jpg", 1.0, 8)
define slow_light = Fade(0.5, 1.0, 1.5, color="#fff")
define light = Fade(0.1, 0.5, 1.0, color="#fff")
image danger:
    "#FF0000"
    linear 0.05 alpha 1.0
    linear 0.05 alpha 0.0
    repeat 2
#注释：立绘名称
#al=艾琳
#ale=爱丽儿
#hfl=华芙琳

#init python:
    # 这个for循环的范围根据实际图片总数修改，这里假设总共5张图
    #for i in range(1, 6):
        #renpy.image("bg_image size_i" + str(i), "bg_size/bg" + str(i) + ".png")

# 游戏在此开始。

label start:
    jump ch1_1
    jump ch1_7_2
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    $renpy.show_screen("ch_in","1-1","序章")
    scene bg 1
    show al (1):
        xalign -0.20 yalign 0.0
    show hfl1:
        xalign 0.5 yalign 0.0
    show ale1:
        xalign 14.0 yalign 0.0
    with dissolve
    lloris "yyyyyy"
    $renpy.hide_screen("ch_in")

    show bg 31 with dissolve

    show bg with hpunch

    scene black with dissolve
    hide bg

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。



    # 此处显示各行对话。

    eileen "您已创建一个新的 Ren'Py 游戏。"

    eileen "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
