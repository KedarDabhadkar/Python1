# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 16:20:49 2016

@author: Zestkay
"""

import pygame, sys, math
from pygame.locals import *

pygame.init()

t=pygame.time.get_ticks()

DISPLAYSURF = pygame.display.set_mode((800, 600))

missileimg= pygame.image.load('missile.png')
gunimg= pygame.image.load('missilelauncher.png')
bulletimg= pygame.image.load('bullet.png')

clock= pygame.time.Clock()
#t=pygame.time.get_time()

missileimg = pygame.transform.scale(missileimg, (25, 50))
gunimg = pygame.transform.scale(gunimg, (30, 70))
bulletimg= pygame.transform.scale(bulletimg, (10, 70))

missileimg.convert()
missilex=200
missiley=10
gunx=400
guny=250
bulletx=415
bullety=250
angle=0
t0=0

pygame.display.set_caption('ShipDefense')

#gun=pygame.Rect(200,50,10,50)

while True: # main game loop
    DISPLAYSURF.fill((255,255,255))
    
#    DISPLAYSURF.blit(gunimg, (gunx, guny))
    
    def getAngle(x1, y1, x2, y2):
        rise = y1 - y2
        run = x1 - x2
        angle = math.atan2(run, rise) 
        angle = angle * (180 / math.pi) 
        
        return angle
        
    def getAngle1 (xb, yb, xm, ym):
        k= (ym-yb)/(xm-xb)
        angle= math.asin((1-k**2)/(1+k**2))
        angle= angle*(180/math.pi)
        return angle
        
    mouseloc=pygame.mouse.get_pos()
    mousex=mouseloc[0]
    mousey=mouseloc[1]
    degrees = getAngle(gunx, guny+70, mousex, mousey)
    rotatedSurf1 = pygame.transform.rotate(gunimg, angle)
    rotatedSurf2 = pygame.transform.rotate(bulletimg, angle)
    
   
    if pygame.mouse.get_pressed()[0]==1:
        
        t1=t-t0        
        rotatedSurf1 = pygame.transform.rotate(gunimg, degrees)
        rotatedSurf2 = pygame.transform.rotate(bulletimg, degrees)
        
        angle= degrees
        missilex= mouseloc[0]
        missiley= mouseloc[1]
        
        bulletx= gunx
        bullety= guny
        
        DISPLAYSURF.blit(missileimg, (missilex, missiley))
        print angle+90
        t0=t

    missiley+=1
    bulletx+=math.cos((angle+90)*(math.pi/180))
    bullety-=math.sin((angle+90)*(math.pi/180))
    
    DISPLAYSURF.blit(missileimg, (missilex, missiley))
    DISPLAYSURF.blit(rotatedSurf1,(gunx, guny))
    DISPLAYSURF.blit(rotatedSurf2,(bulletx, bullety))
    
    pygame.time.delay(10)
    clock.tick()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            print t, t1, t0
            pygame.quit()
            sys.exit()
    pygame.display.update()