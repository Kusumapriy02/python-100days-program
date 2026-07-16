'''
self keyword
----self refers to curent object
'''
class Test:
    def display(self):
        print(self)
te = Test()
print(te)
te.display()

'''
constructor:This constructor intializes the object automatically when it is created...
'''
class Batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display (self):
        print(self.name)
        print(self.branch)
B4 = Batch('kusuma','cs')
B4.display()
        
#protected        
class fam:
    def __init__(self):
        self._name = "kusum"
f = fam()
print(f._name)
#private
class bank:
    def __init__(self):
        self.__pin = '6600';
AC=bank()
print(AC._bank__pin)


class Bank:
    def __init__(self):
        self.__pin ='770'
    def display(self):
        print(self.__pin)
ac = Bank()
ac.display()
'''
Encapsulation :means wrapping the data and methods into a single unit while controling
'''
class atm:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
tran = atm(balance = int(input("Enter Amount:")))
tran.deposit(amount = int(input("Enter Amount:")))
