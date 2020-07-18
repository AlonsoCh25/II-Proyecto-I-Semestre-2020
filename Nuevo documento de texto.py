import pygame
from pygame import *

pygame.mixer.init()
pygame.init()
#pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.play()

a = pygame.mixer.Sound("Sounds/Cannibal_a.ogg")
a.play()
