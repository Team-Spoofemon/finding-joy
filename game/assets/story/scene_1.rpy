define scene_1_choice = "???"

label scene_1:
label .subscene_1:
    play music music_JOY_theme fadeout 0.3 fadein 0.3

    scene bg_front_desk with fade
    show sprite_JOY_front with dissolve

    JOY "Hi! I'm Joy, a pre-med student at San Jose State University."

    JOY "Today I'm at the local PetSmart getting a feel for how a job here might go."

    hide sprite_JOY_front with moveoutright


label .subscene_2:
    scene bg_table with fade
    show sprite_JOY_front at left with dissolve

    JOY "I wonder if I'm going to run into anyone I recognize here..."

    hide sprite_JOY_front with moveoutright
    show sprite_JOY_front at left with moveinleft

    JOY "Oh no... its this fucking guy!"

    show sprite_POMPO_front at right with dissolve

    play music music_POMPO_theme

    POMPO "..."

    JOY "I dont think he noticed me yet... should I say something or just use the healing machine?"

    default choice = ""
    menu:
        "Say something!":
            jump .say_something

        "Use healing machine":
            jump .use_healing_machine

    label .say_something:
        $ choice = "said something"
        JOY "Hey, uh... you?"

        POMPO "Why if it isn't Joy! The sweetest, most blooming blossom this side of Viridian City!"

        JOY "Hah... yeah! That's, uh... me! That's definitely me."

        jump .end

    label .use_healing_machine:
        $ choice = "didnt say anything"

        JOY "Easy enough, I'm not in a talkative mood anyway."

        jump .end

    label .end:
        JOY "man am I glad i [choice]."
        $ data['scene_1']['choice'] = scene_1_choice
        return
