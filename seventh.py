print("sairam")
#file I/O
#first open 
#read(r)
'''
f=open("sam.txt","r") #rt=r (t=text mode)
#data=f.read()
#d1=f.read(8)
line1=f.readline()
#print(data)
#print(d1)
print(line1)
#print(type(data))
f.close()
'''
'''#write(w)  
#f=open("sam.txt","w")
#append(a)
f=open("sam.txt","a")
#wrt=f.write("myself sai ganesh ,i am learning python")
app=f.write("\nthank you")
f.close()
'''
'''
f=open("sam.txt","r+") #read and write
f.write("love")
print(f.read())
f.close()
'''
'''
f=open("sam.txt","w+") #write and read
f.write("sai")
print(f.read())
f.write("sathya")
f.close()
'''
'''
f=open("sam.txt","a+") #append ,write and read
#f.write("sai")
print(f.read())
f.write("narayana")
f.close()
'''
#r+ read+ overwrite (ptr start) -no truncate
#w+ read+ overwrite (ptr start) -truncate
#a+ read+ append (ptr end) -no truncate

#with synatx
with open("sam.txt","r") as f:
    data=f.read()
    print(data)
with open("sam.txt","w") as f:
    f.write("sathya narayana ")