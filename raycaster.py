import sys
import pygame
import random
import math

pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
flooru=[[0,0,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,1]]
white=(255,255,255)
pygame.display.set_caption("raycaster")

clock=pygame.time.Clock()

def castray(floors,angle):
    step=0.1
    currx=0
    curry=0
    counter=0
    while True:
        currx+=math.cos(math.radians(angle))*step
        curry+=math.sin(math.radians(angle))*step
        counter+=1
        if currx<0 or curry<0 or currx>=4 or curry>=4:
            break
        if floors[math.floor(curry)][math.floor(currx)]==1:
                break

    return counter*step

def drawcenteredy(dist,x):
    leds=math.floor(((4*math.sqrt(2))-dist)*8/(4*math.sqrt(2)))
    match leds:
        case 1:
            drawxy(white,x,3)
        case 2:
            drawxy(white,x,3)
            drawxy(white,x,4)
        case 3:
            drawxy(white,x,2)
            drawxy(white,x,3)
            drawxy(white,x,4)
            
        case 4:
            drawxy(white,x,2)
            drawxy(white,x,3)
            drawxy(white,x,4)
            drawxy(white,x,5)
        case 5:
            drawxy(white,x,1)
            drawxy(white,x,2)
            drawxy(white,x,3)
            drawxy(white,x,4)
            drawxy(white,x,5)
        case 6:
            drawxy(white,x,1)
            drawxy(white,x,2)
            drawxy(white,x,3)
            drawxy(white,x,4)
            drawxy(white,x,5)
            drawxy(white,x,6)
        case 8:
            drawxy(white,x,0)
            drawxy(white,x,1)
            drawxy(white,x,2)
            drawxy(white,x,3)
            drawxy(white,x,4)
            drawxy(white,x,5)
            drawxy(white,x,6)
            drawxy(white,x,7)
            

    return leds

def drawxy(color,i,j):
    pixelwidth=50
    pixelspacing=5
    pygame.draw.rect(screen,color,(50+(pixelwidth+pixelspacing)*i,50+(pixelwidth+pixelspacing)*j,pixelwidth,pixelwidth))


running=True
last_step = pygame.time.get_ticks()

angle=0
idx=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    now=pygame.time.get_ticks()
    if now-last_step>=100:
        if angle<=90:
            dist=castray(flooru,angle)
            print(drawcenteredy(dist,idx))
            angle+=7.5
            #drawxy((255,255,255),idx,3)
            idx+=1
        last_step=now



    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
