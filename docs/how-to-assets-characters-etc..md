# HOW TO: Assets, Characters, Etc.
This guide will use the github website to make commits. If you're using the command line, read the gui sections with the understanding that you will translate those instructions into commands.


# How do I make a new character?

- Overview: Create a new rpy file for that character, upload some assets in that same folder, add some variable names for that character in the new file, edit the character doc, youre done!

- Detailed Guide:
    1. First come up with an idea for a character, lets make a new one called `Everest`. For this new character, replace `EVEREST` and `everest` in all of the following links.
    2. Go to the [characters page](https://github.com/Team-Spoofemon/finding-joy/new/main/game/assets/characters)
        - in the upper right hand corder, click "Add file" > Create New File
        - Where it says "Name your file..." type `EVEREST/EVEREST.py`. This will cause a folder to be created and a file.
        - click the green "Commit changes" button
        - Give the "branch name" something meaningful like "creating-character-everest"
        - this file is basically a manifest of images, music, names, and other variable names so that the rest of the project can use them.
        - the reason why this works is `Ren'Py` loads all `.rpy` files at runtime, and any defined variables, music, images are accessible in any other `.rpy` files.
    3. FOR THE REST OF THESE LINKS, change the "main" to the name of your new branch!
    3. Go to the [the character doc](https://github.com/Team-Spoofemon/finding-joy/blob/new-branch-name/game/assets/characters/characters-design-doc.md)
        - SWITCH TO YOUR BRANCH!!! In the upper left hand corner next to the file path, click the dropdown and select the branch you just created.
        - In the upper right hand corner, click on the pencil to edit.
        - Since this is a new character, make sure to give it some basic description.
    4. Go back to the new file you've made, in this case [EVEREST/EVEREST.rpy](https://github.com/Team-Spoofemon/finding-joy/new/new-branch-name/game/assets/characters/EVEREST/EVEREST.rpy)
        - fill its contents like this:
        ```ren'py
        define EVEREST = Character("Everest", color="#c8ffc8")
        define music_EVEREST_theme = "assets/characters/EVEREST/music_EVEREST_theme.ogg"
        image sprite_EVEREST_normal = "assets/characters/EVEREST/sprite_EVEREST_normal.png"
        ```
    5. [Upload new images or music](https://github.com/Team-Spoofemon/finding-joy/upload/new-branch-name/game/assets/characters/EVEREST)
        - the file conventions are:
        - Character pictures `sprite_CHARACTER_emotion.png` - where `CHARACTER` is changable and `emotion` is changable.
        - Character themes `music_CHARACTER_theme.png` - where `CHARACTER` is changable and `theme` is changable to other things like `jingle` or `sadtheme`.


# How do I make a new image for this character?
1. Create some art!
2. Go to the character folder like [EVEREST](https://github.com/Team-Spoofemon/finding-joy/tree/main/game/assets/characters/EVEREST) and right click add files.
    - go ahead and upload those file
    - MAKE SURE WHATEVER FILES YOU UPLOAD HAVE A CODE DEFINITION IN THE CHARACTER FILE!



# How do I make background art?
1. Create some art!
2. Go to the [background folder](https://github.com/Team-Spoofemon/finding-joy/main/game/assets/background) and right click add files.
    - go ahead and upload those file
    - MAKE SURE WHATEVER FILES YOU UPLOAD HAVE A CODE DEFINITION IN THE CHARACTER FILE!
3. NOW YOU HAVE A NEW BRANCH NAME, so edit the link and replace "main" with your branch name.
4. Edit the [background.rpy](https://github.com/Team-Spoofemon/finding-joy/main/game/assets/background/background.rpy)
    - add a new line for the background you uploaded.
    - the convention is `bg_LOCATION_SUBLOCATION.png` - where `LOCATION` is changable and `SUBLOCATION` is changable to things like `interior`, `exterior`.
