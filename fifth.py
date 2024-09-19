print("sai ram")
#loops
#while loops
'''
name=1
while name<=5 :
   print("sathya")
   name+=1
print(name)  
i=1
while i<=10:
   print("sai",i)
   i+=1
print("loop ended")
i=5
while i>=1:
   print(i)
   i-=1
'''
'''
#p1
i=1
while i<=100:
    print(i)
    i+=1
print("loop ended")    
#p2
i=100
while i>=1:
    print(i)
    i-=1
print("loop ended")  
#p3
n=int(input("enter any number: "))
i=1
while i<=10:
    print(n*i)
    i+=1
print("loop ended")    
#p4
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1
#p5
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if nums[i]==x:
     print("found",i)
    else:
        print("finding...")
    i+=1
'''  
'''
#break 
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")   
#continue
i=1
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
print("end of loop")   
'''
'''
#odd numbers
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue #skip
    print(i)
    i+=1 
#even numbers
i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
print("loop ended")  
'''
#for loops(sequential travesal)
'''
sports=["cricket","badminton","volleybal","basketball","football"]
for val in sports:
   print(val)
nums=(1,2,3,4)  
for n in nums:
   print(n) 
str="SathyaNarayana"   
for c in str:
   if(c=="N"):
      print("found",c)
      break
   print(c)
'''
'''
#p1
nums=[1,4,9,16,36,49,64,51,100]
for n in nums:
   print(n)
x=36   
num=(1,4,9,16,36,49,64,51,100)
for n in num:
   if(n==36):
      print("found x",n) 
      break
   print(n)
'''   
#range(start,stop,step)
'''
seq=range(5)
for i in seq:
   print(i)
for i in range(5,8):
   print(i)  
for i in range(1,7,2):
   print(i)
#odd numbers
for i in range(1,20,2):
   print(i)  
#even numbers      
for i in range(2,20,2):
   print(i) 
'''   
#mutiples
'''
n=int(input("enter any number: "))
for i in range(1,11,1):
    print(n*i)
# 1 to 100
for i in range(1,101):
    print(i)
# 100 to 1    
for i in range(100,0,-1):
    print(i)
#pass
for i in range(5):
    pass
print("not required") 
''' 
#p1 (sum)
n=int(input("enter any number: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
'''for i in range(1,n+1):
    sum+=i '''
print("total sum: ",sum)
#p2(factorial)
n=int(input("enter any number: "))
fac=1
i=1
while i<=n:
    fac*=i
    i+=1
'''for i in range(1,n+1):
    fac*=i '''
print("factorial: ",fac)    

