#passing by value
def some(a):
    for j in a:
        print(j)
some([1,2,3])
#reference
a = (1,2,3)
def some(a):
    for j in a:
        print(j)
some(a)
#return keyword:in a function if a return is excuted then it will exit from the function with certain returned values
def myfunc_(b):
    return 5 + b
a = myfunc_(10)
print(a)
def myfunc_(b):
    return 5 + b
a = myfunc_(10)
c = myfunc_(100)
print(a)
print(c)
import builtins
builtin_functions = [
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")
#recursive function:it can call itself repeatedly  until a specified condition is met..
#syntax:def func_name(parameter):
        #if condition : --> base name
        #return statement
        #else:return statement
    #print(func_name(arguments))
def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num-1)
num = 1
print(func_name(num))
