label scene5b:

    show bg_JOY_bedroom

    show sprite_JOY_happy with moveinleft

    JOY "Wow, I had a really good time..."

    JOY "Kinda crazy I'm even allowed a good time these days."

    show sprite_JOY_happy with moveright

    show sprite_JOY_sad at align_right_human

    pause 0.5

    JOY "Do I deserve this? Do I deserve even a little happy?"

    menu:
        JOY "Do I deserve this? Do I deserve even a little happy?"

        "It's too good to be true.":
            $ choice = 'true'
            JOY "Maybe, but I do want to believe it is true."
            jump scene5b_next

        "Why not? You've worked hard":
            $ choice = 'worked'
            JOY "I want to believe that."
            jump scene5b_next

        "Happiness is a fickle thing.":
            $ choice = 'fickle'
            JOY "I'd like to believe I can find happy though."
            jump scene5b_next

label scene5b_next:

    show sprite_JOY_fear at align_right_human

    JOY "UGH! I feel like I blew it!"

    JOY "I said too much and told FAITH I've got these doubts..."

    show sprite_JOY_fear with moveleft

    show sprite_JOY_sad at align_left_human

    JOY "Did I mess up?"

    menu:

        JOY "Did I mess up?"

        "No.":
            $ choice = 'no'
            JOY "You're just trying to trick me."
            jump scene5b_next2

        "Yes.":
            $ choice = 'yes'
            JOY "Are you sure?"
            jump scene5b_next2

label scene5b_next2:

    JOY "*sigh*"

    JOY "But FAITH was right, regardless of how coffee went."

    show sprite_JOY_sad with moveright

    show sprite_JOY_neutral at align_right_human

    JOY "Even if I have self-doubts..."

    JOY "I am passionate."

    JOY "I love animals."

    show sprite_JOY_angry at align_right_human

    JOY "I will keep it up even if work itself sucks!"

    menu:
        JOY "I will keep it up even if work itself sucks!"

        "Damn straight.":
            $ choice = 'straight'
            jump scene5b_next3

label scene5b_next3:

    show sprite_JOY_neutral:
        linear 0.6 xaligh 0.5

    JOY "Even if the world is ending around us!"

    menu:
        JOY "Even if the world is ending around us!""

        "Because this is how we can contribute!":
            $ choice = 'contribute'
            jump scene5b_last

label scene5b_last:

    show sprite_JOY_happy at center

    JOY "Yeah. This is how I will fix the world."

    menu:
        JOY "Yeah. This is how I will fix the world."
        
        "Yes!":
            $ choice = 'yes'
            animate_bg_fadetoblack(delay=0.5)
