# Scene 4b: JOY and FAITH, coffee shop, date scene, guaranteed ends well

label scene4b:
    $ emotion = 0

    scene black with fade
    $ renpy.pause (1.0, hard=True)

    scene bg_CoffeeShop with fade

    show sprite_JOY_neutral with moveinright:
        align_left_human

    $ renpy.pause (0.5, hard=True)

    show sprite_FAITH_neutral with moveinright:
        align_right_human

    $ renpy.pause (0.5, hard=True)

    show sprite_JOY_neutral:
        flip_face_left_to_right
   
    #$ renpy.pause (0.5, hard=True)

    hide sprite_FAITH_neutral
    show sprite_FAITH_happy:
        align_right_human

    FAITH "Wow, I never knew this coffee shop existed! And they allow pets!"

    show sprite_JOY_happy:
        align_left_human

    JOY "Truthfully I had no idea until five minutes ago."

    FAITH "Really? How'd you find out?"

    JOY "Oh, this co-worker I don't really like asked me out here and I turned them down."

    hide sprite_FAITH_happy
    show sprite_FAITH_thinking:
        align_right_human

    FAITH "So you ditched them and decided to ask me instead?"

    hide sprite_JOY_happy
    show sprite_JOY_fear:
        align_left_human

    JOY "Oh no... I'm a bad person, aren't I?"

    hide sprite_FAITH_thinking
    show sprite_FAITH_fear:
        align_right_human

    FAITH "No! No! Nah..."

    hide sprite_JOY_fear
    show sprite_JOY_sad:
        align_left_human

    JOY "I'm so sorry, I shouldn't have done that! I-!"

    hide sprite_FAITH_fear
    show sprite_FAITH_happy:
        align_right_human

    FAITH "I'm kidding, I'm kidding!"

    hide sprite_JOY_sad
    show sprite_JOY_happy:
        align_left_human

    JOY "You scared me! Don't do that to me!"

    FAITH "That was a bad joke, I'm sorry!"

    FAITH "I guess I'm still jumpy since you helped Biscuits."

    JOY "And I'm sorry for asking you out so suddenly!"

    hide sprite_FAITH_happy
    show sprite_FAITH_thinking:
        align_right_human

    FAITH "What kind of company doesn't have a fraternization policy?"

    hide sprite_JOY_happy
    show sprite_JOY_angry:
        align_left_human

    JOY "A bad one."

    hide sprite_JOY_angry
    show sprite_JOY_neutral:
        align_left_human

    JOY "But at least that means I can talk to you, right?"

    JOY "Speaking of which..."

    hide sprite_FAITH_thinking
    show sprite_FAITH_neutral:
        align_right_human

    FAITH "Yeah?"

    hide sprite_JOY_neutral
    show sprite_JOY_fear:
        align_left_human

    JOY "Did you really mean what you said?"

    hide sprite_FAITH_neutral
    show sprite_FAITH_fear:
        align_right_human

    FAITH "Wait, which thing? I feel like I said a lot!"

    JOY "Did you mean what you said about being inspiring?"

    hide sprite_FAITH_fear
    show sprite_FAITH_neutral:
        align_right_human

    FAITH "Oh! Well, yes! Why wouldn't I mean that?"

    hide sprite_JOY_fear
    show sprite_JOY_sad:
        align_left_human

    JOY "It's just..."

    show sprite_FAITH_neutral:
        desaturate
    show bg_CoffeeShop:
        desaturate

    JOY "What am I even yapping about?!"

menu:
    "I don't want you disappointed like I am.":
        jump scene4b_a
    "It's hard sometimes. I don't feel inspiring.":
        jump scene4b_b

label scene4b_a:
    show sprite_FAITH_neutral:
        resaturate
    show bg_CoffeeShop:
        resaturate

    JOY "I don't want you to get into helping animals just to get disappointed like me."

    hide sprite_FAITH_neutral
    show sprite_FAITH_sad:
        align_right_human

    FAITH "Are you disappointed?"

    JOY "Even if I have ten good encounters, having one awful moment ruins everything."

    hide sprite_FAITH_sad
    show sprite_FAITH_neutral:
        align_right_human

    FAITH "I work at my campus Pizza Hut. I know what you mean."

    hide sprite_JOY_sad
    show sprite_JOY_surprised:
        align_left_human

    JOY "You do?"

    FAITH "Yup. Work isn't bad... sometimes people are." 

    FAITH "Thats why I'm thinking about vet school."

    hide sprite_JOY_surprised
    show sprite_JOY_sad:
        align_left_human

    $ emotion += 0

    JOY "Are you sure?"

    jump scene4b_common


label scene4b_b:
    show sprite_FAITH_neutral:
        resaturate
    show bg_CoffeeShop:
        resaturate

    JOY "I love working with animals, you know?"

    hide sprite_FAITH_neutral
    show sprite_FAITH_happy:
        align_right_human

    FAITH "I could tell. That's why I said what I did."

    JOY "But with everything going on —— our funding just got cut."

    hide sprite_FAITH_happy
    show sprite_FAITH_sad:
        align_right_human

    FAITH "I'm so sorry. Which agency was it?"

    JOY "USDA. Without the VSGP grant, so many vet clinics will close."

    JOY "I won't be able to work with animals anymore."

    hide sprite_FAITH_sad
    show sprite_FAITH_neutral:
        align_right_human

    FAITH "You'll pull through this."

    hide sprite_JOY_sad
    show sprite_JOY_happy:
        align_left_human
    
    $ emotion += 1

    JOY "You sound so confident. Why do you think so?"

    FAITH "If you love what you do, you'll find a way to make it happen."

    jump scene4b_common

label scene4b_common:
    hide sprite_FAITH_neutral
    show sprite_FAITH_happy:
        align_right_human

    FAITH "I know I'm a bit naive, but I still {i}want{/i} to believe in things."

    if emotion == 0:
        hide sprite_JOY_sad

    elif emotion == 1:
        hide sprite_JOY_happy

    #hide
    show sprite_JOY_thinking:
        align_left_human

    JOY "Like what? What do you believe right now?"

    FAITH "No matter what, follow your passion."

    FAITH "Even when the world is ending, follow your passion."

    FAITH "Do what you can."

    hide sprite_JOY_thinking
    show sprite_JOY_sad:
        align_left_human

    JOY "The world definitely looks like its ending."

    hide sprite_FAITH_happy
    show sprite_FAITH_neutral:
        align_right_human

    FAITH "And maybe because of that, it's all the more reason."

    hide sprite_FAITH_neutral
    show sprite_FAITH_happy:
        align_right_human

    FAITH "Follow your passion, and that will fix the world."

    hide sprite_JOY_sad
    show sprite_JOY_happy:
        align_left_human

    JOY "Follow your passion, and that will fix the world?"

    FAITH "Yes."

    FAITH "That's what I believe."

    return