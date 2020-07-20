"""Avatar vs Rooks"""
"""Members"""
#Marco Gonzales 2020034547
#Diego Garcia 2020124283
#Kenneth Castillo 2019062984
"""Libraries"""
#######################COSAS POR CAMBIAR#######################
# HACER LA VARIABLE ROW GLOBAL
#
###############################################################

from CLASSES import *
from pygame import *
#from Game import *
import random
from CLASSES import *
from Sand import sand_attacks, Sand, SandAttack
from Rock import rock_attacks, Rock, RockAttack
from Fire import fire_attacks, Fire, FireAttack
from Water import water_attacks, Water, WaterAttack
from Archer import arrows, Archer, Arrow
from Squire import axes, Squire, Sword
from Lumber import sticks, Lumberjack, Stick
from Cannibal import hammers, Cannibal, Hammer

#Set sprite groups
buttons = pygame.sprite.Group()
buttons_grid = pygame.sprite.Group()
button_25 = pygame.sprite.Group()
button_50 = pygame.sprite.Group()
button_100 = pygame.sprite.Group()
sandrooks = pygame.sprite.Group()
rockrooks = pygame.sprite.Group()
firerooks = pygame.sprite.Group()
waterrooks = pygame.sprite.Group()
archeravatars = pygame.sprite.Group()
squireavatars = pygame.sprite.Group()
lumberavatars = pygame.sprite.Group()
cannibalavatars = pygame.sprite.Group()
rooks = pygame.sprite.Group()
avatars = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
row_M = 0
parameter = 0

#Set cursor
cursor = Cursor()

volume = 0.1
#Load the csv
csv_scoreboard = csv_class("ScoreBoard.csv","rt")
matrix = csv_scoreboard.get_matrix()

list_init = []

#Load the list of matrix
for line in matrix[row_M][3]:
    if line != "[" and line != "]" and line != "," and line != "[]" and line != " ":
        list_init += [int(line)]

#Set matrix
gridMatrix = [list_init[5*i : 5*(i+1)] for i in range(9)]

#Set selected
selected = ''

#Set counters
contador = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0


#Set currency
currency = int(matrix[row_M][6])

#Set FPS
FPS = 30


#Set crystals
img_crystal25 = pygame.image.load('images/25_crystal.png')
img_crystal50 = pygame.image.load('images/50_crystal.png')
img_crystal100 = pygame.image.load('images/100_crystal.png')

#Set level
level = int(matrix[row_M][4])

#Set column, row of grid
group = 0

#Set avatars spawn timer
avatar_spawnTime = 4

#Set max avatar spawn
spawn_avatars = True
contador_avatars = 0
max_avatars = 15

avatars_killed = int(matrix[row_M][5])
avatars_left = max_avatars - avatars_killed

# Set background
background = pygame.image.load("images/background_1.png")

# Set new level variables
new_level = False
new_avatars = True
winner = matrix[row_M][2]

#Set move variables
archermove = True
squiremove = True
lumbermove = True
cannibalmove = True

#Set exit
exit_ = False

#Set game over
gameover = False

#Set time
minute, second = 0,0

#Function that creates the window of game over
def game_over():
    #Place an icon on the window
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)
    #Settings of the screen
    pygame.init()
    pygame.font.init
    weight, height = 800,600
    bt_weight,bt_heigth = 70,70
    game_over_screen = pygame.display.set_mode((weight,height))
    
    #Set initial clock
    clock = pygame.time.Clock()

    pygame.mixer.music.set_volume(volume)
    pygame.mixer_music.load('Sounds/Game_Over.mp3')
    pygame.mixer_music.play(1)
    
    #Images of the screen
    background = pygame.image.load("images/game_over.png")
    
    #Background
    game_over_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))
    
    img_return=pygame.image.load("rsc/btn_return.png")
    cursor = Cursor()
    bt_return =Button(img_return,img_return,(weight-bt_weight-10),(height-100),bt_weight,bt_heigth)

    
    #While of the loop
    exit_ = False
    while exit_ != True:
        #Set the blits in the screen
        bt_return.update(game_over_screen,cursor)
        pygame.display.update()
        cursor.update()
        
        #Set th FPS
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Exit
                exit_ = True
                pygame.quit()
                break
            #Define the action of the mouse button
            if event.type == pygame.KEYDOWN:
               if event.key == 13:
                    exit_ = True
                    pygame.quit()
                    main_window()
                    break
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_return.rect):
                    print("Push Return Menu")
                    exit_ = True
                    pygame.quit()
                    main_window()
                    break
                
        
    pygame.quit()

#Function that creates the winner window
def winner():
    #Place an icon on the window
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)
    #Settings of the screen
    pygame.init()
    pygame.font.init
    weight, height = 800,600
    bt_weight,bt_heigth = 70,70
    winner_screen = pygame.display.set_mode((weight,height))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer_music.load('Sounds/Win_sound.mp3')
    pygame.mixer_music.play(1)
    #Set initial clock
    clock = pygame.time.Clock()

    
    #Images of the screen
    background = pygame.image.load("images/Win.png")
    
    #Background
    winner_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))
    
    img_return=pygame.image.load("rsc/btn_return.png")
    cursor = Cursor()
    bt_return =Button(img_return,img_return,(weight-bt_weight-10),(height-100),bt_weight,bt_heigth)

    
    #While of the loop
    exit_ = False
    while exit_ != True:
        #Set the blits in the screen
        bt_return.update(winner_screen,cursor)
        pygame.display.update()
        cursor.update()
        
        #Set th FPS
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Exit
                exit_ = True
                pygame.quit()
                break
            #Define the action of the mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_return.rect):
                    print("Push Return Menu")
                    exit_ = True
                    pygame.quit()
                    main_window()
                    break
                
        
    pygame.quit()

