init:
    define act1_day1_scene_X_choice = "???"

label act1_day1_scene_X:
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
            jump .say_something

        "Use healing machine":
            jump .use_healing_machine

    label .say_something:
        $ act1_day1_scene_X_choice = "said something"
        JOY "Hey, uh... you?"

        POMPO "Why if it isn't Joy! The sweetest, most blooming blossom this side of Viridian City!"

        JOY "Hah... yeah! That's, uh... me! That's definitely me."

        jump .end

    label .use_healing_machine:
        $ act1_day1_scene_X_choice = "didnt say anything"

        JOY "Easy enough, I'm not in a talkative mood anyway."

        jump .end

    label .end:
        JOY "man am I glad i [act1_day1_scene_X_choice]."
        $ data['act1_day1_scene_X']['choice'] = act1_day1_scene_X_choice
        return


# # OTHER INTERESTING SNIPPETS
# label scene_X:
#     play music music_pokemon_center fadeout 0.3 fadein 0.3
#     menu:
#         "Call":
#             call act1_day1_scene_X.label_with_params(5)
#         "Jump":
#             jump act1_day1_scene_X.label_without_params
#     return

# label .label_with_params(x):
# label .label_without_params:
#     play music music_healed fadeout 0.3 fadein 0.3
#     EILEEN "a = [accumulator]" # displays 5 or 3 depending on what path was taken
#     return
