# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:34:23 2016

@author: Zestkay
"""

import pygame, sys, math
from pygame.locals import *
import time

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
missileimg= pygame.image.load('missile.png')
gunimg=pygame.image.load('missilelauncher.png')
pygame.transform.scale(missileimg,(30,200))
missileimg = pygame.transform.scale(missileimg, (50, 100))
gunimg = pygame.transform.scale(gunimg, (30, 70))
speedmissile= 200


missileimg.convert()
missilex=200
missiley=10
gunx=175
guny=230
degrees=90

pygame.display.set_caption('ShipDefense')

#gun=pygame.Rect(200,50,10,50)

while True: # main game loop
    DISPLAYSURF.fill((255,255,255))
    DISPLAYSURF.blit(missileimg, (missilex, missiley))
#    DISPLAYSURF.blit(gunimg, (gunx, guny))
    
    def getAngle(x1, y1, x2, y2):
        rise = y1 - y2
        run = x1 - x2
        angle = math.atan2(run, rise) 
        angle = angle * (180 / math.pi) 
        angle = (angle + 90) % 360
        return angle
        
    
    if pygame.mouse.get_pressed()[0]==1:
        
        mouseloc=pygame.mouse.get_pos()
        mousex=mouseloc[0]
        mousey=mouseloc[1]
        
        missilex= mousex
        missiley= mousey
        
        clock = pygame.time.Clock()
        
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        
        speed= speedmissile*time_sec
        
        missilex+=speed
        
        
    
        errorprior=0
        integral=0
        kp=3
        ki=3
        kd=30
        dt=5
        error=getAngle(gunx, guny+70, mousex, mousey)
    
        
     #   while error!=0:
        error=getAngle(gunx, guny+70, mousex, mousey)
        integral=integral+(error*dt)
        derivative=(error-errorprior)/dt
        output=kp*error+ki*integral+kd*derivative
        errorprior=error
        time.sleep(dt)
        degrees = output
        
        rotatedSurf = pygame.transform.rotate(gunimg, degrees-90)
        DISPLAYSURF.blit(rotatedSurf,(gunx, guny))
        time.sleep(0.1)
        
    else:
      
        rotatedSurf = pygame.transform.rotate(gunimg, degrees-90)
        DISPLAYSURF.blit(rotatedSurf,(gunx, guny))
        
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()