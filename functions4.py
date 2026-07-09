#to delete duplicate value in list using functions

nums = [23,5,6,6,7,23,8]
empty_ = []
def removes_(numbs,empty):
    for j in nums:
        if j not in empty:
            empty_.append(j)
    print(empty_)
removes_(nums,empty_)

#checking whether the number is prime or not
prime_ = 7
count = 0
def prime_check(prime_,count):
    for j in range(1,prime_+1):
         if prime_ % j ==0:
             count += 1
             
    if count == 2:
       print(f'{prime_} is a prime')
    else:
          print(f'{prime_} is not a prime')
prime_check(prime_,count)
def student(name="user"):
    print("Hello",name)
student()
student("kusu")

#checking given character is vowel or not
def check_vowel(ch):
    if ch.lower()in "aeiou":
        return True
    else:
        return False
Alpha_= input("Enter a character:")
if check_vowel(Alpha_):
    print("it is a vowel")
else:
    
    print("it is not vowel")
#counting the upper case and lower case letters using functions
def count_case(text):
    upper_count = 0
    lower_count = 0
    for ch in text:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
    return upper_count, lower_count
sentence = input("Enter a string:")
uper, lower = count_case(sentence)
print("uppercase letters:", uper)
print("lowercase letters:", lower)
        
