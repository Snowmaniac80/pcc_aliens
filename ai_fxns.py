# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:48:58 2016

@author: pilgrim
"""

import sys
import pygame

def check_events(ship):
    '''respond to key presses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.go_rgt = True
            elif event.key == pygame.K_LEFT:
                ship.go_lft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.go_rgt = False
            elif event.key == pygame.K_LEFT:
                ship.go_lft = False


def updt_scrn(ai_set, scrn, ship):
    '''update images on the screen and flip to the new screen'''
    #redraw screen
    scrn.fill(ai_set.bgcolor)
    ship.biteme()
    #make the most recent drawn screen visible
    pygame.display.flip()
