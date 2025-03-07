label actX_dayX_scene_X_style1:
    '''
    Narration / Docstring:
        sublabels - ".subscene_1" allows some organization for ideas
        does not set any global variables
    '''
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

    menu:
        "Say something!":
            $ data['actX_dayX_scene_X']['choice'] = "said something"
            JOY "No way! I'm busy anyways and its not like I want ot talk to him!"

        "Walk away.":
            JOY "Good idea, its not like any good is gonna come out of talking to him"
            $ data['actX_dayX_scene_X']['choice'] = "Walked away"

    JOY "Let's just quietly get the hell outta here. I'm glad I <[data['actX_dayX_scene_X']['choice']]>"

    return


# another way to do choice
label actX_dayX_scene_X_style2:
    '''
    Narration / Docstring:
        uses helper subfunctions to set choices rather than assigning them
    '''
    menu:
        "A)":
            call .set_choice("variable_replace", "A")

        "B)":
            call .set_choice("variable_replace", "B")

    JOY "Picked [data['variable_replace']]"
    return

    # helper "functions"
    label .set_choice(key, value):
        $ data[key] = value
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
