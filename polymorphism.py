# operator overloading=>
# dunder function __add__ => adding
# __sub__ => substracting
# __mul____=> miltiply
# __truediv____ =>division
# __mod____ => a%b
class complexNum:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(f"{self.real} + {self.img}j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complexNum(newReal,newImg)

num1 = complexNum(1,2)
num1.showNum()
num2 = complexNum(3,4)
num2.showNum()
num3 = num1+num2
num3.showNum()