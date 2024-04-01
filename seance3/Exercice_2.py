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
        if self.is_leaf():
            return prefix
        prefix = prefix +'('
        for child in range(len(self.children())):
            prefix = prefix + f'{self.children()[child].__str__()},'
        prefix = prefix[:-1] +')'
        return prefix
    
    def __eq__(self,__value: object):
        if self.__label != __value.__label:
            return False
        elif self.nb_children1()==__value.nb_children1():
            for child in range(len(self.children())):
                if not self.children()[child].__eq__(__value.children()[child]):
                    return False
            return True
        else:
            return False
    
    def empty_tree(self):
        self.__label = '0'
        self.__children = ''
    
    def deriv(self, var: str):
        print(self.__str__())
        operators = ['+', '*']
        nb_variable = 0
        id_variable = 0
        if self.__label == '+':
            for child in range(self.nb_children1()):
                self.child(child).deriv(var)
        elif self.__label == '*':
            for child in range(self.nb_children1()):

                if self.child(child).label() == '0':
                    self.empty_tree()
                    break
                if self.child(child).label() == var:
                    id_variable = child
                    nb_variable = nb_variable + 1
                elif self.child(child).label() in operators :
                    self.child(child).deriv(var)
            if nb_variable != 0:
                self.child(id_variable).__label = nb_variable
            else:
                self.empty_tree()
        elif self.__label == var:
            self.__label = '1'
        else:
            self.__label = '0'
        return self
            
if __name__=='__main__':
    
    un = Tree('1')
    zero = Tree('0')
    dX = Tree('X')
    t1=Tree('a')
    t11 = Tree('X')
    print(t1.label())
    t2 = Tree('a',Tree('b'),Tree('c'))
    print(t2.children())
    print(t2.nb_children1())
    t3 = Tree('a',Tree('b'),Tree('c',Tree('d')))
    t4 = Tree('a',Tree('b'),Tree('c',Tree('d')))
    t5 = Tree('f',Tree('a'),Tree('b'))
    """ print(t3.nb_children1())
    print(t3.nb_children2())
    print(t3.child(1))
    print(t3.is_leaf())
    print(t3.depth())
    print(t3.__str__())
    print(t5.__eq__(t5))
    dX.deriv('X')
    print(dX.__str__())"""
    print(Tree('+', dX, Tree('X')).deriv('X').__str__())
    """print(Tree('+', dX, dX).deriv('X').__eq__(Tree('+', un, un)))"""
    """t1.deriv('X')
    print(t1.__eq__(zero))
    t11.deriv(dX)
    print(t11.__eq__(un))"""
    tcalc = Tree('+', Tree('5'), Tree('*',Tree('X'),Tree('X'),Tree('2')), Tree('*',Tree('X'),Tree('X'),Tree('X')))
    print('')
    print('derivation')
    print(tcalc.__str__())
    tcalc.deriv('X')
    print(tcalc.__str__())