#Function that advances levels in the game
def next_level(contador_4):
    global level, gridMatrix, max_avatars, avatar_spawnTime, background, new_level, new_avatars, avatars_left, avatars_killed, contador_3, contador_avatars, matrix, cursor, minute, second, currency, exit_, FPS

    if new_level == True:
        level += 1
        if level > 3:
            matrix[row_M][2] = 'winner'
            gridMatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            avatars_killed = 0
            contador_avatars = 0
            sand_attacks.empty()
            rock_attacks.empty()
            fire_attacks.empty()
            water_attacks.empty()
            sandrooks.empty()
            rockrooks.empty()
            firerooks.empty()
            waterrooks.empty()
            rooks.empty()
            buttons.empty()
            buttons_grid.empty()
            button_25.empty()
            button_50.empty()
            button_100.empty()
            
            matrix[row_M][6] = currency
            matrix[row_M][4] = 0
            matrix[row_M][5] = avatars_killed
            matrix[row_M][7] = minute
            matrix[row_M][8] = round(second)
            matrix[row_M][3] = gridMatrix
            csv_scoreboard.write(matrix)
            csv_scoreboard.update_matrix("ScoreBoard.csv", "w")
            exit_ = True
            pygame.quit()
            winner()


        if level == 2:
            pygame.mixer_music.stop()
            max_avatars = 15 + int(15 * 0.3)
            avatars_left = max_avatars
            background = pygame.image.load("images/background_2.png")
            avatar_spawnTime = 4 - (4 * 0.3)
            avatars_killed = 0
            contador_3 = 0
            contador_avatars = 0
            pygame.mixer.music.set_volume(volume)
            pygame.mixer_music.load('Sounds/Battle2.mp3')
            pygame.mixer.music.play(-1)
            gridMatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            new_avatars = True
            sand_attacks.empty()
            rock_attacks.empty()
            fire_attacks.empty()
            water_attacks.empty()
            sandrooks.empty()
            rockrooks.empty()
            firerooks.empty()
            waterrooks.empty()
            rooks.empty()

        elif level == 3:
            pygame.mixer_music.stop()
            max_avatars = 15 + int(15 * 0.6)
            avatars_left = max_avatars
            background = pygame.image.load("images/background_3.png")
            avatar_spawnTime = 4 - (4 * 0.6)
            avatars_killed = 0
            contador_3 = 0
            contador_avatars = 0
            pygame.mixer.music.set_volume(volume)
            pygame.mixer_music.load('Sounds/Battle3.mp3')
            pygame.mixer.music.play(-1)
            gridMatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            new_avatars = True
            sand_attacks.empty()
            rock_attacks.empty()
            fire_attacks.empty()
            water_attacks.empty()
            sandrooks.empty()
            rockrooks.empty()
            firerooks.empty()
            waterrooks.empty()
            rooks.empty()

        new_level = False
    new_level = False
            

#Function that defines the spawn of a avatar
def avatar_spawn():
    global contador_3, contador_avatars, FPS, currency, avatar_spawnTime, spawn_avatars, gridMatrix, new_avatars, max_avatars

    x, y = 295, 209
    if new_avatars == True:
        contador_3 += 1 / FPS
        if avatar_spawnTime <= contador_3 <= avatar_spawnTime + 0.05:
            random_avatar = random.randint(0,3)
            random_column = random.randint(0,4)
            if random_avatar == 0 and gridMatrix[0][random_column] == 0:
                archeravatars.add(Archer(x + (random_column * 95), y))
                avatars.add(archeravatars)
                contador_3 = 0
                contador_avatars += 1
            elif random_avatar == 1 and gridMatrix[0][random_column] == 0:
                squireavatars.add(Squire(x + (random_column * 95), y))
                avatars.add(squireavatars)
                contador_3 = 0
                contador_avatars += 1
            elif random_avatar == 2 and gridMatrix[0][random_column] == 0:
                lumberavatars.add(Lumberjack(x + (random_column * 95), y))
                avatars.add(lumberavatars)
                contador_3 = 0
                contador_avatars += 1
            elif random_avatar == 3 and gridMatrix[0][random_column] == 0:
                cannibalavatars.add(Cannibal(x + (random_column * 95), y))
                avatars.add(cannibalavatars)
                contador_3 = 0
                contador_avatars += 1
            if contador_avatars == max_avatars:
                new_avatars = False

    avatar_functions()

