# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:30:18 2016

@author: pilgrim
"""

import pygame

class Ship():
    
    def __init__(self, params, screen):
        '''init ship and starting position'''
        self.screen = screen
        self.params = params
        #load the ship image
        self.image = pygame.image.load('images/shuttle_sm.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        #movement flag
        self.go_rgt = False
        self.go_lft = False
        
    def update(self):
        '''update the ship's position based on the movement flag'''
        if self.go_rgt and (self.center < self.screen_rect.right):
            self.center += self.params.speed
        if self.go_lft and (self.center > 0):
            self.center -= self.params.speed
        
        self.rect.centerx = self.center
        
    def biteme(self):
        '''draw the ship at the current location'''
        self.screen.blit(self.image, self.rect)
