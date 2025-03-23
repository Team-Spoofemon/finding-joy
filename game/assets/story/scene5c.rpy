label scene5c:

    play music bgm_fireplace loop fadein 0.3
    show bg_JoyHouse_BedRoom

    show sprite_JOY_neutral with moveinleft

    JOY "What a long day..."

    JOY "It's one crazy client after another out here!"

    show sprite_JOY_neutral:
        moveright

    show sprite_JOY_sad at align_right_human

    pause 0.5

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
            JOY "Sure, sure-- and I'm alice in Wonderland out here."
            jump scene5c_next

label scene5c_next:

    show sprite_JOY_fear at align_right_human

    JOY "UGH! I shouldn't have snapped like that!"

    JOY "I yelled at a client and I'm supposed to be a professional..."

    show sprite_JOY_fear with moveinleft

    show sprite_JOY_sad at align_left_human

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

    JOY "*sigh*"

    JOY "Well... at least we got that toy out of GRAVY's throat alright."

    show sprite_JOY_sad:
        moveright

    show sprite_JOY_neutral at align_right_human

    JOY "I'll just try harder next time."

    JOY "Even if the people who own the pets are crazy..."

    JOY "I still love animals."

    show sprite_JOY_angry at align_right_human

    JOY "I will keep it up even if work itself sucks!"

    menu:
        JOY "I will keep it up even if work itself sucks! {fast}"  # FEATURE: view prior dialogue

        "Damn straight.":
            $ choice = 'straight'
            jump scene5c_next3

label scene5c_next3:

    show sprite_JOY_neutral:
        linear 0.6 xalign 0.5

    JOY "Even if every pet owner is a psycho owner!"

    menu:
        JOY "Even if every pet owner is a psycho owner! {fast}"  # FEATURE: view prior dialogue

        "Because this is how we can contribute!":
            $ choice = 'contribute'
            jump scene5c_last

label scene5c_last:

    show sprite_JOY_happy at center

    JOY "Yeah. Let's save the animals!"

    menu:
        JOY "Yeah. Let's save the animals! {fast}"  # FEATURE: view prior dialogue

        "Yes!":
            $ choice = 'yes'
            call animate_bg_fadetoblack(delay=0.5)