#Function that gives/check movement, attack and damage recieval to the avatars
def avatar_functions():
    global archermove, squiremove, lumbermove, cannibalmove, currency, avatars_left, avatars_killed, gameover, contador_5, level, FPS, exit_,background, gridMatrix, contador_6

    for archer in archeravatars:
        archer.move(archermove)
        if len(rooks) > 0:
            for allrooks in rooks:
                if (archer.rect.top + 100) >= allrooks.rect.top and archer.rect.left == allrooks.rect.left:
                    archermove = False
                else:
                    archermove = True
        else:
            archermove = True

        if pygame.sprite.spritecollide(archer, sand_attacks, True):
            archer.decrease_health(2)
        elif pygame.sprite.spritecollide(archer, rock_attacks, True):
            archer.decrease_health(4)
        elif pygame.sprite.spritecollide(archer, fire_attacks, True):
            archer.decrease_health(8)
        elif pygame.sprite.spritecollide(archer, water_attacks, True):
            archer.decrease_health(8)
        if archer.health <= 0:
            archer.kill()
            currency += 75
            avatars_left -= 1
            avatars_killed += 1

    for squire in squireavatars:
        squire.move(squiremove)
        if len(rooks) > 0:
            for allrooks in rooks:
                if (squire.rect.top + 100) >= allrooks.rect.top and squire.rect.left == allrooks.rect.left:
                    squiremove = False
                else:
                    squiremove = True
        else:
            squiremove = True

        if pygame.sprite.spritecollide(squire, sand_attacks, True):
            squire.decrease_health(2)
        elif pygame.sprite.spritecollide(squire, rock_attacks, True):
            squire.decrease_health(4)
        elif pygame.sprite.spritecollide(squire, fire_attacks, True):
            squire.decrease_health(8)
        elif pygame.sprite.spritecollide(squire, water_attacks, True):
            squire.decrease_health(8)
        if squire.health <= 0:
            squire.kill()
            currency += 75
            avatars_left -= 1
            avatars_killed += 1

    for lumber in lumberavatars:
        lumber.move(lumbermove)
        if len(rooks) > 0:
            for allrooks in rooks:
                if (lumber.rect.top + 100) >= allrooks.rect.top and lumber.rect.left == allrooks.rect.left:
                    lumbermove = False
                    lumber.attack(True)
                else:
                    lumbermove = True
                    lumber.attack(False)
        else:
            lumbermove = True

        if pygame.sprite.spritecollide(lumber, sand_attacks, True):
            lumber.decrease_health(2)
        elif pygame.sprite.spritecollide(lumber, rock_attacks, True):
            lumber.decrease_health(4)
        elif pygame.sprite.spritecollide(lumber, fire_attacks, True):
            lumber.decrease_health(8)
        elif pygame.sprite.spritecollide(lumber, water_attacks, True):
            lumber.decrease_health(8)
        if lumber.health <= 0:
            lumber.kill()
            currency += 75
            avatars_left -= 1
            avatars_killed += 1

    for cannibal in cannibalavatars:
        cannibal.move(cannibalmove)
        if len(rooks) > 0:
            for allrooks in rooks:
                if (cannibal.rect.top + 100) >= allrooks.rect.top and cannibal.rect.left == allrooks.rect.left:
                    cannibalmove = False
                    cannibal.attack(True)
                else:
                    cannibalmove = True
                    cannibal.attack(False)
        else:
            cannibalmove = True
        if pygame.sprite.spritecollide(cannibal, sand_attacks, True):
            cannibal.decrease_health(2)
        elif pygame.sprite.spritecollide(cannibal, rock_attacks, True):
            cannibal.decrease_health(4)
        elif pygame.sprite.spritecollide(cannibal, fire_attacks, True):
            cannibal.decrease_health(8)
        elif pygame.sprite.spritecollide(cannibal, water_attacks, True):
            cannibal.decrease_health(8)
        if cannibal.health <= 0:
            cannibal.kill()
            currency += 75
            avatars_left -= 1
            avatars_killed += 1

    for allavatars in avatars:
        if allavatars.rect.top >= 849:
            gameover = True
            pygame.mixer_music.stop()
            sand_attacks.empty()
            rock_attacks.empty()
            fire_attacks.empty()
            water_attacks.empty()
            sandrooks.empty()
            rockrooks.empty()
            firerooks.empty()
            waterrooks.empty()
            rooks.empty()
            buttons.empty()
            buttons_grid.empty()
            button_25.empty()
            button_50.empty()
            button_100.empty()
            archeravatars.empty()
            squireavatars.empty()
            lumberavatars.empty()
            cannibalavatars.empty()
            avatars.empty()
            pygame.quit()
            
            game_over()


#Function that spawns a random gem in the determined spot in the screen
def crystal_spawn():
    global contador_2, currency, FPS, button_25, button_50, button_100

    click = pygame.mouse.get_pressed()
    contador_2 += 1 / FPS
    img_square = pygame.image.load("images/square.png")
    mouse = pygame.mouse.get_pos()
    cursor_rect = Button(img_square, img_square, mouse[0], mouse[1], 1, 1)

    if 30 <= contador_2 <= 30.01:
        random_crystal = random.randint(0,2)
        if random_crystal == 0:
            button_25.add(Button(img_crystal25, img_crystal25, 880, 500, 50, 50))
        elif random_crystal == 1:
            button_50.add(Button(img_crystal50, img_crystal50, 880, 500, 50, 50))
        elif random_crystal == 2:
            button_100.add(Button(img_crystal100, img_crystal100, 880, 500, 50, 50))

    if click[0] == 1:
        if pygame.sprite.spritecollide(cursor_rect, button_25, True):
            contador_2 = 0
            if contador_2 == 0:
                currency += 25
        if pygame.sprite.spritecollide(cursor_rect, button_50, True):
            contador_2 = 0
            if contador_2 == 0:
                currency += 50
        if pygame.sprite.spritecollide(cursor_rect, button_100, True):
            contador_2 = 0
            if contador_2 == 0:
                currency += 100

    if contador_2 >= 60:
        button_25.empty()
        button_50.empty()
        button_100.empty()
        contador_2 = 0

#Function that spawns rooks in the map and modifies the matrix
def button_matrix(posx, posy, column, row, button, screen):
    global selected, currency, rooks, all_sprites, sand_rook, parameter

    click = pygame.mouse.get_pressed()
    img_square = pygame.image.load("images/square.png")
    mouse = pygame.mouse.get_pos()
    cursor_rect = Button(img_square, img_square, mouse[0], mouse[1], 1, 1)

    if cursor.colliderect(button.rect):
        if click[0] == 1:
            if selected != '' and gridMatrix[row][column] == 0:
                if row >= 2:
                    if selected == 'SANDROOK':
                        if currency >= 50:
                            gridMatrix[row][column] = 1
                            selected = ''
                            currency -= 50
                            sandrooks.add(Sand(int(parameter), posx, posy))
                            rooks.add(sandrooks)
                    if selected == 'ROCKROOK':
                        if currency >= 100:
                            gridMatrix[row][column] = 2
                            selected = ''
                            currency -= 100
                            rockrooks.add(Rock(int(parameter), posx, posy))
                            rooks.add(rockrooks)
                    if selected == 'FIREROOK':
                        if currency >= 150:
                            gridMatrix[row][column] = 3
                            selected = ''
                            currency -= 150
                            firerooks.add(Fire(int(parameter), posx, posy))
                            rooks.add(firerooks)
                    if selected == 'WATERROOK':
                        if currency >= 150:
                            gridMatrix[row][column] = 4
                            selected = ''
                            currency -= 150
                            waterrooks.add(Water(int(parameter), posx, posy))
                            rooks.add(waterrooks)
            if selected == 'REMOVE' and gridMatrix[row][column] != 0:
                gridMatrix[row][column] = 0
                selected = ''
                pygame.sprite.spritecollide(cursor_rect, rooks, True)

