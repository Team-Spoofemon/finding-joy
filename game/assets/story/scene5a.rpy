label scene5a:

    play music amb_fireplace loop fadein 0.3 volume 0.2
    show bg_JoyHouse_BedRoom:
        desaturate

    show sprite_JOY_angry with moveinleft

    JOY "I can't stand this."

    show sprite_JOY_angry:
        linear 0.4 xalign 0.8
    JOY "I can't fucking stand this."

    hide sprite_JOY_angry
    show sprite_JOY_sad:
        yalign 1.0 xalign 0.8
    JOY "Why are there people like him in the world?"

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

    hide sprite_JOY_sad
    show sprite_JOY_fear:
        yalign 1.0 xalign 0.8
        flip_face_right_to_left
    JOY "UGH! I fucked up--"

    show sprite_JOY_fear:
        linear 1.0 yalign 1.0 xalign 0.2
    JOY "Tomorrow I'll have to deal with him and everyone will know!"

    hide sprite_JOY_fear
    show sprite_JOY_sad:
        xzoom -1.0
        yalign 1.0 xalign 0.2
        flip_face_left_to_right
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

    hide sprite_JOY_sad
    show sprite_JOY_tired:
        yalign 1.0 xalign 0.2
    JOY "*sigh*"

    show sprite_JOY_tired:
        linear 1.0 yalign 1.0 xalign 0.8
    JOY "I know I did the right thing."

    hide sprite_JOY_tired
    show sprite_JOY_fear:
        yalign 1.0 xalign 0.8
        flip_face_right_to_left
    JOY "I stood up for myself."

    hide sprite_JOY_fear
    show sprite_JOY_sad:
        yalign 1.0 xalign 0.8
        flip_left_instant
        flip_face_left_to_right
    JOY "I said my piece."

    hide sprite_JOY_sad
    show sprite_JOY_neutral:
        yalign 1.0 xalign 0.8
    JOY "And now everyone will know."

    hide sprite_JOY_neutral
    show sprite_JOY_angry:
        yalign 1.0 xalign 0.8
    JOY "Now everyone will know!"

    menu:
        JOY "Now everyone will know! {fast}"  # FEATURE: view prior dialogue

        "And you stayed true to yourself!":
            $ choice = choices['scene5a'] = 'true'
            jump scene5a_last

        "You acted with integrity!":
            $ choice = choices['scene5a'] = 'integrity'
            jump scene5a_last

label scene5a_last:

    JOY "Hell yeah."

    hide sprite_JOY_angry
    show sprite_JOY_happy:
        flip_left_instant
        yalign 1.0 xalign 0.8
        linear 1.0 xalign 0.5
    JOY "Yeah. We're okay, right?"

    menu:
        JOY "Yeah. We're okay, right? {fast}"  # FEATURE: view prior dialogue

        "Yes!":
            call animate_bg_fadetoblack(delay=0.5)
