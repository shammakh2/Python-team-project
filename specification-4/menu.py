# Import of Dependencies
import pygame
import sys
import Maze

# Initialises PyGame and sets variables.
pygame.init()
pygame.mouse.set_visible(1)  # Makes the mouse visible on display.
running = True

# Screen GUI
screenHeight = 700
screenWidth = 1000
screenColor = (192, 192, 192)
menuScreen = pygame.display.set_mode((screenWidth, screenHeight))  # Sets the display to given variables
menuScreen.fill(screenColor)  # Fills display with passed color variable
pygame.display.update()  # Updates the PyGame display to remain up-to-date

# Defining Rectangle variables
rectWidth = 400
rectHeight = 200
rectColor = (125, 125, 125)
surface = menuScreen

# Drawing rectangles
mazebutton = pygame.draw.rect(surface, rectColor, (300, 250, rectWidth, rectHeight))

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
    font = pygame.font.SysFont('Roboto', 90)

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
title = Title("Specification 4", (280, 100))
mazebuttontext = Label("Maze Generator", (370, 330))
descriptionl1 = Blurb("We have used PyGame to demonstrate a new library.", (250, 550))
descriptionl2 = Blurb("Please click the 'Maze Generator' button to begin.", (260, 600))

# Calls upon the render method to render instances of text.
title.render()
mazebuttontext.render()
descriptionl1.render()
descriptionl2.render()

# Updates PyGame display at the end to keep things up-to-date.
pygame.display.update()

# Loop to update button
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if mazebutton.collidepoint(pos):

                pygame.display.set_caption('Maze Generator')
                pygame.quit()
                Maze.check_input_int(None, True)
        elif pygame.mouse.get_pos():
            pos1 = pygame.mouse.get_pos()
            status = False
            if mazebutton.collidepoint(pos1):
                if mazebutton != pygame.draw.rect(menuScreen, (255, 0, 0), (299, 249, 402, 202)):
                    mazebutton = pygame.draw.rect(menuScreen, (255, 0, 0), (299, 249, 402, 202))
                    mazebuttontext.render()
                    pygame.display.update()
            elif mazebutton != pygame.draw.rect(surface, rectColor, (300, 250, rectWidth, rectHeight)):
                mazebutton = pygame.draw.rect(surface, rectColor, (300, 250, rectWidth, rectHeight))
                mazebuttontext.render()
                pygame.display.update()



