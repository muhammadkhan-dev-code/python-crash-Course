# 1: conditional statements
#  if and elif and else
marks=90

if marks>=90:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
elif marks>=60 and marks<70:
    print("Grade D")
else:
    print("Grade F")

age= input("Enter your age: ")
age=int(age)
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# list in python
# multiple values in a single variable using list
fruits= ["apple", "banana", "mango", "grapes"]
print(fruits) # print whole list
print(fruits[0]) # print first item
print(fruits[2]) # print third item 
if "banana" in fruits:
    print("Banana is present in the list")
else:
    print("Banana is not present in the list")
print("Length of fruits list is: ", len(fruits)) # length of list
#  add values in list
fruits.append("orange") # add item to the list
print("Fruits list after adding orange: ", fruits)
# remove item from list
fruits.remove("mango") # remove mango from list
