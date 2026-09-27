#list
marks=[102.9,100.3,90.4,67.4]
print(marks)
print(type(marks))
#we can access any ele in list also can manipulate
#in list there can be diffrent datatypes only allowed in python
Info =["Noushe",1029,"CSE"]
print(Info)
Info[0]="Ashrafia"
print(Info) #so it's mutable in list
#list slicing here ending index not included
print(marks[1:3]) #100.3,90.4
print(marks[-3:-1]) #100.3,90.4

#print(marks.append(90.76)) wrong proc
marks.append(90.76)#added at last
print(marks) 

marks.sort() #sorting
print(marks) #char string all can be sort here
#list.insert(index,ele)
#print(marks.insert(3,90.3)) wrong proc
marks.insert(3,90.3)
print(marks) 

marks.reverse()#backwarding
print(marks)
#list.remove(ele) here when the ele will appear as first then it will rmv it
marks.remove(90.3)
print(marks)
#list.pop(index) declared index deleted
marks.pop(2)
print(marks)
