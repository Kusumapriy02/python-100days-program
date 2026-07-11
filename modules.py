''' A module is a python file (.py) that contains reusable code
1.variables
2.functions
3.objects
4.classes
5.statements
why this: instead of writing same code repeatedly ,we can store it in a module and use it whenever needed..
TYPES:user_defined,Built in
'''
import first_module
print(first_module.sub(5,6))
print(first_module.sub(51,6))
''' import specific function
'''
from first_module import add,sub
print(sub(45,7))
import  first_module as m
print(m.sub(45,7))

import first_module
print(first_module.power(6,7))
import  first_module as m
print(m.module(3,4))
''''
built in :
math
os
sys
random
''math'':sqrt(square root),factorial(factorial),power(pow),roundup(ceil),pi value(pi)
'''
import math
print(math.sqrt(25))
print(math.factorial(5))
''' os:The os module is used to interact with operating system: getcwd()--> current directory,mkdir()-->make directory
'''
import os
print(os.getcwd())
'''sys --> this will provide the information about python interpreter
'''
import sys
print(sys.version)
'''random : used to generate random values
'''
import random
print(random.randint(100000,999999))
colors = ['yellow','red','blue','green']
print(random.choice(colors))
