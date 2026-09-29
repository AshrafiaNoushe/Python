#methods
class student:
    def __init__(self):
        pass
    def dept_info(self,batch,session):
        self.batch = batch
        self.session = session
    def student_info(self,name,cg):
        self.name = name
        self.cg = cg
    def get_info(self):
        return self.batch, self.session,self.name,self.cg
s1 = student()
s1.dept_info("CSE-22", "2022-23")
s1.student_info("Ashrafia Noushe", 3.66)
f = open("input.txt","a")
f.write(f"{s1.batch},{s1.session},{s1.name},{s1.cg}")
print(s1.get_info())