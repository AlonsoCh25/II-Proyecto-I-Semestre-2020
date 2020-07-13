"""Avatar vs Rooks"""
"""Members"""
#Marco Gonzales
#Diego Garcia 2020124283
#Kenneth Castillo 2019062984
"""Libraries"""
from CLASSES import *
from pygame import *

"""Functions"""
def principal_window(row):
    #Settings of the screen
    pygame.init()
    weight, height = 952,768
    screen = pygame.display.set_mode((weight,height))
    
    #CSV Archive
    csv_scoreboard = csv_class("ScoreBoard.csv","rt")

    #Matrix
    matrix = csv_scoreboard.get_matrix()
    
    #Settings of the bottons
    bt_weight,bt_heigth = 200,150

    #Fonts
    font_user = pygame.font.Font("triforce.ttf",40)

    #Text
    user_text = matrix[row][0] 
    scoreboard_text = "ScoreBoard:" +" "+ matrix[row][1]
    
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
        screen.blit(txt_user,(0,0))
        screen.blit(txt_scoreboard,(0,40))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv","w")
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
                    csv_scoreboard.write(matrix)
                    csv_scoreboard.update_matrix("ScoreBoard.csv","w")
                    exit_ = True
                if cursor.colliderect(bt_help.rect):
                    print("Push Help")
                    help_window()
                    exit_ = True
                    pygame.quit()
                    break
                
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

def login_window():
    #import pygame_textinput
    #Settings of the screen
    pygame.init()
    pygame.font.init
    weight, height = 400,300
    login_screen = pygame.display.set_mode((weight,height))
    
    
    
    #FONT
    font = pygame.font.Font(None,30)
    font_user = pygame.font.Font("triforce.ttf",40)
    
    #Text input
    box_input = pygame.Rect(100, 110, 140, 32)

    #Color of the box
    color_inactive = (0,0,0)
    color_active = (255,255,255)
    color = color_inactive

    #Set the initial active of the box
    active = False

    #Content the text of the user
    text = ''
    User = "User Name"

    #render the elements
    txt_user = font_user.render(User, True, (0,0,0))
    user_rect = txt_user.get_rect()
    
    #Sttings of the bottons
    bt_weight,bt_heigth = 200,150
    
    #Set initial clock
    clock = pygame.time.Clock()
    
    #Images of the screen
    background = pygame.image.load("rsc/background.jpeg")
    img_login = pygame.image.load("rsc/btn_login.png")
    img_login_b = pygame.image.load("rsc/btn_login_b.png")
    
    
    
    #Buttons of the screen
    cursor = Cursor()
    bt_login = Button(img_login,img_login_b,(weight/2-(bt_weight/2)),(weight/3+20),bt_weight,bt_heigth)

    
    pygame.display.update()
    #While of the loop
    exit_ = False
    while exit_ != True:
        #Background
        login_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))

        #render the elements
        txt = font.render(text, True, (0,0,0))
        
        #Scale the boxof the text
        width = max(100, txt.get_width()+10)
        box_input.w = width
        box_input.x = round((weight//2)-(width//2))
        
                                
        
        
        #Set the blits in the screen
        login_screen.blit(txt, (box_input.x+5, box_input.y+5))
        pygame.draw.rect(login_screen, color, box_input, 2)
        bt_login.update(login_screen,cursor)
        login_screen.blit(txt_user,(round(((weight/2)-(user_rect.w/2))),60))
        
        cursor.update()

        
        pygame.display.update()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_login.rect):
                    transition_login(text)
                    print("Push Login")
                    exit_ = True
                    
                # when the user click in the box, this is active
                if box_input.collidepoint(event.pos):
                    # Set the value of the variable
                    active = not active
                else:
                    active = False
                #Set the current color of the box
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
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

def transition_login(user):
    csv_scoreboard = csv_class("ScoreBoard.csv","rt")
    matrix = csv_scoreboard.get_matrix()
    
    initial_scoreboard = "0"
    found = False
    row = 0
    if matrix != []:
        for usr in matrix:
            if usr[0] == user:
                found = True
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv","w")
                principal_window(row)
            else:
                row += 1
        if not found:     
            matrix.append((user, initial_scoreboard))
            csv_scoreboard.write(matrix)
            csv_scoreboard.update_matrix("ScoreBoard.csv","w")
            principal_window(row)
    else:
        matrix.append([user, initial_scoreboard])
        csv_scoreboard.write(matrix)
        csv_scoreboard.update_matrix("ScoreBoard.csv","w")
        principal_window(row)

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
    
    
