import pygame
from Flechador import flechas, flechadores, Flechador, Flecha
from Escudero import espadas, escuderos, Escudero, Espada
from Lenador import lenadores, Lenador
from Canibal import canibales, Canibal

'''Archivo .py para probar las animaciones/ver los sprites importandolos de otros
documentos .py que contienen las clases.'''

white = 255,255,255
width = 600
height = 800
FPS = 60

avatars = pygame.sprite.Group()


def main():

    pygame.init()
    pantalla = pygame.display.set_mode((width, height))
    salir = False
    reloj = pygame.time.Clock()

    '''Para la implementacion en el juego real esto tiene que cambiarse puesto a que 
    de esta manera solo deja implementar un sprite del mismo tipo a la vez'''
    flechador = Flechador()
    flechadores.add(flechador)
    escudero = Escudero()
    escuderos.add(escudero)
    lenador = Lenador()
    lenadores.add(lenador)
    canibal = Canibal()
    canibales.add(canibal)
    avatars.add(flechador, escudero, lenador, canibal)

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        reloj.tick(FPS)
        pantalla.fill(white)

        '''Para la implementacion en el juego real esto tiene que cambiarse puesto a que 
            de esta manera siempre van a aparecer los sprites y no va a ser de manera
            aleatoria.'''
        flechador.spawn = True
        escudero.spawn = True
        lenador.spawn = True
        canibal.spawn = True
        if flechador.spawn == True:
            flechadores.update(pantalla)
            flechas.update(pantalla)
            flechador.attack()
        if escudero.spawn == True:
            escuderos.update(pantalla)
            escudero.attack()
        if lenador.spawn == True:
            lenadores.update(pantalla)
            lenador.attack()
        if canibal.spawn == True:
            canibales.update(pantalla)
            canibal.attack()

        pygame.display.update()

    pygame.quit()

main()