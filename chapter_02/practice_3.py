import sys, pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangles")
pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 255, 255),
    (255, 0, 255),
    (255, 255, 0),
    (255, 255, 255)
]
num = 0
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0, 0, 200))

    # move the rectangle
    pos_x += vel_x
    pos_y += vel_y

    # keep rectangle on the screen
    if pos_x > 400 or pos_x < 0:
        vel_x = -vel_x
        num += 1
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
        num += 1

    # draw the rectangle
    color = colors[num % 8]
    width = 0
    pos = pos_x, pos_y, 200, 100
    pygame.draw.rect(screen, color, pos, width)

    pygame.display.update()