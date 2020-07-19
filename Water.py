import pygame

water_attacks = pygame.sprite.Group()
FPS = 30

"""__________________________________________________________________________________"""

class Water(pygame.sprite.Sprite):
    def __init__(self, attack_time, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/rooks/water_rook_a.png")
        self.image = pygame.transform.scale(self.image, (95, 80))
        self.rect = self.image.get_rect()
        self.attack_time = attack_time
        self.health = 16
        self.damage = 8
        self.rect.x = x
        self.rect.y = y
        self.counter_attack = 0

        self.health_bar100 = pygame.image.load('images/health_bar100.png')
        self.health_bar100 = pygame.transform.scale(self.health_bar100, (90, 30))
        self.health_bar75 = pygame.image.load('images/health_bar75.png')
        self.health_bar75 = pygame.transform.scale(self.health_bar75, (90, 30))
        self.health_bar50 = pygame.image.load('images/health_bar50.png')
        self.health_bar50 = pygame.transform.scale(self.health_bar50, (90, 30))
        self.health_bar25 = pygame.image.load('images/health_bar25.png')
        self.health_bar25 = pygame.transform.scale(self.health_bar25, (90, 30))
        self.health_bar0 = pygame.image.load('images/health_bar0.png')
        self.health_bar0 = pygame.transform.scale(self.health_bar0, (90, 30))
        self.health_bar = self.health_bar100
        self.rect_health_bar = self.image.get_rect()
        self.rect_health_bar.left = x + 2
        self.rect_health_bar.top = y + 5

    def decrease_health(self, damage):
        self.health -= damage
        if 8 <= self.health < 12:
            self.health_bar = self.health_bar75
        elif 4 <= self.health < 8:
            self.health_bar = self.health_bar50
        elif 0 < self.health < 4:
            self.health_bar = self.health_bar25
        elif self.health <= 0:
            self.health_bar = self.health_bar0

    def update(self, superficie):
        self.counter_attack += 1
        if self.counter_attack >= self.attack_time * FPS:
            water = WaterAttack(self.rect.centerx, self.rect.bottom)
            water_attacks.add(water)
            self.counter_attack = 0

        superficie.blit(self.image, self.rect)
        superficie.blit(self.health_bar, self.rect_health_bar)

"""__________________________________________________________________________________"""

class WaterAttack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/rooks/water_rook_attack.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.bottom < 295:
            self.kill()
        superficie.blit(self.image, self.rect)