label scene5a:

    play music amb_fireplace loop fadein 0.3 volume 0.2
    show bg_JoyHouse_BedRoom

    show sprite_JOY_angry with moveinleft:
        align_left_human
        flip_face_left_to_right

    JOY "I can't stand this."

    JOY "I can't fucking stand this."

    show sprite_JOY_angry:
        moveright
    hide sprite_JOY_angry
    show sprite_JOY_sad:
        align_right_human
        flip_face_right_to_left

    JOY "Why are there people like him in the world?"

    #woe
    menu:
        JOY "Why are there people like him in the world? {fast}"  # FEATURE: view prior dialogue

        "You know why.":
            $ choice = choices['scene5a'] = 'why'
            JOY "I know. Nobody has ever told them no before."
            jump scene5a_common

        "Death to men.":
            $ choice = choices['scene5a'] = 'death'
            JOY "Yeah, but that's not a viable biological strategy..."
            jump scene5a_common

        "They're emboldened.":
            $ choice = choices['scene5a'] = 'emboldened'
            JOY "But what can I do about that?"
            jump scene5a_common

    label scene5a_common:

        hide sprite_JOY_angry
        show sprite_JOY_fear with moveinleft

        JOY "UGH! I fucked up--"

        pause 0.5

        JOY "Tomorrow I'll have to deal with him and everyone will know!"

        show sprite_JOY_fear:
            align_left_human
        hide sprite_JOY_fear
        show sprite_JOY_sad:
            align_left_human

        JOY "Oh my god... did I do the right thing?"

        menu:
            JOY "Oh my god... did I do the right thing? {fast}"  # FEATURE: view prior dialogue

            "No.":
                $ choice = choices['scene5a'] = "No."
                JOY "You're just trying to trick me."
                jump scene5a_almostlast

            "Yes.":
                $ choice = choices['scene5a'] = "Yes."
                JOY "Are you sure?"
                jump scene5a_almostlast

    label scene5a_almostlast:

    JOY "*sigh*"

    pause 0.5

    JOY "I know I did the right thing."

    show sprite_JOY_fear:
        moveright
    hide sprite_JOY_fear
    show sprite_JOY_neutral

    JOY "I stood up for myself."

    JOY "I said my piece."

    JOY "And now everyone will know."

    pause 1.0

    hide sprite_JOY_neutral
    show sprite_JOY_angry:
        align_left_human

    JOY "Now everyone will know!"

    menu:
        JOY "Now everyone will know! {fast}"  # FEATURE: view prior dialogue

        "And you stayed true to yourself!":
            $ choice = choices['scene5a'] = 'true'
            jump scene5a_last

        "You acted with integrity!":
            $ choice = choices['scene5a'] = 'integrity'
            hide sprite_JOY_angry
            show sprite_JOY_happy
            jump scene5a_last

label scene5a_last:

    if choice == 'true':
        hide sprite_JOY_angry
        show sprite_JOY_neutral
        JOY "Hell yeah."

        call animate_bg_fadetoblack(delay=0.5)

    elif choice == 'integrity':
        hide sprite_JOY_angry
        show sprite_JOY_happy
        JOY "Yeah. We're okay, right?"

        menu:
            JOY "Yeah. We're okay, right? {fast}"  # FEATURE: view prior dialogue

            "Yes!":
                call animate_bg_fadetoblack(delay=0.5)
