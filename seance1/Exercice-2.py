# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:01:55 2024

@author: chris
"""

def searchlongerword(selection):
    words=list()
    potential_solutions = list()
    solution = list()
    
#extraction du fichier de mots    
    dictionary = open("frenchssaccent.dic",'r')
    for lign in dictionary:
        words.append(lign[0:len(lign)-1])
    dictionary.close()

    
#Parcourt la liste de mots et cree une liste ,pour chaque mot, contenant ses lettres
    for i in range(len(words)):
        word = list(words[i])
#Parcourt la selection de lettres donnee
        for j in range(len(selection)):
            if selection[j] in word:
                word.remove(selection[j])
#On supprime la lettre pour être sur de ne eviter les doubles
        if len(word)==0:
#potential_solutions recense les mots du dictionnaires que l'on peut ecrire avec les lettres de la selection
            potential_solutions.append(words[i])
#Boucle pour trouver le mot le plus long parmi les solutions proposees
    solution = potential_solutions[0]
    for k in range(len(potential_solutions)):
        if len(potential_solutions[k]) > len(solution):
            solution = potential_solutions[k]
    print('potential_solutions')
    print('the longer word in dictionay with the letter selection is : ', solution)
    