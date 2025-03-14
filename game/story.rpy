label start:
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
