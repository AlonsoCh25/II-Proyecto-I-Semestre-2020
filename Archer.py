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
        self.rect_health_bar.top = y - 10

    def move(self, movement):
        if movement == True:
            self.counter_move += 1

            if self.counter_move >= self.movement_time * FPS:
                self.rect.top += 80
                self.rect_health_bar.top += 80
                self.counter_move = 0

    def decrease_health(self, damage):
        self.health -= damage
        if 3 <= self.health < 4:
            self.health_bar = self.health_bar75
        elif 2 <= self.health < 3:
            self.health_bar = self.health_bar50
        elif 0 < self.health < 2:
            self.health_bar = self.health_bar25
        elif self.health <= 0:
            self.health_bar = self.health_bar0

    def update(self, superficie):

        self.counter_attack += 1

        if self.counter_attack >= self.attack_time * FPS:
            change_pos = 10
            self.image = pygame.image.load('images/avatars/archer2.png')
            self.image = pygame.transform.scale(self.image, (95, 80))
            self.change_counter += 1
            #self.song.play()
            if self.change_counter >= change_pos:
                arrow = Arrow(self.rect.centerx, self.rect.bottom)
                arrows.add(arrow)
                self.counter_attack = 0
                self.image = pygame.image.load('images/avatars/archer1.png')
                self.image = pygame.transform.scale(self.image, (95, 80))
                self.change_counter = 0

        superficie.blit(self.image, self.rect)
        superficie.blit(self.health_bar, self.rect_health_bar)

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