label scene_X:
    play music music_pokemon_center fadeout 0.3 fadein 0.3
    menu:
        "Call":
            call scene_1.label_with_params(5)
        "Jump":
            jump scene_1.label_without_params
    return


label .label_with_params(x):
label .label_without_params:
    play music music_healed fadeout 0.3 fadein 0.3
    EILEEN "a = [accumulator]" # displays 5 or 3 depending on what path was taken
    return
