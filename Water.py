import pygame

water_attacks = pygame.sprite.Group()
water_rooks = pygame.sprite.Group()
FPS = 60

"""__________________________________________________________________________________"""

class Water(pygame.sprite.Sprite):
    def __init__(self, attack_time):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('water.png')
        self.rect = self.imagen.get_rect()
        self.attack_time = attack_time
        self.health = 16
        self.damage = 8
        self.cost = 150
        self.spawn = False
        self.rect.centerx = 400 #hay que ver como definimos el spawn
        self.rect.bottom = 600 #^^^^^^^^
        self.counter_attack = 0

    def update(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def spawn(self):
        #argumento if
            self.spawn = True #hay que ver como definimos el spawn de estas tambien

    def attack(self):
        self.counter_attack += 1
        if self.counter_attack >= self.attack_time*FPS:
            water = WaterAttack(self.rect.centerx, self.rect.bottom)
            water_attacks.add(water)
            water_rooks.add(water)
            self.counter_attack = 0

    def rect(self):
        return self.rect

"""__________________________________________________________________________________"""

class WaterAttack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("water_attack.png")
        self.rect = self.imagen.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        superficie.blit(self.imagen, self.rect)