# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:48:58 2016

@author: pilgrim
"""

import sys
import pygame
from torpedo import Torpedo as torp
from comet import Comet
# %%
def check_events(params, screen, ship, torpedos):
    '''respond to key presses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # %%
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.go_rgt = True
            elif event.key == pygame.K_LEFT:
                ship.go_lft = True
            elif event.key == pygame.K_SPACE and \
                                        len(torpedos) < params.torpedo_number:
                #launch torpedo!
                new_torp = torp(params, screen, ship)
                torpedos.add(new_torp)
            elif event.key == pygame.K_F12:
                sys.exit()
        # %%
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.go_rgt = False
            elif event.key == pygame.K_LEFT:
                ship.go_lft = False

# %%
def make_comets(params, screen, comets):
    '''creat many incoming comets'''
    if params.comet_number > len(comets):
        comet = Comet(params, screen)
        comets.add(comet)

def updt_comet(params, screen, comets):
    make_comets(params, screen, comets)
    comets.update()
    for comet in comets.copy():
        if comet.rect.y >= params.scrn_hgt:
            comets.remove(comet)

# %%
def updt_torpedo(torpedos):
    '''update drawing of topedoes for display and remove old ones'''
    torpedos.update()
    #remove abandoned torpedoes
    for torpedo in torpedos.copy():
        if torpedo.rect.bottom <= 0:
            torpedos.remove(torpedo)
        #print(len(torpedos))


# %%
def updt_scrn(params, screen, ship, comets, torpedoes):
    '''update images on the screen and flip to the new screen'''
    #redraw screen
    screen.fill(params.bgcolor)
    ship.biteme()
    comets.draw(screen)
    for torpedo in torpedoes.sprites():
        torpedo.draw()
    #make the most recent drawn screen visible
    pygame.display.flip()