#Function that gives/checks attacking and damage recieval to rooks
def damage_rooks():
    global health_fireRook, health_waterRook, group

    for sand_rook in sandrooks:
        if pygame.sprite.spritecollide(sand_rook, arrows, True):
                sand_rook.decrease_health(2)
        elif pygame.sprite.spritecollide(sand_rook, axes, True):
            for sand_rook in sandrooks:
                sand_rook.decrease_health(3)
        elif pygame.sprite.spritecollide(sand_rook, sticks, True):
                sand_rook.decrease_health(9)
        elif pygame.sprite.spritecollide(sand_rook, hammers, True):
                sand_rook.decrease_health(12)

        if sand_rook.health <= 0:
            gridMatrix[int((sand_rook.rect.top - 209) / 80)][int((sand_rook.rect.left - 295) / 95)] = 0
            sand_rook.kill()

    for rock_rook in rockrooks:
        if pygame.sprite.spritecollide(rock_rook, arrows, True):
                rock_rook.decrease_health(2)
        if pygame.sprite.spritecollide(rock_rook, axes, True):
                rock_rook.decrease_health(3)
        elif pygame.sprite.spritecollide(rock_rook, sticks, True):
                rock_rook.decrease_health(9)
        elif pygame.sprite.spritecollide(rock_rook, hammers, True):
                rock_rook.decrease_health(12)
        if rock_rook.health <= 0:
            gridMatrix[int((rock_rook.rect.top - 295) / 95)][int((rock_rook.rect.left - 209) / 80)] = 0
            rock_rook.kill()

    for fire_rook in firerooks:
        if pygame.sprite.spritecollide(fire_rook, arrows, True):
            fire_rook.decrease_health(2)
        if pygame.sprite.spritecollide(fire_rook, axes, True):
            fire_rook.decrease_health(3)
        elif pygame.sprite.spritecollide(fire_rook, sticks, True):
            fire_rook.decrease_health(9)
        elif pygame.sprite.spritecollide(fire_rook, hammers, True):
            fire_rook.decrease_health(12)
        if fire_rook.health <= 0:
            gridMatrix[int((fire_rook.rect.top - 295) / 95)][int((fire_rook.rect.left - 209) / 80)] = 0
            fire_rook.kill()

    for water_rook in waterrooks:
        if pygame.sprite.spritecollide(water_rook, arrows, True):
            water_rook.decrease_health(2)
        if pygame.sprite.spritecollide(water_rook, axes, True):
            water_rook.decrease_health(3)
        elif pygame.sprite.spritecollide(water_rook, sticks, True):
            water_rook.decrease_health(9)
        elif pygame.sprite.spritecollide(water_rook, hammers, True):
            water_rook.decrease_health(12)
        if water_rook.health <= 0:
            gridMatrix[int((water_rook.rect.top - 295) / 95)][int((water_rook.rect.left - 209) / 80)] = 0
            water_rook.kill()

#Function that draws the matrix of buttons
def draw_grid(column, row, screen):
    global contador

    x, y = 295, 209
    img_square = pygame.image.load("images/square.png")
    img_squareSelect = pygame.image.load("images/select_square.png")
    if row == 9:
        return
    if column == 5:
        return draw_grid(0, row + 1, screen)
    else:
        button = Button(img_square, img_squareSelect, x + (column * 95), y + (row * 80), 95, 80)
        button_matrix(x + (column * 95), y + (row * 80), column, row, button, screen)
        damage_rooks()
        if contador < 45:
            buttons_grid.add(button)
            buttons.add(buttons_grid)
            contador += 1
        return draw_grid(column + 1, row, screen)

