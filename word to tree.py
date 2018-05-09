# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:17:51 2018

@author: Simon
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:41:07 2018

@author: Simon
"""

import string

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


def decomposed_words_dict(words_list):
    """
    Each word of words_list became the key of a dictionnary. The corresponding value is a 
    dictionnary taking the letters composing the word as keys and the numbers of 
    times you find this letter into the word as values. 
    For example, ['ai','arbre'] gives : 
    {'ai' : {'a' : 1, 'i' : 1} , 'arbre' : { 'a' : 1 , 'b' : 1 , 'e' : 1 , 'r' : 2} }
    """
    words_dict = {}
    for word in words_list:
        
        # Creating here the subdictionnary
        tempDict = {}
        for ltr in word:
            tempDict[ltr] = tempDict.get(ltr, 0) + 1
        print(tempDict)
        # Assigning the subdictionnary to the word key
        words_dict[word]=tempDict
        
    return words_dict
    
            
text = load_words_list('liste_francais.txt')
aDict = decomposed_words_dict(text)
print(aDict)