import pygame

win_x = 600
win_y = 600
wide = 60
grid = []

class Cell:
    def __init__(self, col, row):
        self.col = col
        self.row = row
def main ():
    pygame.init()
    screen = pygame.display.set_mode((win_x, win_y))
    pygame.display.set_caption('Maze Generator')
    background = pygame.Surface(screen.get_size())
    background.fill((80,80,80))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == '__main__':
    main()