#Function that makes the game window function
def principal_window():
    global selected, currency, buttons, FPS, background, rooks, all_sprites, gridMatrix, level, avatar_spawnTime, new_level, avatars_left, avatars_killed, contador_avatars, max_avatars, exit_, contador_4, minute, second
    global selected, currency, buttons, FPS, background, rooks, all_sprites, gridMatrix, level, avatar_spawnTime, new_level, avatars_left, avatars_killed, parameter
    print(parameter)

    #Place an icon on the window
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)

    pygame.mixer.init()
    pygame.init()
    width , height = 1000, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Window")

    #Set clock
    clock = pygame.time.Clock()

    #CSV Archive
    csv_scoreboard = csv_class("ScoreBoard.csv", "rt")
    matrix = csv_scoreboard.get_matrix()
    
    list_init = []

    #Load the list of matrix
    for line in matrix[row_M][3]:
        if line != "[" and line != "]" and line != "," and line != "[]" and line != " ":
            list_init += [int(line)]

    #Set matrix
    gridMatrix = [list_init[5*i : 5*(i+1)] for i in range(9)]

    #Set currency
    currency = int(matrix[row_M][6])

    level = int(matrix[row_M][4])

    avatars_killed = int(matrix[row_M][5])
    
    #Set font
    font = pygame.font.Font("triforce.ttf", 40)

    #Images of the screen
    img_currency = pygame.image.load("images/crystal_currency.png")
    img_currency = pygame.transform.scale(img_currency, (100,100))

    img_sandRook = pygame.image.load("images/rooks/sand_rook_a.png")
    img_sandRook_b = pygame.image.load("images/rooks/sand_rook_b.png")

    img_rockRook = pygame.image.load("images/rooks/rock_rook_a.png")
    img_rockRook_b = pygame.image.load("images/rooks/rock_rook_b.png")

    img_fireRook = pygame.image.load("images/rooks/fire_rook_a.png")
    img_fireRook_b = pygame.image.load("images/rooks/fire_rook_b.png")

    img_waterRook = pygame.image.load("images/rooks/water_rook_a.png")
    img_waterRook_b = pygame.image.load("images/rooks/water_rook_b.png")

    img_squareSelect2 = pygame.image.load("images/select_square.png")
    img_squareSelect2 = pygame.transform.scale(img_squareSelect2, (150, 150))

    img_remove = pygame.image.load('images/remove.png')


    #Create the buttons and cursor
    bt_sandRook = Button(img_sandRook, img_sandRook_b, 0, 150, 150, 150)
    bt_rockRook = Button(img_rockRook, img_rockRook_b, 0, 310, 150, 150)
    bt_fireRook = Button(img_fireRook, img_fireRook_b, 0, 460, 150, 150)
    bt_waterRook = Button(img_waterRook, img_waterRook_b, 0, 625, 150, 150)
    bt_remove = Button(img_remove, img_remove, 0, 775, 150, 150)
    buttons.add(bt_sandRook, bt_rockRook, bt_fireRook, bt_waterRook, bt_remove)

    #Set timer
    second = int(matrix[row_M][8])
    minute = int(matrix[row_M][7])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer_music.load('Sounds/Battle1.mp3')
    if level == 2:
        avatar_spawnTime = 4 - (4 * 0.3)
        max_avatars = 15 + int(15 * 0.3)
        avatars_left = max_avatars - avatars_killed
        background = pygame.image.load("images/background_2.png")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer_music.load('Sounds/Battle2.mp3')
    elif level == 3:
        avatar_spawnTime = 4 - (4 * 0.6)
        max_avatars = 15 + int(15 * 0.6)
        avatars_left = max_avatars - avatars_killed
        pygame.mixer.music.set_volume(volume)
        pygame.mixer_music.load('Sounds/Battle3.mp3')
        background = pygame.image.load("images/background_3.png")


    for row in range(len(gridMatrix)):
        for column in range(len(gridMatrix[row])):
            if gridMatrix[row][column] == 1:
                rooks.add(Sand(2, 295 + (column * 95), 209 + (row * 80)))
            if gridMatrix[row][column] == 2:
                rooks.add(Rock(2, 295 + (column * 95), 209 + (row * 80)))
            if gridMatrix[row][column] == 3:
                rooks.add(Fire(2, 295 + (column * 95), 209 + (row * 80)))
            if gridMatrix[row][column] == 4:
                rooks.add(Water(2, 295 + (column * 95), 209 + (row * 80)))

    #Set music
    pygame.mixer.music.play(-1)

    #pause = False
    while exit_ != True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                #Set currency
                matrix[row_M][6] = currency  
                matrix[row_M][4] = level
                matrix[row_M][5] = avatars_killed
                matrix[row_M][7] = minute
                matrix[row_M][8] = round(second)
                matrix[row_M][3] = gridMatrix
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv", "w")
                exit_ = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_sandRook.rect):
                    selected = 'SANDROOK'
                if cursor.colliderect(bt_rockRook.rect):
                    selected = 'ROCKROOK'
                if cursor.colliderect(bt_fireRook.rect):
                    selected = 'FIREROOK'
                if cursor.colliderect(bt_waterRook.rect):
                    selected = 'WATERROOK'
                if cursor.colliderect(bt_remove.rect):
                    selected = 'REMOVE'

        clock.tick(FPS)

        #Timer
        second += 1 / FPS
        if second >= 60:
            minute += 1
            second = 0
        timer_text = font.render(": ".join([str(int(minute)), str(int(second)).zfill(2)]), True, (255, 255, 255))

        #Avatars restantes
        avatars_left_text = font.render(str(avatars_left), True, (255,255,255))
        avatars_killed_text = font.render(str(avatars_killed), True, (255,255,255))

        #User
        user_t = matrix[row_M][0]
        user = font.render(user_t, True, (255, 255, 255))
        
        #Combinar login con esto para que el user sea el que hizo el login

        #Currency
        currency_text = font.render(str(currency), True, (255, 255, 255))

        #Update screen
        screen.blit(pygame.transform.scale(background, (width, height)), (0, 0))
        screen.blit(timer_text, (210,5))
        screen.blit(user, (10,5))
        screen.blit(img_currency, (790, -15))
        screen.blit(currency_text, (890, 15))
        screen.blit(avatars_left_text, (460, 85))
        screen.blit(avatars_killed_text, (555, 85))

        if selected == 'SANDROOK':
            screen.blit(img_squareSelect2, (0, 150))
        if selected == 'ROCKROOK':
            screen.blit(img_squareSelect2, (0, 310))
        if selected == 'FIREROOK':
            screen.blit(img_squareSelect2, (0, 460))
        if selected == 'WATERROOK':
            screen.blit(img_squareSelect2, (0, 625))
        if selected == 'REMOVE':
            screen.blit(img_squareSelect2, (0, 775))


        # Place buttons in the screen
        cursor.update()
        buttons.update(screen, cursor)
        button_25.update(screen, cursor)
        button_50.update(screen, cursor)
        button_100.update(screen, cursor)
        rooks.update(screen)
        avatars.update(screen)
        arrows.update(screen)
        axes.update(screen)
        sticks.update(screen)
        hammers.update(screen)
        sand_attacks.update(screen)
        rock_attacks.update(screen)
        fire_attacks.update(screen)
        water_attacks.update(screen)
        all_sprites.update(screen)

        draw_grid(0, 0, screen)
        crystal_spawn()
        avatar_spawn()
        if avatars_left == 0 and avatars_killed == max_avatars:
            new_level = True
            next_level(0)
        if level > 3:
            contador_4 += 1
            if contador_4 >= 5 * FPS:
                next_level(contador_4)


        pygame.display.update()

    pygame.quit()













