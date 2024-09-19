print("sairam")
'''
#functions
def sum(a,b):
    s=a+b
    return s
print(sum(2,3))
print(sum(5,9))

def print_s():
    print("sathya")

print_s()
print(print_s()) #no return

#avg of 3 nums
def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
cal_avg(2,3,5)   
'''
#built-in functions
# print()
print("sai")
# len() 
print(len("sathya"))
# type()
print(type("sathya"))
# range()
print(range(5))
#default parameters
def cal_p(a=2,b=3):
    print(a*b)
    return a*b
cal_p()
cal_p(4,5)
cal_p(5)
#p1
nums=[1,2,3,4]
def len_l(list):
    print(len(list))

len_l(nums)
#p2
def same_l(list):
    for i in list:
        print(i,end=" ")
same_l(nums)
#p3
def fact(n):
    fac=1
    for i in range(1,n+1):
      fac*=i
    print(fac)
fact(6)   
#p4 USD TO INR
def con_(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD= ",inr_val,"INR")
con_(1000)   