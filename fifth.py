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