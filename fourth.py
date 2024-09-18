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