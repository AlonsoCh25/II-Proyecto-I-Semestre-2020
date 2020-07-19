import pygame
import random
#import playsound
from CLASSES import *
from Sand import sand_attacks, Sand, SandAttack
from Rock import rock_attacks, Rock, RockAttack
from Fire import fire_attacks, Fire, FireAttack
from Water import water_attacks, Water, WaterAttack
from Archer import arrows, Archer, Arrow
from Squire import axes, Squire, Sword
from Lumber import sticks, Lumberjack, Stick
from Cannibal import hammers, Cannibal, Hammer
from MAIN import *
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
print("LEI ESTo")
global row_M
row_M = 0
global parameter
parameter = 0

#Set cursor
cursor = Cursor()

#Load the csv
csv_scoreboard = csv_class("ScoreBoard.csv","rt")
matrix = csv_scoreboard.get_matrix()

#Set matrix
gridMatrix = matrix[row_M][3]
print(gridMatrix)

#Set selected
selected = ''

#Set counters
contador = 0
contador_2 = 0
contador_3 = 0

#Set currency
currency = matrix[row_M][6]

#Set FPS
FPS = 30

#Set crystals
img_crystal25 = pygame.image.load('images/25_crystal.png')
img_crystal50 = pygame.image.load('images/50_crystal.png')
img_crystal100 = pygame.image.load('images/100_crystal.png')

#Set level
level = matrix[row_M][4]

#Set column, row of grid
group = 0

#Set attack speed
attack_speed = parameter

#Set avatars spawn timer
avatar_spawnTime = 4
if level == 2:
    avatar_spawnTime = 4 - (4 * 0.3)
elif level == 3:
    avatar_spawnTime = 4 - (4 * 0.6)

#Set max avatar spawn
spawn_avatars = True
contador_avatars = 0
max_avatars = 15
if level == 2:
    max_avatars = 15 + int(15 * 0.3)
if level == 3:
    max_avatars = 15 + int(15 * 0.6)

avatars_left = max_avatars
avatars_killed = matrix[row_M][5]

# Set background
background = pygame.image.load("images/background_1.png")
if level == 2:
    background = pygame.image.load("images/background_2.png")
elif level == 3:
    background = pygame.image.load("images/background_3.png")



# Set new level variables
new_level = False
new_avatars = True
winner = matrix[row_M][2]

#Set move variables
archermove = True
squiremove = True
lumbermove = True
cannibalmove = True


def next_level():
    global level, gridMatrix, max_avatars, avatar_spawnTime, background, new_level, new_avatars, avatars_left, avatars_killed, contador_3, contador_avatars, winner

    if new_level == True:
        level += 1
        if level > 3:
            winner = 'winner'
            '''background = pygame.image.load('images/winner.png')
            pygame.mixer_music.stop()
            pygame.mixer_music.load('Sounds/Winner.mp3')
            pygame.mixer_music.play()
            gridMatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            sand_attacks.empty()
            rock_attacks.empty()
            fire_attacks.empty()
            water_attacks.empty()
            sandrooks.empty()
            rockrooks.empty()
            firerooks.empty()
            waterrooks.empty()
            rooks.empty()'''

        if level == 2:
            pygame.mixer_music.stop()
            max_avatars = 15 + int(15 * 0.3)
            avatars_left = max_avatars
            background = pygame.image.load("images/background_2.png")
            avatar_spawnTime = 4 - (4 * 0.3)
            avatars_killed = 0
            contador_3 = 0
            contador_avatars = 0
            pygame.mixer_music.load('Sounds/Battle2.mp3')
            pygame.mixer.music.play()
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
            pygame.mixer_music.load('Sounds/Battle3.mp3')
            pygame.mixer.music.play()
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

def avatar_spawn():
    global contador_3, contador_avatars, FPS, currency, avatar_spawnTime, spawn_avatars, gridMatrix, new_avatars
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


def avatar_functions():
    global archermove, squiremove, lumbermove, cannibalmove, currency, avatars_left, avatars_killed
    for archer in archeravatars:
        archer.move(archermove)
        for allrooks in rooks:
            if (archer.rect.top + 100) >= allrooks.rect.top and archer.rect.left == allrooks.rect.left:
                archermove = False
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
        for allrooks in rooks:
            if (squire.rect.top + 100) >= allrooks.rect.top and squire.rect.left == allrooks.rect.left:
                squiremove = False
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
        for allrooks in rooks:
            if (lumber.rect.top + 100) >= allrooks.rect.top and lumber.rect.left == allrooks.rect.left:
                lumbermove = False
                lumber.attack()
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
        for allrooks in rooks:
            if (cannibal.rect.top + 100) >= allrooks.rect.top and cannibal.rect.left == allrooks.rect.left:
                cannibalmove = False
                cannibal.attack()
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


