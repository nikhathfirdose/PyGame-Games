import pygame
import sys
from pygame.locals import *
#  python.linting.mypyArgs

x = 10
y = 10
screen = 0
red = [255, 0, 0]
white = [255, 255, 255]


def my_quit():
    pygame.quit()
    sys.exit(0)


def check_inputs(events):
    global x, y, screen
    for event in events:
        if(event.type == QUIT):
            my_quit()
        else:
            if(event.type == KEYDOWN):
                if(event.key == K_ESCAPE):
                    my_quit()
                elif(event.key == K_LEFT):
                    x -= 5
                    print("LEFT")
                elif(event.key == K_RIGHT):
                    x += 5
                    print("RIGHT")
                else:
                    print(event.key)
    screen.fill(red)
    pygame.draw.rect(screen, white, (x, 50, 50, 10))
    pygame.display.update()


def main():
    global screen
    pygame.init()
    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Slither Snake Game")
    screen = pygame.display.get_surface()
    pygame.display.update()
    while True:
        check_inputs(pygame.event.get())


main()
