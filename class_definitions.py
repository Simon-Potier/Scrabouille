# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:54:31 2018

@author: Simon
"""

class Users(object):
    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password = password
        # self.pix = pix # Add pix later ???
    
    def __str__(self):
        ans = 'User name : ' + self.user_name + '\nPassword : ' + self.password
        return ans
    
    def getUser_name(self):
        return self.user_name
    
    def getPassword(self):
        return self.password
    
class Tiles(object):
    def __init__(self,letter,value,remainder):
        self.letter = letter
        self.value = value
        self.remainder = remainder
    
    def __str__(self):
        ans = letter + 'Pt: ' + value + 'Remains: ' + remainder
        return ans
    
    def initialize_list():
        pass
    

        
        
        
        
        
        
        