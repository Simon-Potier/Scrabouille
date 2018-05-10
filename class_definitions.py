# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:54:31 2018

@author: Simon
"""
import random
import string

# =============================================================================
# tilesDict = {'a': [1, 9], 'b': [3, 2], 'c': [3, 2], 'd': [2, 3], 
#                       'e': [1, 15], 'f': [4, 2], 'g': [2, 2], 'h': [4, 2], 
#                       'i': [1, 8], 'j': [8, 1], 'k': [10, 1], 'l': [1, 5], 
#                       'm': [2, 3], 'n': [1, 6], 'o': [1, 6], 'p': [3, 2], 
#                       'q': [8, 1], 'r': [1, 6], 's': [1, 6], 't': [1, 6], 
#                       'u': [1, 6], 'v': [4, 2], 'w': [10, 1], 'x': [10, 1], 
#                       'y': [10, 1], 'z': [10, 1], 'blank': [0, 2]}
# =============================================================================

tilesValues = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
               'i': 1, 'j': 8, 'k': 10, 'l': 1, 'm': 2, 'n': 1, 'o': 1,
               'p': 3, 'q': 8, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4,
               'w': 10, 'x': 10, 'y': 10, 'z': 10, 'blank': 0}

tilesList = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'c',
             'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e',
             'e', 'e', 'e', 'e', 'e', 'f', 'f', 'g', 'g', 'h', 'h', 'i', 'i',
             'i', 'i', 'i', 'i', 'i', 'i', 'j', 'k', 'l', 'l', 'l', 'l', 'l',
             'm', 'm', 'm', 'n', 'n', 'n', 'n', 'n', 'n', 'o', 'o', 'o', 'o',
             'o', 'o', 'p', 'p', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's',
             's', 's', 's', 's', 't', 't', 't', 't', 't', 't', 'u', 'u', 'u',
             'u', 'u', 'u', 'v', 'v', 'w', 'x', 'y', 'z', 'blank', 'blank']

def load_words_list(file_name):
    """ 
    Create a list of lower case words from a given .txt list
    Takes in : a .txt of the words, every word on a new line
    Returns : a list of words, lower cased 
    """
    in_file = open(file_name,'r')
    words_string = in_file.read().lower()
    words_list = words_string.split()
    return words_list

class User(object):
    def __init__(self,user_name, password,hand = []):
        self.user_name = user_name
        self.password = password
        self.hand = []
        # self.pix = pix # Add pix later ???
    
    def __str__(self):
        ans = 'User name : ' + self.user_name + '\nPassword : ' + self.password
        return ans
    
    def getUser_name(self):
        return self.user_name
    
    def getPassword(self):
        return self.password
    

p1 = User('Player1', 'PWPlayer1')
p2 = User('Player2', 'PWPlayer2')


def dealHand(pX):
    for i in range(7-len(pX.hand)):
        # Assigns a tile to the hand and remove tile from tilesList
        if len(tilesList) > 0:
            randTile = random.choice(tilesList)
            tilesList.remove(randTile)
            pX.hand.extend(randTile)
        else:
            break
    
    return pX.hand
     

def wordScore(word):
    score = 0
    for i in word :
        score += tilesValues[i]
    if len(word) == 7:
        score += 50
    
    return score
        
def validWord(word,wordList):
    low = wordList[0]
    print('low is : ' + low)
    high = wordList[-1]
    print('high is : ' + high)
    mid = wordList[len(wordList)//2]
    print('mid is : ' + mid)
    if mid == word or low == word or high == word :
        return True
    elif len(wordList) == 1 and word != wordList[0] or :
        return False
    else :
        if word > mid:
            return validWord(word,wordList[len(wordList)//2+1:-1])
        else :
            return validWord(word,wordList[0:len(wordList)//2-1])
    

wordList = load_words_list('ODS6.txt')



# =============================================================================
# class Tiles(object):
#     def __init__(self,letter,value,remainder):
#         self.letter = letter
#         self.value = value
#         self.remainder = remainder
#     
#     def __str__(self):
#         ans = letter + 'Pt: ' + value + 'Remains: ' + remainder
#         return ans
#     
#     def initialize_list():
#         pass
# =============================================================================



        
        
        
        
        
        
        