import sys, pygame
from pygame.locals import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0, 80, 0))

    for i in range(1000):
        # draw the line
        color = 100, 255, 200
        width = 1
        start_x = randint(0, 600)
        start_y = randint(0, 500)
        end_x   = randint(0, 600)
        end_y   = randint(0, 500)
        start_point = (start_x, start_y)
        end_point = (end_x, end_y)
        pygame.draw.line(screen, color, start_point, end_point, width)

    pygame.display.update()
