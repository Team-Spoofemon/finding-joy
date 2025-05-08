label scene4c:
    play music amb_TheTreehouseRadio_HospitalAmbience loop fadein 0.3  # audio_office
    show bg_PetCheap_ExamRoom

    #stage: JOY and enter from the right

    JOY "Good thing I turned SID down, right?"

    #stage: JOY turns to WOE
    show bg_PetCheap_ExamRoom:
        desaturate

    JOY "I'm not really into doing that, right? Or coworkers, right?"

    menu:
        JOY "I'm not really into doing that, right? Or coworkers, right? {fast}"  # FEATURE: view prior dialogue

        "Or clients, for that matter!":
            JOY "FAITH was charming, but I do like keeping work and play seperate."
            show sprite_JOY_happy
            jump scene4c_common

        "The right person will come along!1":
            JOY "We've been telling ourselves that for years, Joy..."
            show sprite_JOY_sad
            jump scene4c_common

        "We all die alone, you see...":
            JOY "Okay, I am really in some kind of state! Bad intrusive thoughts!"
            show sprite_JOY_angry
            jump scene4c_common

label scene4c_common:
    show bg_PetCheap_ExamRoom:
        resaturate

    show sprite_JOY_neutral with moveinleft

    QUESTION "Hey uh... is this where i'm supposed to go for pets?"

    JOY "Here we go..."

    show sprite_DOPEY_neutral with moveinright

    QUESTION "Uh, hello? I think my dog is like, and not okay and stuff?"

    JOY "Yes, come on in. What's your name sir?"

    DOPEY "Oh Uh, my name is DOPEY. What's up?"

    JOY "Whats...up? Wahat's up is, you said your dog isn't feeling well?"

    DOPEY "I mean I'm not super sure. It's really hard to tell."

    JOY "What do you mean its hard to tell--"

    show sprite_JOY_fear

    JOY "OH MY GOD!"

    show sprite_GRAVY_fear with moveinleft

    JOY "What do you mean its hard to tell?! There's a  toy stuck in your dog's throat!"

    DOPEY "Oh yeah. I mean... this happens a lot actually."

    show sprite_JOY_angry

    JOY "I'm sorry, come againz?"

    DOPEY "Nickles, Magic the gathering cards, a bunch of rubber bands this oen time..."

    GRAVY "Woof."

    show sprite_JOY_sad

    DOPEY "My dad's car keys, one of those spinny top things, a few spoons..."

    GRAVY "Woof."

    show sprite_JOY_thinking

    DOPEY "My favorite belt, a stress ball, and even my homework another time but nobody believed me..."

    GRAVY "Woof."

    show sprite_JOY_happy

    JOY "Hah hah! Okay, okay! I think I get the picture."

    show sprite_JOY_happy with moveinleft

    DOPEY "Yeah but GRAVY never seems bothered by it, so I don't know."

    JOY "Let's just... see if we can unstuck what's in GRAVY's throat, alright?"

    #stage: Joy and GRAVY shake

    DOPEY "Um, okay."

    #stage: JOY and GRAVY shake

    DOPEY "I guess so."

    #stage: Joy and GRAVY shake

    DOPEY "Am I in trouble?"

    #stage: JOY and GRAVY shake

    JOY "Almost... Yes! Yes sir!"

    show sprite_GRAVY_happy
    show sprite_JOY_neutral with moveinleft

    DOPEY "So I am? I am in trouble?"

    show sprite_JOY_surprise

    JOY "Huh? What? What do you mean you're in trouble? Where do you think you are?"

    DOPEY "Um, like, the principle's office but for pets?"

    JOY "You know what? No. You're not in trouble. Come back anytime. GRAVY too."

    DOPEY "Okay I guess."

    show sprite_DOPEY_neutral:
        flip_face_left_to_right

    DOPEY "Come on, GRAVY."

    show sprite_DOPEY_neutral:
        exit_right

    show sprite_GRAVY_happy:
        exit_right

    JOY "That was..."

    #stage: JOY turns to WOE
    show bg_PetCheap_ExamRoom:
        desaturate

    JOY "What was that?"

    menu:
        JOY "What was that? {fast}"  # FEATURE: view prior dialogue

        "The dumbest pair of animals in the kingdom.":
            JOY "There should be an award for that right? "
            hide sprite_JOY_happy

        "The happiest pair of animals in the kingdom.":
            JOY "Yeah, they're cute and deserve each other. "
            hide sprite_JOY_happy

    show bg_PetCheap_ExamRoom:
        resaturate
    JOY "Who needs a date whenyou get to bear witness to true love like that?"

    #show sprite_JOY_neutral with exit_right
