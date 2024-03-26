# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:47:32 2024

@author: chris
"""
import math

class Fraction :
    def __init__(self, numerator, denominator):
        assert numerator == int(numerator) 
        assert denominator==int(denominator)
        assert denominator != 0
        self.numerator = numerator
        self.denominator = denominator
    
    def show(self):
        return f"{self.numerator}/{self.denominator}"
    
    def multiply(self, other_self):
        self.numerator = self.numerator * other_self.numerator
        self.denominator = self.denominator * other_self.denominator
        return Fraction(self.numerator, self.denominator)
        
    def add(self, other_self):
        self.numerator = self.numerator*other_self.denominator + other_self.numerator*self.denominator
        self.denominator = self.denominator * other_self.denominator
        return Fraction(self.numerator, self.denominator)
    
    def simplify(self):
        assert math.gcd(self.numerator,self.denominator)
        a=math.gcd(self.numerator,self.denominator)
        self.numerator=int(self.numerator/a)
        self.denominator=int(self.denominator/a)
        return Fraction(self.numerator, self.denominator)


def H(n):
    fraction = Fraction(0,1)
    for i in range(1,n+1):
        k=Fraction(1,i)
        fraction.add(k)
        fraction.simplify()
    while math.gcd(fraction.numerator,fraction.denominator)!=1:
        fraction.simplify()
    return fraction.show()

def Leib(n):
    fraction=Fraction(0,1)
    for i in range(n+1):
        k=Fraction((-1)**i,2*i+1)
        fraction.add(k)
        fraction.simplify()
    while math.gcd(fraction.numerator,fraction.denominator)!=1:
        fraction.simplify()
    return fraction.show()

        
# utilisation de la classe 
#je n'arrive pas à faire fonctionner 'if name==main' 
#if __name__ == " __main__": 

print("Exercices 1 et 2")
f1 = Fraction(3,4)
f2 = Fraction(1,2)
a = f1.add(f2)
print(Fraction(3,4).show()+' + '+f2.show()+' = '+a.simplify().show())
f1 = Fraction(3,4)
f2 = Fraction(1,2)
a = f1.multiply(f2)
print(Fraction(3,4).show()+' * '+f2.show()+' = '+a.simplify().show())


print("Exercices 3 et 4")
print("H(10000) =" + H(10000))
print("Leibniz(10000) ="+Leib(1000))