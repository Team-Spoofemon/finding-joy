# Story
"Finding Joy"


## Overview
"Finding Joy" is an interactive visual short story. You play as JOY's inner voice, and as she interacts with coworkers, clients, and cute animals--you play as her inner voice, affecting her decisions and sparring with her conciousness. This short story represents a vertical slice proof of concept that a team of students from SJSU can come together and actually ship a game with equal parts of work and effort, tying together disciplines like visual art, music, story, and programming.


## Perspective
- perspective: 3rd person omniscient
    - JOY talks in 1st person with the player
    - JOY talks in 3rd person with other characters


## Characters
- main
    - JOY - mid 20s, titular character of the story
    - WOE - the player character, JOY's inner voice, attempts to influence JOY
- side
    - SID - mid 20s, vet tech coworker, has an attitude matching that of a punchable face, date scene available
    - FAITH - mid 20s, client, sweetheart wtih dreams, date scene available, sweet mannered, idealistic, androgynous
        - BISCUITS - a mutt cat, has a big welt in their chest
    - KELLY - mid 20s, client, always on the phone, sweet when talking in person, angry when on the phone, woman-coded
        - BUTTER - a golden retriever, has a big splinter in their paw
    - DOPEY - mid 20s, client, a derpy human, dumb as rocks, (think drooling, cross-eyed like [this](../../../misc/derpy-1.png) or [that](../../../misc/derpy-2.png)), unaware of whats happening around them, male-coded
        - GRAVY - a derpy dog, has something comically big stuck in its neck (its not in severe pain tho)
- aux
    - SHOPKEEPER - mid 20s, shopkeeper of the coffee shop



## Emotions (some relevant per character, not all)
- people
    - 4 basic emotions:
        1. happy
        2. sad
        3. fear
        4. angry
    - 4 states:
        1. neutral
        2. thinking - https://emojipedia.org/face-with-raised-eyebrow
        3. tired
        4. surprised
- animals
    - happy
    - distressed (whatever illness aflicts them)


## Plot - Synopsis
- scene 1: JOY arrives at reception, runs into KELLY, solves their pet issue
- scene 2: JOY sees FAITH, solves their pet issue
- scene 3: JOY enters break room, SID suggests JOY should go out on a date, choses between asking SID, FAITH, or refusing
- scene 4a: JOY and SID, coffee shop, date scene, guaranteed ends poorly
- scene 4b: JOY and FAITH, coffee shop, date scene, guaranteed ends well
- scene 4c: JOY enters the operating table, sees DOPEY, solves their pet issue
- scene 5a: JOY enters bedroom, they found joy in turning SID down and having values
- scene 5b: JOY enters bedroom, they found joy in the optimisim in other people
- scene 5c: JOY enters bedroom, they found joy in doing the thing they love


## Settings
- Notes:
    - each location has the perspective of "onto", where both characters are in the frame and the location exists between the two characters.
- Locations:
    - PetCheap_FrontDesk - front desk of a vet clinic, see [vet desk](../../../misc/pet-desk.jpg)
    - PetCheap_OperatingTable - operating table of a vet clinic with kennels, see [vet table](../../../misc/vet-table.avif)
    - PetCheap_BreakRoom - a small office breakroom with a coffee pot and some keurig cups, see [break room](../../../misc/break-room.jpg)
    - CoffeeShop - a coffee shop looking at a table (for a date scene), see [coffee shop](../../../misc/coffee-shop.jpeg)
    - JoyHouse_Bedroom - a bedroom that a single woman might have, see [womans bedroom](../../../misc/womans-bedroom.jpeg)



## Mechanics:
- the last spoken dialogue should still display for the player, see [line 189 in templates](../../../game/assets/story/templates/actX_dayX_scene_X.rpy)
- JOY turns to WOE: desaturate the background and have JOY face the player with an appropriate facial expression, see [line 174 in templates](../../../game/assets/story/templates/actX_dayX_scene_X.rpy)
- animation and dialogue should be at the quality of [act1_day3_scene1](../../../game/assets/story/_old/act1/day3/act1_day3_scene1.rpy) for the animations, placement, pacing and [act1_day3_scene5](../../../game/assets/story/_old/act1/day3/act1_day3_scene5.rpy) for the choices


