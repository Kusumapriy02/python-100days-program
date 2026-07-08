#lambda function: this is also called as annonymous function..,it can take n number of arguments but having only one expression
#syntax: lambda arguments : expression
some = lambda an,so :an + so
print(some(10,8))
some = lambda an,so :an - so
print(some(10,8))
some = lambda an,so :an * so
print(some(10,8))
some = lambda an,so :an % so
print(some(10,8))
some = lambda an,so,why :an + so*why
print(some(10,8,2))
#filter():it is builtin function use to filter elements from an itterables such as list ,tuple and set based on condition
#syntax:filter(function,itterable):This filter() unction returns filter object so we can convert that into list,set,tuple
nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 ==0,nums)
print(set(rev))
nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 !=0,nums)
print(set(rev))
#list comprehension:This offers a shorter syntax when we want to create a new list from the old
#syntax:variable_name = [expression loop condition]
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_]
print(new_)
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_ if j%2==0]
print(new_)
#dictionary comprehension: This offers a shorter syntax when we want to create a new dict from the old dict
#syntax:variable_name = [expression loop]
old_dict = {1:2, 3:4,5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j%2 == 0}
print(new_dict)
      
