label scene2:

    show bg_PetCheap_FrontDesk

    # *stage:* JOY enters from the right and ends up on the left looking left.
    show sprite_JOY_neutral with moveinright

    JOY "Well that was crazy. That was CRAZY."

    show bg_PetCheap_FrontDesk

    menu:
        JOY "Well that was crazy. That was CRAZY. {fast}"  # FEATURE: view prior dialogue

        "The next is going to be a phycopath!":
            JOY "Dear god in heaven, no!"
            hide sprite_JOY_fear
            jump scene2_common

        "Please no more...":
            JOY "We can survive, I know it"
            hide sprite_JOY_happy
            jump scene2_common

        "Why not join the crazy, like the joker?":
            JOY "Just one bad day away, huh?"
            hide sprite_JOY_angry
            jump scene2_common

label scene2_common:

        show sprite_JOY_neutral with moveinleft

        QUESTION "Oh my god, are you the vet?"

        JOY "Yes I am, how can I help you?"

        show sprite_FAITH_fear

        FAITH "I'm Faith and this is BISCUITS-there's something inside his chest!"

        show sprite_BISCUITS_fear with moveinright
        show sprite_JOY_neutral at center with moveinright

        JOY "Poor thing..."

        FAITH "What's wrong? Are they going to be okay?"

        show sprite_JOY_fear

        JOY "Don't be, that's what I'm here for."
        # stage: Joy and Biscuits shake

        JOY "Cats go outside a lot..."

        FAITH "Oh no! I promise I'll never let BISCUITS go again!"

        # stage: JOY and BISCUITS shake

        JOY "I'm sure you just want your BISCUITS..."

        #stage: Joy and BISCUITS...

        JOY "I'm sure you just want your BISCUITS..."

        show sprite_BISCUITS_happy
        show sprite_FAITH_sad with moveinright
        show sprite_JOY_neutral with moveinleft


        FAITH "BISCUITS is happy, I'll come outside with you"

        JOY "I'm just happy to help. Come by anytime."

        show sprite_FAITH_happy with moveinleft

        FAITH "Thank you so much! Watching you work was insipring!"

        show sprite_JOY_neutral

        JOY "It's no problem, I--"

        show sprite_JOY_happy

        JOY "Inspring? Really?"

        FAITH "Yep! Do you mind if we use the backyard for a minute?"

        JOY "Sure thing."

        show sprite_FAITH_happy:
            flip_face_right_to_left

        FAITH "Come on, BISCUITS! Let's calm down outside for a bit."

        show sprite_FAITH_happy:
            exit_left

        JOY "Wow. Inspiring, huh?"

        menu:
            JOY "Wow. Inspiring, huh? {fast}"  # FEATURE: view prior dialogue

            "I wasn't expecting that":
                JOY "Right? this feels really cool!"
                show sprite_JOY_happy

            "Slide into those DM's or else":
                JOY "Be gone, intrusive thoughts! Horny jail for you!"
                show sprite_JOY_angry
                # UNLOCK ROMANCE OPTION
                $ choices['faith-unlock'] = True

        pause 1.0  # let the animations complete

        call animate_bg_fadetoblack(delay=0.2)
