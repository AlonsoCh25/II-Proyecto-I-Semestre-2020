import pygame

swords = pygame.sprite.Group()
FPS = 30

"""__________________________________________________________________________________"""

class Squire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/avatars/squire1.png')
        self.image = pygame.transform.scale(self.image, (95, 80))
        self.song = pygame.mixer.Sound("Sounds/squire.ogg")
        self.rect = self.image.get_rect()
        self.attack_time = 15
        self.movement_time = 10
        self.health = 10
        self.damage = 3
        self.spawn = False
        self.rect.left = x
        self.rect.top = y
        self.counter_attack = 0
        self.counter_move = 0
        self.change_counter = 0

    def update(self, superficie, gridMatrix):

        self.counter_attack += 1

        if self.counter_attack >= self.attack_time * FPS:
            change_pos = 10
            self.image = pygame.image.load('images/avatars/squire2.png')
            self.image = pygame.transform.scale(self.image, (95, 80))
            self.change_counter += 1
            self.song.play()
            if self.change_counter >= change_pos:
                sword = Sword(self.rect.centerx, self.rect.bottom)
                swords.add(sword)
                self.counter_attack = 0
                self.image = pygame.image.load('images/avatars/squire1.png')
                self.image = pygame.transform.scale(self.image, (95, 80))
                self.change_counter = 0

        self.counter_move += 1

        if self.counter_move >= self.movement_time * FPS:
            self.rect.top += 80
            self.counter_move = 0

        superficie.blit(self.image, self.rect)

"""__________________________________________________________________________________"""

class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/avatars/sword.png")
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self, superficie):
        self.rect.y += self.speedy
        if self.rect.top > 1000:
            self.kill()
        superficie.blit(self.image, self.rect)
