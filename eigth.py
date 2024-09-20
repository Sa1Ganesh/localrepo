#oops in pyhton
print("sai ram")
'''
class Student:
    college_name="jain" #class attribute
    name="anonymous"
    def __init__(self,fullname,marks):
       self.name=fullname #object attritube ,>class attr
       self.marks=marks
       print("adding a new student")
    def welocme(self):  #methods(functions)
       print("welcome student",self.name)
    def get_marks(self)
       return self.marks
        

s1=Student("ganesh",97)
print(s1.name,s1.marks) 
s2=Student("akhil",98)
print(s2.name,s2.marks)

s1.welocme()
print(s1.get_marks()) 

'''

'''
class Car:
    color="white"
    brand="mercedes"
c1=Car()
print(c1.color)
print(c1.brand)
'''
'''
#p1
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is",sum/3)
    @staticmethod
    def college(): #static methods
        print("jain")

s1=Student("sai",[95,96,98])
s1.get_avg()
s1.college()
'''
#abstraction and
#encapsulation
class Car:
    def  __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started ..") 
car1=Car()
car1.start()           
#p1
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("RS.",amount ,"was debited")
        print("total balance",self.get_balance())
    #credit method
    def credit(self,amount):
        self.balance+=amount
        print("RS.",amount ,"is credited")
        print("total balance",self.get_balance()) 
    def get_balance(self):
        return self.balance

acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(5000)





