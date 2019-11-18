<h1>Backtracking Maze Generator</h1>

<h4>1.Introduction</h4>
This program made as a part of specification 4 is a depth first maze generator game.
You can launch up the file using the following code in the specification 4 directory

    python Maze.py
    
The program will use a head pointer to carve out a random path in the grid every time.

***Note:** It will take a longer time to generate larger mazes*

<h4>Player and the Goal</h4>
Once the maze is generated, the head pointer will return back to the top left corner of the screen
and change to green color.

When it turns green, it is time to play.
The goal for you is to guide the head pointer to red marked square on the bottom right corner of the 
screen to win the game.

<h6> Controls </h6>

`Move up    =  UP Arrow key or "w" key`

`Move down  =  DOWN Arrow key or "s" key`

`Move left  =  LEFT Arrow key or "a" key`

`Move right =  RIGHT Arrow key or "d" key`

<h4> Configuration and Extra functionality</h4>

<h5> The Menu </h5>
Bring your cursor over to the top left corner of the screen and you will find a menu button. 

Clicking the menu button will give you the following options:

<h6> Pause the program </h6>

To pause the program, press the first button ( "▶" button) and it will stop the generator.

<h6> The settings menu </h6>
The second button ( "⚙" button) will lead you to the settings

In the settings menu, you can change the Resolution X (width) and Resolution Y (height) of the screen in pixels.
You can also add the number rows and columns and the width (in pixels) of the cells.

Pressing Save will reload the generator with all your inputs
If you leave all the inputs empty, it will load the best possible settings for your system.

If you press the Close button, it will close the settings menu.

***Note:** All values in settings are optional. If you leave some values empty or enter wrong values. The program will
give priority to your entered values and set the others to the best possible for your system or default values.

<h6> Quit button </h6>
Pressing the Quit button will quit the game.

