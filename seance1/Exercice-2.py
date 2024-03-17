# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:01:55 2024

@author: chris
"""

def search_longer_word(selection):
    words=list()
    potential_solutions = list()
    solution = list()
    
#extraction du fichier de mots    
    dictionary = open("frenchssaccent.dic",'r')
    for lign in dictionary:
        words.append(lign[0:len(lign)-1])
    dictionary.close()

    
#Parcourt la liste de mots et cree une liste, pour chaque mot, contenant ses 
#lettres
    for word_index in range(len(words)):
        word = list(words[word_index])
#Parcourt la selection de lettres donnee
        for selection_index in range(len(selection)):
            if selection[selection_index] in word:
                word.remove(selection[selection_index])
#On supprime la lettre pour être sur de ne eviter les doubles
        if len(word)==0:
#potential_solutions recense les mots du dictionnaires que l'on peut ecrire 
#avec les lettres de la selection
            potential_solutions.append(words[word_index])
#Boucle pour trouver le mot le plus long parmi les solutions proposees
    solution = potential_solutions[0]
    for potential_index in range(len(potential_solutions)):
        if len(potential_solutions[potential_index]) > len(solution):
            solution = potential_solutions[potential_index]
    print('the longer word in dictionay with the letter selection is : ', 
          solution)
    return None
    