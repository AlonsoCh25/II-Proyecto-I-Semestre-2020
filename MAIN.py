"""Avatar vs Rooks"""
"""Members"""
#Marco Gonzales
#Diego Garcia 2020124283
#Kenneth Castillo 2019062984
"""Libraries"""
import CLASSES
import pygame

"""Functions"""
def principal_window():
    #Settings of the screen
    pygame.init()
    weight, height = 800,600
    screen = pygame.display.set_mode((weight,height))
    
    #Set initial clock
    clock = pygame.time.Clock()
    
    #Images of the screen
    background = pygame.image.load("rsc/menu_game.png")

    #While of the loop
    exit_ = False
    while exit_ != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True

        clock.tick(60)
        pygame.display.update()
        screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))

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
    
    #Call the functions of the multi_line_reader
    multi_line_reader(credits_screen, txt, 20,20, font, (255,255,255), justification="left")

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
    credits_screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))
    
    #Call the functions of the multi_line_reader
    multi_line_reader(help_screen, txt, 20,20, font, (255,255,255), justification="left")

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


def multi_line_reader(screen, txt, x,y, font, colour=(128,128,128), justification="left"):
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
            xpos = x + (width_diff // 2)
        screen.blit(bitmap, (xpos, y) )
        y += bitmap.get_height()


principal_window()
    
    
