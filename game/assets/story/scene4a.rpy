# Scene 4a - Joy and Sid's Coffee Shop Date

label scene4a:

    scene black with fade
    $ renpy.pause (1.0, hard=True)

    scene bg_CoffeeShop with fade

    show sprite_SID_neutral with moveinright:
        align_right_human

    $ renpy.pause (0.5, hard=True)

    show sprite_JOY_neutral with moveinright:
        align_left_human

    $ renpy.pause (0.5, hard=True)

    show sprite_JOY_neutral:
        flip_face_left_to_right

    hide sprite_SID_neutral
    show sprite_SID_angry:
        align_right_human

    SID "Man, the coffee is pricey and they still want tips?"

    JOY "What's wrong with tips?"

    SID "Prices are high, so business is doing fine! No tips needed!"

    hide sprite_JOY_neutral
    show sprite_JOY_thinking:
        align_left_human

    JOY "PetCheap is doing fine, but we're not. Tips would be nice, right?"

    hide sprite_SID_angry
    show sprite_SID_neutral:
        align_right_human

    SID "But when taxes go down they'll give us more money!"

    hide sprite_JOY_thinking
    show sprite_JOY_neutral:
        align_left_human

    JOY "Taxes will go down? When is that happening?"

    SID "Yep! Right after all the waste and abuse gets thrown out!"

    JOY "The waste and abuse, huh?"

    hide sprite_SID_neutral
    show sprite_SID_happy:
        align_right_human

    SID "The right person is in charge! Good things are finally happening!"

    hide sprite_JOY_neutral
    show sprite_JOY_angry:
        align_left_human

    JOY "What kind of good things?"

    SID "All of the wrong people are getting out of the way. It's a new age."

    hide sprite_JOY_angry
    show sprite_JOY_sad:
        align_left_human

    JOY "That's one way of looking at it."

    hide sprite_SID_happy
    show sprite_SID_thinking:
        align_right_human

    SID "You're interested in this kind of stuff?"

    hide sprite_JOY_sad
    show sprite_JOY_neutral:
        align_left_human

    JOY "Of course. What happens over there affects over here."

    hide sprite_SID_thinking
    show sprite_SID_happy:
        align_right_human

    SID "Sure, sure--but isn't this nice? We could do this every day, just you and me!"

    hide sprite_JOY_neutral
    show sprite_JOY_fear:
        align_left_human

    JOY "Tempting offer--"

    SID "Such a good offer! Coffee, I pay for food--"

    hide sprite_JOY_fear
    show sprite_JOY_angry:
        align_left_human

    JOY "I mean it's a tempting offer, but I'll have to pass."

    hide sprite_SID_happy
    show sprite_SID_neutral:
        align_right_human

    SID "Huh?"

    SID "What do you mean?"

    hide sprite_SID_neutral
    show sprite_SID_angry:
        align_right_human

    SID "After I paid for coffee, what do you mean \"you'll pass\"?"

    hide sprite_JOY_angry
    show sprite_JOY_sad:
        align_left_human

    JOY "I mean that this thing is a one-time thing."

    SID "You little... How can you be so ungrateful?"

    hide sprite_JOY_sad
    show sprite_JOY_angry:
        align_left_human

    JOY "Excuse me?"

    SID "I set this up and I did everything right!"

    hide sprite_JOY_angry
    show sprite_JOY_fear:
        align_left_human

    JOY "Um."

    SID "What? Are you just too good for me or something?"

    #change saturation to talk to WOE
    show sprite_SID_angry:
        desaturate
    show bg_CoffeeShop:
        desaturate

    JOY "The FUCK did he just ask?"

menu:
    "Slap the shit out of him.":
        jump Scene4a_a
    "De-escalate.":
        jump Scene4a_b
    "Slap the {i}shit{/i} out of him.":
        jump Scene4a_c

label Scene4a_a:
    #change saturation back
    show sprite_SID_angry:
        resaturate
    show bg_CoffeeShop:
        resaturate

    $ renpy.pause (1.0, hard=True)

    hide sprite_JOY_fear
    show sprite_JOY_happy:
        align_left_human

    JOY "Sid."

    SID "What?"

    JOY "Not knowing how things work isn't sexy."

    hide sprite_SID_angry
    show sprite_SID_sad:
        align_right_human

    hide sprite_JOY_happy
    show sprite_JOY_neutral:
        align_left_human
        flip_face_right_to_left

    JOY "Goodbye."

    hide sprite_JOY_neutral with moveoutleft

    jump Scene4a_common

label Scene4a_b:
    #change saturation back
    show sprite_SID_angry:
        resaturate
    show bg_CoffeeShop:
        resaturate

    $ renpy.pause (1.0, hard=True)

    hide sprite_JOY_fear
    show sprite_JOY_sad:
        align_left_human

    JOY "I'm really sorry--I just don't think we would work well together."

    SID "What?"

    hide sprite_SID_angry
    show sprite_SID_sad:
        align_right_human

    hide sprite_JOY_sad
    show sprite_JOY_neutral:
        align_left_human
        flip_face_right_to_left

    JOY "See you at work tomorrow."

    hide sprite_JOY_neutral with moveoutleft

    jump Scene4a_common

label Scene4a_c:
    #change saturation back
    show sprite_SID_angry:
        resaturate
    show bg_CoffeeShop:
        resaturate

    $ renpy.pause (1.0, hard=True)

    hide sprite_JOY_fear
    show sprite_JOY_angry:
        align_left_human

    JOY "The VSGA."

    SID "What the fuck is that?"

    JOY "The fucking Veterinary Services Grant Program. It's part of USDA."

    JOY "And one billion just got cancelled."

    hide sprite_SID_angry
    show sprite_SID_sad:
        align_right_human

    SID "Wait no... PetCheap doesn't-!"

    JOY "We're the \"waste and abuse.\""

    hide sprite_SID_sad
    show sprite_SID_angry:
        align_right_human

    SID "Wait no... You're lying!"

    hide sprite_JOY_angry
    show sprite_JOY_thinking:
        align_left_human

    JOY "I wonder when I'll see your ass at unemployment with me?"

    hide sprite_SID_angry
    show sprite_SID_sad:
        align_right_human

    SID "They're only going after criminals! Not me!"

    hide sprite_JOY_thinking
    show sprite_JOY_neutral:
        align_left_human
        flip_face_right_to_left

    JOY "Maybe you can ask me out next time--when we're in line together."

    hide sprite_JOY_neutral with moveoutleft

    jump Scene4a_common

label Scene4a_common:
    hide sprite_SID_sad
    show sprite_SID_angry:
        align_right_human

    SID "So now I'm stuck with the bill?"

    SID "Thanks a lot, feminism! Where's the equity here?"

    hide sprite_SID_angry
    show sprite_SID_sad:
        align_right_human

    SID "This is some dee-ee-aye bullshit!"

    #stage: SHOPKEEPER approaches from the left facing right and ends up in the center.
    show sprite_SHOPKEEPER_neutral with moveinleft:
        #flip_face_left_to_right
        xalign 0.5
        yalign 1.0

    SHOPKEEPER "Excuse me sir?"

    hide sprite_SID_sad
    show sprite_SID_angry:
        align_right_human

    SID "What?"

    SHOPKEEPER "The kind lady who just left gave us five dollars cash."

    hide sprite_SID_angry
    show sprite_SID_neutral:
        align_right_human

    SID "What?"

    SHOPKEEPER "Would you like your refund as credits or sent to your card?"

    hide sprite_SID_neutral
    show sprite_SID_sad:
        align_right_human

    SID "Card, please."

    return