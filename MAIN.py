"""Avatar vs Rooks"""
"""Members"""
#Marco Gonzales
#Diego Garcia 2020124283
#Kenneth Castillo 2019062984
"""Libraries"""
#######################COSAS POR CAMBIAR#######################
# HACER LA VARIABLE ROW GLOBAL
#
###############################################################

from CLASSES import *
from pygame import *

"""Functions"""
def principal_window():
    global row
    #Settings of the screen
    pygame.init()
    weight, height = 952,768
    screen = pygame.display.set_mode((weight,height))
    
    #CSV Archive
    csv_scoreboard = csv_class("ScoreBoard.csv","rt")

    #Matrix
    matrix = csv_scoreboard.get_matrix()
    
    #Settings of the bottons
    bt_weight,bt_heigth = 150,75

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
            if event.type == pygame.QUIT:
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv","w")
                exit_ = True
                pygame.quit()
                break
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
                if cursor.colliderect(bt_scoreboard.rect):
                    print("Push Scoreboard")
                    exit_ = True
                    pygame.quit()
                    scoreboard_window()
                    break



        

    pygame.quit()

def credits_window():
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

        pygame.display.update()
        clock.tick(60)
        
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
                    principal_window()
                    break
                
        
    pygame.quit()

def login_window():
    #import pygame_textinput
    #Settings of the screen
    pygame.init()
    pygame.font.init
    weight, height = 500,400
    login_screen = pygame.display.set_mode((weight,height))
    
    
    
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
                exit_ = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(bt_login.rect):
                    if text != "" and int(parameter)>0:
                        print("Push Login")
                        exit_ = True
                        pygame.quit()
                        transition_login(text)
                        break
                    
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


    #Background
    help_screen.blit(pygame.transform.scale(background,(weight, height)),(0,0))
    
    #Call the functions of the multi_line_reader
    multi_line_reader(help_screen, txt, 20,190, font,(255,255,255), justification="left-justify")
    img_return=pygame.image.load("rsc/btn_return.png")
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
                    principal_window()
                    break
    pygame.quit()
def scoreboard_window():
    #Settings of the screen
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

    txt = ""
    for line in matrix_csv:
        txt += "\n"
        txt += "\n"
        for t in line:
            txt += str(t)
            
    #Images of the screen
    background = pygame.image.load("rsc/window_scoreboard.png")


    #Background
    scoreboard_screen.blit(pygame.transform.scale(background,(weight, height)),(0,0))
    
    #Call the functions of the multi_line_reader
    multi_line_reader(scoreboard_screen, txt, -(470),200, font,(255,255,255), justification="center")
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
                    principal_window()
                    break
                    
    pygame.quit()

def transition_login(user):
    csv_scoreboard = csv_class("ScoreBoard.csv","rt")
    matrix = csv_scoreboard.get_matrix()
    
    initial_scoreboard = " 0 "
    found = False
    global row
    row = 0
    if matrix != []:
        for usr in matrix:
            if usr[0] == user:
                found = True
                csv_scoreboard.write(matrix)
                csv_scoreboard.update_matrix("ScoreBoard.csv","w")
                principal_window()
            else:
                row += 1
        if not found:     
            matrix.append((user, initial_scoreboard))
            csv_scoreboard.write(matrix)
            csv_scoreboard.update_matrix("ScoreBoard.csv","w")
            principal_window()
    else:
        matrix.append([user, initial_scoreboard])
        csv_scoreboard.write(matrix)
        csv_scoreboard.update_matrix("ScoreBoard.csv","w")
        principal_window()

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
    
    
