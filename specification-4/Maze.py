import pygame
import random

pygame.init()
wide = 50
rows = 10
cols = 10
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
        self.neighbor = []

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
        return self.x, self.y, wide, wide
    def char_size(self):
        return self.x + 2 , self.y + 2, wide - 3, wide - 3

    def find_neighbor(self):
        self.neighbor = []
        for all in grid:
            if 0 <= all.x <= win_x and 0 <= all.y <= win_y:
                if (all.col == self.col + 1 and  all.row == self.row) or (all.col == self.col - 1 and all.row == self.row) or (all.col == self.col and  all.row == self.row + 1) or (all.col == self.col and  all.row == self.row - 1):
                        self.neighbor.append(all)


    def find_next(self):
        self.next_possible = []
        for ob in self.neighbor:
            if not ob.visited:
                self.next_possible.append(ob)
        if len(self.next_possible) > 0:
            return random.choice(self.next_possible)

class player:
    def __init__(self, current):
        self.__on_cell = current

    def __str__(self):
        return f"This is on {self.__on_cell.col} and {self.__on_cell.row}"

    def loc_set(self, current):
        self.__on_cell = current

    def loc_get(self):
        return self.__on_cell

    def movement_up(self):
        for x in self.__on_cell.neighbor:
            if x.col == self.__on_cell.col and x.row == self.__on_cell.row - 1:
                if self.__on_cell.sides[0] is False:
                    self.__on_cell = x


    def movement_down(self):
        for x in self.__on_cell.neighbor:
            if x.col == self.__on_cell.col and x.row == self.__on_cell.row + 1:
                if self.__on_cell.sides[2] is False:
                    self.__on_cell = x
                    print(f"x: {self.__on_cell.x}  y: {self.__on_cell.y}")
                    print('down')



    def movement_left(self):
        for x in self.__on_cell.neighbor:
            if x.row == self.__on_cell.row and x.col == self.__on_cell.col - 1:
                if self.__on_cell.sides[3] is False:
                    self.__on_cell = x


    def movement_right(self):
        for x in self.__on_cell.neighbor:
            if x.row == self.__on_cell.row and x.col == self.__on_cell.col + 1:
                if self.__on_cell.sides[1] is False:
                    self.__on_cell = x
                    print('right')

    





def main ():
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    game_loading = True
    game_start = False
    press_time = 0
    stack = []
    visited = 1
    loop_de_loop = []
    for y in range(0,rows):
        for x in range(0,cols):
            grid.append(Cell(x,y))
    for cell in grid:
        cell.find_neighbor()
        loop_de_loop.append(cell.draw_cell)
    current = grid[0]
    player_is_born_in_this_foreign_land = player(current)
    pygame.key.set_repeat(5)
    while True:
        pygame.time.Clock().tick(15)
        if press_time > 0:
            press_time += 1
        if press_time > 5:
            press_time = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and press_time == 0:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_is_born_in_this_foreign_land.movement_up()
                    current = player_is_born_in_this_foreign_land.loc_get()

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player_is_born_in_this_foreign_land.movement_down()
                    current = player_is_born_in_this_foreign_land.loc_get()

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player_is_born_in_this_foreign_land.movement_left()
                    current = player_is_born_in_this_foreign_land.loc_get()

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player_is_born_in_this_foreign_land.movement_right()
                    current = player_is_born_in_this_foreign_land.loc_get()


        screen.blit(background, (0,0))
        next_cell = current.find_next()
        for x in loop_de_loop:
            x()
        if game_loading is True and game_start is False:
            if current.visited:
                pygame.draw.rect(screen, (255, 255, 150, 100), current.char_size())
            else:
                pygame.draw.rect(screen, (130, 130, 255, 100), current.char_size())
            current.visited = True
            if next_cell is not None:
                if not next_cell.visited:
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
        if game_loading is False and game_start is True:
            pygame.draw.rect(screen, (77, 255, 136, 100), (current.x, current.y, wide, wide ))

        pygame.display.update()

if __name__ == '__main__':
    main()

