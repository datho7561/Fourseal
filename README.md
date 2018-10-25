# Fourseal

## ABOUT

This is a top-down game where you play as one of four sword wielding classes (only 3 are implemented so far).

Eventually, I intend for it to be a multiplayer PVP game.

Right now, I have set up a demo, where you must defend the totem/obelisk in the center of the map from an onslaught of creatures.

If you are interested in trying it out, please refer to the RUNNING IT section. Have fun!

## CONTROLS

Use WASD to move, SPACE to attack, and SHIFT to use your special move. Each class has a different special, as well as different attack strengths and movement speeds.

## RUNNING IT

This game is written in python 3 with pygame, which means that to run it you will need these installed.
1. Installing Python
    * If you already have python, run `python --version` or `python3 --version` in a terminal or command prompt to make sure that you have python 3 installed
    * Otherwise, [download and run the installer for python 3](https://www.python.org/downloads/)
    * Make sure that python is added to the path so that you can run it in terminal or command prompt
2. Installing pygame
    * If you are on Mac/Linux, run `pip3 install pygame`
    * If you are on Windows, run `pip install pygame`
3. Launching the game:
    * In a command prompt/terminal, make sure that you are in the same folder as the downloaded source code
    * For Mac/Linux, run `python3 main.py`
    * For Windows, run `python main.py`
4. Character selection:
    * You will be prompted to enter a letter representing the class you pick before the game launches
    * Once you have done this, the game should have launched. Have fun!

## FAQ
__Q:__ Why am I an oddly-shaped shrubbery?

__A:__ You are, in fact, not a shrubbery, but a poorly drawn jubejube.

__Q:__ Why, then, am I a jubejube?

__A:__ Many of the images in the game are placeholders. I have worked on the back end of animating the characters, but haven't put in the time to create all the images needed to animate the characters. I expect that this will take some time for me to get around to.

## DEVELOPMENT

This game is currently incredibly rough around the edges:
* It probably contains bugs and exploits
* It is very lacking in visual effects
* The HUD leaves a lot to be desired
* Many things described in the source code are not implemented or only partially implemented

I currently intend to be working on it in my spare time for fun. I will do my best to push or release stable versions of this game when it gets to that stage.

If you are interested in what I have planned, please see `Decisions.txt` file or the `TODO:` notes scattered throughout the src. 

## MAP FILES

I am working on creating a specific standard for the map file, so that it will be easy for anyone to create their own maps for the game.  The file `MapFilePlanning.txt` has some information. As of right now, many of the features described in that map are not yet implemented. (Only the background and foreground are actually read into the game). Also of note is the file `MapGenerator.py`, which I use to help me create maps to test on.