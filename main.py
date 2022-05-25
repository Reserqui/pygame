import sys
from copy import copy

import pygame

pygame.init()
f=False
screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 40, 40)
print(help(pygame.Rect))
rick = [copy(rect)]

BLACK=(0,0,0)
while True:
    for event in pygame.event.get():
        rick = [copy(rect)]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            f=True
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -40)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 40)
            rick.append(rect)
        print('rect', rect)
        print('rickin', rick)
    pygame.draw.rect(screen, (255, 0, 0), rect, 0)
    if f:
        pygame.draw.rect(screen, (0, 0, 0), rick[0], 0)
        f=False
    #print('rickout',rick)
    pygame.display.flip()
