import pygame

lenadores = pygame.sprite.Group()
FPS = 30

"""__________________________________________________________________________________"""

class Lumberjack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/avatars/lumberjack1.png')
        self.image = pygame.transform.scale(self.image, (95, 80))
        self.rect = self.image.get_rect()
        self.attack_time = 5
        self.movement_time = 13
        self.health = 20
        self.damage = 9
        self.spawn = False
        self.rect.left = x
        self.rect.top = y
        self.counter_pos = 0
        self.counter_attack = 0
        self.counter_move = 0

    def update(self, superficie, gridMatrix):

        self.counter_attack += 1

        if self.counter_attack >= self.attack_time * FPS:
            self.image = pygame.image.load('images/avatars/lumberjack2.png')
            self.image = pygame.transform.scale(self.image, (95, 80))
            self.change_pos = 10
            self.counter_pos += 1
            if self.counter_pos >= self.change_pos:
                self.image = pygame.image.load('images/avatars/lumberjack1.png')
                self.image = pygame.transform.scale(self.image, (95, 80))
                self.counter_pos = 0
                self.counter_attack = 0

        self.counter_move += 1

        if self.counter_move >= self.movement_time * FPS:
            self.rect.top += 80
            self.counter_move = 0

        superficie.blit(self.image, self.rect)