# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joy")
define w = Character("Woe")

# The game starts here.

label scene52:

    # These display lines of dialogue.


    j "I can't stand this. I can't fucking stand this."

    j "Why are there people like him in the world? Why?"

    $ choice = None #labels choice as none

    menu: #starts menu

            "You know why":                 #choice label
                $ choice = "know"           #keyword

            "Death to men":                 #choice label
                $ choice = "death"          #keyword

            "They're being emboldened":     #choice label
                $ choice = "emboldened"     #keyword

    if choice == "know":                    #user selects know, this will run

        show woe frusrated 

        j "Yeah, because nobody has ever told them no in their life! I get it."

    elif choice == "death":

        show woe happy

        w "But if I pulled that off, that's not a viable strategy for the existence of our species...plus illegal."

    elif choice == "emboldened":

        show woe confident

        w "But what the hell am I supposed to do about that?" 


    jump continue_game

label continue_game:


    j "UGH! I fucked up--now when I come back tomorrow I'm going to have to deal with him and everyone's going to know and!!"


    j "Oh my god... did I do the right thing"

    $ choice = None #labels choice as none 

    menu:

            "No":
                $ choice = "No"

            "Yes":
                $ choice = "Yes"
        
    if choice == "No":

        show joy mad

        j "You're just trying to trick me"

    elif choice == "Yes":

        show joy unsure

        j "Are you sure?"

    jump continue_again

label continue_again:

    j "Sigh."

    j "I'm just so done."

    $ choice = None #labels choice as none 

    menu:

            "You'll be fine":
                $ choice = "fine"

            "if tomorrow even comes, it's just going to have even more crazy shit in it":
                $ choice = "crazy"
       
    if choice == "fine":

        show joy calm


    elif choice == "crazy":
        
        show joy nervous

    jump continue_again2

label continue_again2:


    j "Yeah"

    j "This is fine. I'll deal with tomorrow when it comes. We're ok. I'm ok. We're ok right?"


    menu:   

            "Yes":
                $ choice = "Yes" 

            "No":
                $ choice = "No"

    if choice == "Yes":

        show joy calm

    elif choice == "No":

        show joy nervous

    jump continue_game_again

label continue_game_again:

    j "We're ok. I'm ok. It's ok."

    # This ends the game.

    return
