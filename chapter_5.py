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

# Se ts
# unordered collection of unique items mutable
food={"pizza","burger","pasta"}
print(type(food))

empty_set=set() # to create an empty set
food.add("fries")
food.remove("pasta") # raises error if item not found
food.discard("pasta") # does not raise error if item not found
food.pop() # removes and returns an arbitrary item