"""Functions"""
def main_window():
    #Contains the row of the matrix the user is in
    global row_M
    
    #Contain the parameter of attack frequency
    global parameter

    #Place an icon on the window
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)
    
    #Settings of the screen
    pygame.init()
    weight, height = 952,768
    screen = pygame.display.set_mode((weight,height))
    
    pygame.mixer.music.set_volume(volume)
    pygame.mixer_music.load('Sounds/Menu.mp3')
    pygame.mixer_music.play(1)
    #CSV Archive
    csv_scoreboard = csv_class("ScoreBoard.csv","rt")

    #Matrix
    matrix = csv_scoreboard.get_matrix()
    
    #Settings of the bottons
    bt_weight,bt_heigth = 150,75

    #Fonts
    font_user = pygame.font.Font("triforce.ttf",40)

    #Text
    user_text = matrix[row_M][0]
    if int(matrix[row_M][8]) <= 9:
        scoreboard_text = "ScoreBoard:" +" "+ matrix[row_M][7] + ":" + "0" + matrix[row_M][8]
    else:
        scoreboard_text = "ScoreBoard:" +" "+ matrix[row_M][7] + ":" + matrix[row_M][8]
    #Render
    txt_user = font_user.render(user_text, True, (255,255,255))
    txt_scoreboard = font_user.render(scoreboard_text, True, (255,255,255))

    #Set initial clock
    clock = pygame.time.Clock()
    
    #Images of the screen
    background = pygame.image.load("rsc/menu_game.png")
    
    img_credits = pygame.image.load("rsc/btn_credits.png")
    img_credits_b = pygame.image.load("rsc/btn_credits_b.png")
    
    img_exit = pygame.image.load("rsc/btn_exit.png")
    img_exit_b = pygame.image.load("rsc/btn_exit_b.png")
    
    img_help = pygame.image.load("rsc/btn_help.png")
    img_help_b = pygame.image.load("rsc/btn_help_b.png")
    
    img_login = pygame.image.load("rsc/btn_login.png")
    img_login_b = pygame.image.load("rsc/btn_login_b.png")
    
    img_play = pygame.image.load("rsc/btn_play.png")
    img_play_b = pygame.image.load("rsc/btn_play_b.png")

    img_scoreboard = pygame.image.load("rsc/btn_scoreboard.png")
    img_scoreboard_b = pygame.image.load("rsc/btn_scoreboard_b.png")

    #Create the buttons and cursor
    cursor = Cursor()
    bt_credits = Button(img_credits,img_credits_b,(weight-bt_weight-10),0,bt_weight,bt_heigth)
    bt_exit = Button(img_exit,img_exit_b,(weight-bt_weight-10),(height-200),bt_weight,bt_heigth)
    bt_help = Button(img_help,img_help_b,(weight-bt_weight-10),100,bt_weight,bt_heigth)
    bt_login = Button(img_login,img_login_b,(weight/2-(bt_weight/2)),(weight/2),bt_weight,bt_heigth)
    bt_play = Button(img_play,img_play_b,(weight/2-(bt_weight/2)),(weight/2+100),bt_weight,bt_heigth)
    bt_scoreboard = Button(img_scoreboard,img_scoreboard_b,(weight-bt_weight-10),200,bt_weight,bt_heigth)
    
    #While of the loop
    exit_ = False
    while exit_ != True:
        clock.tick(60)
        screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))

        #Put the buttons in the screen
        bt_credits.update(screen,cursor)
        bt_exit.update(screen,cursor)
        bt_help.update(screen,cursor)
        bt_login.update(screen,cursor)
        bt_play.update(screen,cursor)
        bt_scoreboard.update(screen,cursor)
        cursor.update()
        screen.blit(txt_user,(0,0))
        screen.blit(txt_scoreboard,(0,40))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            #Load the events
            if event.type == pygame.QUIT:
                #Save the CSV 
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv","w")
                #Exit
                exit_ = True
                pygame.quit()
                break
            #Define the actions of the mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_credits.rect):
                    print("Push credits")
                    exit_ = True
                    pygame.quit()
                    credits_window()
                    break
                if cursor.colliderect(bt_exit.rect):
                    print("push_exit")
                    csv_scoreboard.write(matrix)
                    csv_scoreboard.update_matrix("ScoreBoard.csv","w")
                    exit_ = True
                    pygame.quit()
                    break
                if cursor.colliderect(bt_help.rect):
                    print("Push Help")
                    exit_ = True
                    pygame.quit()
                    help_window()
                    break
                if cursor.colliderect(bt_login.rect):
                    print("Push Login")
                    exit_ = True
                    pygame.quit()
                    login_window()
                    break
                if cursor.colliderect(bt_play.rect):
                    print("Push Play")
                    exit_ = True
                    pygame.quit()
                    transition_login(user_text, "principal_window")
                    break
                if cursor.colliderect(bt_scoreboard.rect):
                    print("Push Scoreboard")
                    exit_ = True
                    pygame.quit()
                    scoreboard_window()
                    break
    pygame.quit()

def credits_window():
	#Place an icon on the window
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)
    #Settings of the screen
    pygame.init()
    pygame.font.init
    weight, height = 800,600
    bt_weight,bt_heigth = 70,70
    credits_screen = pygame.display.set_mode((weight,height))

    #FONT
    font = pygame.font.Font("triforce.ttf",35)

    
    #Set initial clock
    clock = pygame.time.Clock()
    
    #Load the txt
    a_txt = open("credits.txt")
    txt = a_txt.read()
    
    #Images of the screen
    background = pygame.image.load("rsc/window_credits.png")
    
    #Background
    credits_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))

    y = height-200
    #Call the functions of the multi_line_reader
    multi_line_reader(credits_screen, txt, -225,190, font,(255,255,255), justification="center")
    img_return=pygame.image.load("rsc/btn_return.png")
    cursor = Cursor()
    bt_return =Button(img_return,img_return,(weight-bt_weight-10),(height-100),bt_weight,bt_heigth)

    
    #While of the loop
    exit_ = False
    while exit_ != True:
        #Set the blits in the screen
        bt_return.update(credits_screen,cursor)
        pygame.display.update()
        cursor.update()

        #Set th FPS
        pygame.display.update()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Exit
                exit_ = True
                pygame.quit()
                break
            #Define the action of the mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_return.rect):
                    print("Push Return Menu")
                    exit_ = True
                    pygame.quit()
                    main_window()
                    break
                
        
    pygame.quit()
