'''
attributes
-------
-Attributes are variables that belongs to an object or the class
'''
class how:
    def details(self,name,age):
        self.name = name
        self.age = age
    
s1 = how()
s1.details('kusu',23)
print(s1.name)
'''
methods:These are nothing but the function inside the class
'''
class calculator:
    def add(self,num,num_2):
        print(num + num_2)
        
cal = calculator()
cal.add(45,6)
