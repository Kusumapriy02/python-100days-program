#set:it is a collection of unorder elements that are seperated by ","and it is muttable can remove duplicate values  by itself..
go = {1,2,3,4,2,3}
print(go)
#methods:union(),intersection()
#union():(|):combine the elements from both set
#syntax:set_1.union(set_2)
go = {1,2,3,4}
so = {4,5,6,7}
print(go | so)
print(go.union(so))
#intersection():common element from both sets
#syntax:set_1.intersection(set_2)
go = {1,2,3,4}
so = {4,5,6,7}
print(go & so)
print(go.intersection(so))
#symentric difference:^ all different elements from both sets
go = {1,2,3,4}
so = {4,5,6,7}
print(go ^ so)
print(go.symmetric_difference(so))
#add():used to add new element into set
go = {1,2,3,4}
go.add(5)
print(go)
#remove(): to del from set based on element
go = {1,2,3,4}
go.remove(4)
print(go)
#pop():to del value based opn index
go = {1,2,3,4}
go.pop()
print(go)
#discard:
go = {1,2,3,4}
go.discard(9)
print(go)
