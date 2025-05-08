label scene5c:

    play music amb_fireplace loop fadein 0.3 volume 0.2
    show bg_JoyHouse_BedRoom:
        desaturate

    show sprite_JOY_neutral with moveinleft

    JOY "What a long day..."

    show sprite_JOY_neutral:
        linear 0.4 xalign 0.8
    JOY "It's one crazy client after another out here!"

    hide sprite_JOY_neutral
    show sprite_JOY_sad:
        yalign 1.0 xalign 0.8
    JOY "The clients are crazy right? Or am I the crazy one?"

    menu:
        JOY "The clients are crazy right? Or am I the crazy one? {fast}"  # FEATURE: view prior dialogue

        "You're the crazy one.":
            $ choice = 'crazy'
            JOY "Yeah, uhuh. Verry funny, me."
            jump scene5c_next

        "No, no, no-- they're crazy.":
            $ choice = 'them'
            JOY "Right? Like, hello?"
            jump scene5c_next

        "We're all going crazy.":
            $ choice = 'all'
            JOY "Sure, sure-- and I'm Alice in Wonderland out here."
            jump scene5c_next

label scene5c_next:

    hide sprite_JOY_sad
    show sprite_JOY_fear:
        yalign 1.0 xalign 0.8
        flip_face_right_to_left
    JOY "UGH! I shouldn't have snapped like that!"

    show sprite_JOY_fear:
        linear 1.0 yalign 1.0 xalign 0.2
    JOY "I yelled at a client and I'm supposed to be a professional..."

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
            jump scene5c_next2

        "Yes.":
            $ choice = 'yes'
            JOY "Are you sure?"
            jump scene5c_next2

label scene5c_next2:

    hide sprite_JOY_sad
    show sprite_JOY_tired:
        yalign 1.0 xalign 0.2
    JOY "*sigh*"

    show sprite_JOY_tired:
        linear 1.0 yalign 1.0 xalign 0.8
    JOY "Well... at least we got that toy out of GRAVY's throat alright."

    hide sprite_JOY_tired
    show sprite_JOY_neutral:
        yalign 1.0 xalign 0.8
        flip_face_right_to_left
    JOY "I'll just try harder next time."

    hide sprite_JOY_neutral
    show sprite_JOY_angry:
        yalign 1.0 xalign 0.8
        flip_left_instant
        flip_face_left_to_right
    JOY "Even if the people who own the pets are crazy..."

    hide sprite_JOY_angry
    show sprite_JOY_happy:
        yalign 1.0 xalign 0.8
    JOY "I still love animals."

    hide sprite_JOY_happy
    show sprite_JOY_angry:
        yalign 1.0 xalign 0.8
    JOY "I will keep it up even if work itself sucks!"

    menu:
        JOY "I will keep it up even if work itself sucks! {fast}"  # FEATURE: view prior dialogue

        "Damn straight.":
            $ choice = 'straight'
            jump scene5c_next3

label scene5c_next3:

    show sprite_JOY_angry:
        flip_face_right_to_left
    JOY "Even if every pet owner is a psycho!"

    menu:
        JOY "Even if every pet owner is a psycho! {fast}"  # FEATURE: view prior dialogue

        "Because this is how we can contribute!":
            $ choice = 'contribute'
            jump scene5c_last

label scene5c_last:

    hide sprite_JOY_angry
    show sprite_JOY_happy:
        flip_left_instant
        yalign 1.0 xalign 0.8
        linear 1.0 xalign 0.5
    JOY "Yeah. Let's save the animals!"

    menu:
        JOY "Yeah. Let's save the animals! {fast}"  # FEATURE: view prior dialogue

        "Yes!":
            call animate_bg_fadetoblack(delay=0.5)
