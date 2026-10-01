class parentX:
    def __init__(self):
        pass
    def show_parent(self):
        print("showing parent class")
        
class childY(parentX):
    def __init__(self):
        print("child const")
        
    def showChild(self):
        super().show_parent()
        print("child class method..")
        
c1 = childY()
c1.showChild()