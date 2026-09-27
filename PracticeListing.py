"""
mov1=print(input("Enter 1st fav movie name: "))
mov2=print(input("Enter 2nd fav movie name: "))
mov3=print(input("Enter 3rd fav movie name: "))
""" #here will show none as ami print korsi jsut not storing in mov1,2,3
mov1=input("Enter 1st fav movie name: ")
mov2=input("Enter 2nd fav movie name: ")
mov3=input("Enter 3rd fav movie name: ")
movies=[]
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#to check palindrome we need to copy 1st list
list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6]
list_copy1=list1
list_copy1.reverse()
if(list_copy1==list2):
    print("Palindrome")
else:
    print("No")