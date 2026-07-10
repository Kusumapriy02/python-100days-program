'''generator:This is a special function that returns the itertor,instead of returning all the values at once...,here we are going to use yield key word
''
def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))

''working of generator:when a function is called ,it doesnot excute the function immediately ..,it will returns the generator object,then the function will pause at each yield...
' the next() is called again, execution resumes from where it stopped
'''
def demo():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("End")
    yield 3
how = demo()
print(next(how))
'''
'with generator

'''
def how(so):
    for i in range(so):
        yield i*i
any_= how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
'''without generator
'''
def sqt(n):
    for j in range(n):
        print(j*j)
sqt(5)
'''''functions:returns complete result
     function will end after the return the values
     more memory usage
     this function never resume
     generator:
     yield
     return one value at once
     pauses after every yield
     less memory usage
     resumes after next()
     yield keyword:This will produces the values
     but the yield pauses the functions
     and yield will save the functions current state
     yield will continues where it stopped
     next():
     The next() function is used to retrieve the next value from a generator''
'''
def how(so):
    for i in range(so):
        yield i*i
any_= how(5)
print(next(any_))
print(next(any_))
'''stopIteration:
calling next() function after all values retrieve then it will raise stopiteration exception
stop iteration exception
'''
def how(so):
    for i in range(so):
        yield i*i
any_= how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
''
def how(so):
    for i in range(so):
        yield i
any_= how(10)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
'''generator expression :the generator expression is similar to a list comprehension but uses  parenthesis() instead of []
'''
gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
