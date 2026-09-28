list = [1,2,3,4,6]

for el in list: # here can be num, el, val
    #print(el) #if i print print(list)=> here list size er full list print hobe
    if(el==3):
        el+=1
        continue
    print(el)

for num in list:
    print(num)

#if we want something after loop we can use else

for val in list:
    print(val)
else:
    print("Ended") #we can use it as break

#when char=='O' print o found and break

str="Going there bye"
for char in str:
    if(char=='o'):
        print("o founded")
        break
    print(char)
else:
    print("Ended")


#search and print num using loop
tupl = (12,45,34,5,67,8,9,0,98)
x=8
i=0
for el in tupl:
    print(el)
    i+=1
    if(el==x):
        print("Found at",i)