# Start of Act 1, Day 3, Scene 1
# JOY services FAITH who comes in with her cat who has a botfly infection
transform moveright:
    linear 0.6 xpos 0.5

label act1_day3_scene1:

    play music music_theme2

    scene black with fade
    $ renpy.pause (0.5, hard=True)

    scene bg_PetCheap_ExamRoom

    show sprite_JOY_front:
        xalign 0.15
        yalign 1.0

    JOY "Okay, here we go things are starting to pick up."

    QUESTION "Please somebody help! My cat!!"

    JOY "Here we go..."

    SUSAN "Yeah, you're gonna want to get that fixed. Joy? You back there?"

    JOY "Yes I'm here Susan! Can you show the patient in?"

    show sprite_FAITH_front with moveinright:
        xalign 0.85
        yalign 1.0

    QUESTION "Oh my god, are you the vet?"

    JOY "Yes I am, how can I help you?"

    show sprite_FAITH_worried:
        xalign 0.85
        yalign 1.0
    hide sprite_FAITH_front


    FAITH "I'm Faith and this is Biscuits--there's something alive inside my cat's chest!!"

    show sprite_BISCUITS_worried with moveinright:
        xalign 0.85
        yalign 1.0

    show sprite_JOY_front:
        moveright

    $ renpy.pause (1.2, hard=True)

    JOY "Poor thing..."

    JOY "It seems like Biscuits has something called a botfly embedded, sweetie."

    JOY "He's going to be just fine!"

    FAITH "That's a relief.. I'm just so worried!"

    JOY "Don't be, that's what I'm here for."

    #Insert Minigame 5: The botfly is loose and you have to shoot it


    stop music fadeout 0.5
    scene black with fade

    return
    #replace return with a jump to Act 1, Day 3, Scene 2