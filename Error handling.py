''' Error handling:
syntax error:
---------
'''
for j in range(1,10):
    print(j)
    ''''
output:syntax error
indentation error:
'''
a = 30
if a>=10:
    print("Greater number")
else :
   print()
'''
value error:(raised when a function receives the right type of argument but an inapproprate value).
-------
'''
a = int(input("enter a number:"))
''''
ouput: value error
try
---------
the try block will test the code for error
syntax:try
exacept: This except let us handle the error in the code
syntax : except:
else
finally
'''
try:
    num = int(input("enter a number:"))
    num_2 = int(input("ENTER a num: "))
    print(num/num_2)

except ZeroDivisionError:
    print('will get Zerodivision error')
#handling specific exception:
try:
    num = int(input("Enter a number:"))
    result = 10/num
    print(result)
except ValuError:
    print("please enter a valid integer.")
except ZeroDvisionError:
    print("Cannot divide by Zeo")
#else: the else block runs only if no exception occurs.
try:
    num = int(input("Enter a number:"))
    result = 10 / num
except ZeroDivisionError:
    print("cannot divide by zero.")
else:
    print("Result:",result)
#finally :the finally block will excute either code contain error or not.

try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision error')
except ValueError:
    print('will get value error')
else:
    print('no error')
finally:
    print('end')
