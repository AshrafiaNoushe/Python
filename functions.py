def sum(a,b):
    sum = a+b
    print(sum)
    return sum

sum(2,5)
def helloP(): #without parameter func call
    print("Hello Noushe") #No return

helloP()
output = helloP()
print(output) #None print cz no ret
def avgnum(a,b,c):
    sum = a+b+c
    avg=(sum)/3
    return avg

average = avgnum(1,23,4)
print(average)
#len check
cities =["jessore","khulna","dhaka","chandpur"]

def lenthList(list):
    return len(list)

x = lenthList(cities)
print(x)
def printsingle_ele(list):
    for val in list:
        print(val)

printsingle_ele(cities)

#finding factorial of n
n = int(input("Enter the num:"))
def fact(num):
    sum = 1
    for el in range(1,n+1):
        sum *=el

    return sum
f = fact(n)
print(f)