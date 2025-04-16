# **RPS**
#### Video Demo:  [-](-)
#### Description:
RPS is a tiny Rock, Paper, Scissors game. Player combats PC in a "battle".

**DATA STORAGE**

Application do not store any data.

**THE MAIN FUNCTION**

The main function serves as central hub for RPS game.
Calls main_menu() function to display main menu of the game.
RPS uses simple user menu, with three basic options, placed in an infinite loop. 

It allows user to:
1. Play,
2. Rules, 
3. Quit.

**Case 1**: user calls play_game() function.

**Case 2**: user calls display_rules() function.

**Case 3**: user terminates the program.

The game uses loops and exceptions to validate users input.

**THE play_game() FUNCTION**

The search_planet() function enables users to choose which type of "weapon" they want to "equip" against the "enemy".
After the decision computer randomly chooses his "weapon".
Function checks which player won the battle and annouces outcome.
Game repeats until player quits.

**THE display_rules() FUNCTION**

The display_rules() function prints out rules of the game.

**HOW TO COMPILE**
1. Open terminal window.
2. Go to Solaris directory.
3. Run: python rps.py
