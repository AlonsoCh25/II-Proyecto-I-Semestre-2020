import pygame

canibales = pygame.sprite.Group()
FPS = 60

"""__________________________________________________________________________________"""

class Canibal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('canibalA.png')
        self.rect = self.imagen.get_rect()
        self.attack_time = 3
        self.movement_time = 14
        self.health = 25
        self.damage = 12
        self.spawn = False
        self.rect.centerx = 400 #hay que ver como definimos el spawn
        self.rect.bottom = 600 #^^^^^^^^
        self.counter_pos = 0
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
            self.imagen = pygame.image.load("canibalB.png")
            self.change_pos = 10
            self.counter_pos += 1
            if self.counter_pos >= self.change_pos:
                self.imagen = pygame.image.load("canibalA.png")
                self.counter_pos = 0
                self.counter_attack = 0

    def rect(self):
        return self.rect