import pygame

#Clase para saber la posicion del cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0,0,1,1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

#Clase para crear los botones se requiere dos imagenes preferiblemente para una mejor
#estetica para cuando el cursor este sobre el boton este brille
class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen1, imagen2, x, y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x,y)
    def update(self, pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual, self.rect)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    salir = False
    black = 0, 0, 0
    white = 255, 255, 255
    reloj = pygame.time.Clock()
    colordefondo = black

    #Aqui se cargan las imagenes
    bola1 = pygame.image.load("ball.png")
    bola2 = pygame.image.load("ball_b.png")

    #Aqui se da la creacion de los botones y cursor
    cursor = Cursor()
    boton = Boton(bola1, bola2, 350, 100)
    boton2 = Boton(bola2, bola1, 350, 300)
    #Al boton se requiere pasarle la foto inactiva foto activa y cordenadas x y y en ese orden

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

            #Evento para checkar si cuando se da un click el mouse se encuentra sobre
            #alguno de los botones
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton.rect):
                    #Aqui se pone la accion que queremos que haga cuando se hace click en el boton
                    #En este caso solo puse que cambiara de fondo
                    colordefondo = white
                if cursor.colliderect(boton2.rect):
                    colordefondo = black

        reloj.tick(60)
        pantalla.fill(colordefondo)

        #Esto hace que aparezcan en pantalla
        boton.update(pantalla, cursor)
        boton2.update(pantalla, cursor)
        cursor.update()

        pygame.display.update()

    pygame.quit()

main()
