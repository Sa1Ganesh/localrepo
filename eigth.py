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


s1=Student("sai",[95,96,98])
s1.get_avg()