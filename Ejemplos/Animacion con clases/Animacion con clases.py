import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
    def mover(self, vel):
        self.rect = self.rect.move(vel)
    def update(self, superficie):
        superficie.blit(self.imagen,self.rect)
    def rect(self):
        return self.rect

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800,600))
    salir = False
    black = 0, 0, 0
    
    reloj= pygame.time.Clock()
    
    ball = pygame.image.load("ball.png")
    ball_b = pygame.image.load("ball_b.png")

    Bola = Ball(ball)
    vel_Bola = [1,0]
    
    Bola_b = Ball(ball_b)
    vel_Bola_b = [0,1]
    
    
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                
        Bola.mover(vel_Bola)
        if (Bola.rect).left < 0 or (Bola.rect).right > 800:
            vel_Bola[0] = -vel_Bola[0]
            
        Bola_b.mover(vel_Bola_b)
        if (Bola_b.rect).top < 0 or (Bola_b).rect.bottom > 600:
            vel_Bola_b[1] = -vel_Bola_b[1]

        reloj.tick(500)
        pantalla.fill(black)
        Bola.update(pantalla)
        Bola_b.update(pantalla)
        pygame.display.update()
    
    pygame.quit()

main()


