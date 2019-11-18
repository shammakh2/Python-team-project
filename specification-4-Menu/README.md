# Menu
#### Introduction
The Menu is developed using python in PyCharm. Its purpose is to allow the user to navigate into the Maze.py file in
order to play the game.

Please note, the menu.py file is located in the specification-4 directory.

##### Dependecies
The Menu.py file uses 2 main libraries in order to function. These are:
1. Sys
2. PyGame

Whilst the Sys library is not necessary it allows us to close the game display via the red cross on the top right of the window.

### Outline
The Menu works off a set of screen variables to define the GUI display. It also uses the built-in functionality of
pygame to draw rectangles which become our button.

The button is styled and has text displayed in the same location to provide the rectangle with a label.
The file uses class inheritance to define a text class and several subclasses for titles, labels and a description.

Finally, there is a while loop which has if statements in order to change the style of the rectangle when you hover over
it. Furthermore, it has functionality to open the Maze.py file when the rectangle is clicked upon by the user.
