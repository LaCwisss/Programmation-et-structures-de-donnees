# -*- coding: utf-8 -*-

def search_longer_word(selection):
    words=list()
    potential_solutions = list()
    
#extraction du fichier de mots    
    dictionary = open("frenchssaccent.dic",'r')
    for lign in dictionary:
        words.append(lign[0:len(lign)-1])
    dictionary.close()

    for i in range(len(words)):
        word = list(words[i])
#joker compte differencie les mots avec ou sans '?'
        joker=0
        for j in range(len(selection)):
            if selection[j] in word:
                word.remove(selection[j])
        if len(word) == 1:
            if '?' in selection:
                joker=word[0]
                potential_solutions.append((words[i],joker))
        if len(word)==0:
            potential_solutions.append((words[i],joker))
#on retourne une liste tuple (mot,joker) avec joker = 0 (pas de '?') ou la lettre remplacee par '?'
    return potential_solutions


value_letters = {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'd': 2, 'g': 2, 'm': 2, 'b': 3, 'c': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'j': 8, 'q': 8, 'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}
def score(potential_solutions):
    list_scores=list()
    for word in potential_solutions:
        value_word=0    
        letters = list(word[0])
        joker = word[1]
        for letter in letters:
            value_word = value_word + value_letters[letter]
#on retire la valeur de la lettre 'joker'
        if joker != 0:
            value_word = value_word - value_letters[joker]
        list_scores.append(value_word)
    return list_scores

def max_score(potential_solutions):
    list_scores = score(potential_solutions)
    maximum = list_scores[0]
    word_max = potential_solutions[0][0]
    for i in range(len(list_scores)):
        if maximum < list_scores[i]:
            maximum = list_scores[i]
            word_max = potential_solutions[i][0]
    return word_max, maximum


a=search_longer_word(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j','?'])
b=max_score(a)
print(b)