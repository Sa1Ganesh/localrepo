print("sairam")
#dictinary (key:value pairs)
#unorderd,mutable,no duplicate keys
'''
info={
    "key":"value",
    "name":"sathya",
    "place":"puttaparthi",
    "age":22,
    "is_adult":True,
    "marks":[25,24.5],
    "grade":("A","B"),
    1:"sai"
}
print(info)
print(type(info))
print(info["name"])
info["name"]:"sai"
print(info)
null_dict={}
print(null_dict)
'''
#nested dictionaries
'''
student={
    "name":"ganesh",
    "subjects":{
        "maths":74,
        "phy":59,
        "che":60
    }
}
print(student)
print(student["subjects"]["che"])
#dictionary methods
#mydict.keys()
print(student.keys())
#mydict.values()
print(student.values())
#mydict.items()
print(student.items())
#mydict.get("key")
print(student.get("name"))
#mydict.update(newdict)
student.update("place":"puttaparthi")
print(student)
'''
#set
#unordered ,immutable,unique elements
'''
collection={1,2,3,3,4,"sai","sai"}
print(collection)
print(type(collection))
print(len(collection))
num={}
print(type(num))
num1=set()
print(type(num1))
'''
#set methods
col=set()
#set.add(el)
col.add(1)
col.add(3)
col.add(1)
col.add(3)
col.add(2)
col.add(5)
print(col)
#set.remove(el)
col.remove(3)
print(col)
#set.pop()
col.pop()
print(col)
#set.clear()
'''col.clear()
print(col)'''
col1={7,8,9,5}
#set.union(set2)
print(col.union(col1))
#set.intersection(set2)
print(col.intersection(col1))
#p1
dict={
    "table":["furniture","rows and columns"],
    "cat":"animal"
}
print(dict)
#p2
subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(subjects))
#p3
'''marks={}
x=int(input("enter maths: "))
marks.update({"mat":x})
y=int(input("enter physics: "))
marks.update({"phy":y})
z=int(input("enter chemistry: "))
marks.update({"che":z})
print(marks)'''
#p4
values={9,"9.0"}
print(values)
