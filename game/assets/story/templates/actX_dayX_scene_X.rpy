label actX_dayX_scene_X_style1:
    '''
    Narration / Docstring:
        sublabels - ".subscene_1" allows some organization for ideas
        does not set any global variables
    '''
label .subscene_1:
    play music bgm_menu fadeout 0.3 fadein 0.3

    scene bg_PetCheap_FrontDesk with fade
    show sprite_JOY_front with dissolve

    JOY "Hi! I'm Joy, a pre-med student at San Jose State University."

    JOY "Today I'm at the local PetSmart getting a feel for how a job here might go."

    hide sprite_JOY_front with moveoutright


label .subscene_2:
    scene bg_PetCheap_ExamRoom with fade
    show sprite_JOY_front at left with dissolve

    JOY "I wonder if I'm going to run into anyone I recognize here..."

    hide sprite_JOY_front with moveoutright
    show sprite_JOY_front at left with moveinleft

    JOY "Oh no... its this fucking guy!"

    show sprite_POMPO_front at right with dissolve

    play music music_POMPO_theme

    POMPO "..."

    JOY "I dont think he noticed me yet... should I say something or just use the healing machine?"

    menu:
        "Say something!":
            $ data['actX_dayX_scene_X']['choice'] = "said something"
            JOY "No way! I'm busy anyways and its not like I want ot talk to him!"

        "Walk away.":
            JOY "Good idea, its not like any good is gonna come out of talking to him"
            $ data['actX_dayX_scene_X']['choice'] = "Walked away"

    JOY "Let's just quietly get the hell outta here. I'm glad I <[data['actX_dayX_scene_X']['choice']]>"

    return


# helper "functions"
label set_choice(key, value):
    $ data[key] = value
    return

# another way to do choice
label actX_dayX_scene_X_style2:
    '''
    Narration / Docstring:
        uses helper subfunctions to set choices rather than assigning them
    '''
    menu:
        "A)":
            call set_choice("variable_replace", "A")

        "B)":
            call set_choice("variable_replace", "B")

    JOY "Picked [data['variable_replace']]"
    return


# label templates_scene_X:
#     play music music_pokemon_center fadeout 0.3 fadein 0.3
#     menu:
#         "Call":
#             call actX_dayX_scene_X.label_with_params(5)
#         "Jump":
#             jump actX_dayX_scene_X.label_without_params
#     return

# label .label_with_params(x):
# label .label_without_params:
#     play music music_healed fadeout 0.3 fadein 0.3
#     EILEEN "a = [accumulator]" # displays 5 or 3 depending on what path was taken
#     return


# https://www.renpy.org/doc/html/layeredimage.html

label debug_animation:
    # https://www.renpy.org/doc/html/transforms.html#atl
    image sprite_JOY_front_moving:
        animation
        "assets/characters/JOY/sprite_JOY_neutral.png"
        xalign 0.0
        linear 5.0 xalign 1.0
        repeat

    show sprite_JOY_front_moving

    JOY "debug animation"

    hide sprite_JOY_front_moving with dissolve

    JOY "debug animation dissolve"

    show sprite_JOY_front_moving:  # unrelated image
        animation
        "assets/characters/JOY/sprite_JOY_fear.png"
        xalign 0.0
        linear 5.0 xalign 1.0
        repeat

    JOY "show vs image"

    JOY "note, without return, this image will continue to move forever"




# label play_dialogue_and_animate(character, dialogue):
#     play sound "assets/audio/bombomb.ogg"
#     character dialogue
#     return

layeredimage faith:
    # zoom 1.4
    # at recolor_transform  # not sure what it is, doesnt work either

    always:
        "assets/characters/FAITH/sprite_FAITH_happy.png"
    attribute worried:
        "assets/characters/FAITH/sprite_FAITH_fear.png"

    # group expressions:
    #     pos (100, 600)
    #     attribute happy default:
    #         ""

layeredimage biscuits:
    # https://gruntsteel.itch.io/distant-travels/devlog/452114/how-to-set-up-layeredimages-in-renpy-new-sprite-teaser
    # helped

    always:
        "assets/characters/FAITH/BISCUITS/sprite_BISCUITS_front.png"
    group emotions:
        attribute worried:
            "assets/characters/FAITH/BISCUITS/sprite_BISCUITS_fear.png"
        attribute happy:
            "assets/characters/FAITH/BISCUITS/sprite_BISCUITS_happy.png"

init python:
    def bombomb_voice(event, interact=True, **kwargs):
        # https://www.renpy.org/doc/html/character_callbacks.html#character-callbacks
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("assets/audio/bombomb.ogg")
        elif event == "slow_done":
            renpy.sound.stop()

define f = Character("faith", callback=bombomb_voice)

transform xflip:
    ease_elastic 0.5 xzoom -1.0 yzoom 1.0

label debug_conversation:

    show bg_PetCheap_ExamRoom:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)

    "petcheap saturated? Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce interdum odio eget pharetra semper."

    show bg_PetCheap_ExamRoom:
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    "petcheap un saturated? Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce interdum odio eget pharetra semper."

    hide bg_PetCheap_ExamRoom

    "moving joy is still there since it never went away... show statement just keeps adding images atop other images"

    menu:
        "petcheap un saturated? Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce interdum odio eget pharetra semper. {fast}"

        "how do i":
            "first choice"
        "display previous dialogue below, just figured it out, dont make it a choice...":
            "first choice"


    show faith
    f "my name is faith"

    show biscuits:
        xalign .5
        yalign .6

    f "this is biscuits"

    show faith worried:
        animation
        xalign 0.5
        linear 0.05 xalign 0.51
        linear 0.05 xalign 0.5
        linear 0.05 xalign 0.49
        repeat

    f "i am worried"

    show faith worried at xflip:
        animation

    f "sorry for spazzing"

    show biscuits happy
    f "biscuits is happy im worried"
