''' Class trein write a book ticket ,get satus(no of seats),where istrein is arrived ? '''
'''Solving by me'''
# class Trein:
#     def __init__(self,TicketNo,Satus,Place):
#         self.TicketNo = TicketNo
#         self.Satus = Satus
#         self.Place = Place
    
    
#     def printInfo(self):
#         print(f"Ticket No is: {self.TicketNo}")
#         print(f"Status No is: {self.Satus}")
#         print(f"Place No is: {self.Place}")

#     @staticmethod
#     def greeting():
#         print("Good Morning")
    

# Ticket1 = Trein(34,'Seat NO: 25','sujapur')
# Ticket1.greeting()
# Ticket1.printInfo()

'''Solving by Mentor'''

class trein:

    def __init__(self):
        self.seats = 78
        self.fare = 175
    
    def bookTickets(self):
        self.seats -= 1
    
    def getStatus(self):
        print(self.seats)
    
    def getFareInfo(self):
        print(self.fare)

    
tr = trein()
tr.bookTickets()
tr.getStatus()
tr.getFareInfo()
tr.getStatus()
tr.getStatus()
tr.getStatus()
     