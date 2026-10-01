#del is used to delete objects or method

class account:
    def __init__(self,accName, password):
        self.accName = accName
        self.password = password
        
p1 = account("Ashu","23456")
del p1.password
print(p1.accName)
## __ double underscore deye variable/method private korte pari
#private properties only class e access korte parbo