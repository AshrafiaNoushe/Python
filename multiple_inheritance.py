class student:
    def studentInfo(self, name, roll):
        self.name = name
        self.roll = roll
        return name, roll
        
class marks:
    def countMarks(self,s1,s2,s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        return s1,s2,s3
    
class Result(student,marks):
    def show_result(self):
        self.result = (self.s1+self.s2+self.s3)/3
        return self.name, self.roll, self.s1, self.s2, self.s3, self.result

t1 = Result()
t1.studentInfo("Noushe","B220101029")
t1.countMarks(90,95,99)
print(t1.show_result())