import pygame

fire_attacks = pygame.sprite.Group()
fire_rooks = pygame.sprite.Group()
FPS = 30

"""__________________________________________________________________________________"""

class Fire(pygame.sprite.Sprite):
    def __init__(self, attack_time, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/rooks/fire_rook_a.png")
        self.image = pygame.transform.scale(self.image, (95, 80))
        self.rect = self.image.get_rect()
        self.attack_time = attack_time
        self.health = 16
        self.damage = 8
        self.rect.x = x
        self.rect.y = y
        self.counter_attack = 0

    def update(self, superficie):
        superficie.blit(self.image, self.rect)

    def spawn(self):
        #argumento if
            self.spawn = True #hay que ver como definimos el spawn de estas tambien

    def attack(self):
        self.counter_attack += 1
        if self.counter_attack >= self.attack_time*FPS:
            fire = FireAttack(self.rect.centerx, self.rect.bottom)
            fire_attacks.add(fire)
            fire_rooks.add(fire)
            self.counter_attack = 0

    def rect(self):
        return self.rect

"""__________________________________________________________________________________"""

class FireAttack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/rooks/fire_attack.png")
        self.image = pygame.transform.scale(self.image, (95, 80))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        superficie.blit(self.image, self.rect)