# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
#更改键位
init:
    $ config.underlay.append(renpy.Keymap(history = ShowMenu("history")))
    $ config.keymap["history"] = [ 'mousedown_4' ]
    $ config.keymap['dismiss'].append('mousedown_5')
    $ config.keymap['rollback']= ['K_PAGEUP']


define lloris = Character("洛里斯")
define e = Character("艾琳")
define ariel = Character("爱丽儿")
define kelly = Character("凯莉谱索")
define warfarin = Character("华芙琳")

define Alika = Character("Alika", image="Alika")
init python:
    # 这个for循环的范围根据实际图片总数修改，这里假设总共5张图
    for i in range(1, 6):
        renpy.image("bg_image size_i" + str(i), "bg_size/bg" + str(i) + ".png")

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "您已创建一个新的 Ren'Py 游戏。"

    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
