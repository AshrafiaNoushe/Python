#range(start?, stop, step?) by default start =0 and i++
#range(5)=>0,1,2,3,4
#step mean koto inc

for el in range(0,100,2):
    print(el)

#multiplication
n = 2
for el in range(1,11):
    print(f"{n} x {el} = {n * el}") #f" use koira str print er moddo val print kora jai {val} use koira

#pass statement for a lopp where i don't need to do anything
for el in range(12):
    pass #will do nothing

#practice sum of n muner 1 to n
n = int(input("Enter the num: "))

sum =0
for el in range(1,n+1):
    print(f"{el}+ {sum} = ")
    sum+=el
    print(f"{sum}")

#find factorial

n = int(input("Enter the num: "))
sum = 1
for el in range(1,n+1):
    print(f"{el}*{sum}")
    sum*=el
    print(f"= {sum}")