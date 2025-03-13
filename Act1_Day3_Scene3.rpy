
# character definition

define j = Character("Joy")

define i = Character("Idiot")

define p = Character("Pompo")

define r = Character("")

define jo = Character("John")

# game start

label Act1_Day3_Scene3:

    #unsure of file names but I tried

    scene background_examroom

    show sprite_JOY_front with moveinleft

    show CharacterArt_Idiot with moveinright

    j "Aaaaaand there we go! All better!"

    i "Finally! If I have to miss another day of trading becuase of my kid's stupid pet, I'm gonna--"

    j "Okay! It's been a pleasure, sir! Have a great day."

    i "Humph"

    hide CharacterArt_Idiot with move

    pause 1.5

    show sprite_Pompo_front with moveinright 

    p "So I guess you've met IDOT eh? Yeah apparently that dog loves eating random stuff."

    j "Is that so..."

    r "*CRASH*!!!"

    p "Oh what the hell now?"

    jo "Hey Joy? Pompo? Can we get some help out here if you're not busy?"

    p "They're being so lazy aren't they? What's PetCheap paying them for if they're just gonna ask for our help anyway?"

    j "I'm gonna go help them out. The more help the better, right?"

    hide sprite_JOY_front with move

    p "Sure, sure."

    return
