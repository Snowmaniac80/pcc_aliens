# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:44:41 2016

@author: pilgrim
"""

class Settings():
    '''a clas to store all settings for alien invation'''
    def __init__(self):
        '''init game settings'''
        #screen settings
        self.scrn_width = 1200
        self.scrn_hgt = 800
        self.bgcolor = (0, 0, 81)
        #ship settings
        self.speed = 1.5
        