import pygame
import random

wide = 40
rows = 15
cols = 15
win_x = 700
win_y = 700
screen = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Maze Game and Generator')
grid = []

pygame.init()

class Cell:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.sides = [True, True, True, True]
        self.visited = False
        self.x = self.col * wide + ((win_x) - (cols * wide))/2
        self.y = self.row * wide + ((win_y) - (rows * wide))/2
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

class mena:
    def __init__(self):
        self.open = False
        self.open_ready = False
        self.big_open = False
        self.pos = -50
        self.alpha = 20
        self.big_pos = 0
        self.pause = False
        self.typin = False

class settin:
    def __init__(self,surface, x, y, wid, hgt, label):
        self.input = ''
        self.Surface = surface
        self.color_inactive = (255, 0, 0)
        self.color_active = (0, 0, 255)
        self.active = False
        self.x = x
        self.y = y
        self.wid = wid
        self.label = label
        self.hgt = hgt
        self.rect = pygame.Rect(x,y,wid,hgt)

    def render(self):
        if self.active == False:
            color = self.color_inactive
        elif self.active == True:
            color = self.color_active
        return pygame.draw.rect(self.Surface, color, self.rect, 4)

    def lable_rend(self):
        return pygame.font.Font('unifont.ttf', 17).render(self.label, True, (0,0,0))

