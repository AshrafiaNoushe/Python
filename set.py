#collection of unordered items and it's immutable and unique
#we can't use list and dict in set because they are mutable
# #(set ele) are not mutable cz we cant modify them but the set elements can be added, rmv
collection={1,2,3,4,5,"ashu","noushe",3} #duplicate 
print(collection)
print(type(collection))
empty1={}
print(type(empty1))
empty_set = set()
print(type(empty_set))
empty_set.add(4)
empty_set.add(9)
empty_set.add(0)
print(empty_set)
#set.union(set2) 2set combined
#set.intersection(set2) 2 set common ele
set1={1,2,34,55,68,0,3}
set2={4,5,68,54,2,32,34,0}
print(set1.union(set2))
print(set2.intersection(set1))