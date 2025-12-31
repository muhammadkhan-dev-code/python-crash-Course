# ---------Lecture 4 Dictionary and Sets ------------
 # Dictionary :  are used to store data in key  value 
# Unordered  mutable  dont allow duplicate keys 


info ={
    "name":"Muhammad khan",
    "subjects":["python","c","java"],
    "cgpa":8.9,
    "topics":("dict","sets"),
    "dept":"Software Engineering",
    "is_adult":True
}

print(info)
print(type(info))
print(info["is_adult"]) # true

info["name"]="Muhammad Ali"
info["surname"]="surname" # new key value  pair would be added 
# empty dict
null_dict={}

null_dict["name"]="Muhammad Khadim"

# nested dictionary

student={
    "name":"Muhammad Khan",
     "subjects":{
         "DS&A":94,
         "DS":100,
         "Flutter":100,
     }
}

print(student["subjects"]["DS"]) # 100

# methods in Dictionary
print("All keys in Student Dict ")

print(student.keys()) # return all keys from the dictionary nested keys will not returned

# type casting 
print("length of dict ",len(list(student.keys()))) # type casting
# len(student)

print("All values in dict : ",student.values()) # return all the values from dictionary
print(student.items()) # return all key value pair from dic as a tuple  
# dict_items([('name', 'Muhammad Khan'), ('subjects', {'DS&A': 94, 'DS': 100, 'Flutter': 100})])

print(student.get("name"))  # if the key is not exist inside the dictionary will not give an any error
print(student["name"]) # if the keys are not available in dict will give error
update_dict= student.update({"city":"Jamshoro","Dict":"Huyderabad",})
# print(student) if we will pass a sae key the value will be overwrite


# -------------Sets In Python -------------- 
# items are unique and immutable 
# list and dict can not be stored in Set

# collection={}  empty dictionary

null_set=set()
collection={1,2,3,4,"Hello","World",2,3}
# print(collection)
# print(type(collection)) <class 'set'>

print(len(collection))

# Methods In Sets

# set -> mutable and elements inside the set can not be immutable
nums={1,2,3,4}
nums.add(5)
print("values added inside the set after adding 5 :",nums)
print("values after removing the 5", nums.remove(5))
print(nums.clear())

# pop method remove the random value
numbers={1,3,4,5,6}
print(numbers.pop())

# union method is  sets
set_1={1,2,3,4}
set_2={4,5,6,}

print("Union Set", set_1.union(set_2))
print("Intersection of sets Set 1 & Set 2 :",set_1.intersection(set_2))