def main ():
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    game_loading = True
    game_start = False
    press_time = 0
    stack = []
    visited = 1
    loop_de_loop = []
    open = mena()
    font = pygame.font.Font('unifont.ttf', 20)
    adjust_font = pygame.font.Font('unifont.ttf', 17)
    readjust_font = pygame.font.Font('unifont.ttf', 12)
    big_menu = pygame.Surface((win_x + 60, win_y + 60))
    res_x = settin(big_menu, 130, 250, 80, 30, 'Resolution x')
    res_y = settin(big_menu, 130, 350, 80, 30, 'Resolution y')
    col_create = settin(big_menu, 300, 300, 80, 30, 'Column Number')
    row_create = settin(big_menu, 300, 400, 80, 30, 'Row Number')
    cell_sizl = settin(big_menu, 130, 450, 80, 30, 'Cell width')

    def menu(mous, mousp):
        mouse = pygame.mouse.get_pos()
        surface2 = pygame.Surface((50,120))
        surface2.set_alpha(200)
        menu_surf = pygame.Surface((40,40))
        menu_surf.set_alpha(open.alpha)
        menu_settings_surf = pygame.Surface((40,40))
        menu_pause_surf = pygame.Surface((40, 40))
        menu_quit_surf = pygame.Surface((40, 40))
        text = font.render(u'\u2630', True, (255,255,255))
        big_exit = font.render('Exit', True, (0, 0, 0))
        pause_text = font.render('▶', True, (255,255,255))
        settings = adjust_font.render('⚙', True, (255,255,255))
        power = readjust_font.render('⏻', True, (255,255,255))
        if open.open_ready == True and 0 < mouse[0] <= 40 and 0 < mouse[1] < 40:
            pygame.draw.rect(menu_pause_surf, (128,128,255), pygame.Rect(0, 0, 40, 40))
        if open.open_ready == True and 0 < mouse[0] <= 40 and 40 < mouse[1] < 80:
            pygame.draw.rect(menu_settings_surf, (128,128,255), pygame.Rect(0, 0, 40, 40))
        if open.open_ready == True and 0 < mouse[0] <= 40 and 80 < mouse[1] < 120:
            pygame.draw.rect(menu_quit_surf, (255, 50, 50), pygame.Rect(0, 0, 40, 40))
        button_on_liddle_menu = pygame.Surface(big_menu.get_size(), pygame.SRCALPHA)
        big_menu.fill((255,255,255))
        big_menu.set_alpha(155)
        pygame.draw.rect(surface2, (50, 50, 50), pygame.Rect(0, 0, 50, 120))
        pygame.draw.rect(menu_surf, (130, 130, 130), pygame.Rect(0, 0, 40, 40))
        surface2.blit(menu_pause_surf, (10, 0))
        surface2.blit(pause_text, (22, 11))
        surface2.blit(menu_settings_surf, (10, 40))
        surface2.blit(settings, (19, 50))
        surface2.blit(menu_quit_surf, (10, 80))
        surface2.blit(power, (22, 90))
        screen.blit(surface2, (open.pos,0))
        menu_surf.blit(text, (10,8))
        screen.blit(menu_surf, (50 + open.pos, 40))
        res_x.render()
        big_menu.blit(res_x.lable_rend(), (20, 255))
        res_y.render()
        big_menu.blit(res_y.lable_rend(), (20, 355))
        col_create.render()
        big_menu.blit(col_create.lable_rend(), (180, 305))
        row_create.render()
        big_menu.blit(row_create.lable_rend(), (200, 405))
        cell_sizl.render()
        big_menu.blit(cell_sizl.lable_rend(), (20, 455))
        screen.blit(big_menu, (0, (win_y*-1 -50 + open.big_pos)))

        pygame.draw.rect(button_on_liddle_menu, (200, 50, 50), ((big_menu.get_rect()[2] - big_menu.get_rect()[2]*0.40) + (win_x - (cols * wide))/2, (big_menu.get_rect()[3] - big_menu.get_rect()[3]*0.25) + (win_y - (rows * wide))/2 , 80, 30))
        button_on_liddle_menu.blit(big_exit, (( 10 + big_menu.get_rect()[2] - big_menu.get_rect()[2]*0.40) + (win_x - (rows * wide))/2,
                                              (5 + big_menu.get_rect()[3] - big_menu.get_rect()[3]*0.25) + (win_y - (rows * wide))/2, 80, 30))
        screen.blit(button_on_liddle_menu, (0, (win_y * -1 - 50 + open.big_pos)))

        if 0 < mouse[0] <= 50 and 0 < mouse[1] < 120:
            if open.alpha < 155:
                open.alpha += 30
            if open.open == False and open.pos > -50:
                open.pos -= 10
        elif not 0 < mouse[0] <= 50 or not 0 < mouse[1] < 120:
            if open.alpha > 20:
                open.alpha -= 30
            open.open = False
            if open.open == False and open.pos > -50:
                open.pos -= 10
        if open.pos >= -10:
            open.open_ready = True
        if open.pos < -10:
            open.open_ready = False
        if open.open == True and open.pos < -10:
            open.pos += 10
        if open.big_open == True and open.big_pos < win_y:
            open.big_pos += 50
        elif open.big_open == False and open.big_pos > win_y*-1 -50:
            open.big_pos -= 50

        if mous != None and hasattr(mousp, 'button'):
            if mousp.button == 1:
                if 0 < mous[0] <= 50 and 0 < mous[1] < 120:
                    open.open = True
                if open.open_ready == True and 0 < mous[0] <= 40 and 0 < mous[1] < 40:
                    open.open = False
                    if open.pause == False:
                        open.pause = True
                        pygame.time.delay(10)
                    elif open.pause == True:
                        open.pause = False
                        pygame.time.delay(10)
                if open.open_ready == True and 0 < mous[0] <= 40 and 40 < mous[1] < 80:
                    open.big_open = True
                if open.open_ready == True and 0 < mous[0] <= 40 and 80 < mous[1] < 120:
                    pygame.quit()
                    main()
                if open.big_open == True and (10 + big_menu.get_rect()[2] - big_menu.get_rect()[2]*0.40) < mous[0] <= ( 10 + big_menu.get_rect()[2] - big_menu.get_rect()[2]*0.40) + 80 and (5 + big_menu.get_rect()[3] - big_menu.get_rect()[3]*0.25) < mous[1] < (5 + big_menu.get_rect()[3] - big_menu.get_rect()[3]*0.25) + 30:
                    open.big_open = False

                if open.big_open == True and 130 < mous[0] <= 210 and (250 + (win_y*-1 -50 + open.big_pos))< mous[1] <= 280 + (win_y*-1 -50 + open.big_pos):
                    res_x.active = True
                    res_y.active = False
                    col_create.active = False
                    row_create.active = False
                    cell_sizl.active = False
                if open.big_open == True and 130 < mous[0] <= 210 and (350 + (win_y*-1 -50 + open.big_pos))< mous[1] <= 380 + (win_y*-1 -50 + open.big_pos):
                    res_y.active = True
                    res_x.active = False
                    col_create.active = False
                    row_create.active = False
                    cell_sizl.active = False
                if open.big_open == True and 300 < mous[0] <= 380 and (300 + (win_y*-1 -50 + open.big_pos))< mous[1] <= 330 + (win_y*-1 -50 + open.big_pos):
                    col_create.active = True
                    res_x.active = False
                    res_y.active = False
                    row_create.active = False
                    cell_sizl.active = False
                if open.big_open == True and 300 < mous[0] <= 380 and (400 + (win_y*-1 -50 + open.big_pos))< mous[1] <= 430 + (win_y*-1 -50 + open.big_pos):
                    row_create.active = True
                    res_x.active = False
                    res_y.active = False
                    col_create.active = False
                    cell_sizl.active = False
                if open.big_open == True and 130 < mous[0] <= 210 and (450 + (win_y*-1 -50 + open.big_pos))< mous[1] <= 480 + (win_y*-1 -50 + open.big_pos):
                    cell_sizl.active = True
                    res_x.active = False
                    res_y.active = False
                    col_create.active = False
                    row_create.active = False



    for y in range(0,rows):
        for x in range(0,cols):
            grid.append(Cell(x,y))
    for cell in grid:
        cell.find_neighbor()
        loop_de_loop.append(cell.draw_cell)
    current = grid[0]
    player_is_born_in_this_foreign_land = player(current)
    pygame.key.set_repeat(50)
    while True:
        pygame.time.Clock().tick(20)
        mousp = None
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousp = event


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
            if open.pause == False:
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
        if hasattr(mousp, 'pos'):
            menu(mousp.pos, mousp)
        else:
            menu(None, None)

        pygame.display.update()

if __name__ == '__main__':
    main()

