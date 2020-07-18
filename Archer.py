import pygame

arrows = pygame.sprite.Group()
FPS = 30
"""__________________________________________________________________________________"""

class Archer(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/avatars/archer1.png')
        self.image = pygame.transform.scale(self.image, (95, 80))
        self.song = pygame.mixer.Sound("Sounds/archer_attack.ogg")
        self.rect = self.image.get_rect()
        self.attack_time = 10
        self.movement_time = 12
        self.health = 5
        self.damage = 2
        self.rect.left = x
        self.rect.top = y
        self.counter_attack = 0
        self.counter_move = 0
        self.change_counter = 0
        self.y_pos = 0

    def update(self, superficie, gridMatrix):

        self.counter_attack += 1

        if self.counter_attack >= self.attack_time * FPS:
            change_pos = 10
            self.image = pygame.image.load('images/avatars/archer2.png')
            self.image = pygame.transform.scale(self.image, (95, 80))
            self.change_counter += 1
            self.song.play()
            if self.change_counter >= change_pos:
                arrow = Arrow(self.rect.centerx, self.rect.bottom)
                arrows.add(arrow)
                self.counter_attack = 0
                self.image = pygame.image.load('images/avatars/archer1.png')
                self.image = pygame.transform.scale(self.image, (95, 80))
                self.change_counter = 0

        self.counter_move += 1

        if self.counter_move >= self.movement_time * FPS:
            self.rect.top += 80
            self.counter_move = 0

        superficie.blit(self.image, self.rect)

"""__________________________________________________________________________________"""

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/avatars/arrow.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.top > 1000:
            self.kill()
        superficie.blit(self.image, self.rect)
