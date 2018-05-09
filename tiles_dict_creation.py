# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:47:53 2018

@author: Simon
"""

# =============================================================================
#     0 point : Joker ×2 (appelés en français jokers ou lettres blanches)
#     1 point : E ×15, A ×9, I ×8, N ×6, O ×6, R ×6, S ×6, T ×6, U ×6, L ×5
#     2 points : D ×3, M ×3, G ×2
#     3 points : B ×2, C ×2, P ×2
#     4 points : F ×2, H ×2, V ×2
#     8 points : J ×1, Q ×1
#     10 points : K ×1, W ×1, X ×1, Y ×1, Z ×1
# =============================================================================

import string

def tiles_dict_creation():
    tiles_dict={}
    for i in string.ascii_lowercase:
        value = input("enter value for letter " + i + ' ')
        quantity = input("enter quantity of letter " + i + ' ')
        tiles_dict[i] = [value,quantity]
    tiles_dict['blank'] = [0,2]
    return tiles_dict
        
tiles_dict = tiles_dict_creation()
print(tiles_dict)    
        