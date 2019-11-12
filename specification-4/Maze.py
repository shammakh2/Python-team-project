import pygame
import math

pygame.init()
wide = 60
win_x = (wide*10) + 1
win_y = (wide*10) + 1
screen = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Maze Generator')
grid = []

class Cell:
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def draw_cell(self):
        x = self.col * wide
        y = self.row * wide

        pygame.draw.line(screen, (255,0,0), (x,y), (x+wide,y))
        pygame.draw.line(screen, (255, 0, 0), (x + wide, y), (x + wide , y+wide))
        pygame.draw.line(screen, (255, 0, 0), (x, y+wide), (x + wide, y + wide))
        pygame.draw.line(screen, (255, 0, 0), (x, y), (x, y + wide))

def main ():
    background = pygame.Surface(screen.get_size())
    background.fill((80,80,80))

    num_row = math.floor(win_y/wide)
    num_col = math.floor(win_x/wide)

    for y in range(0,num_row):
        for x in range(0,num_col):
            grid.append(Cell(x,y))



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(background, (0,0))
        for cell in grid:
            cell.draw_cell()
        pygame.display.flip()

if __name__ == '__main__':
    main()

