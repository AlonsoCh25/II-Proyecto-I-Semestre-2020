import pygame

espadas = pygame.sprite.Group()
escuderos = pygame.sprite.Group()
FPS = 60

"""__________________________________________________________________________________"""

class Escudero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('escudero.png')
        self.rect = self.imagen.get_rect()
        self.attack_time = 15
        self.movement_time = 10
        self.health = 10
        self.damage = 3
        self.spawn = False
        self.rect.centerx = 400 #hay que ver como definimos el spawn
        self.rect.bottom = 250 #^^^^^^^^
        self.counter_attack = 0
        self.counter_move = 0

    def update(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def mover(self):
        self.counter_move += 1
        if self.counter_move >= self.movement_time*FPS:
            #hay que implementar codigo para moverse una casilla
            self.counter_move = 0

    def attack(self):
        self.counter_attack += 1
        if self.counter_attack >= self.attack_time*FPS:
            espada = Espada(self.rect.centerx, self.rect.bottom)
            espadas.add(espada)
            escuderos.add(espada)
            self.counter_attack = 0

    def rect(self):
        return self.rect

"""__________________________________________________________________________________"""

class Espada(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("espada.png")
        self.rect = self.imagen.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.top > 800:
            self.kill()
        superficie.blit(self.imagen, self.rect)