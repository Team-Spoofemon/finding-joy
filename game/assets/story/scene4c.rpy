# scene 4c: JOY enters the operating table, sees DOPEY, solves their pet issue

label scene4c:
    play music amb_RelaxedMusicLab_DentistWaitingRoom loop fadein 0.3 volume 0.2  # audio_office
    show bg_PetCheap_ExamRoom

    # *stage*: JOY and enter from the right
    show sprite_JOY_tired with moveinright:
        align_center_human
        flip_face_right_to_left

    JOY "Good thing I turned SID down, right?"

    # *stage*: JOY turns to WOE
    show bg_PetCheap_ExamRoom:
        desaturate
    JOY "I'm not really into dating clients or coworkers, right?"

    menu:
        JOY "I'm not really into dating clients or coworkers, right? {fast}"  # FEATURE: view prior dialogue

        "Or clients, for that matter!":
            # *stage:* JOY is happy
            $ joy_state = 'happy'
            hide sprite_JOY_tired
            show sprite_JOY_happy:
                align_center_human
                flip_left_instant
            JOY "FAITH was charming, but I do like keeping work and play seperate."
            jump scene4c_common

        "The right person will come along!":
            # *stage:* JOY is sad
            $ joy_state = 'sad'
            hide sprite_JOY_tired
            show sprite_JOY_sad:
                align_center_human
                flip_left_instant
            JOY "We've been telling ourselves that for years, Joy..."
            jump scene4c_common

        "We all die alone, you see...":
            # *stage:* JOY is angry
            $ joy_state = 'angry'
            hide sprite_JOY_tired
            show sprite_JOY_angry:
                align_center_human
                flip_left_instant
            JOY "Okay, I am really in some kind of state! Bad intrusive thoughts!"
            jump scene4c_common

