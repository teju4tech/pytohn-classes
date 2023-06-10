'''Create a class Employee and add salary
   and increment propertics to it.
   write a method salaryAfterIncrement method
   with a @property decorator with s setter
   changes the value of Increment based on the 
   sallry?
'''
'''MI solution'''
# class Employee:
#    def __init__(self,salary):
#       self.salary = salary
   
#    def salaryAfterIncrement(self):
#       self.salary = 1000 + self.salary
   
#    @property
#    def salary(self):
#       return self.salary
   
#    # @Increment.salary(self,value)
#    # self.salary = value

   
# em = Employee(1000)
# print(em.salary)
# salaryAfterIncrement()
# print(em.salary)


'''Menter's solution'''

class Employee:
   def __init__(self,salary,increment):
      self.salary = salary
      self.increment = increment

   @property
   def salaryAfterIncrement(self):
      return self.salary * (1+self.increment)
   
   @salaryAfterIncrement.setter
   def salaryAfterIncrement(self):
      self.salary = self.salary *(1+self.increment) 
   
emp1 = Employee(12000, 0.1)
print(emp1.salaryAfterIncrement)