def sort_matrix():
    sort = True
    archive_csv = csv_class("ScoreBoard.csv","rt")
    matrix_csv = archive_csv.get_matrix()
    row = 0
    minutes = 7
    seconds = 8
    while sort:
        if len(matrix_csv)-1 > row:
            if matrix_csv[row][minutes] < (matrix_csv[row+1][minutes]):
                B = matrix_csv[row][minutes]
                matrix_csv[row][minutes] = matrix_csv[row+1][minutes]
                matrix_csv[row+1][minutes] = B
                row = 0
            elif matrix_csv[row][minutes] == matrix_csv[row+1][minutes]:
                if matrix_csv[row][seconds] < matrix_csv[row+1][seconds]:
                    B = matrix_csv[row][seconds]
                    matrix_csv[row][seconds] = matrix_csv[row+1][seconds]
                    matrix_csv[row+1][seconds] = B
                    row = 0
                elif matrix_csv[row][minutes] >= matrix_csv[row+1][minutes]:
                    row += 1
            elif matrix_csv[row][minutes] > matrix_csv[row+1][minutes]:
                row += 1
        else:
            archive_csv.write(matrix_csv)
            archive_csv.update_matrix("ScoreBoard.csv","w")
            sort = False

def login_window():
    #import pygame_textinput
    #Settings of the screen
    sort_matrix()
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)
    pygame.init()
    pygame.font.init
    weight, height = 500,400
    login_screen = pygame.display.set_mode((weight,height))

    pygame.mixer.music.set_volume(volume)
    pygame.mixer_music.load('Sounds/Login Sound.mp3')
    pygame.mixer_music.play(1)
    
    
    #FONT
    font = pygame.font.Font(None,30)
    font_user = pygame.font.Font("triforce.ttf",40)
    
    #Text input
    box_input = pygame.Rect(100, 110, 140, 32)
    box_input_p = pygame.Rect(200, 225, 140, 32)

    #Color of the box
    color_inactive = (0,0,0)
    color_active = (255,255,255)
    color = color_inactive

    color_inactive_p = (0,0,0)
    color_active_p = (255,255,255)
    color_p = color_inactive
    
    #Set the initial active of the box
    active = False
    active_p = False

    #Content the text of the user
    text = ''
    User = "User Name"
    text_attack = "Attack Frequency"
    global parameter
    parameter = ""

    #render the elements
    txt_user = font_user.render(User, True, (0,0,0))
    user_rect = txt_user.get_rect()

    txt_attack = font_user.render(text_attack, True, (0,0,0))
    attack_rect = txt_attack.get_rect()
    
    #Sttings of the bottons
    bt_weight,bt_heigth = 150,75
    
    #Set initial clock
    clock = pygame.time.Clock()
    
    #Images of the screen
    background = pygame.image.load("rsc/background.jpeg")
    img_login = pygame.image.load("rsc/btn_login.png")
    img_login_b = pygame.image.load("rsc/btn_login_b.png")
    
    
    
    #Buttons of the screen
    cursor = Cursor()
    bt_login = Button(img_login,img_login_b,(weight/2-(bt_weight/2)),(weight/3+150),bt_weight,bt_heigth)

    
    pygame.display.update()
    #While of the loop
    exit_ = False
    while exit_ != True:
        #Background
        login_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))

        #render the elements
        txt = font.render(text, True, (0,0,0))
        txt_parameter = font.render(parameter, True, (0,0,0))
        
        #Scale the box of the text
        width = max(100, txt.get_width()+10)
        box_input.w = width
        box_input.x = round((weight//2)-(width//2))

        width_p = max(100, txt_parameter.get_width()+10)
        box_input_p.w = width_p
        box_input_p.x = round((weight//2)-(width_p//2))
                                
        #Set the blits in the screen
        login_screen.blit(txt, (box_input.x+5, box_input.y+5))
        pygame.draw.rect(login_screen, color, box_input, 2)
        bt_login.update(login_screen,cursor)
        login_screen.blit(txt_user,(round(((weight/2)-(user_rect.w/2))),60))

        login_screen.blit(txt_parameter, (box_input_p.x+5, box_input_p.y+5))
        pygame.draw.rect(login_screen, color_p, box_input_p, 2)
        login_screen.blit(txt_attack,(round(((weight/2)-(attack_rect.w/2))),175))
        
        cursor.update()

        
        pygame.display.update()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Exit
                exit_ = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_login.rect):
                    if text != "" and int(parameter)>0:
                        print("Push Login")
                        exit_ = True
                        pygame.quit()
                        transition_login(text, "main_window")
                        break
                ####BOX OF THE TEXT###
                # when the user click in the box, this is active
                if box_input.collidepoint(event.pos):
                    # Set the value of the variable
                    active = not active
                else:
                    active = False
                #Set the current color of the box
                color = color_active if active else color_inactive
                
                # when the user click in the box, this is active for the other box
                if box_input_p.collidepoint(event.pos):
                    # Set the value of the variable for the other box
                    active_p = not active_p
                else:
                    active_p = False
                #Set the current color of the box for the other box
                color_p = color_active_p if active_p else color_inactive_p

            #Write text in the box of the screen
            #Add the text to a variable
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if active_p:
                    if event.key == pygame.K_BACKSPACE:
                        parameter = parameter[:-1]
                    else:
                        if event.key>=48 and event.key<=59:
                            parameter += event.unicode
    pygame.quit()
    
def help_window():
    #Settings of the screen
    pygame.init()
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)
    pygame.font.init
    weight, height = 1050,768
    bt_weight,bt_heigth = 70,70
    help_screen = pygame.display.set_mode((weight, height))
    
    #FONT
    font = pygame.font.Font("triforce.ttf",16)
    
    #Set initial clock
    clock = pygame.time.Clock()
    
    #Load the txt
    a_txt = open("help.txt")
    txt = a_txt.read()
    
    #Images of the screen
    background = pygame.image.load("rsc/window_help.png")
    img_return=pygame.image.load("rsc/btn_return.png")

    #Background
    help_screen.blit(pygame.transform.scale(background,(weight, height)),(0,0))
    
    #Call the functions of the multi_line_reader
    multi_line_reader(help_screen, txt, 20,190, font,(255,255,255), justification="left-justify")

    cursor = Cursor()
    bt_return =Button(img_return,img_return,(weight-bt_weight-10),(height-100),bt_weight,bt_heigth)
    pygame.display.update()
    #While of the loop
    exit_ = False
    while exit_ != True:
        clock.tick(60)
        pygame.display.update()
        #Set the blits in the screen
        bt_return.update(help_screen,cursor)
        pygame.display.update()
        cursor.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_return.rect):
                    print("Push Return Menu")
                    exit_ = True
                    pygame.quit()
                    main_window()
                    break
    pygame.quit()

            
        
        
        
def scoreboard_window():
    #Settings of the screen
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)
    pygame.init()
    pygame.font.init
    weight, height = 1050,768
    bt_weight,bt_heigth = 70,70
    scoreboard_screen = pygame.display.set_mode((weight, height))
    
    #FONT
    font = pygame.font.Font("triforce.ttf",32)
    
    #Set initial clock
    clock = pygame.time.Clock()

    #Load the csv
    archive_csv = csv_class("ScoreBoard.csv","rt")
    matrix_csv = archive_csv.get_matrix()

    #Load the user and score as a text, only when the user is the winner.
    txt = ""
    for l in matrix_csv:
        if str(l[2]) == "winner":
            if int(l[8]) <= 9:
                txt += str(l[0])
                txt += " "
                txt += str(l[7])
                txt += ":"
                txt += "0"
                txt += str(l[8])
                txt += "\n"
                txt += "\n"
            else:
                txt += str(l[0])
                txt += " "
                txt += str(l[7])
                txt += ":"
                txt += str(l[8])
                txt += "\n"
                txt += "\n"
            
            
    #Images of the screen
    background = pygame.image.load("rsc/window_scoreboard.png")


    #Background
    scoreboard_screen.blit(pygame.transform.scale(background,(weight, height)),(0,0))
    
    #Call the functions of the multi_line_reader
    multi_line_reader(scoreboard_screen, txt, -(410),200, font,(255,255,255), justification="center")
    img_return=pygame.image.load("rsc/btn_return.png")
    cursor = Cursor()
    bt_return =Button(img_return,img_return,(weight-bt_weight-10),(height-100),bt_weight,bt_heigth)
    pygame.display.update()
    #While of the loop
    exit_ = False
    while exit_ != True:
        clock.tick(60)
        #Set the blits in the screen
        bt_return.update(scoreboard_screen,cursor)
        pygame.display.update()
        cursor.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_return.rect):
                    exit_ = True
                    print("Push Return Menu")
                    pygame.quit()
                    main_window()
                    break
                    
    pygame.quit()

