# @property convert methods into variable/attributes


class result:
    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    @property
    def calculateResult(self):
        return (self.sub1 + self.sub2 + self.sub3) / 3


t1 = result(99, 97, 95)
print(t1.calculateResult)
t1.sub3 = 90
print(t1.calculateResult)
