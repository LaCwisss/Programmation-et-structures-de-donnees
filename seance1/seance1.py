# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:01:55 2024

@author: chris
"""

words=list()
dictionary = open("frenchssaccent.dic",'r')
for lign in dictionary:
    words.append(lign[0:len(lign)-1])
dictionary.close()


def searchlongerword(selection):
    n = len(selection)
    solution=None
    newselection=list()
    existence=True
    for word in dictionary :
        letters=set(word)
        for letter in letters:
            if letter not in selection:
                good=False
                break
        if good==False:
            good=True
            break
        newselection.append(word)
    if len(newselection)=0:
        return "no french word matched with the letters of the selection given"
    else:  
        index_size_max=0
        for word in newselection:
        