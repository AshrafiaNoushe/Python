n = int(input("Enter the num: "))

def recursion_n(num):
    if(num==0):
        return
    print(num)
    recursion_n(num-1)

recursion_n(n)

#factorial
def facto(num):
    if(num==0 or num==1):
        return 1
    else:
        return num* facto(num-1)

print(facto(5))
#sum of n numbers
def sum(num):
    if(num==0 or num==1):
        return 1
    else:
        return sum(num-1)+num

print(sum(5))