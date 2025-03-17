label start:
    stop music fadeout 1.0  # from the menu

    jump scene3


    return

label debug:
    call debug_animation
    call debug_conversation
    # call actX_dayX_scene_X_style1
    # call actX_dayX_scene_X_style2
    # jump start  -- infinite loop, will never reach return
    return
