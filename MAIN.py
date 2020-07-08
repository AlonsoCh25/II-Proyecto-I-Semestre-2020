"""Avatar vs Rooks"""
"""Members"""
#Marco Gonzales
#Diego Garcia 2020124283
#Kenneth Castillo 2019062984
"""Libraries"""
import CSV
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

principal_window()
    
    
