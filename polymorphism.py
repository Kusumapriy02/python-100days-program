'''
polymorphism: polymorphism means many form and it alliws same method,function or operator to perform different task depending on the same object...
types:
method overloading:means having multiple methods with the same name but different parameters
method overriding
operator overloading


method overloading:
'''
class cal:
    def sum(self,num,num_2 = 0):
        print(num - num_2)
    def sum(self,num,num_2 = 0,num_3=0):
        print(num-num_2-num_3)
obj = cal()
obj.sum(4,7)
'''
method overriding: the method overriding occurs when a child class provides its own implementation of a method already defined in its parent class....
'''
class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d = animal()
d.sound()
'''
operator overloading:this allows operator (+,-,*) to work differently for user-friendly objects
__add__(+)
__sub__(-)
__mul__(*)
__truediv__(/)
__eg__()(==)
__it__()(<)
'''
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = student(56)
s2 = student(66)
print(s1 + s2)
'''
abstraction:
Data abrastraction: Data abstraction is a process of hiding implemented details and showing only essential data to the user
eg: atm\car\app
'''
from abc import ABC,abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass


class bank:
    @abstractmethod
    def interest(self):
        raise NotimplementedError('Subclass must implement interest()')
class SBI(bank):
    def interest(self):
        print('SBI interest Rate:6.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate:5.5%')
class ICIC(bank):
    def interest(self):
        print('ICIC interest Rate:7.5%')
bank = [SBI(),HDFC(),ICIC()]

for j in bank:
    j.interest()
    
    
