
#dictionary:key value seperated by ":" and keys are unique ,not duplicate inthe place of keys we have to use immutable datatype... ......,it is muttable
details_ = {"name": "Teja",1:"number",(6,7):[1,2]}
print(details_)
#methods: key(),values(),item(),clear()
#keys():used to get all the keys from dict
#syntax: variable_name.keys())
details_ = {"name" :"sundari",
            "Age":56,
            "gender" :"female"}
print(details_.keys())
#values():used to get all the value from dict
#syntax: variable_name.values())
details_ = {"name" :"sundari",
            "Age":56,
            "gender" :"female"}
print(details_.values())
#items():used to get bothkey and value in a pair
#syntax:variable_name.items())
details_ = {"name" :"sundari",
            "Age":56,
            "gender" :"female"}
print(details_.items())
#clear():if we use the clear the dict will become empty
details_ = {"name" :"sundari",
            "Age":56,
            "gender" :"female"}
details_.clear()
print(details_)
#update:we can update any value 
details_ = {"name" :"sundari",
            "Age":56,
            "gender" :"female"}
details_.update({"name":"kumari"})
details_.update({"mob":"8976344367"})
print(details_)
