# -*- coding: utf-8 -*-
"""
Created on Wed May  9 19:06:57 2018

@author: Simon
"""


tiles_dict = {'a': ['1', '9'], 'b': ['3', '2'], 'c': ['3', '2'], 'd': ['2', '3'], 'e': ['1', '15'], 'f': ['4', '2'], 'g': ['2', '2'], 'h': ['4', '2'], 'i': ['1', '8'], 'j': ['8', '1'], 'k': ['10', '1'], 'l': ['1', '5'], 'm': ['2', '3'], 'n': ['1', '6'], 'o': ['1', '6'], 'p': ['3', '2'], 'q': ['8', '1'], 'r': ['1', '6'], 's': ['1', '6'], 't': ['1', '6'], 'u': ['1', '6'], 'v': ['4', '2'], 'w': ['10', '1'], 'x': ['10', '1'], 'y': ['10', '1'], 'z': ['10', '1'], 'blank': [0, 2]}
initial_tiles_dict = {}
for i in string.ascii_lowercase:
    initial_tiles_dict[i] = [int(tiles_dict[i][0]),int(tiles_dict[i][1])]
initial_tiles_dict['blank']=[0,2]
print(initial_tiles_dict)