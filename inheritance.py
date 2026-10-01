class car:
    def start(self):
        print("staring...")
    def stop(self):
        print("stopping...")
        
        
class toyotaCar(car): #toyota inherited car class => eivabe define korbo
    def carName(self, name):
        self.name = name
        print(name)

c1=toyotaCar()
print(c1.carName("Toyota"))
# 3 types of inheritance
#1. single. 2.multi-level 3.multiple
# 1. child-parent 2, chile = another parent, 3, one inheriting multiple

#multiple inheritance
class A:
    def ClassA(self):
        print("Welcome to class A")
class B:
    def ClassB(self):
        print("Welcome to class B")       
class C(A,B):
    def __init__(self):
        print("Welcome to class C")
c1=C()
c1.ClassA()
c1.ClassB()
print(c1.ClassA())
print(c1.ClassB())