import pygame
import math
import random

pygame.init()
wide = 50
win_x = (wide*20) + 3
win_y = (wide*20) + 3
screen = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Maze Generator')
grid = []

class Cell:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.sides = [True, True, True, True]
        self.visited = False
        self.x = self.col * wide
        self.y = self.row * wide

    def __str__(self):
        return f"I am Col {self.col} and Row {self.row}"

    def draw_cell(self):

        if self.visited == True:
            pygame.draw.rect(screen, (70, 70, 70, 255), self.loc())
        if self.sides[0]:
            pygame.draw.line(screen, (128,128,255), (self.x,self.y), (self.x+wide,self.y), 3) #Top
        if self.sides[1]:
            pygame.draw.line(screen, (128,128,255), (self.x + wide, self.y), (self.x + wide , self.y+wide), 3) #Right
        if self.sides[2]:
            pygame.draw.line(screen, (128,128,255), (self.x, self.y+wide), (self.x + wide, self.y + wide), 3) #Bottom
        if self.sides[3]:
            pygame.draw.line(screen, (128,128,255), (self.x, self.y), (self.x, self.y + wide), 3) #Left


    def loc(self):
        return (self.x, self.y, wide,wide)

    def find_neighbor(self):
        self.neighbor = []
        for all in grid:
            if all.x >= 0 and all.y >= 0 and all.x <= win_x and all.y <= win_y:
                if (all.col == self.col + 1 and  all.row == self.row) or (all.col == self.col - 1 and all.row == self.row) or (all.col == self.col and  all.row == self.row + 1) or (all.col == self.col and  all.row == self.row - 1):
                    if all.visited != True:
                        self.neighbor.append(all)
        if len(self.neighbor) > 0:
            return random.choice(self.neighbor)


def main ():
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))

    num_row = math.floor(win_y/wide)
    num_col = math.floor(win_x/wide)
    stack = []

    for y in range(0,num_row):
        for x in range(0,num_col):
            grid.append(Cell(x,y))
    for cell in grid:
        cell.draw_cell()
    current = grid[0]

    while True:
        pygame.time.Clock().tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(background, (0,0))
        next_cell = current.find_neighbor()
        if current.visited:
            pygame.draw.rect(screen, (255, 255, 150, 100), current.loc())
        else:
            pygame.draw.rect(screen, (0, 0, 130, 100), current.loc())
        current.visited = True
        if next_cell is not None:
            if next_cell.visited == False:
                if next_cell.col - current.col == 1:
                    current.sides[1] = False
                    next_cell.sides[3] = False
                if next_cell.col - current.col == -1:
                    current.sides[3] = False
                    next_cell.sides[1] = False
                if next_cell.row - current.row == 1:
                    current.sides[2] = False
                    next_cell.sides[0] = False
                if next_cell.row - current.row == -1:
                    current.sides[0] = False
                    next_cell.sides[2] = False
                stack.append(current)
                current = next_cell
        else:
            if len(stack) > 0:
                current = stack.pop()


        pygame.display.flip()

if __name__ == '__main__':
    main()

