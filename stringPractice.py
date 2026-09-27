str1="This is Noushe.\t I am 23 years old.\n Nice to meet you."
print(str1)
str2="Cse 23"
print(str1+str2)
print(len(str2)) #space also counted
#str1[0] = '2' # can't do it, can't access or manipulate this way. error
print(str2[1:4]) #str[:4] = 0 to 3
#\t for tab. \n for new line


#Slicing only in python not in anyother lang
str3="CSE"
#-3-2-1
print(str3[-3:-1])
print(str3.endswith("E")) #to check if it's end with some char or not, will return T/F
#str.capitalize()-> just str er 1st letter cptl hoi
#str.replace(old, new) ->old existing str part, new= new str
#str.find(word) => word match korle matching er 1st char index ret
#str.count("word")=> word koibar appear hoise count ret
