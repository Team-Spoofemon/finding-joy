label scene5b:

    play music amb_fireplace loop fadein 0.3 volume 0.2
    show bg_JoyHouse_BedRoom:
        desaturate

    show sprite_JOY_happy with moveinleft

    JOY "Wow, I had a really good time..."

    show sprite_JOY_happy:
        linear 0.4 xalign 0.8
    JOY "Kinda crazy I'm even allowed a good time these days."

    hide sprite_JOY_neutral
    show sprite_JOY_happy:
        yalign 1.0 xalign 0.8
    JOY "Do I deserve this? Do I deserve even a little happiness?"

    menu:
        JOY "Do I deserve this? Do I deserve even a little happiness? {fast}"  # FEATURE: view prior dialogue

        "It's too good to be true.":
            $ choice = 'true'
            JOY "Maybe, but I do want to believe it is true."
            jump scene5b_next

        "Why not? You've worked hard!":
            $ choice = 'worked'
            JOY "I want to believe that."
            jump scene5b_next

        "Happiness is a fickle thing.":
            $ choice = 'fickle'
            JOY "I'd like to believe I can find happiness though."
            jump scene5b_next

label scene5b_next:

    hide sprite_JOY_happy
    show sprite_JOY_fear:
        yalign 1.0 xalign 0.8
        flip_face_right_to_left
    JOY "UGH! I feel like I blew it!"

    show sprite_JOY_fear:
        linear 1.0 yalign 1.0 xalign 0.2
    JOY "I said too much and told FAITH I've got these doubts..."

    hide sprite_JOY_fear
    show sprite_JOY_sad:
        xzoom -1.0
        yalign 1.0 xalign 0.2
        flip_face_left_to_right
    JOY "Did I mess up?"

    menu:
        JOY "Did I mess up? {fast}"  # FEATURE: view prior dialogue

        "No.":
            $ choice = 'no'
            JOY "You're just trying to trick me."
            jump scene5b_next2

        "Yes.":
            $ choice = 'yes'
            JOY "Are you sure?"
            jump scene5b_next2

label scene5b_next2:

    hide sprite_JOY_sad
    show sprite_JOY_tired:
        yalign 1.0 xalign 0.2
    JOY "*sigh*"

    show sprite_JOY_tired:
        linear 1.0 yalign 1.0 xalign 0.8
    JOY "But FAITH was right, regardless of how coffee went."

    hide sprite_JOY_tired
    show sprite_JOY_neutral:
        yalign 1.0 xalign 0.8
        flip_face_right_to_left
    JOY "Even if I have self-doubts..."

    hide sprite_JOY_neutral
    show sprite_JOY_angry:
        yalign 1.0 xalign 0.8
        flip_left_instant
        flip_face_left_to_right
    JOY "I am passionate."

    hide sprite_JOY_angry
    show sprite_JOY_happy:
        yalign 1.0 xalign 0.8
    JOY "I love animals."

    hide sprite_JOY_happy
    show sprite_JOY_angry:
        yalign 1.0 xalign 0.8
    JOY "I will keep it up even if work itself sucks!"

    menu:
        JOY "I will keep it up even if work itself sucks! {fast}"  # FEATURE: view prior dialogue

        "Damn straight.":
            $ choice = 'straight'
            jump scene5b_next3

label scene5b_next3:

    hide sprite_JOY_angry
    show sprite_JOY_neutral:
        yalign 1.0 xalign 0.8
        flip_face_right_to_left
    JOY "Even if the world is ending around us!"

    menu:
        JOY "Even if the world is ending around us! {fast}"  # FEATURE: view prior dialogue

        "Because this is how we can contribute!":
            $ choice = 'contribute'
            jump scene5b_last

label scene5b_last:

    hide sprite_JOY_neutral
    show sprite_JOY_happy:
        flip_left_instant
        yalign 1.0 xalign 0.8
        linear 1.0 xalign 0.5
    JOY "Yeah. This is how I will fix the world."

    menu:
        JOY "Yeah. This is how I will fix the world. {fast}"  # FEATURE: view prior dialogue

        "Yes!":
            call animate_bg_fadetoblack(delay=0.5)
