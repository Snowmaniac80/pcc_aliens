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
        self.ship_speed = 1.5
        #bullet settings
        self.torpedo_speed = 1
        self.torpedo_width = 3
        self.torpedo_height = 15
        self.torpedo_color = (0, 204, 0)
        self.torpedo_number = 3
        self.comet_number = 5
