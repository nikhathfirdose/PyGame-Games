import pygame
import sys
import os
from pygame.locals import *
#  python.linting.mypyArgs


red = [255, 0, 0]

pygame.init()
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Slither Snake Game")

screen = pygame.display.get_surface()
screen.fill(red)
# pygame.display.flip()

while True:
    for event in pygame.event.get():
        print(event)
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
    pygame.display.update()
