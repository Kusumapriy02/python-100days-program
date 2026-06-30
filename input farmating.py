#input formating from users
#1.input():THE INPUTBFUNCTION IS USED TO TAKE INPUT FROM USER..
#FOR INT:
num = 89
num_2 = int(input("ENTER A NUMBER:"))
print(num + num_2)
#string:
how = input("Enter a char:")
print(how + 'Teja')
#float:
sal = float(input("ENTER A NUMBER:"))
print(sal,"is the monthly salary")
#list:
group = list(map(int,input().split()))
print(group)
#tuple:
group = tuple(map(int,input().split()))
print(group)
hii = tuple(input().split())
print(hii)
#eval:
num = eval(input("enter:"))
print(type(num))

name_ = input("enter your name:")
age_ = int(input("enter your age:"))
print(name_,"your age is",age_)
print(f"{name_} your age is {age_}")
#module format:
name_ = input("enter your name:")
age_ = int(input("enter your age:"))
print("My name is %s and i'm %d years old"%(name_,age_))
                  
