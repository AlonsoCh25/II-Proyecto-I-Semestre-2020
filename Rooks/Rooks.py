import pygame
import random
from Sand import sand_attacks, sand_rooks, Sand, SandAttack
from Rock import rock_attacks, rock_rooks, Rock, RockAttack
from Fire import fire_attacks, fire_rooks, Fire, FireAttack
from Water import water_attacks, water_rooks, Water, WaterAttack

'''Archivo .py para probar las animaciones/ver los sprites importandolos de otros
documentos .py que contienen las clases.'''

white = 255,255,255
width = 600
height = 800
FPS = 60

rooks = pygame.sprite.Group()





def main():

    pygame.init()
    pantalla = pygame.display.set_mode((width, height))
    salir = False
    reloj = pygame.time.Clock()
    spawn_counter = 0
    spawn = 120

    '''Para la implementacion en el juego real esto tiene que cambiarse puesto a que 
    de esta manera solo deja implementar un sprite del mismo tipo a la vez'''
    sandrook = Sand(5)
    sand_rooks.add(sandrook)
    rockrook = Rock(5)
    rock_rooks.add(rockrook)
    firerook = Fire(5)
    fire_rooks.add(firerook)
    waterrook = Water(5)
    water_rooks.add(waterrook)
    rooks.add(waterrook, rockrook, firerook, waterrook)


    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        reloj.tick(FPS)
        pantalla.fill(white)
        print(sand_attacks)
        print(sand_rooks)


        '''Para la implementacion en el juego real esto tiene que cambiarse puesto a que 
            de esta manera siempre van a aparecer los sprites y no va a ser de manera
            aleatoria.'''
        sandrook.spawn = True
        rockrook.spawn = True
        firerook.spawn = True
        waterrook.spawn = True
        if sandrook.spawn == True:
            sand_rooks.update(pantalla)
            sand_attacks.update(pantalla)
            sandrook.attack()
        if rockrook.spawn == True:
            rock_rooks.update(pantalla)
            rock_attacks.update(pantalla)
            rockrook.attack()
        if firerook.spawn == True:
            fire_rooks.update(pantalla)
            fire_attacks.update(pantalla)
            firerook.attack()
        if waterrook.spawn == True:
            water_rooks.update(pantalla)
            water_attacks.update(pantalla)
            waterrook.attack()

        pygame.display.update()

    pygame.quit()

main()