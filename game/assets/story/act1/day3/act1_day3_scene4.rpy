label act1_day3_scene4:

# replace scene when available

scene bg_PetCheap_ExamRoom

# first character

show sprite_JOY_exhausted

JOY "I'm exhuasted! One more thing and I swear to God--"

hide sprite_JOY_exhausted

show sprite_POMPO_smug

POMPO "Well look who it is! And here I thought today couldn't get any better."

hide sprite_POMPO_smug

show sprite_JOY_annoyed

JOY "Oh here we go..."

show sprite_JOY_front at left


show sprite_POMPO_smug at right

JOY "What have you got for me this time?"

POMPO "Oh, don't be like that! The other technicians are covering for me and I just finished uPOMPO with Glasha's client, so this time it's not about work."

show sprite_JOY_curious

JOY "And what is that?"

show sprite_POMPO_flirty

POMPO "There's this great coffee place in the plaza next door-- it has the best dark roast. Let's hang out after work and I'll take you there."

show sprite_JOY_flirty

JOY "You're... asking me out?"

show sprite_JOY_curious

show sprite_POMPO_smug

POMPO "Now we're getting the idea! Whaddya say?"

hide sprite_POMPO_smug

hide sprite_JOY_curious

show sprite_JOY_front

JOY "This is a bad idea right? This is a terrible idea, right?"


$ choice = None # to store user choice

menu:

    "He's cute...":
        $ choice = "yes"

    "At least it's free.":
        $ choice = "sure"

    "Shoot him down.":
        $ choice = "no"

if choice == "yes":

    show sprite_JOY_flirty

    JOY "Bad JOY! Horny jail for you! Bad JOY!"

elif choice == "sure":

    show sprite_JOY_happy

    JOY "Okay fine! I'll try to pretend his ick has magically vanished for the next 60 minutes! But there's NO WAY I'm letting this go further than coffee!"

elif choice == "no":

    show sprite_JOY_sad

    JOY "You know this guy will just ask again! I'll just turn him down at the shoPOMPO while we talk. It'll be fineeeee!"


# Joy turns back to walk away

show sprite_JOY_front at left


show sprite_JOY_front

JOY "Looks like I'll see you after our shift."

show sprite_POMPO_happy at right

POMPO "Sounds like a plan!"



return
