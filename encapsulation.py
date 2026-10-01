#encalpsulation #to create private method we need to put two underscore before method name
# example: __method
class bankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def getBalance(self):
        return self.__balance
    
b1 = bankAccount(5000)
#b1.__init__(5000) error =>init main class er moddo val deye delei hbe, not this
b1.deposit(3000)
print(b1.getBalance())
#__balance
#This makes it a private attribute (name-mangled), so we don't normally access it directly from outside the class.
#For example:
#print(account.__balance)=>error
