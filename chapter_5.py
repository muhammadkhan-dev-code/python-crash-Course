# dictionary in Python
# mutable unordered collection of items
# no duplicate keys allowed 
student={
    "name":"MUHAMMAD KHAN",
    "age":22,
    "city":"karachi",
    "rollNumber":"22SW068",
    
}

print(type(student))
print(student["name"]) 
student["favSubject"]="Mathematics"

# removing an item
student.pop("favSubject") # pop(key)
student.keys() # returns all keys

student.values() # returns all values in tuple format

student.items() # returns all items as (key,value) pairs

for key,value in student.items():
    print(f"{key}:{value}")





