import pygame
from CLASSES import *


def principal_window():
    pygame.init()
    width , height = 1000, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Window")


    #Set clock
    clock = pygame.time.Clock()
    FPS = 60

    #CSV Archive
    csv_scoreboard = csv_class("ScoreBoard.csv", "rt")

    #Matrix
    matrix = csv_scoreboard.get_matrix()

    #Set font
    font = pygame.font.Font("triforce.ttf", 40)

    #Images of the screen
    background = pygame.image.load("images/background_1.png")
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

    #Create the buttons and cursor
    cursor = Cursor()
    bt_sandRook = Button(img_sandRook, img_sandRook_b, 0, 150, 150, 150)
    bt_rockRook = Button(img_rockRook, img_rockRook_b, 0, 310, 150, 150)
    bt_fireRook = Button(img_fireRook, img_fireRook_b, 0, 460, 150, 150)
    bt_waterRook = Button(img_waterRook, img_waterRook_b, 0, 625, 150, 150)

    
    #Set timer
    second = 0
    minute = 0

    #Set currency
    currency = 0


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
                    break
                if cursor.colliderect(bt_rockRook.rect):
                    break
                if cursor.colliderect(bt_fireRook.rect):
                    break
                if cursor.colliderect(bt_waterRook.rect):
                    break


        clock.tick(FPS)

        #Timer
        second += 1 / FPS
        if second >= 60:
            minute += 1
            second = 0
        timer_text = font.render(": ".join([str(int(minute)), str(int(second)).zfill(2)]), True, (255, 255, 255))

        #User
        user = font.render('PEPITO', True, (255, 255, 255))
        #Combinar login con esto para que el user sea el que hizo el login

        #Currency
        currency = 9999
        currency_text = font.render(str(currency), True, (255, 255, 255))

        #Update screen
        screen.blit(pygame.transform.scale(background, (width, height)), (0, 0))
        screen.blit(timer_text, (210,5))
        screen.blit(user, (10,5))
        screen.blit(img_currency, (790, -15))
        screen.blit(currency_text, (890, 15))

        # Place buttons in the screen
        cursor.update()
        bt_sandRook.update(screen, cursor)
        bt_rockRook.update(screen, cursor)
        bt_fireRook.update(screen, cursor)
        bt_waterRook.update(screen, cursor)

        pygame.display.update()

    pygame.quit()

'''def pause_window():
    if paused == True:
        bt_continue = Button()
        bt_exit = Button()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_continue):
                    pause = False
                if cursor.colliderect(bt_exit.rect):
                    csv_scoreboard.write(matrix)
                    csv_scoreboard.update_matrix("ScoreBoard.csv", "w")
                    exit = True
'''
principal_window()
