import pygame

rock_attacks = pygame.sprite.Group()
FPS = 30

"""__________________________________________________________________________________"""

class Rock(pygame.sprite.Sprite):
    def __init__(self, attack_time, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/rooks/rock_rook_a.png")
        self.image = pygame.transform.scale(self.image, (95, 80))
        self.rect = self.image.get_rect()
        self.attack_time = attack_time
        self.health = 14
        self.damage = 4
        self.rect.x = x
        self.rect.y = y
        self.counter_attack = 0

    def decrease_health(self, damage):
        self.health -= damage

    def update(self, superficie):
        self.counter_attack += 1
        if self.counter_attack >= self.attack_time * FPS:
            rock = RockAttack(self.rect.centerx, self.rect.bottom)
            rock_attacks.add(rock)
            self.counter_attack = 0

        superficie.blit(self.image, self.rect)

"""__________________________________________________________________________________"""

class RockAttack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/rooks/rock_rook_attack.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        superficie.blit(self.image, self.rect)