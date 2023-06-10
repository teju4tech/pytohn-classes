'''Constructor'''
class Employee:
    # center = "No One Can Beat me"
    # def __init__(option1,option2,option3,..)
    def __init__(self, Name, Branch,center):
        self.Name = Name
        self.Branch = Branch
        self.center = center
    
    def printObj(self):
        print(f"The Name is {self.Name}")
        print(f"The Branch is {self.Branch}")
        print(f"The Center is {self.center}")
    
    @staticmethod
    def greet():
        print('Good Morning')

info = Employee("Tejuka",'Devolpement Operations','Delhi')
Rohan = Employee("Rohan",'Deployments','Mumbai')
info.printObj()
Rohan.printObj()

