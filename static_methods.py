class student:
    @staticmethod #static method er decoration eita must debo method define korar age or else error ashbe
    def welcome_msg(): #in normal method we use self as parameter but if we don't want to use any self param we can use stacic method
        print("welcome...")

s1=student()
s1.welcome_msg()

class calculator_try:
    @staticmethod
    def mul_num(a,b):
        return a*b
    def add_num(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return num1+num2
    @staticmethod
    def sub(c,d):
        print("substracting....")
        #if i call within the print it will show none cz there is no return val
    @staticmethod
    def sub2(c,d):
        print("substracting....")
        return c-d
t1 = calculator_try()
print(t1.mul_num(2,3))
print(t1.add_num(7,9))
t1.sub(7,1) #we can simply call this without printing val it will give output not the return val
t1.sub2(5,2)
#print(t1.sub(4,1))
print(t1.sub2(4,1))# here we got ret val




