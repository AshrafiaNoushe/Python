f = open("input.txt","r")
data = f.read() #f.read(5)=> 1st 5 letter ashbe spc included(by default read one char at a time like one by one)
print(data)
print(type(data))
f.close()
# w mode exixting file theke data erase kore new data overwrite kore
# a =>append mode exixting+new data write
#f.readline() read oneline at a time
f1= open("input2.txt","r")
string = f1.readline() #here output e extra new line ashbe as line er sesh e input file e\n invisible thake so output e count hoi
print(string)
print(type(string))
str = f1.readline()
print(str)
char = f1.read() #full file read korbe 
print(char)
print(type(char))
rd_one_char = f1.read(5) #will read five letter including space
print(rd_one_char)
f1.close()
ff = open("input.txt","w")
ff.write("overwriting....") #overwrite

f2 = open("input2.txt","a")
f2.write(" now using append")
ff.close()
f2.close()
