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
        super().__init__()
        self.screen = screen
        #creat torpedo at 0,0 then correct position to shuttle loc
        self.rect = pygame.Rect(0, 0, params.torpedo_width, params.torpedo_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #store as float
        self.y = float(self.rect.y)
        self.color = params.torpedo_color
        self.speed = params.torpedo_speed

    def update(self):
        '''move the bullet up the screen'''
        self.y -= self.speed
        #why do we do this in two steps???
        self.rect.y = self. y

    def draw(self):
        '''draw the torpedo'''
        pygame.draw.rect(self.screen, self.color, self.rect)
