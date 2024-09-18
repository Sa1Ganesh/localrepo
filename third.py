print("sai ram")
'''
#lists []
#mutable data type
marks=[95,94.6,85,86.7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
student=["sai",85,"delhi",1.0]
print(student)
student[0]="sathya" #mutable
print(student)
#list slicing
print(marks[0:2])
print(marks[:3])
print(marks[0:])
print(marks[-3:-1])
#list methods
list=[2,1,3,6]
#list.append()
list.append(7)
print(list)
#list.sort()
list.sort()
print(list)
#list.sort(reverse=True)
list.sort(reverse=True)
print(list)
#list.reverse()
list.reverse()
print(list)
#list.insert(idx,el)
list.insert(5,10)
print(list)
#list.remove()
list.remove(10)
print(list)
#list.pop(idx)
list.pop(2)
print(list)
'''
#tuples()
#immutable data type
'''
tup=(2,3,1,5,1)
print(type(tup))
print(tup[0])
#tup[0]=6 #immutable
tup=(1,)
print(tup)
#tuple slicing same as list
#tuple methods
#tuple.index(el)
print(tup.index(1))
#tuple.count(el)
print(tup.count(1))
'''
#p1
'''
movies=[]
mov1=input("enter 1st movie: ")
mov2=input("enter 2nd movie: ")
mov3=input("enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("fav movies :",movies)
'''
'''
movies=[]
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))
print("fav movies: ",movies)
'''
#p2
list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome") 
#p3
'''grade=("c","d","a","a","b","b","a")
print(grade.count("a"))
grade=["c","d","a","a","b","b","a"]
grade.sort()
print(grade)'''