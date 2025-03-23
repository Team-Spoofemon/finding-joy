label start:
    stop music fadeout 1.0  # from the menu

    call scene3

    if choices['scene3'] == 'sid':
        call scene4a
        call scene5a
    elif choices['scene3'] == 'faith':
        call scene4b
        call scene5b
    elif choices['scene3'] == 'work':
        call scene4c
        call scene5c

    return

label debug:
    call debug_animation
    call debug_conversation
    # call actX_dayX_scene_X_style1
    # call actX_dayX_scene_X_style2
    # jump start  -- infinite loop, will never reach return
    return
