"""Avatar vs Rooks"""
"""Members"""
#Marco Gonzales
#Diego Garcia 2020124283
#Kenneth Castillo 2019062984
"""Libraries"""
from CLASSES import *
import pygame

"""Functions"""
def principal_window():
    #Settings of the screen
    pygame.init()
    weight, height = 952,768
    screen = pygame.display.set_mode((weight,height))
    
    #Sttings of the bottons
    bt_weight,bt_heigth = 200,150

    
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
    bt_credits = Button(img_credits,img_credits_b,(weight-bt_weight),0,bt_weight,bt_heigth)
    bt_exit = Button(img_exit,img_exit_b,(weight-bt_weight),(height-200),bt_weight,bt_heigth)
    bt_help = Button(img_help,img_help_b,(weight-bt_weight),100,bt_weight,bt_heigth)
    bt_login = Button(img_login,img_login_b,(weight/2-(bt_weight/2)),(weight/2),bt_weight,bt_heigth)
    bt_play = Button(img_play,img_play_b,(weight/2-(bt_weight/2)),(weight/2+100),bt_weight,bt_heigth)
    bt_scoreboard = Button(img_scoreboard,img_scoreboard_b,(weight-bt_weight),200,bt_weight,bt_heigth)
    
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

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_credits.rect):
                    print("Push credits")
                    credits_window()
                    exit_ = True
                    pygame.quit()
                    break
                if cursor.colliderect(bt_exit.rect):
                    print("push_exit")
                    exit_ = True
                if cursor.colliderect(bt_help.rect):
                    print("Push Help")
                    help_window()
                    exit_ = True
                    pygame.quit()
                    break
                if cursor.colliderect(bt_login.rect):
                    print("Push Login")
                if cursor.colliderect(bt_play.rect):
                    print("Push Play")
                if cursor.colliderect(bt_scoreboard.rect):
                    print("Push Scoreboard")


        

    pygame.quit()

def credits_window():
    #Settings of the screen
    pygame.init()
    pygame.font.init
    weight, height = 800,600
    credits_screen = pygame.display.set_mode((weight,height))
    
    #FONT
    font = pygame.font.Font(None,20)
    
    #Set initial clock
    clock = pygame.time.Clock()
    
    #Load the txt
    a_txt = open("credits.txt")
    txt = a_txt.read()
    
    #Images of the screen
    background = pygame.image.load("rsc/background.jpeg")
    
    #Background
    credits_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))

    y = height-200
    #Call the functions of the multi_line_reader
    multi_line_reader(credits_screen, txt, 20,20, font,(255,255,255), justification="center")
    
    pygame.display.update()

    
    #While of the loop
    exit_ = False
    while exit_ != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True
                
        #Set the blits in the screen
        

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    
def help_window():
    #Settings of the screen
    pygame.init()
    pygame.font.init
    weight, height = 800,600
    help_screen = pygame.display.set_mode((weight,height))
    
    #FONT
    font = pygame.font.Font(None,20)
    
    #Set initial clock
    clock = pygame.time.Clock()
    
    #Load the txt
    a_txt = open("help.txt")
    txt = a_txt.read()
    
    #Images of the screen
    background = pygame.image.load("rsc/background.jpeg")
    
    #Background
    help_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))
    
    #Call the functions of the multi_line_reader
    multi_line_reader(help_screen, txt, 20,20, font,(255,255,255), justification="left")

    pygame.display.update()
    #While of the loop
    exit_ = False
    while exit_ != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True

        clock.tick(60)
        pygame.display.update()
        #Set the blits in the screen

    pygame.quit()


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

principal_window()
    
    
