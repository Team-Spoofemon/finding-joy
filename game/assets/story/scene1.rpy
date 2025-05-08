# scene 1: JOY arrives at reception, runs into KELLY, solves their pet issue

label scene1:
    play music amb_office loop fadein 0.3
    show bg_PetCheap_FrontDesk

    # *stage:* JOY enters from the right happily and is ready to start the day.
    show sprite_JOY_happy with moveinleft:
        align_left_human
        flip_face_right_to_left

    JOY "Alright, JOY! New day, new chance, you'll do great!"

    show bg_PetCheap_FrontDesk:
        desaturate
    JOY "Right? We've got this!"

    # *stage:* JOY turns to WOE
    $ washappy = False
    menu:
        JOY "Right? We've got this! {fast}"  # FEATURE: view prior dialogue

        "Sure we do!":
            JOY "That's right, JOY! That's the spirit!"
            $ washappy = True
            # JOY stays happy

        "But I don't know whats going on...":
            hide sprite_JOY_happy
            show sprite_JOY_neutral:
                align_left_human
                flip_left
            JOY "We know enough. Let's do this."

        "We'll play it slow?":
            hide sprite_JOY_happy
            show sprite_JOY_neutral:
                align_left_human
                flip_left
            JOY "You're right. Gotta pace myself."

    # *stage:* JOY moves to the left.
    show bg_PetCheap_FrontDesk:
        resaturate

    QUESTION "Yeah, yeah, yeah, I'll be right there!"

    if washappy:
        show sprite_JOY_neutral:
            align_left_human
            flip_left
    hide sprite_JOY_happy
    JOY "Looks like we've got the first client already?"

    show sprite_JOY_neutral:
        flip_face_left_to_right

    # *stage:* KELLY and BUTTER enter from the right
    show sprite_KELLY_angry with moveinright:
        align_right_human

    QUESTION "Fix what you broke, you hear me?"

    hide sprite_JOY_neutral
    show sprite_JOY_sad:
        align_left_human
    JOY "Uh, yes. I will? Who might you be?"

    # *stage:* KELLY turns to the right. KELLY is angry.
    show sprite_KELLY_angry:
        flip_face_right_to_left
    KELLY "My name's KELLY, damnit! Just fix it!"

    hide sprite_JOY_sad
    show sprite_JOY_thinking:
        align_left_human
    JOY "Fix... what exactly?"

    # *stage:* KELLY turns to the left. KELLY is happy.
    hide sprite_KELLY_angry
    show sprite_KELLY_happy:
        align_right_human
        flip_left
    show sprite_KELLY_happy:
        align_right_human
        flip_face_left_to_right

    KELLY "I wasn't talking to you! Can you fix my precious BUTTER?"

    show sprite_BUTTER_fear with moveinright:
        align_right_human
    hide sprite_JOY_thinking
    show sprite_JOY_fear:
        align_left_human

    # *stage:* KELLY turns to the right. KELLY is angry.
    hide sprite_KELLY_happy
    show sprite_KELLY_angry:
        align_right_human
        flip_face_right_to_left
    KELLY "And you! Fix what you broke!"

    # *stage:* JOY is fear

    JOY "What the hell?"

    # *stage:* JOY turns to WOE
    show sprite_BUTTER_fear:
        desaturate
    show sprite_KELLY_angry:
        desaturate
    show bg_PetCheap_FrontDesk:
        desaturate

    JOY "I should so something, right?"

    menu:
        JOY "I should so something, right? {fast}"  # FEATURE: view prior dialogue

        # WOE
        # a) This person is N-U-T-S!
        "This person is N-U-T-S!":
            JOY "Big scary lady is NUTS, amen!"

        # b) In and out. Lets go, quick...
        "In and out. Lets go, quick...":
            JOY "You're right--lets not poke the big scary lady!"

    # *stage:* JOY moves to the center, BUTTER moves to the center, KELLY turns to the left, KELLY is angry, JOY is happy
    show sprite_BUTTER_fear:
        resaturate
    show sprite_KELLY_angry:
        resaturate
    show bg_PetCheap_FrontDesk:
        resaturate
    hide sprite_JOY_fear
    show sprite_JOY_surprised:
        align_left_human
    pause 0.6

    JOY "Hi there, BUTTER! Aww, there's a splinter in your paw."

    show sprite_BUTTER_fear:
        move_in_front_of_left
        resaturate
    pause 0.6

    hide sprite_JOY_surprised
    show sprite_JOY_happy:
        align_left_human
    JOY "I'll pull out that owie and make things better."

    hide sprite_JOY_happy
    show sprite_JOY_fear:
        align_left_human
    show sprite_KELLY_angry:
        bounce
    KELLY "There's something wrong with your head, isn't there?!"

    # *stage:* JOY and BUTTER shake
    hide sprite_JOY_fear
    show sprite_JOY_neutral:
        align_left_human
        bounce
    show sprite_BUTTER_fear:
        bounce
    pause 0.2

    JOY "Ok just ignore and focus!"

    hide sprite_JOY_neutral
    show sprite_JOY_fear:
        align_left_human
    show sprite_KELLY_angry:
        bounce(multiply=2)
    KELLY "Well it's not my problem!"

    # *stage:* JOY and BUTTER shake
    hide sprite_JOY_fear
    show sprite_JOY_neutral:
        align_left_human
    show sprite_JOY_neutral:
        align_left_human
        bounce(multiply=2)
    show sprite_BUTTER_fear:
        bounce(multiply=2)
    pause 0.2
    JOY "Just a bit more..."

    hide sprite_JOY_neutral
    show sprite_JOY_fear:
        align_left_human
    show sprite_KELLY_angry:
        bounce(multiply=4)
    KELLY "How long is this going to take?"

    hide sprite_JOY_neutral
    show sprite_JOY_happy:
        align_left_human
        bounce(multiply=4)
    show sprite_BUTTER_fear:
        bounce(multiply=4)
    JOY "Got it! We're all set to go!"

    # *stage:* BUTTER is happy
    hide sprite_BUTTER_fear
    show sprite_BUTTER_happy:
        in_front_of_left
        bounce
    BUTTER "Bark! Bark!"

    # *stage:* KELLY is still turned to the right.

    hide sprite_KELLY_angry
    show sprite_KELLY_happy:
        align_right_human
        flip_left
    show sprite_KELLY_happy:
        align_right_human
        flip_face_left_to_right
    KELLY "Oh you fixed it? Finally?"

    JOY "Yes, we did!"

    # *stage:* KELLY turns to the left.

    hide sprite_JOY_happy
    show sprite_JOY_fear:
        align_left_human
    hide sprite_KELLY_happy
    show sprite_KELLY_angry:
        align_right_human
        flip_face_right_to_left
    KELLY "Not you, you stupid--oh!"

    show sprite_BUTTER_happy:
        flip_face_right_to_left
    hide sprite_KELLY_angry
    show sprite_KELLY_happy:
        align_right_human
        flip_left
    show sprite_KELLY_happy:
        align_right_human
        flip_face_left_to_right
    KELLY "BUTTER, you're all fixed!"

    show sprite_BUTTER_happy:
        flip_face_left_to_right
    hide sprite_JOY_fear
    show sprite_JOY_tired:
        align_left_human
    JOY "Yes. That's what I've been trying to say."

    show sprite_BUTTER_happy:
        flip_face_right_to_left
    KELLY "Bravo, five stars! Let's go sweetie and--"

    # *stage:* KELLY turns to the right
    hide sprite_JOY_tired
    show sprite_JOY_thinking:
        align_left_human
    hide sprite_KELLY_happy
    show sprite_KELLY_angry:
        align_right_human
        flip_face_right_to_left
    KELLY "If I come back and its not fixed, you'll be sorry!"

    # *stage:* KELLY and BUTTER exit right
    show sprite_KELLY_angry:
        exit_right
    show sprite_BUTTER_happy:
        exit_right

    pause 1.0  # let the animations complete

    hide sprite_JOY_thinking
    show sprite_JOY_tired:
        align_left_human
    JOY "God, what a way to start to the day..."

    # *stage:* JOY walks from the center to the left
    show sprite_JOY_tired:
        flip_face_right_to_left
        exit_left

    # SCENE END.
    pause 1.0  # let the animations complete

    call animate_bg_fadetoblack(delay=0.2)
