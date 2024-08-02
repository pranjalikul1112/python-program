#class Car:
  #  color = "blue"
 #   brand = "spresso"
#car1 = Car()
#print(car1.color)
#print(car1.brand)

#class Student:
#
 #   def __init__(self,name,marks):
  #      self.name = name
   #     self.marks = marks
    #    print("adding new student in database..")

#s1 = Student("pranjali  kul",98)
#print(s1.name, s1.marks)#pranjali kul

#s2 = Student("mayuresh kul",99)
#print(s2.name, s2.marks)

#class Student:
#parameterized constructor
 #   def __init__(self,name,marks):
  #      self.name = name
   #     self.marks = marks
    #    print("adding new student in database..")

#s1 = Student("pranjali  kul",98)
#print(s1.name, s1.marks)#pranjali kul
#s2 = Student("mayuresh kul",99)
#print(s2.name, s2.marks)
#let's practice
#create student class that takes name and marks of 3 subjects as argumets in constructor then create a method to print the average
#class Student:
 #   def __init__(self,name,marks):
  #      self.name = name
   #     self.marks = marks
    #def get_avg(self):
     #   sum = 0
      #  for val in self.marks:
       #     sum += val
        #print("hi",self.name,"your avg score is:", sum/3)
#s1 = Student("pranjali kul",[99,99,97])
#s1.get_avg()
#s1.name = "mayuresh kul"
#s1.get_avg()
#let's practice
#create account class with 2 attributes - balance and account no.
#create methods for debit,credit and printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance = ",self.get_balance())
    
    def get_balance(self):
        return self.balance



acc1 = Account(10000, 11122003)
acc1.debit(10000)
acc1.credit(500)
acc1.credit(40000)