## Music
- menu music
- atomsphere per scene, things like a veterinarian office or a coffee shop, etc. (creative commons also fine)


# Needed Assets:
- music:
    - can we get some folley? things like a veterinarian office or a coffee shop, or that kind of thing?
        - recordings as well (creative commons)
    - maybe a leitmotif for every scenario? so scene 1, 2, 3, 4, 5 all get leitmotifs? (even if that's just a retrograde or inversion or harmony)


## Planning:
- programming / story:
    - 1, 3 unique and sets up the choice, do scene 3 first, scene 1 last
    - 4a / 4b are the same idea, a dating scene that goes badly or well
    - 2 / 4c are the same idea, seeing a client and fixing their animal
    - 5a,b,c is different depending on the choice
- music
    - atmosphere
        - scene 1, 3 - office sounds, photocopier noises, telephone ringing, coffee pots, boiling water
        - scene 2/4c - hospital sounds like beeps, tools clacking on metal, curtains being drawn
        - scene 5a,b,c - evening sounds like crickets or a fireplace
- art:
    - hannah
        - characters
            - JOY based on [sprite_JOY_front](../../../game/assets/characters/JOY/sprite_JOY_front.png)
                - 4 basic emotions:
                    1. happy
                    2. sad
                    3. fear
                    4. angry
                - 4 states:
                    1. neutral - change the current image to "neutral"
                    2. thinking - https://emojipedia.org/face-with-raised-eyebrow
                    3. tired
                    4. surprised
                - clothing
                    - formal (low priority)
            - FAITH based on [sprite_FAITH_front](../../../game\assets\characters\FAITH\sprite_FAITH_front.png) which will be renamed to `sprite_FAITH_happy`
                - thinking
                - neutral
            - BISCUITS
                - distress based on [sprite_BISCUITS_worried](../../../game\assets\characters\FAITH\BISCUITS\sprite_BISCUITS_worried.png), make the welt BIG
            - KELLY based on [sprite_KELLY_front](../../../game\assets\characters\KELLY\sprite_KELLY_front.png)
                - happy - remove the `kelly` name tag
                - angry - make her expression LIVID even exaggerated
    - lee
        - backgrounds:
            - PetCheap_BreakRoom - a small office breakroom with a coffee pot and some keurig cups, see [break room](../../../misc/break-room.jpg)
            - JoyHouse_Bedroom - a bedroom that a single woman might have, see [womans bedroom](../../../misc/womans-bedroom.jpeg)
        - characters
            - BUTTER - a golden retriever
                - happy
                - distressed (has a BIG splinter in their paw)
            - DOPEY - mid 20s, client, a derpy human, dumb as rocks, (think drooling, cross-eyed like [this](../../../misc/derpy-1.png) or [that](../../../misc/derpy-2.png)), unaware of whats happening around them, male-coded
                - neutral ONLY (they only have one expression)
            - GRAVY - a derpy dog, has something comically big stuck in its neck (its not in severe pain tho)
                - happy - in this case, just the same dog smiling without the hiliarios neck (also their neck is really thin?)


## Nice to Haves:
- custom character background text image (each Character(window_background))
- "wiggle" / "bounce" animation
    - every time a character talks, make sure the sprite wiggles to show they're doing something
- when joy gets close to an animal and "fixes" them, the two sprites need to jiggle together to portray activity
- music
    - 4 emotions music, especially angry when something angry happens it would be good to have a "tense" music playing
    - maybe a leitmotif for every scenario? so scene 1, 2, 3, 4, 5 all get leitmotifs? (even if that's just a retrograde or inversion or harmony)
    - folley for specific moments like taking a splinter out of a paw, sitting down at a coffee shop, etc.
- misc:
    - game icon - `config.window_icon` + `icon.ico/icon.icns` which needs to be copied into the build folders 1 level up
    - splash screen
    - menu card (lee)
    - credits / about text
    - custom gui?
