# character definitions

define j = Character("Joy")

define p = Character("Pompo")


#game start

label scene_50_lol:

# replace scene when available

scene bg placeholder

# first character
# replace when available

show joy exhausted

j "I'm exhuasted! One more thing and I swear to God--"

hide joy exhuasted

show pompo smug

p "Well look who it is! And here I thought today couldn't get any better."

hide pompo smug

show joy annoyed

j "Oh here we go..."

show joy front at left


show pompo smug at right

j "What have you got for me this time?"

p "Oh, don't be like that! The other technicians are covering for me and I just finished up with Glasha's client, so this time it's not about work."

show joy curious

j "And what is that?"

show pompo flirty

p "There's this great coffee place in the plaza next door-- it has the best dark roast. Let's hang out after work and I'll take you there."

show joy flirty

j "You're... asking me out?"

show joy curious

show pompo smug

p "Now we're getting the idea! Whaddya say?"

hide pompo smug

hide joy curious

show joy frontfacing

j "This is a bad idea right? This is a terrible idea, right?"


$ choice = None # to store user choice

menu:

    "He's cute...":
        $ choice = "yes"

    "At least it's free.":
        $ choice = "sure"

    "Shoot him down.":
        $ choice = "no"

if choice == "yes":

    show joy flirty

    j "Bad JOY! Horny jail for you! Bad JOY!"

elif choice == "sure":

    show joy happy

    j "Okay fine! I'll try to pretend his ick has magically vanished for the next 60 minutes! But there's NO WAY I'm letting this go further than coffee!"

elif choice == "no":

    show joy sad

    j "You know this guy will just ask again! I'll just turn him down at the shop while we talk. It'll be fineeeee!"

jump continue_game

label continue_game:

# Joy turns back to walk away

show joy walkingleft at left


show joy walkingback

j "Looks like I'll see you after our shift."

show pompo happy at right

p "Sounds like a plan!"



return
