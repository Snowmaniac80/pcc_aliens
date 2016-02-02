# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:05:47 2016

@author: pilgrim
"""

import pygame
from pygame.sprite import Sprite

class Torpedo(Sprite):
    '''a class to managed topedos fired by the shuttle craft'''
    
    def __init__(self, params, screen, ship):
        '''the emerging torpedo'''
        super(Torpedo, self).__init__()
        self.screen = screen
        #creat torpedo at 0,0 then correct position to shuttle loc
        self.rect = pygame.Rect(0, 0, params.topedo_width, params.topedo_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #store as float
        self.y = float(self.rect.y)
        self.color = params.torpedo_color
        self.speed = params.torpedo_speed
        