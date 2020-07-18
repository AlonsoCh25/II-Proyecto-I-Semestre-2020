import pygame

sand_attacks = pygame.sprite.Group()
sand_rooks = pygame.sprite.Group()
FPS = 30

"""__________________________________________________________________________________"""

class Sand(pygame.sprite.Sprite):
    def __init__(self, attack_time, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/rooks/sand_rook_a.png')
        self.image = pygame.transform.scale(self.image, (95,80))
        self.rect = self.image.get_rect()
        self.attack_time = attack_time
        self.health = 12
        self.damage = 2
        self.rect.left = x
        self.rect.top = y
        self.counter_attack = 0

    def update(self, superficie):
        superficie.blit(self.image, self.rect)

    def remove(self):
        self.kill()

    def spawn(self):
        #argumento if
            self.spawn = True #hay que ver como definimos el spawn de estas tambien

    def attack(self):
        self.counter_attack += 1
        if self.counter_attack >= self.attack_time * FPS:
            sand = SandAttack(self.rect.centerx, self.rect.bottom)
            sand_attacks.add(sand)
            sand_rooks.add(sand)
            self.counter_attack = 0

    def health(self):
        pass

    def rect(self):
        return self.rect

"""__________________________________________________________________________________"""

class SandAttack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("images/rooks/sand_attack.png")
        self.rect = self.imagen.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        superficie.blit(self.imagen, self.rect)