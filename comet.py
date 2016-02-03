# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:30:18 2016

@author: pilgrim
"""

import pygame
import random
from pygame.sprite import Sprite

class Comet(Sprite):

    def __init__(self, params, screen):
        '''init comet and starting position'''
        super().__init__()
        self.screen = screen
        self.params = params
        #load the comet image
        if random.randint(0,1):
            self.image = pygame.image.load('images/comet_sm.png')
        else:
            self.image = pygame.image.load('images/fireball_sm.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #init comet position
        self.rect.x = random.randint(0,params.scrn_width)
        self.rect.y = self.rect.height * -1
        self.delay = random.randint(0,5)
        self.frame = 0

    def update(self):
        '''update the comet position'''
        if self.delay == self.frame:
            self.rect.y += 1
            self.frame = 0
        else:
            self.frame += 1

    def biteme(self):
        '''draw the ship at the current location'''
        self.screen.blit(self.image, self.rect)
