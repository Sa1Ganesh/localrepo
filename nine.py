print("sai ram")
#oops part 2
#del
'''
class Student:
    def __init__(self,name):
        self.name=name
s1=Student("sathya")
print(s1.name)    
del s1
print(s1.name)    
'''
#private attributes and methods
'''
class Account:
    def __init__(self,acc_no,acc_pw):
        self.acc_no=acc_no
        self.__acc_pw=acc_pw #private(__)
    def reset_pass(self):
        print(self.__acc_pw)

acc1=Account("12345","abcd")
print(acc1.acc_no)
#print(acc1.__acc_pw) 
print(acc1.reset_pass())   
'''
 #inheritance
#single inheritance
'''
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")    
 
class Toyotacar(Car): 
    def __init__(self,name):
        self.name=name

car1=Toyotacar("fortuner")
car2=Toyotacar("prius")

print(car1.name)
print(car1.start())
print(car2.name)
print(car2.color)
print(car2.stop())
'''
#mutlilevel inheritance
'''
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")    
 
class Toyotacar(Car): 
    def __init__(self,brand):
        self.name=brand

class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesel")
car1.start()    
'''
#multiple inheritance
'''
class A:
    varA="welcome to class A"
class B:
    varB="welocme to the class B"
class C(A,B):
    varC=("welcome to class C"
          )
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
'''
#super method
'''
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started ..")
    @staticmethod
    def stop():
        print("car stopped ..")

class Toyotacar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1=Toyotacar("prius","electric")
print(car1.type)
#print(car1.start())
'''
#class method
'''
class Person:
    name="anonymous"

    #def changeName(self,name):
        #self.name=name
        #Person.name=name
        #self.__class__.name="sathya"
    @classmethod
    def changeName(cls,name):
        cls.name=name 
p1=Person()
p1.changeName("saiganesh")
print(p1.name)
print(Person.name)
'''
'''
class Student:
    def __init__(self,mat,phy,che):
     self.mat=mat
     self.phy=phy
     self.che=che
     self.percentage=str((self.mat+self.phy+self.che)/3)+"%"


stu1=Student(95,96,99)
print(stu1.percentage)

stu1.phy=85
print(stu1.phy)
print(stu1.percentage)

class Student:
    def __init__(self,mat,phy,che):
     self.mat=mat
     self.phy=phy
     self.che=che

    @property
    def percentage(self):
       return str((self.mat+self.phy+self.che)/3)+"%"
     

stu1=Student(95,96,99)
print(stu1.percentage)

stu1.phy=85
print(stu1.phy)
print(stu1.percentage)
'''
#polymorphism :operator overloading
'''
print(1+2) #addition
print("apna"+"college") #concat
print([1,2,3]+[4,5,6])#merge

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
  
    def shownumber(self):
        print(self.real,"i+",self.img,"j")
    
    #def add(self,num2):
    def __add__(self,num2): #dunder function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)

num1=Complex(1,3)
num1.shownumber()
num2=Complex(2,5)
num2.shownumber()

#num3=num1.add(num2)
num3=num1+num2
num3.shownumber()
'''
#p1
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self) :
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
    
c1=Circle(21)
print(c1.area())
print(c1.perimeter())
#p2
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetails(self):
        print("role",self.role)
        print("dept",self.dept)
        print("salary",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT","75000")

eng1=Engineer("sathya",14)
eng1.showdetails()
#p3
print("thank you shradha \nsai ram")



