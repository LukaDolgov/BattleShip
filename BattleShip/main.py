import pygame
from sys import exit
from random import randint, choice
from boatinfo import Boat

  
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('BattleShip')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
small_font = pygame.font.Font('font/Pixeltype.ttf', 25)
game_active = 0
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music2.mp3')
bg_music.set_volume(0.5)
#bg_music.play(loops = -1)

#sprites
boat_group = pygame.sprite.Group()
boat_group.add(Boat('aircraft'))
boat_group.add(Boat('destroyer'))
boat_group.add(Boat('cruiseboat'))
boat_group.add(Boat('submarine'))
boat_group.add(Boat('gunboat'))
  




#objects + text
board1_surface = pygame.image.load('graphics/board1u.png').convert_alpha()
board1_surface = pygame.transform.rotozoom(board1_surface, 0, 1) #board1 surface is 160, 90 pos
board1_rect = board1_surface.get_rect(topleft = (160, 80))

#boats
aircraft_surface = pygame.image.load('graphics/aircraftboat.png').convert_alpha()
aircraft_surface = pygame.transform.rotozoom(aircraft_surface, 0, .5)
aircraft_rect = aircraft_surface.get_rect(center = (580, 160))

destroyer_surface = pygame.image.load('graphics/destroyerboat.png').convert_alpha()
destroyer_surface = pygame.transform.rotozoom(destroyer_surface, 0, .5)
destroyer_rect = destroyer_surface.get_rect(center = (580, 260))


choose_pieces_text_surface = test_font.render('Choose your boats! Click to drop!', False, 'blue')
choose_pieces_text_surface_rect = choose_pieces_text_surface.get_rect(bottomleft = (280, 70))



#intro screen
game_name = test_font.render('BATTLESHIP', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (500, 80))

intro_boat_surface = pygame.image.load('graphics/introboat.png')
intro_boat_surface = pygame.transform.rotozoom(intro_boat_surface, 0, 1)
intro_boat_rect = intro_boat_surface.get_rect(center = (540, 175))

game_message = test_font.render('Click or press space to begin', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (500, 380))


#reset button
reset_surface = pygame.Surface((200, 50))
reset_surface.fill("blue")
reset_surface_rect = reset_surface.get_rect(center = (330, 435))
inside_box = pygame.Surface((180, 40))
inside_box_rect = inside_box.get_rect(center = (100, 25))
inside_box.fill("black")
text_surface = small_font.render("reset", True, 'blue')
text_rect = text_surface.get_rect(center=(100, 25))
reset_surface.blit(inside_box, inside_box_rect)
reset_surface.blit(text_surface, text_rect)


def msg_flicker():
    current_time = int(pygame.time.get_ticks() / 500)
    if current_time % 2 == 0: 
       screen.blit(game_message, game_message_rect)     
       
def return_pos():
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    
def hover_color():
    mouse_pos = pygame.mouse.get_pos()
    for i in range(0, 10):
         for j in range(0, 10):
           if grid[i][j] != "X":
             if grid[i][j].collidepoint(mouse_pos):
               pygame.draw.rect(screen, 'red', grid[i][j])



rows, cols = 10, 10
grid = [[pygame.Rect(186 + 29.5 * i, 104 + 29.5 * j, 28, 28) for i in range(cols)] for j in range(rows)]
availible_boats = ["air", "dest", "cruise", "sub", "gun"]

def checkborders(i, j, sprite):
    length = sprite.length
    rotation = sprite.rot_index
    if rotation == 0:
        for z in range (0, length):
            if j + z >= len(grid[0]) or grid[i][j + z] == "X":
                sprite.rot_index = 0
                sprite.rect.center = sprite.default
                sprite.following = False
                return False
    elif rotation == 1:
        for z in range (0, length):
            if i + z >= len(grid) or grid[i + z][j] == "X":
                sprite.rot_index = 0
                sprite.rect.center = sprite.default
                sprite.following = False
                return False
    return True


def placeboat(i, j, sprite):
    sprite.ypos = i 
    sprite.xpos = j
    new_rect = []
    sum = sprite.length * 29.5
    if (sprite.rot_index == 0):
      new_rect = pygame.Rect(grid[i][j].x - 10, grid[i][j].y - 5, sum, 29.5)
    elif (sprite.rot_index == 1):
      new_rect = pygame.Rect(grid[i][j].x - 10, grid[i][j].y - 10, 29.5, sum)
    for z in range (0, sprite.length):
      if (sprite.rot_index == 0):
         grid[i][j + z] = "X"
      elif (sprite.rot_index == 1):
         grid[i + z][j] = "X"
    sprite.set_rect(new_rect)
    sprite.following = False

def reset_board():
    for sprite in boat_group:
          sprite.rot_index = 0
          sprite.rect = sprite.image.get_rect(center = sprite.default)
          sprite.xpos = 0
          sprite.ypos = 0
    global grid 
    grid = [[pygame.Rect(186 + 29.5 * i, 104 + 29.5 * j, 28, 28) for i in range(cols)] for j in range(rows)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            return_pos()
            mouse_pos = pygame.mouse.get_pos()
            for i in range(0, 10):
               for j in range(0, 10):
                if grid[i][j] != "X":
                  if grid[i][j].collidepoint(mouse_pos):
                    for sprite in boat_group:
                        if sprite.following == True:
                            if (checkborders(i, j, sprite)):
                                placeboat(i, j, sprite)
                            else: print("Need dif spot")
            if reset_surface_rect.collidepoint(mouse_pos):
                reset_board()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if (game_active): game_active = 0
                else: game_active = 1
            if event.key == pygame.K_r:
                print("rotating")
                mouse_pos = pygame.mouse.get_pos()
                for sprite in boat_group:
                    if sprite.following == True and sprite.rot_index == 0:
                        sprite.rot_index = 1
                        sprite.image = sprite.rot[1]
                        sprite.rect.center = mouse_pos
                    elif sprite.following == True and sprite.rot_index == 1:
                        sprite.rot_index = 0
                        sprite.image = sprite.rot[0]
                        sprite.rect.center = mouse_pos
            
        
        
    if game_active == 1:
       screen.fill('lightblue')
       screen.blit(board1_surface, board1_rect)
       screen.blit(choose_pieces_text_surface, choose_pieces_text_surface_rect)
       screen.blit(reset_surface, reset_surface_rect)
       selectboard = pygame.draw.rect(screen, 'red', pygame.Rect(500, 105, 400, 290))
       boat_group.draw(screen)
       boat_group.update()
       hover_color()
    elif game_active == 0:
       screen.fill('blue')
       screen.blit(game_name, game_name_rect)
       screen.blit(intro_boat_surface, intro_boat_rect)
       msg_flicker()
    pygame.display.update()  
    clock.tick(60)