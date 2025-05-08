# # scene 2: JOY sees FAITH, solves their pet issue

label scene2:
    play music amb_RelaxedMusicLab_DentistWaitingRoom loop fadein 0.3 volume 0.2  # audio_office
    show bg_PetCheap_ExamRoom

    # *stage:* JOY enters from the right and ends up on the left looking left.
    show sprite_JOY_tired with moveinright:
        align_center_human
        flip_face_right_to_left

    show bg_PetCheap_ExamRoom:
        desaturate
    JOY "Well that was crazy. That was CRAZY."

    # *stage:* JOY turns to WOE
    menu:
        JOY "Well that was crazy. That was CRAZY. {fast}"  # FEATURE: view prior dialogue

        "The next is going to be a phycopath!":
            $ joy_state = 'fear'
            hide sprite_JOY_tired
            show sprite_JOY_fear:
                align_center_human
                flip_left_instant
            JOY "Dear god in heaven, no!"
            jump scene2_common

        "Please no more...":
            $ joy_state = 'happy'
            hide sprite_JOY_tired
            show sprite_JOY_happy:
                align_center_human
                flip_left_instant
            JOY "We can survive, I know it."
            jump scene2_common

        "Why not join the crazy, like the joker?":
            $ joy_state = 'angry'
            hide sprite_JOY_tired
            show sprite_JOY_angry:
                align_center_human
                flip_left_instant
            JOY "Just one bad day away, huh?"
            jump scene2_common


