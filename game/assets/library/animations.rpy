
transform moveright:
    linear 0.6 xpos 0.5


transform exit_right:
    linear 1.0 xpos 1.5


transform exit_left:
    linear 1.0 xpos -0.5

transform align_left_human:
    # xpos 0.1
    xalign 0.1
    yalign 1.0


transform align_right_human:
    # xpos 0.2
    xalign 0.9
    yalign 1.0


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


label animate_bg_fadetoblack(delay=0.5):
    stop music fadeout delay  # from anywhere
    scene black with fade
    $ renpy.pause (delay, hard=True)


label animate_bg_fadeinblack(delay=0.2):
    stop music fadeout delay  # from anywhere
    scene black with fade
    # $ renpy.pause (delay, hard=True)
