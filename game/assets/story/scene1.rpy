# scene 1: JOY arrives at reception, runs into KELLY, solves their pet issue

label scene1:
    play music amb_office loop fadein 0.3
    show bg_PetCheap_FrontDesk

    # *stage:* JOY enters from the right happily and is ready to start the day.
    show sprite_JOY_happy with moveinleft:
        align_left_human
        flip_face_right_to_left

    JOY "Alright, JOY! New day, new chance, you'll do great!"

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

    if washappy:
        show sprite_JOY_neutral:
            align_left_human
            flip_left
    hide sprite_JOY_happy

    # *stage:* JOY moves to the left.

    QUESTION "Yeah, yeah, yeah, I'll be right there!"

    JOY "Looks like we've got the first client already?"

    show sprite_JOY_neutral:
        flip_face_left_to_right

    # *stage:* KELLY and BUTTER enter from the right
    show sprite_KELLY_angry with moveinright:
        align_right_human

    QUESTION "Fix what you broke, you hear me?"

    JOY "Uh, yes. I will. What seems to be the problem?"

    # *stage:* KELLY turns to the right. KELLY is angry.
    show sprite_KELLY_angry:
        flip_face_right_to_left
    KELLY "My name's KELLY, damnit! Just fix it!"

    hide sprite_JOY_neutral
    show sprite_JOY_thinking:
        align_left_human
    JOY "Fix... what exactly?"

    # *stage:* KELLY turns to the left. KELLY is happy.
    hide sprite_KELLY_angry
    show sprite_KELLY_happy:
        flip_right
        align_right_human
        flip_face_left_to_right

    KELLY "I wasn't talking to you! Fix my BUTTER please?"

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

    # JOY
    # Hi there, BUTTER! What seems to be the problem?

    # JOY
    # Ah there's a splinter in your paw.

    # KELLY
    # There's something wrong with your head, isn't there?!

    # *stage:* JOY and BUTTER shake

    # JOY
    # Almost...

    # *stage:* JOY and BUTTER shake

    # KELLY
    # Well it's not my problem!

    # JOY
    # Just a bit more...

    # *stage:* JOY and BUTTER shake

    # JOY
    # Got it! We're all set to go--?

    # *stage:* BUTTER is happy

    # BUTTER
    # Bark! Bark!

    # *stage:* KELLY is still turned to the right.

    # KELLY
    # Oh you fixed it? Finally?

    # JOY
    # Yes, we did.

    # *stage:* KELLY turns to the left.

    # KELLY
    # Not you, you stupid--oh! BUTTER, you're all fixed!

    # JOY
    # Yes. That's what I've been trying to say.

    # KELLY
    # Bravo, five stars! Let's go sweetie and--

    # *stage:* KELLY turns to the right

    # KELLY
    # If I come back and its not fixed, you'll be sorry!

    # *stage:* KELLY and BUTTER exit right

    # JOY
    # Goodness... what a start to the day.

    # *stage:* JOY walks from the center to the left

    # SCENE END.


    pause 1.0  # let the animations complete

    call animate_bg_fadetoblack(delay=0.2)
