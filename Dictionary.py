#dictionary is used to store data key:val pairs
#built-in in python dict={} & it is mutable we can cng or manipulate val, it's unorderd, don't allow duplicate
info = {
    "key":"value",
    "marks" : [70,90,45,78,87],
    "tupl" : ("A+","A+","A+"),
    "name":"Noushe",
    "cgpa" : 3.80,
    "age" : 23,
    "is_adult": True,
}
print(info)
print(type(info))
info["name"]="Ashrafia" #mutable
print(info)
null_dict={} #empty dictionary
null_dict["name"] ="epty one"
print(null_dict)