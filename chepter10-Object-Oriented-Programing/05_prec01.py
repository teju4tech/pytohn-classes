'''Storing a info for microsoft companey'''

class Programmer:
    def __init__(self,Name,Uidno,language,companey):
        self.Name = Name
        self.Uidno = Uidno
        self.language = language
        self.companey = companey

    @staticmethod
    def greet():
        greet("Good Morning")

    def printObj(self):
        print(f"The Name is {self.Name}")
        print(f"The UserId is {self.Uidno}")
        print(f"The language is {self.language}")
        print(f"The companey is {self.companey}\n")
    

Teju = Programmer("Tejpal singh",34,'C++','Microsoft')
Ishi = Programmer("Ishika singh",35,'java','Microsoft')
Anu = Programmer("Anuraag sharma",36,'javascript','Microsoft')
Subh = Programmer("Subham Dhakad",37,'Rust','Microsoft')
Teju.printObj()
Ishi.printObj()




        

    