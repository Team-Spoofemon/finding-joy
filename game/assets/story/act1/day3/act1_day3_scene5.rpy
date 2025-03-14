
# Scene 51 starts here.

label act1_day3_scene5:

    scene black with fade

    $ point = 0

    scene bg_CoffeeShop

    show sprite_POMPO_front with moveinleft:
        xalign 0.85
        yalign 1.0

    show sprite_JOY_front:
        xalign 0.15
        yalign 1.0

    POMPO "I think the coffee got a little bit more expensive. And they still want tips?"

    JOY "What’s wrong with tips?"

    POMPO "Prices are so high, shouldn’t that mean that business is fine and they don’t need tips?"

    JOY "I’m pretty sure this place doesn’t pass on those profits to the barista. Prices went up for dog blood testing and our pay isn’t going to go up either."

    POMPO "Sure it will! Once the government gets rid of all of the waste and abuse their taxes are going to go down!"

    POMPO "Then they can pay people more and there won’t be any need for tips! I can’t wait."

    JOY "You really think that’s what’s going to happen?"

    POMPO "Oh definitely. Now that the right person is in charge we can finally recruit more of the right people and get rid of everyone who’s been dragging the rest of us down."

    JOY "If you say so."

    POMPO "I didn’t think you’d be interested in talking about this kind of stuff. Isn’t this nice? We can do this every day if you want!"

    JOY "Tempting offer, but I'll have to pass."

    POMPO "..."

    POMPO "What do you mean you’ll have to pass?"

    JOY "I mean that this thing is a one-time thing."

    POMPO "One time? What, I'm not good enough for you?"

    JOY "?!"

    JOY "The FUCK did he just ask?"

    WOE " "

menu:
    "You're not into blowhards. Just tell him that. See how that goes.":
        jump scene51_choice1a
    "There's many fish in the sea! That's got to be new advice he's never heard before!" if point > 0:
        jump scene51_choice1b
    "I'm seeing someone. I'm definitely seeing someone." if point > 1:
        jump scene51_choice1c

label scene51_choice1a:
    JOY "Sorry, but I don't like the way you think and I don't like the way you talk--we wouldn't work."

    JOY "I think the world is complicated. You think the world is simple. It isn't."

    jump scene51_choice_common

label scene51_choice1b:
    JOY "Sorry, I'm sure you're good enough for the right person, but I don't think that person is me."

    jump scene51_choice_common

label scene51_choice1c:
    JOY "Sorry, I'm seeing someone."

    jump scene51_choice_common

label scene51_choice_common:
    POMPO "So now I'm stuck with the bill? Thanks a lot, feminism! Where's the equity here?"

    hide sprite_JOY_front with moveoutleft

    show sprite_SHOPKEEPER_front with moveinleft:
        xalign 0.15
        yalign 1.0

    SHOPKEEPER "Your bill has been reduced by $4.50. Have a nice day, sir."

    POMPO "..."

    scene black with fade

    return
