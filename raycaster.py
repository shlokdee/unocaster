import sys
import pygame

pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("raycaster")

clock=pygame.time.Clock()

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    for i in range(13):
        for j in range(8):
            pygame.draw.rect(screen,(255,255,255),(50+35*i,50+35*j,30,30))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
