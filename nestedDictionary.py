student ={
    "name" : "Ashrafia Noushe",
    "marks": {
        "Math" : 90,
        "English" : 100,
        "Chemistry" : 98
    }
}
print(student)
print(student["marks"])
print(student["marks"]["English"])
student.keys() #all key show
student.values() #all val show
student.items() #ret all (key, val) pairs as  tuples
student.get("math") #math er val ret
#print(student["math2"]) will ret a error but if we use student.get["math2"] no error just simply None
#we will always use dict.get("key") not dict["key"]
#to add new dict.update(new val)
student.update({"city":"Jessore"})
print(student)
#or
new_dict = {
    "dept" : "CSE",
}
student.update(new_dict)
print(student)