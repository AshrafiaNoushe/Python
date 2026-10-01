class ATM:
    def __init__(self, balance):
        self.__balance = balance
        self.i = 0

    def __checkBalance(self):
        return self.__balance

    def withdrawMoney(self, amount):
        pin = self.__checkPin()
        if pin:
            if amount <= self.__checkBalance():
                self.__balance -= amount
                print("Money deducted ", amount)
                print("Balance: ", self.__balance)
                return self.__balance
            else:
                print("Insufficient Balance...")

    def __checkPin(self):
        x = "12345"
        pin = input("Enter PIN: ")
        if pin == x:
            print("PIN Varified")
            return True
        elif pin != x:
            print("Wrong PIN, Try again..")
            self.i += 1
            if self.i == 3:
                print("Card Blocked...")
                return False
            return self.__checkPin()

    def addMoney(self, credit):
        self.__balance += credit
        print(f"Money added {credit} to main balance")
        print("Current Balance: ", self.__balance)


SwapOne = ATM(50000)
SwapOne.withdrawMoney(3400)
SwapOne.addMoney(5000)
