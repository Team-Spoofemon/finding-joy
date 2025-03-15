label act1_day3_scene6:

    scene black with fade

    scene bg_JoyHouse_entry

    show sprite_JOY_mad

    JOY "I can't stand this. I can't fucking stand this."

    JOY "Why are there people like him in the world? Why?"

    $ choice = None #labels choice as none

    menu: #starts menu

            "You know why":                 #choice label
                $ choice = "know"           #keyword

            "Death to men":                 #choice label
                $ choice = "death"          #keyword

            "They're being emboldened":     #choice label
                $ choice = "emboldened"     #keyword

    if choice == "know":                    #user selects know, this will run

        show sprite_JOY_frustrated

        JOY "Yeah, because nobody has ever told them no in their life! I get it."

    elif choice == "death":

        show sprite_JOY_happy

        JOY "But if I pulled that off, that's not a viable strategy for the existence of our species...plus illegal."

    elif choice == "emboldened":

        show sprite_JOY_frustrated

        JOY "But what the hell am I supposed to do about that?"


    show sprite_JOY_mad

    JOY "UGH! I fucked up--now when I come back tomorrow I'm going to have to deal with him and everyone's going to know and!!"


    JOY "Oh my god... did I do the right thing"

    $ choice = None #labels choice as none

    menu:

            "No":
                $ choice = "No"

            "Yes":
                $ choice = "Yes"

    if choice == "No":

        show sprite_JOY_mad

        JOY "You're just trying to trick me"

    elif choice == "Yes":

        show sprite_JOY_unsure

        JOY "Are you sure?"


    JOY "Sigh."

    JOY "I'm just so done."

    $ choice = None #labels choice as none

    menu:

            "You'll be fine":
                $ choice = "fine"

            "if tomorrow even comes, it's just going to have even more crazy shit in it":
                $ choice = "crazy"

    if choice == "fine":

        show sprite_JOY_calm


    elif choice == "crazy":

        show sprite_JOY_nervous


    JOY "Yeah"

    JOY "This is fine. I'll deal with tomorrow when it comes. We're ok. I'm ok. We're ok right?"


    menu:

            "Yes":
                $ choice = "Yes"

            "No":
                $ choice = "No"

    if choice == "Yes":

        show sprite_JOY_calm

    elif choice == "No":

        show sprite_JOY_nervous


    JOY "We're ok. I'm ok. It's ok."

    scene black with fade

    return