def transition_login(user, window):
    #Load the csv
    csv_scoreboard = csv_class("ScoreBoard.csv","rt")
    matrix = csv_scoreboard.get_matrix()
    #Set the matrix empty
    matrix_v = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    #Set the initial level,avatars and score.
    level = 1
    currency = 150
    avatars_killed = 0
    seconds = 0
    minutes = 0
    initial_scoreboard = " 0 "
    found = False
    global row_M
    row_M = 0
    #If the matrix is not empty, search the user
    if matrix != []:
        for usr in matrix:
            if usr[0] == user and usr[2] == "loser":
                found = True
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv","w")
                if window == "main_window":
                    main_window()
                if window == "principal_window":
                    principal_window()
            else:
                row_M += 1
        #If the user is not found, creat a new user.
        if not found:     
            matrix.append([user, initial_scoreboard, "loser", matrix_v, level, avatars_killed,currency, minutes, seconds])
            csv_scoreboard.write(matrix)
            csv_scoreboard.update_matrix("ScoreBoard.csv","w")
            main_window()
    #Whe the matrix is empty, add the user
    else:
        matrix.append([user, initial_scoreboard, "loser", matrix_v, level, avatars_killed,currency])
        csv_scoreboard.write(matrix)
        csv_scoreboard.update_matrix("ScoreBoard.csv","w")
        main_window()

def multi_line_reader(screen, txt, x,y, font,colour=(128,128,128), justification="left"):
    def update():
        screen.blit(bitmap, (xpos, y))
    justification = justification[0].upper()
    text = txt.strip().replace('\r','').split('\n')
    max_width = 0
    text_bitmaps = []
    #Convert line a line, in bits to represent in screen
    for line in text:
        text_bit_map = font.render(line, True, colour)
        text_width  = text_bit_map.get_width()
        text_bitmaps.append((text_width, text_bit_map))
        if (max_width < text_width):
            max_width = text_width
    # Paint all the text bitmaps to the screen with justification
    for (width, bitmap) in text_bitmaps:
        xpos = x
        width_diff = max_width - width
        if (justification == 'R'):  # right-justify
            xpos = x + width_diff
        elif (justification == 'C'): # centre-justify
            xpos = (width_diff // 2)-x
        update()
        y += bitmap.get_height()

login_window()
#game_over()
    
