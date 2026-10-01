class car:
    def start(self):
        self.__checkEngine()
        self.__satartEngine()
    def __checkEngine(self):
        print("checking engine...")

    def __satartEngine(self):
        print("starting engine....")

c1 = car()
c1.start()
#print(c1.start())