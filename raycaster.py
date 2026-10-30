import sys
import pygame
import random

pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("raycaster")

clock=pygame.time.Clock()

def drawxy(color,i,j):
    pixelwidth=50
    pixelspacing=5
    pygame.draw.rect(screen,color,(50+(pixelwidth+pixelspacing)*i,50+(pixelwidth+pixelspacing)*j,pixelwidth,pixelwidth))


running=True
last_step = pygame.time.get_ticks()


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    now=pygame.time.get_ticks()
    if now-last_step>=100:
        k=random.randint(0,7)
        drawxy((36*k,36*k,36*k),random.randint(0,12),random.randint(0,7))
        last_step=now



    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
