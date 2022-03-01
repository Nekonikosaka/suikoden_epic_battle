#coding : utf-8
from operator import truediv
import pygame
pygame.init()

#Creation fenetre
pygame.display.set_mode((800, 600))
pygame.display.set_caption("SUIKODEN EPIC BATTLE")

running = True


while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
