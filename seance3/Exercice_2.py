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
        assert i <= len(self.children())
        return self.children()[i]
    
    def is_leaf(self):
        return self.nb_children1()==0 
    
    def depth(self):
        depth = 0 
        if len(self.children())>0:
            depth = 1
        for child in range(len(self.children())):
            depth = depth + self.__children[child].depth()
        return depth
    
    def __str__(self):
        prefix = f'{self.__label}'
        if len(self.children())==0:
            return prefix
        prefix = prefix +'('
        for child in range(len(self.children())):
            prefix = prefix + f'{self.children()[child].__str__()},'
        prefix = prefix[:-1] +')'
        return prefix
    

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
    print(t3.is_leaf())
    print(t3.depth())
    print(t3.__str__())
    