import pygame
import math
import random

pygame.init()
wide = 100
rows = 8
cols = 8
win_x = (wide*cols) + 3
win_y = (wide*rows) + 3
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
    def char_size(self):
        return (self.x + 2 , self.y +2, wide-3,wide-3)

    def find_neighbor(self):
        self.neighbor = []
        for all in grid:
            if all.x >= 0 and all.y >= 0 and all.x <= win_x and all.y <= win_y:
                if (all.col == self.col + 1 and  all.row == self.row) or (all.col == self.col - 1 and all.row == self.row) or (all.col == self.col and  all.row == self.row + 1) or (all.col == self.col and  all.row == self.row - 1):
                    if all.visited != True:
                        self.neighbor.append(all)
        if len(self.neighbor) > 0:
            return random.choice(self.neighbor)

class player:
    def __init__(self, x, y, col, row):
        self.x = x
        self.y = y
        self.col = col
        self.row = row

    def char_size(self):
        return (self.x + 3, self.y + 3, wide - 6, wide - 6)



def main ():
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))

    game_loading = True
    game_start = False
    stack = []
    visited = 1
    loop_de_loop = []
    for y in range(0,rows):
        for x in range(0,cols):
            grid.append(Cell(x,y))
    for cell in grid:
        loop_de_loop.append(cell.draw_cell)
    current = grid[0]

    # def player_up():


    while True:
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if pygame.K_UP or pygame.K_w:

                if pygame.K_DOWN or pygame.K_s:

                if pygame.K_LEFT or pygame.K_a:

                if pygame.K_RIGHT or pygame.K_d:
        screen.blit(background, (0,0))
        next_cell = current.find_neighbor()
        for x in loop_de_loop:
            x()
        if game_loading == True and game_start == False:
            if current.visited:
                pygame.draw.rect(screen, (255, 255, 150, 100), current.char_size())

            else:
                pygame.draw.rect(screen, (130, 130, 255, 100), current.char_size())
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
                    visited += 1
            else:
                if len(stack) > 0:
                    current = stack.pop()
            if visited == rows*cols and current == grid[0]:
                game_loading = False
                game_start = True
        if game_loading == False and game_start == True:
            player_is_born_in_this_foreign_land = player(current.x, current.y)
            pygame.draw.rect(screen, (77, 255, 136, 100), player_is_born_in_this_foreign_land.char_size())



        pygame.display.update()

if __name__ == '__main__':
    main()

