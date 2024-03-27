# -*- coding: utf-8 -*-

class Tree:
    def __init__(self, label, *children):
        self.__label = label
        self.__children = children
    
    def label(self):
        return f"{self.__label}"
    
    def children(self):
        return self.__children
    
    def nb_children1(self):
        return len(self.__children)
    def nb_children2(self):
        count=len(self.__children)
        for child in range(len(self.__children)):
            count = count + self.children()[child].nb_children2()           
        return count
    
    def child(self, i: int):
        return self.children()[i]
    
    def is_leaf(self):
        return self.nb_children1()==0 
        
if __name__=='__main__':
    t1=Tree('a')
    print(t1.label())
    t2 = Tree('a',Tree('b'),Tree('c'))
    print(t2.children())
    print(t2.nb_children1())
    t3 = Tree('a',Tree('b'),Tree('c',Tree('d')))
    print(t3.nb_children1())
    print(t3.nb_children2())
    print(t3.child(1))
    print(t1.is_leaf())