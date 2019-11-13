# Import of Dependencies
import pygame
import sys

# Initialises PyGame and sets variables.
pygame.init()
pygame.mouse.set_visible(1)  # Makes the mouse visible on display.
running = True

# Screen GUI
screenHeight = 720
screenWidth = 1280
screenColor = (255, 229, 204)
menuScreen = pygame.display.set_mode((screenWidth, screenHeight))  # Sets the display to given variables
menuScreen.fill(screenColor)  # Fills display with passed color variable
pygame.display.update()  # Updates the PyGame display to remain up-to-date

class Title:
    """Static Variables for the font of text"""
    fontColor = (0, 0, 0)
    font = pygame.font.SysFont('Roboto', 60)

    def __init__(self, content, surface,):
        """Dynamic text variable for each instance"""
        self.content = content
        self.surface = surface

    def render(self):
        """Function to render text and blit it onto the display."""
        textRender = self.font.render(self.content, False, self.fontColor)
        menuScreen.blit(textRender, self.surface)
        pygame.display.update()


# Text Class Template
class Text:
    """Static Variables for the font of text"""
    fontColor = (0, 0, 0)
    font = pygame.font.SysFont('Roboto', 36)

    def __init__(self, content, surface,):
        """Dynamic text variable for each instance"""
        self.content = content
        self.surface = surface
        Title.__init__(self, content, surface)

    def render(self):
        """Function to render text and blit it onto the display."""
        textRender = self.font.render(self.content, False, self.fontColor)
        menuScreen.blit(textRender, self.surface)
        pygame.display.update()


class Title(Text):
    font = pygame.font.SysFont('Roboto', 10)


class Blurb(Text):
    pass

class Label(Text):
    pass


# Button Class template
class Button:
    """Static button variables for all buttons"""
    color = (192, 192, 192)
    height = 225
    width = 400
    surface = menuScreen

    def __init__(self, xPosition, yPosition):
        """Constructor with dynamic variables."""
        self.xPosition = xPosition
        self.yPosition = yPosition

    def drawRec(self):
        """Draws the rectangle and updates surface display."""
        pygame.draw.rect(menuScreen, self.color, (self.xPosition, self.yPosition, self.width, self.height))
        pygame.display.update()


# Creates instances of buttons and sets their x, y positions
mazebutton = Button(150, 250)
tttbutton = Button(700, 250)

# Calls upon the drawRec method to draw the instances of buttons.
mazebutton.drawRec()
tttbutton.drawRec()

# Defining instances of text.
title = Title("Specification 4", (400, 100))
mazebuttontext = Text("Maze Generator.", (200, 300))
tttbuttontext = Text("Tic-Tac-Toe.", (750, 300))
descriptionl1 = Text("We have used PyGame to demonstrate a variation of skills.", (210, 550))
descriptionl2 = Text("The Maze button will start an instance of the maze game.", (215, 600))
descriptionl3 = Text("The Tic-Tac-Toe button will start an instance of the game.", (215, 650))

# Calls upon the render method to render instances of text.
title.render()
mazebuttontext.render()
tttbuttontext.render()
descriptionl1.render()
descriptionl2.render()
descriptionl3.render()

# Updates PyGame display at the end to keep things up-to-date.
pygame.display.update()

# Loop to close the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos)
