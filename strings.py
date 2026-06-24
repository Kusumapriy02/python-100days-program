#data types
#int
num = 8

#float
num_2 = 7.89
num = 6.89

print(num//2)

##string: it is a sequence of character that are enclosed in ' '," " ,""" """,  it is imuttable,concatination:adds to strings,tuple,list (+)
so = "python"
any_ = "is a language"
print(so + any_)

#indexing:This is used to access the particular char in the string by pass index position value,It has postive (it start from 0) and negative (last to first)indexing
so = "python"
print(so[4])
print(so[-2])


#methods:replace(),join(),split(),count()
#replace():it is used to change any substring in that particular string...
#syntax-->variable_name.repalce("old string","new string",count)
so = "python is language"
print(so.replace("a","A",2))
print(so)

#join():This method used to add a new substring after each char in the string
#syntax:"string".join(varia_name))
so = "python is language"
print("$".join(so))

#split:This method can divide the string into index in to list,based on the string pass by us.....
#syntax:variable_name.spilt('substring')
so = "python is a language"
print(so.split("is"))

#count:used to count the substring in particular string and also specify the index position
#syntax:variable_name.count("substring",starting index,ending index)
so = "python is a language"
print(so.count("is"))
#string built-in function:len(),min(),max()
#len():This finds len of the char present in str
so = "python is a language"
print(len(so))
#min():will get the min char in the str
so = "python is a language"
print(min(so))
#max():will get the max char in the str
so = "python is a language"
print(max(so))


