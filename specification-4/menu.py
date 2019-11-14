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
screenColor = (192, 192, 192)
menuScreen = pygame.display.set_mode((screenWidth, screenHeight))  # Sets the display to given variables
menuScreen.fill(screenColor)  # Fills display with passed color variable
pygame.display.update()  # Updates the PyGame display to remain up-to-date

# Defining Rectangle variables
rectWidth = 400
rectHeight = 225
rectColor = (255, 255, 255)
surface = menuScreen

# Drawing rectangles
mazebutton = pygame.draw.rect(surface, rectColor, (150, 250, rectWidth, rectHeight))
tttbutton = pygame.draw.rect(surface, rectColor, (700, 250, rectWidth, rectHeight))


# Updates PyGame display
pygame.display.update()


# Text Class Template
class Text:
    """Static Variables for the font of text"""
    fontColor = (0, 0, 0)
    font = pygame.font.SysFont('Roboto', 10)

    def __init__(self, content, surface):
        """Dynamic text variable for each instance"""
        self.content = content
        self.surface = surface

    def render(self):
        """Function to render text and blit it onto the display."""
        textRender = self.font.render(self.content, False, self.fontColor)
        menuScreen.blit(textRender, self.surface)
        pygame.display.update()


# Child Classes of Text class
class Title(Text):  # Child class for a Title instances.
    font = pygame.font.SysFont('Roboto', 60)

    def __init__(self, content, surface):
        super().__init__(content, surface)


class Blurb(Text):  # Child class for Blurb/Description Instances.
    font = pygame.font.SysFont('Roboto', 28)

    def __init__(self, content, surface):
        super().__init__(content, surface)


class Label(Text):  # Child class for Label Instances.
    font = pygame.font.SysFont('Roboto', 48)

    def __init__(self, content, surface):
        super().__init__(content, surface)


# Defining instances of text.
title = Title("Specification 4", (400, 100))
mazebuttontext = Label("Maze Generator.", (200, 300))
tttbuttontext = Label("Tic-Tac-Toe.", (750, 300))
descriptionl1 = Blurb("We have used PyGame to demonstrate a variation of skills.", (210, 550))
descriptionl2 = Blurb("The Maze button will start an instance of the maze game.", (215, 600))
descriptionl3 = Blurb("The Tic-Tac-Toe button will start an instance of the game.", (215, 650))

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
            if mazebutton.collidepoint(pos):
                print("Pew!")
            elif tttbutton.collidepoint(pos):
                print("Pow!")
        elif event.type == pygame.MOUSEMOTION:
            if mazebutton.collidepoint(pygame.mouse.get_pos()):
                print("Test") 
            else:
                pass
        else:
            pass

