# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:16:12 2016

@author: pilgrim
"""

import pygame
from settings import Settings
from ship import Ship
import ai_fxns as gf
from pygame.sprite import Group

def run_game():
    # %%
    '''initialize the game and create a screen object'''
    pygame.init()
    ai_set = Settings()
    screen = pygame.display.set_mode((ai_set.scrn_width, ai_set.scrn_hgt))
    pygame.display.set_caption("Alien Invation")
    #make ship
    ship = Ship(ai_set, screen)
    #make a comet
    comets = Group()
    torpedos = Group()
    # %%
    #Main Loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ai_set, screen, ship, torpedos)
        ship.update()
        gf.updt_comet(ai_set, screen, comets)
        gf.updt_torpedo(torpedos)
        gf.updt_scrn(ai_set, screen, ship, comets, torpedos)
    # %%

run_game()
