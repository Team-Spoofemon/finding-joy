screen alpha_magic:
    add Appearing("assets/characters/FAITH/sprite_FAITH_front.png", 100, 200):
        xalign 0.5
        yalign 0.5

label start:
    show screen alpha_magic

    "Can you find the logo?"

    return

label start1:
    stop music fadeout 1.0  # from the menu

    # call debug

    call act1_day3_scene1
    call act1_day3_scene4
    call act1_day3_scene5
    call act1_day3_scene6

    return

label debug:
    call actX_dayX_scene_X_style1
    call actX_dayX_scene_X_style2
    # jump start  -- infinite loop, will never reach return
    return
