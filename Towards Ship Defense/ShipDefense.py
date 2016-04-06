# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 00:42:09 2016

@author: Zestkay
"""

import pygame, sys, math
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
missileimg= pygame.image.load('missile.png')
gunimg=pygame.image.load('missilelauncher.png')
pygame.transform.scale(missileimg,(30,200))
missileimg = pygame.transform.scale(missileimg, (50, 100))
gunimg = pygame.transform.scale(gunimg, (30, 70))


missileimg.convert()
missilex=200
missiley=10
gunx=175
guny=230

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
    mouseloc=pygame.mouse.get_pos()
    mousex=mouseloc[0]
    mousey=mouseloc[1]
    degrees = getAngle(gunx, guny+70, mousex, mousey)
    rotatedSurf = pygame.transform.rotate(gunimg, degrees-90)
    DISPLAYSURF.blit(rotatedSurf,(gunx, guny))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()