#list data type:It is the collection of different data typees enclosed in[] seperated by ,List is muttable
all_type = [1,'devara',[1,2]]
print(all_type)
#methods:append(),extend(),pop(),remove(),insert(),clear(),index(),count(),reverse(),copy()
#List basically known as muttable lets prove
#append:variable_name.append(int):This is used to add new item into list,but it will add in last index position
any_ = [1,2,3,4]
print(any_)
any_.append(5)
print(any_)
any_.append(6)
print(any_)
#muttable:The datatype can be modified, immutable:cannot be modifiy
#eg:immuatable:string
so = 'AI is important'
print(so)
print(so.replace('AI','Ds'))
print(so)
#eg:muttable:list
any_ = [1,2,3,4]
print(any_)
any_.append(5)
print(any_)
any_.append(6)
print(any_)
#extend():this also add a item in the lNDEX position ,but it will give each value in the each index positions
any_=[1,2,3,4]
any_.extend([23,24])
print(any_)
print(len(any_))
any_=[1,2,'python is a language',[45,78,"java is a language",[1,23],90],'Hello']
print(any_[3])
print(any_[3][2][10])
#pop():this will delete the value from the list but,it will del based on index position
#syntax:var_name.pop(index)
any_ = [1,2,3,4]
print(any_)
any_.pop(2)
print(any_)
#remove:used to del the item from the list, but it will del direct value from list
#syntax:var_nam.remove(value)
any_ = [1,2,3,4]
print(any_)
any_.remove(2)
print(any_)
#insert():It add  the valuen in particular index
any_ = [1,2,3,4]
print(any_)
any_.insert(2,23)
print(any_)
#sort:
any_=[23,45,67]
any_.sort()
print(any_)
#clear:
any_=[23,45,67]
any_.clear()
print(any_)
#index:
any_=[23,45,67]
any_.index(45)
print(any_)
#reverse:
any_=[23,45,67]
any_.reverse()
print(any_)
#copy:
any_=[23,45,67]
waste = any_.copy()
print(any_)




