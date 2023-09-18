screen ch_in(ch_no,ch_name):
    style_prefix "ch_in"
    zorder 100
    add "gui/chapter_bg.png"

    hbox:
        text "章节" style"ch_in_tiltle"

        vbox:

            text "[ch_no]"
            text "[ch_name]"

style ch_in_label is say_label

style ch_in_tiltle:
    size 55
    xpos 20
    ypos 25
    color "#FFFFFF"

style ch_in_text:
    text_align 0.5
    xpos 98
    ypos 125
    size 19
