class student:
    def __init__(self): #__init__(self) built-in no cng #default cons
        pass

    #name = "Noushe"
    def __init__(self,fullname,marks): #parameterized constructor
        self.name = fullname
        self.marks = marks



f= open("input.txt","w")
s1 = student("Ashu",90)
f.write(f"{s1.name},{s1.marks}")
print(s1.name, s1.marks)
f.close()