def button_matrix(posx, posy, column, row, button, screen):
    global selected, currency, rooks, all_sprites, sand_rook, attack_speed

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
                            sandrooks.add(Sand(attack_speed, posx, posy))
                            rooks.add(sandrooks)
                    if selected == 'ROCKROOK':
                        if currency >= 100:
                            gridMatrix[row][column] = 2
                            selected = ''
                            currency -= 100
                            rockrooks.add(Rock(attack_speed, posx, posy))
                            rooks.add(rockrooks)
                    if selected == 'FIREROOK':
                        if currency >= 150:
                            gridMatrix[row][column] = 3
                            selected = ''
                            currency -= 150
                            firerooks.add(Fire(attack_speed, posx, posy))
                            rooks.add(firerooks)
                    if selected == 'WATERROOK':
                        if currency >= 150:
                            gridMatrix[row][column] = 4
                            selected = ''
                            currency -= 150
                            waterrooks.add(Water(attack_speed, posx, posy))
                            rooks.add(waterrooks)
            if selected == 'REMOVE' and gridMatrix[row][column] != 0:
                gridMatrix[row][column] = 0
                selected = ''
                pygame.sprite.spritecollide(cursor_rect, rooks, True)


def damage_rooks():
    global health_fireRook, health_waterRook, group

    for sand_rook in sandrooks:
        if pygame.sprite.groupcollide(sandrooks, arrows, False, True):
                sand_rook.decrease_health(2)
        elif pygame.sprite.groupcollide(sandrooks, axes, False, True):
            for sand_rook in sandrooks:
                sand_rook.decrease_health(3)
        elif pygame.sprite.groupcollide(sandrooks, sticks, False, True):
                sand_rook.decrease_health(9)
        elif pygame.sprite.groupcollide(sandrooks, hammers, False, True):
                sand_rook.decrease_health(12)
        if sand_rook.health <= 0:
            gridMatrix[((sand_rook.rect.left - 295) / 95)][((sand_rook.rect.top - 209) / 80)] = 0
            sand_rook.kill()


    for rock_rook in rockrooks:
        if pygame.sprite.groupcollide(rockrooks, arrows, False, True):
                rock_rook.decrease_health(2)
        if pygame.sprite.groupcollide(rockrooks, axes, False, True):
                rock_rook.decrease_health(3)
        elif pygame.sprite.groupcollide(rockrooks, sticks, False, True):
                rock_rook.decrease_health(9)
        elif pygame.sprite.groupcollide(rockrooks, hammers, False, True):
                rock_rook.decrease_health(12)
        if rock_rook.health <= 0:
            rock_rook.kill()

    for fire_rook in firerooks:
        if pygame.sprite.groupcollide(firerooks, arrows, False, True):
            fire_rook.decrease_health(2)
        if pygame.sprite.groupcollide(firerooks, axes, False, True):
            fire_rook.decrease_health(3)
        elif pygame.sprite.groupcollide(firerooks, sticks, False, True):
            fire_rook.decrease_health(9)
        elif pygame.sprite.groupcollide(firerooks, hammers, False, True):
            fire_rook.decrease_health(12)
        if fire_rook.health <= 0:
            fire_rook.kill()

    for water_rook in waterrooks:
        if pygame.sprite.groupcollide(waterrooks, arrows, False, True):
            water_rook.decrease_health(2)
        if pygame.sprite.groupcollide(waterrooks, axes, False, True):
            water_rook.decrease_health(3)
        elif pygame.sprite.groupcollide(waterrooks, sticks, False, True):
            water_rook.decrease_health(9)
        elif pygame.sprite.groupcollide(waterrooks, hammers, False, True):
            water_rook.decrease_health(12)
        if water_rook.health <= 0:
            water_rook.kill()


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


def principal_window():
    global selected, currency, buttons, FPS, background, rooks, all_sprites, gridMatrix, level, avatar_spawnTime, new_level, avatars_left, avatars_killed
    #Place an icon on the window
    icon = pygame.image.load("rsc/logo_game.png")
    pygame.display.set_icon(icon)

    pygame.mixer.init()
    pygame.init()
    width , height = 1000, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Window")

    print(row_M, "In Game")
    #Set clock
    clock = pygame.time.Clock()

    #CSV Archive
    csv_scoreboard = csv_class("ScoreBoard.csv", "rt")

    #Matrix
    matrix = csv_scoreboard.get_matrix()
    gridMatrix = matrix[row_M][3]

    #Set currency
    currency = matrix[row_M][6]

    level = matrix[row_M][4]

    avatars_killed = matrix[row_M][5]
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
    second = 0
    minute = 0

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
    pygame.mixer_music.load('Sounds/Battle1.mp3')
    pygame.mixer.music.play()

    #While loop
    exit = False
    #pause = False
    while exit != True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv", "w")
                exit = True

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
        print(row_M)
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
            next_level()


        pygame.display.update()

    pygame.quit()
