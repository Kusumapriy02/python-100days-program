#functions:it is block of code that can be reusable, can avoid the repeated line of code...
#they aretwo types :built in:: print(),max(),min(),sum() ,user define:this function starts with a keyword (def)
def add(a,b):
    print(a + b)
add(3,4)
#types of arguments: requeried arguments, default,keyword,variable length
#required arguments: we have to pass same number a4guments with defination of the function
def add(a,b):
    print(a+b)
add(2,3)#we shouldnot use like this we should give exact value through the arguments
#default argument:
def add(a,b):
    print(a)
num = 3
num_2 = 8
def add(a , b):
    print(a)
add(num,num_2)    
#key word():
def add(a,b):
    print(a + b)
add(a = 8, b = 9)
a = 6
b = 9
def add(a,b):
    print(a + b)
add(a , b)
#variable length:can pass n number of arguments and just use (*arg) in the parameters, will receive tuple of arguments
num = 7
num_2 = 8
num_3 = 7
num_4 = 5
def add(*a):
    print(a)
add(num,num_2,num_3,num_4)
def all_(**Any):
    print(Any['AGE'])
all_(Name = "KUSU",AGE =19)
#GLOBAL VARIABLE:
num = 8
def func_():
    print(num)
func_()#8 can be used throughout the  function
#local variable:
def fun():
    num_ = 9
    print(num)
fun()
print(num)
#to change the global variable  by using keyword (global) that can change completely inside and outside function
num = 89
def fun():
    global num
    num = 8
    print(num)
fun()
print(num)
    
    
    
    
