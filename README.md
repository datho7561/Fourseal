# Fourseal

## ABOUT

This is a bird's eye view action game where you play as one of three sword wielding classes.

Eventually, I intend for it to be a multiplayer PVP game.

Right now, I have set up a demo, where you must defend the totem/obelisk in the center of the map from an onslaught of chess pieces.

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
__Q:__ Why am I a jubejube?

__A:__ Many of the images in the game are placeholders. I have worked on the back end of animating the characters, but haven't put in the time to create all the images needed to animate the characters. I expect that this will take some time for me to get around to.

## DEVELOPMENT

This game is currently incredibly rough around the edges:
* It contains bugs and exploits
    * Because directional isn't implemented yet, you can stand on the obelisk and hold attack
* It is very lacking in visual effects
* The HUD leaves a lot to be desired
* There are files of code which are written butuntested and not implemented in the main game

I currently intend to be working on it in my spare time for fun. I will do my best to push or release stable versions of this game when it gets to that stage.

If you are interested in what I have planned, please see `Decisions.txt` file or the `TODO:` notes scattered throughout the src.

## CURRENT BARRIERS FOR DEVELOPMENT

These are the issues I'm facing and why currently (20 Jan, 2019) I feel an inhibition to work on this at the moment.

 * The core concept isn't as fun as I expected it to be, at least with the features that are available now
    * I think fleshing out the special attacks, adding directional attacking, and adding better maps might help with this, but I'm not entirely sure
 * I don't have sufficient time or skill to complete the character pixel art
 * I need to redesign the main file in order to make it more maintainable
     * This means spending a decent amount of time planning how to do this
     * I will have to do a refactor, which will take a decent amount of coding
     * This is also necessary in order to make a better menu system and configurable matches (i.e. different maps)
 * I need to implement a good pathfinding algorithm for the enemies
     * I have read a bit about A* with path smoothing and Theta* but need to read more in order to understand them and implement them
 * I need to make a custom key mapping system and figure out the default mappings for up to 4 players

## MAP FILES

I am working on creating a specific standard for the map file, so that it will be easy for anyone to create their own maps for the game.  The file `MapFilePlanning.txt` has some information. As of right now, many of the features described in that map are not yet implemented. (Only the background and foreground are actually read into the game). Also of note is the file `MapGenerator.py`, which I use to help me create maps to test on.