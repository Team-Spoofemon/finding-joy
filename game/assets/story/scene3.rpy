# scene 3: JOY enters break room, SID suggests JOY should go out on a date, choses between asking SID, FAITH, or refusing

label scene3:

    show bg_PetCheap_FrontDesk

    # *stage:* JOY enters from the right and ends up on the left looking left.
    show sprite_JOY_neutral with moveinright:
        align_left_human
        flip_face_right_to_left

    JOY "I am exhausted! Colorful characters everywhere!"

    QUESTION "Did someone say character?"

    JOY "Oh, here we go. It's the tech..."

    # *stage:* JOY turns to the right. SID enters from the right.
    show sprite_JOY_neutral:
        flip_face_left_to_right
    show sprite_SID_neutral with moveinright:
        align_right_human
        flip_face_right_to_left

    SID "If you're looking for character, look no further!"

    JOY "Very funny."

    SID "Hey, your words!"

    # *stage:* JOY turns to the left.
    show sprite_JOY_neutral:
        flip_face_right_to_left

    SID "There's this great coffee place next door! Let's check it out!"

    JOY "..."

    SID "Well?"

    # *stage:* JOY is fear.
    show sprite_JOY_neutral:
        flip_face_left_to_right
    pause 0.5
    hide sprite_JOY_neutral
    show sprite_JOY_fear:
        align_left_human

    JOY "Are you... asking me out?"

    SID "Now you get the idea! Whaddya say?"

    hide sprite_JOY_fear
    show sprite_JOY_neutral:
        align_left_human
        flip_face_right_to_left

    JOY "We're coworkers! Why would you ask me out?"

    SID "PetCheap doesnt have a fraternization policy!"

    # *stage:* JOY is neutral.
    show sprite_JOY_neutral:
        flip_face_left_to_right

    JOY "You're kidding."

    SID "Yup! Coworkers and clients are even on the table! Whaddya say?"

    # *stage:* JOY turns to WOE.
    show sprite_SID_neutral:
        desaturate
    show bg_PetCheap_FrontDesk:
        desaturate

    hide sprite_JOY_neutral
    show sprite_JOY_fear:
        align_left_human

    JOY "Bad idea, right? Dating this guy is a terrible idea, right?"

    # WOE
    menu:
        JOY "Bad idea, right? Dating this guy is a terrible idea, right? {fast}"  # FEATURE: view prior dialogue

        "He's cute! And free coffee!":
            $ choice = choices['scene3'] = 'sid'
            JOY "Ok, fine. What's the literal worst that can happen?"
            jump scene3_common

        "NO SHOT! I've got work to do!":
            $ choice = choices['scene3'] = 'work'
            JOY "Horny jail for me. Seems cruel, but necessary."
            jump scene3_common

        "Wait... then Faith is an option!":
            # IF UNLOCK ROMANCE OPTION 4B
            #     c) Wait, wait, wait... CLIENTS are on the table!
            $ choice = choices['scene3'] = 'faith'
            JOY "You're insane, you know that? But why not!"
            jump scene3_common


label scene3_common:
    show sprite_SID_neutral:
        resaturate
    show bg_PetCheap_FrontDesk:
        resaturate

    pause 0.6
    hide sprite_JOY_fear

    if choice == 'sid':
        # *stage:* JOY is neutral.
        show sprite_JOY_neutral:
            align_left_human

        JOY "Looks like we're getting coffee."

        SID "Sounds like a plan!"

        # *stage:* JOY and SID exit right together.
        show sprite_SID_neutral:
            flip_face_left_to_right

        show sprite_SID_neutral:
            exit_right
        show sprite_JOY_neutral:
            exit_right

        pause 1.0 # let the animations complete

    elif choice == 'work':
        # *stage:* JOY is angry.
        show sprite_JOY_angry:
            align_left_human

        JOY "The next client is coming. I've gotta go."

        # *stage:* JOY exits right. SID is sad and faces right.
        show sprite_JOY_angry:
            exit_right

        pause 1.0  # let the animations complete

        show sprite_SID_neutral:
            flip_face_right_to_left

        SID "What the hell just happened?"

        show sprite_SID_neutral:
            flip_face_left_to_right

        SID "Thanks, Obama!"

        # *stage:* SID faces left, pauses, faces right, and exists.
        show sprite_SID_neutral:
            exit_right

    elif choice == 'faith':
        # *stage:* JOY is happy.
        show sprite_JOY_happy:
            align_left_human

        JOY "You know, I just remembered I need to powder my nose."

        # *stage:* JOY exits right. SID is sad and faces right.
        show sprite_JOY_happy:
            exit_right

        pause 1.0  # let the animations complete

        show sprite_SID_neutral:
            flip_face_left_to_right

        SID "Rain check! I get it! Next week for sure!"

        # *stage:* SID faces left, pauses, faces right, and exists.
        show sprite_SID_neutral:
            exit_right

    pause 1.0  # let the animations complete

    call animate_bg_fadetoblack(delay=0.2)
