#tuple vs list 
#in tuple we use () & in list we use []
#tuple is inmutable mean amra manipulate korte parbo na jmn list e korsi
tup = (1,2,3,4,5)
print(tup)
print(type(tup))
#single val tuple
tup2=(1,) #need the comma
#tup[1] = 90 #can't do it like we did in list
#to find ele in tuple tup.index(ele) it will ret index
print(tup.index(3))
#to count a ele apperance tup.count(ele)
print(tup.count(2))