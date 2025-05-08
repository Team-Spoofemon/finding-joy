
transform moveright:
    linear 0.6 xpos 0.5


transform exit_right:
    linear 1.0 xpos 1.5


transform exit_left:
    linear 1.0 xpos -0.5


transform align_y_06:
    yalign 0.6


transform align_x_04:
    xalign 0.4


transform align_left_human:
    # xpos 0.1
    xalign 0.1
    yalign 1.0


transform align_center_human:
    # xpos 0.1
    xalign 0.45
    yalign 1.0


transform align_right_human:
    # xpos 0.2
    xalign 0.9
    yalign 1.0


transform move_align_left_human:
    # xpos 0.1
    linear 0.4 xalign 0.1
    yalign 1.0


transform move_align_center_human:
    # xpos 0.1
    linear 0.4 xalign 0.45
    yalign 1.0


transform move_align_right_human:
    # xpos 0.2
    linear 0.4 xalign 0.9
    yalign 1.0


transform in_front_of_left:
    # xpos 0.2
    xalign 0.3
    yalign 1.0


transform move_in_front_of_left(xalign_=0.3):
    # xpos 0.2
    linear 1.0 xalign xalign_
    yalign 1.0


transform right_of_right:
    # xpos 0.2
    xalign 0.8
    yalign 1.0


transform move_right_of_right(xalign_=0.8, yalign_=1.0):
    # xpos 0.2
    linear 1.0 xalign xalign_
    yalign yalign_


transform flip_left:
    xzoom -1.0 yzoom 1.0


transform flip_right:
    xzoom 1.0 yzoom 1.0


transform bounce(multiply=1):
    # https://lemmasoft.renai.us/forums/viewtopic.php?p=477118&sid=4edc0c5c93d5e757116c9a1b6009e7cf#p477118
    easein  .05 yoffset -10 * multiply
    easeout .05 yoffset 0 * multiply
    easein  .05 yoffset -4 * multiply
    easeout .05 yoffset 0 * multiply
    yoffset 0


transform flip_left_instant:
    # https://www.renpy.org/doc/html/transforms.html#warpers
    # https://easings.net/
    xzoom -1.0 yzoom 1.0


transform flip_right_instant:
    # https://www.renpy.org/doc/html/transforms.html#warpers
    # https://easings.net/
    xzoom 1.0 yzoom 1.0


transform flip_face_right_to_left:
    # https://www.renpy.org/doc/html/transforms.html#warpers
    # https://easings.net/
    easein_quint 0.5 xzoom -1.0 yzoom 1.0


transform flip_face_left_to_right:
    easein_quint 0.5 xzoom 1.0 yzoom 1.0


transform desaturate:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    linear 0.6 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
    linear 0.6 blur 10


transform resaturate:
    linear 0.6 blur 0
    linear 0.6 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)


label animate_bg_fadetoblack(delay=0.5):  # from anywhere
    stop music fadeout delay
    stop audio fadeout delay
    stop sound fadeout delay
    scene black with fade
    $ renpy.pause (delay, hard=True)


label animate_bg_fadeinblack(delay=0.2):
    stop music fadeout delay
    stop audio fadeout delay
    stop sound fadeout delay
    scene black with fade
    # $ renpy.pause (delay, hard=True)