label scene2_common:
    show bg_PetCheap_ExamRoom:
        resaturate

    QUESTION "Please somebody help! My cat!!"

    # *stage:* JOY moves to the left.
    if joy_state == 'fear':
        hide sprite_JOY_fear
    elif joy_state == 'happy':
        hide sprite_JOY_happy
    else:
        hide sprite_JOY_angry

    show sprite_JOY_tired:
        align_center_human
        flip_left_instant
    JOY "Here we go..."

    show sprite_JOY_tired:
        move_align_left_human
        flip_face_left_to_right
    show sprite_FAITH_neutral with moveinright:
        align_right_human
        flip_left_instant

    QUESTION "Oh my god, are you the vet?"

    hide sprite_JOY_tired
    show sprite_JOY_neutral:
        align_left_human
    JOY "Yes I am, how can I help you?"

    # *stage:* FAITH is fear.
    hide sprite_FAITH_neutral
    show sprite_FAITH_fear:
        align_right_human
        flip_left_instant
    FAITH "I'm Faith and this is BISCUITS. There's something inside his chest!"

    # *stage:* BISCUITS comes in from the right to the center. JOY moves from the left to the center.
    show sprite_BISCUITS_fear with moveinright:
        align_right_human
        align_y_06
    hide sprite_JOY_neutral
    show sprite_JOY_sad:
        align_left_human
    JOY "Poor thing..."

    FAITH "What's wrong? Are they going to be okay?"

    hide sprite_JOY_sad
    show sprite_JOY_happy:
        align_left_human
    JOY "Your BISCUITS has a botfly, but they're going to be just fine!"

    # *stage:* JOY is happy.
    hide sprite_FAITH_fear
    show sprite_FAITH_happy:
        align_right_human
        flip_left_instant
    show sprite_BISCUITS_fear:
        move_in_front_of_left(0.4)
        align_y_06
    FAITH "That's a relief... I'm just so worried!"

    # *stage:* JOY is happy.
    JOY "Don't be, that's what I'm here for."

    # *stage*: Joy and Biscuits shake
    hide sprite_JOY_happy
    show sprite_JOY_neutral:
        align_left_human
        bounce
    show sprite_BISCUITS_fear:
        align_x_04
        bounce
    JOY "Botflies happen when..."

    # *stage:* JOY and BISCUITS shake
    show sprite_JOY_neutral:
        bounce
    show sprite_BISCUITS_fear:
        align_x_04
        bounce
    JOY "Cats go outside a lot..."

    hide sprite_FAITH_happy
    show sprite_FAITH_fear:
        align_right_human
        flip_left_instant
    FAITH "Oh no! I promise I'll never let BISCUITS go again!"

    # *stage*: JOY and BISCUITS shake
    show sprite_JOY_neutral:
        bounce(multiply=2)
    show sprite_BISCUITS_fear:
        align_x_04
        bounce(multiply=2)
    JOY "I'm sure you just want your BISCUITS..."

    # *stage:* JOY and BISCUITS shake
    show sprite_JOY_neutral:
        bounce(multiply=4)
    show sprite_BISCUITS_fear:
        align_x_04
        bounce(multiply=4)
    JOY "To be..."

    # *stage:* JOY and BISCUITS shake
    hide sprite_JOY_neutral
    show sprite_JOY_happy:
        align_left_human
        bounce(multiply=8)
    hide sprite_BISCUITS_fear
    show sprite_BISCUITS_happy:
        in_front_of_left
        align_x_04
        align_y_06
        bounce(multiply=8)
    JOY "Happy!"

    JOY "There! We got it! All better now."

    # *stage:* BISCUITS is happy, FAITH approaches center from right and is sad. JOY returns to the left and is neutral.
    show sprite_BISCUITS_happy:
        move_right_of_right(yalign_=0.6)
    hide sprite_FAITH_fear
    show sprite_FAITH_sad:
        flip_left_instant
        align_right_human
    FAITH "BISCUITS I'm so sorry, I'll come outside with you next time!"

    hide sprite_FAITH_sad
    show sprite_FAITH_happy:
        flip_left_instant
        align_right_human
    FAITH "Thank you, Doctor!"

    JOY "I'm just happy to help. Come by anytime."

    # *stage:* FAITH approaches left and is happy.

    FAITH "Thank you so much! Watching you work was insipring!"

    # *stage:* JOY is neutral
    hide sprite_JOY_happy
    show sprite_JOY_neutral:
        align_left_human
    JOY "It's no problem, I--"

    # *stage:* JOY is happy.
    hide sprite_JOY_neutral
    show sprite_JOY_thinking:
        align_left_human
    JOY "Inspring? Really?"

    FAITH "Yep! Do you mind if we use the backyard for a minute?"

    hide sprite_JOY_thinking
    show sprite_JOY_neutral:
        align_left_human
    JOY "Sure thing."

    # *stage:* FAITH turns right.
    show sprite_FAITH_happy:
        flip_face_right_to_left

    FAITH "Come on, BISCUITS! Let's calm down outside for a bit."

    show sprite_BISCUITS_happy:
        bounce
    BISCUITS "Mao."

    show sprite_FAITH_happy:
        flip_face_left_to_right
        exit_right
    show sprite_BISCUITS_happy:
        flip_face_right_to_left
        exit_right
    pause 1.0  # let the animations complete

    # *stage:* JOY turns to WOE
    show bg_PetCheap_ExamRoom:
        desaturate
    hide sprite_JOY_neutral
    show sprite_JOY_thinking:
        align_left_human
    JOY "Wow. Inspiring, huh?"

    menu:
        JOY "Wow. Inspiring, huh? {fast}"  # FEATURE: view prior dialogue

        "I wasn't expecting that!":
            # *stage:* JOY is happy
            hide sprite_JOY_thinking
            show sprite_JOY_happy:
                align_left_human
            JOY "Right? this feels really cool!"

        "Slide into those DM's or else!":
            # UNLOCK ROMANCE OPTION
            $ choices['faith-unlock'] = True
            hide sprite_JOY_thinking
            show sprite_JOY_angry:
                align_left_human
            JOY "Be gone, intrusive thoughts! Horny jail for you!"

    show bg_PetCheap_ExamRoom:
        resaturate
    pause 1.0  # let the animations complete

    call animate_bg_fadetoblack(delay=0.2)
