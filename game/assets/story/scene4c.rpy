label scene4c:

   #stage: JOY and enter from the right

   JOY "Good thing I turned SID down, right?"

   #stage: JOY turns to WOE

   JOY "I'm not really into doing that, right? Or coworkers, right?"

   menu:
      WOE

      "Or clients, for that matter":
   $ choice = choices['scene4'] = 'sid'
   JOY "FAITH was charming, but I do like keeping work and play seperate. sprite_JOY_happy"
   jump scene4c_common

   "The right person will come along1":
   $ choice = choices['scene4'] = 'sid'
   JOY "We've been telling ourselves that for years, Joy... sprite_JOY_sad"
   jump scene4c_common

   "We all die alone, you see":
   $ choice = choices['scene4'] = 'sid'
   JOY "Okay, I am really in some kind of state! Bad intrusive thoughts! sprite_JOY_angry"
   jump scene4c_common

label scene4c_common:

   show sprite_JOY_neutral with moveleft

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

   show sprite_Biscuits_neutral with moveinleft

   JOY "What do you mean its hard to tell?! There's a  toy stuck in your dog's throat!"

   DOPEY "Oh yeah. I mean... this happens a lot actually."

   show sprite_JOY_angry

   JOY "I'm sorry, come againz?"

   DOPEY "Nickles, Magic the gathering cards, a bunch of rubber bands this oen time..."

   Gravy "Woof."

   show sprite_JOY_sad

   DOPEY "My dad's car keys, one of those spinny top things, a few spoons..."

   GRAVY "Woof."

   show sprite_JOY_thinking

   DOPEY "My favorite belt, a stress ball, and even my homework another time but nobody believed me..."

   GRAVY "Woof."

   show sprite_JOY_happy

   JOY "Hah hah! Okay, okay! I think I get the picture."

   show sprite_GRAVY_neutral with moveinright
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
   show sprite_JOY_neutral with moveleft

   DOPEY "So I am? I am in trouble?"

   show sprite_JOY_surprise

   JOY "Huh? What? What do you mean you're in trouble? Where do you think you are?"

   DOPEY "Um, like, the principle's office but for pets?"

   JOY "You know what? No. You're not in trouble. Come back anytime. GRAVY too."

   DOPEY "Okay I guess."

   show sprite_DOPEY_neutral with flip_face_left_to_right:

   DOPEY "Come on, GRAVY."

   show sprite_DOPEY_neutral with exit_right_:
   show sprite_GRAVY_neutral with exit_right_:

   JOY "That was..."

   #stage: JOY turns to WOE

   JOY "What was that?"

   menu:
   WOE

   "The dumbest pair of animals in the kingdom"
   $ choice = chocies['scene4'] = 'sid'
   JOY "There should be an award for that right? hide sprite_JOY_happy"
   jumpscene4_common

   "The happiest pair of animals in the kingdom"
   $ choice = choices['scene4'] = 'sid'
   JOY "Yeah, they're cute and deserve each other. hide sprite_JOY_happy"
   jumpscene4_common

   JOY "Who needs a date whenyou get to bear witness to true love like that?"

   #show sprite_JOY_neutral with exit_right