label scene4c_common:
    show bg_PetCheap_ExamRoom:
        resaturate

    QUESTION "Hey uh... is this where i'm supposed to go for pets?"

    if joy_state == 'happy':
        hide sprite_JOY_happy
    elif joy_state == 'sad':
        hide sprite_JOY_sad
    else:
        hide sprite_JOY_angry

    show sprite_JOY_tired:
        align_center_human
        flip_left_instant
    JOY "Here we go..."

    # *stage:* JOY moves to the left.
    # *stage:* DOPEY comes in from the right.
    show sprite_JOY_tired:
        move_align_left_human
        flip_face_left_to_right
    show sprite_DOPEY_neutral with moveinright:
        align_right_human
        flip_face_left_to_right

    QUESTION "Uh, hello? I think my dog is like, and not okay and stuff?"

    hide sprite_JOY_tired
    show sprite_JOY_neutral:
        align_left_human
    JOY "Yes, come on in. What's your name sir?"

    DOPEY "Oh uh, my name is DOPEY. What's up?"

    hide sprite_JOY_neutral
    show sprite_JOY_thinking:
        align_left_human
    JOY "Whats...up? What's up is, you said your dog isn't feeling well?"

    DOPEY "I mean I'm not super sure. It's really hard to tell."

    JOY "What do you mean its hard to tell--"

    # *stage:* GRAVY comes lumbering in
    show sprite_GRAVY_fear with moveinright:
        align_right_human
        xalign 0.8
    # *stage:* JOY is fear
    hide sprite_JOY_thinking
    show sprite_JOY_fear:
        align_left_human
    JOY "OH MY GOD!"

    show sprite_GRAVY_fear:
        bounce
    GRAVY "Woof."

    JOY "What do you mean its hard to tell?! There's something stuck in your dog's throat!"

    DOPEY "Oh yeah. I mean... this happens a lot actually."

    # *stage:* JOY is angry
    hide sprite_JOY_fear
    show sprite_JOY_angry:
        align_left_human

    JOY "I'm sorry, come again?"

    DOPEY "Yeah, GRAVY's eaten a bunch of stuff..."

    show sprite_GRAVY_fear:
        bounce
    GRAVY "Woof."

    # *stage:* JOY is fear
    hide sprite_JOY_angry
    show sprite_JOY_fear:
        align_left_human
    DOPEY "Nickles, Magic the gathering cards, a bunch of rubber bands this oen time..."

    show sprite_GRAVY_fear:
        bounce
    GRAVY "Woof."

    # *stage:* JOY is sad
    hide sprite_JOY_fear
    show sprite_JOY_sad:
        align_left_human

    DOPEY "My dad's car keys, one of those spinny top things, a few spoons..."

    show sprite_GRAVY_fear:
        bounce
    GRAVY "Woof."

    # *stage:* JOY is thinking
    hide sprite_JOY_sad
    show sprite_JOY_thinking:
        align_left_human

    DOPEY "My favorite belt, a stress ball, and even my homework another time but nobody believed me..."

    show sprite_GRAVY_fear:
        bounce
    GRAVY "Woof."

    # *stage:* JOY is happy
    hide sprite_JOY_thinking
    show sprite_JOY_happy:
        align_left_human

    JOY "Hah hah! Okay, okay! I think I get the picture."

    # *stage:* GRAVY comes in from the right to the center. JOY moves from the left to the center.
    show sprite_GRAVY_fear:
        move_in_front_of_left(0.3)

    DOPEY "Yeah but GRAVY never seems bothered by it, so I don't know."

    JOY "Let's just... see if we can unstuck what's in GRAVY's throat, alright?"

    # *stage*: Joy and GRAVY shake
    hide sprite_JOY_happy
    show sprite_JOY_neutral:
        align_left_human
        bounce
    show sprite_GRAVY_fear:
        bounce

    DOPEY "Um, okay."

    # *stage*: JOY and GRAVY shake
    show sprite_JOY_neutral:
        bounce(multiply=2)
    show sprite_GRAVY_fear:
        bounce(multiply=2)
    DOPEY "I guess so."

    # *stage*: Joy and GRAVY shake
    show sprite_JOY_neutral:
        bounce(multiply=2)
    show sprite_GRAVY_fear:
        bounce(multiply=2)
    DOPEY "Am I in trouble?"

    # *stage*: JOY and GRAVY shake
    # *stage:* GRAVY is happy. JOY returns to the left and is neutral.
    hide sprite_JOY_neutral
    show sprite_JOY_happy:
        align_left_human
        bounce(multiply=2)
    hide sprite_GRAVY_fear
    show sprite_GRAVY_happy:
        align_right_human
        align_x_03
        bounce(multiply=2)
    JOY "Almost... Yes! Got it!"

    DOPEY "So I am? I am in trouble?"

    # *stage:* JOY is surprise
    hide sprite_JOY_happy
    show sprite_JOY_tired:
        align_left_human

    JOY "Huh? What? What do you mean you're in trouble? Where do you think you are?"

    DOPEY "Um, like, the principle's office but for pets?"

    hide sprite_JOY_surprised
    show sprite_JOY_tired:
        align_left_human
    JOY "You know what? No. You're not in trouble. Come back anytime. GRAVY too."

    DOPEY "Okay I guess."

    # *stage:* DOPEY turns to the right.
    show sprite_GRAVY_happy:
        flip_face_left_to_right

    DOPEY "Come on, GRAVY."

    # *stage:* DOPEY and GRAVY exit right.
    show sprite_GRAVY_happy:
        exit_right
    show sprite_DOPEY_neutral:
        exit_right

    pause 1.0  # let the animations complete

    JOY "That was..."

    # *stage*: JOY turns to WOE
    show bg_PetCheap_ExamRoom:
        desaturate

    JOY "What was that?"

    menu:
        JOY "What was that? {fast}"  # FEATURE: view prior dialogue

        "The dumbest pair of animals in the kingdom.":
            $ joy_state = 'thinking'
            hide sprite_JOY_tired
            show sprite_JOY_thinking:
                align_left_human
            JOY "There should be an award for that level of stupid, right? "

        "The happiest pair of animals in the kingdom.":
            $ joy_state = 'happy'
            hide sprite_JOY_tired
            show sprite_JOY_happy:
                align_left_human
            JOY "Yeah, they're cute and deserve each other. "

    show bg_PetCheap_ExamRoom:
        resaturate
    if joy_state == 'thinking':
        hide sprite_JOY_thinking
        show sprite_JOY_happy:
            align_left_human
    JOY "Who needs a date when you get to bear witness to true love like that?"

    pause 1.0  # let the animations complete

    call animate_bg_fadetoblack(delay=0.2)
