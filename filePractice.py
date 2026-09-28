f = open("sample.txt","w") #will auto create the file if not exist
f.close()

with open("sample.txt","r") as f:
    data = f.read()
    print(data)

with open("sample.txt","w") as f:
    f.write("now")

    #if we follow the with one then don't need f.close