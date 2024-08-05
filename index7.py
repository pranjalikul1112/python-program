#class Account:
 #   def __init__(self, acc_no, acc_pass):
  #      self.acc_no = acc_no
   #     self.__acc_pass = acc_pass

   # def reset_pass(self):
    #    print(self.__acc_pass)

#acc1 = Account("11122003","abcd")

#print(acc1.acc_no)
#print(acc1.reset_pass())
#inheritance
#single inheritance
#class Car:
 #   color = "black"
  #  @staticmethod
   # def start():
    #    print("car started..")

    #@staticmethod
    #def stop():
     #   print("car stopped")

#class ToyotaCar(Car):
 #   def __init__(self,name):
  #      self.name= name
#car1 = ToyotaCar("fortuner")
#car2 = ToyotaCar("prius")

#print(car1.color)

#Multi-level inheritance
#class Car:
 #   @staticmethod
  #  def start():
   #     print("car started..")

    #@staticmethod
    #def stop():
     #   print("car stopped.")

#class ToyotaCar(Car):
 #   def __init__(self,brand):
  #      self.brand = brand

#class Fortuner(ToyotaCar):
 #   def __init__(self, type):
  #      self.type = type

#car1 = Fortuner("diesel")
#car1.start()

#Multiple inheritance
#class A:
 #   varA = "welcome to class A"

#class B:
 #   varB = "welcome to class b"

#class C(A,B):
 #   varC = "welcome to class C"

#c1 = C()

#print(c1.varC)
#print(c1.varB)
#print(c1.varA)
#super method
#class Car:
    #def __init__(self, type):
     #   self.type = type

    #@staticmethod
    #def start():
   #     print("car started")

  #  def stop():
 #       print("car stopped")

#class ToyotaCar(Car):
    #def __init__(self, name ,type):
   #     super().__init__(type)
  #      self.name = name
 #       super().start()
#car1  = ToyotaCar("prius","electric" )
#print(car1.type)   
#class method
#class Person:
 #   name = "anonymous"
#
 #   #def changeName(self,name):
     #   self.__class__.name = "pranjali"

  #  @classmethod
   # def changeName(cls, name):
    #    cls.name = name

#p1 = Person()
#p1.changeName("kul pranjali")
#print(p1.name)
#print(Person.name)

#Property
#class Student:
 #   def __init__(self,phy,chem,math):
  #      self.phy = phy
   #     self.chem = chem
    #    self.math = math
        

    #@property
    #def percentage(self):
     #   return str((self.phy + self.chem + self.math) / 3) + "%"

#stu1 = Student(98,97,99)
#print(stu1.percentage)

#stu1.phy = 86
#print(stu1.percentage)

#polymorphism
#class Complex:
 #   def __init__(self, real, img):
  #      self.real = real
   #     self.img = img

    #def showNumber(self):
     #   print(self.real,"i +",self.img,"j")

    #def __add__(self, num2):
     #   newReal = self.real + num2.real
      #  newImg = self.img + num2.img
       # return Complex(newReal,newImg)
    
    #def __sub__(self, num2):
     #   newReal = self.real - num2.real
      #  newImg = self.img - num2.img
       # return Complex(newReal,newImg)
    
#num1 = Complex(1, 3)
#num1.showNumber()

#num2 = Complex(4, 6)
#num2.showNumber()

#num3 = num1 - num2
#num3.showNumber()

#practice question
# define a circle class to create a circle with radius r using the constructor.
#define an area() method of the class ehich calculate the area of the circle .
#define a perimeter() method of the class which allows you to calulate the perimeter of the cirle.
#class Circle:
 #   def __init__(self, radius):
  #      self.radius = radius

   # def area(self):
    #    return (22/7) * self.radius ** 2
    
    #def perimeter(self):
     #   return 2 * (22/7) * self.radius
    
#c1 = Circle(21)
#print(c1.area())
#print(c1.perimeter())
#Define a employee class with attributes role,department and salary this classs show details() method.
#create an engineer class that inherits properties from employee and attributes:name and age
#class Employee:
 #   def __init__(self,role,dept,salary):
  #      self.role = role
   #     self.dept = dept
    #    self.salary = salary

    #def showDetails(self):
     #   print("role =",self.role)
      #  print("dept =",self.dept)
       # print("salary =",self.salary)

#class Engineer(Employee):
 #   def __init__(self,name,age):
  #      self.name = name
   #     self.age = age
    #    super().__init__("Engineer","IT","75.000")

#engg1 = Engineer("pranjali  kul", 20)
#engg1.showDetails()

#create a class called order which stores item and its price.
#under dunder function _ _ gt_ _()to convey that:
#order1>order2 if price of order 1>price of order2
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)
print(odr2 > odr1)