#file: file is created using open()function
'''
there are two ways to open a file..
1.open()
syntax:
do = open('file name','mode')
#statement
close()
2.with(keyword):
syntax:
with open('file name','mode) as do:
do = open('demo.txt','r')
print(do.read())
close()

r = used  to read a file and this read() will read file line by line...,we can specify the size
w: creates a file or overwrites an exsting one.
x:creates a file only if it doesnot already exist
a : creates a file if needed otherwise appends data to existing fie
'''
with open("demo.txt","w") as do:
    print(do.write('hello'))
'''
a : creates a file if needed otherwise appends data to existing fie
'''
with open('demo.txt','a')as do:
    print(do.write('we are using file handling'))
'''
x: used to create a new by adding the inside the file,incase if the file is present it will raise an error.
with open('sakiyaa.txt','x')as do:
    print(do.write('we are using file handling'))

'''
with open('demo.txt','r')as do:
    print(do.read(50))
'''
readline():thus readline() function will read only one line at a time...
eg:
'''
with open('demo.txt','r')as do:
    print(do.readline())
'''
readlines():readlines() reads whole file and give it in a list 
'''
with open('demo.txt','r')as do:
    print(do.readlines())


