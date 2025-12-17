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

# modifie item in list
fruits[1]= "kiwi" # change banana to kiwi
print("Fruits list after modification: ", fruits)
print("Length of fruits list is: ", len(fruits)) # length of list after modification

markss= [85, 90, 78, 92, 88]
total= sum(markss) # sum of all marks
average= total/len(markss) # average marks
print("Total marks: ", total)
print("Average marks: ", average)
#modify marks
markss[2]= 80 # change 78 to 80
print("Marks list after modification: ",markss)

# slicing in list 
numbers= [10, 20, 30, 40, 50, 60, 70, 80, 90]
# slice from index 2 to 5
sliced_numbers= numbers[2:6] # 30,40,50,60
print("Sliced numbers from index 2 to 5: ", sliced_numbers)
# slice from start to index 4
sliced_numbers_start= numbers[:5] # 10,20,30,40,
print("Sliced numbers from start to index 4: ", sliced_numbers_start)
# slice from index 5 to end
sliced_numbers_end= numbers[5:] # 60,70,80,90
print("Sliced numbers from index 5 to end: ", sliced_numbers_end)
# slice with step
sliced_numbers_step= numbers[::2] # 10,30,50,70,90
print("Sliced numbers with step 2: ", sliced_numbers_step)

# max and min in list
max_number= max(numbers)
min_number= min(numbers)
print("Maximum number in the list: ", max_number)
print("Minimum number in the list: ", min_number)

# reverse list 
print("Reversed list: ", numbers.reverse())
# sort list
print("Sorted list: ", numbers.sort())
numbers.append(100)
print("List after appending 100: ", numbers)
#  pop method will remove last item from the list
last_item= numbers.pop()
print("Last item removed using pop: ", last_item)
print("List after popping last item: ", numbers)
# insert with index
numbers.insert(len(numbers), 100) # insert 100 at  last index 
print("List after inserting 100 at last index: ", numbers)

# tuple in python
# immutable list () is used for tuple to store multiple data 
colors= ("red", "green", "blue", "yellow")
print("Colors tuple: ", colors)
print("First color: ", colors[0]) # first item
print("Length of colors tuple: ", len(colors)) # length of tuple
# tuple unpacking
color1, color2, color3, color4= colors
print("Unpacked colors: ", color1, color2, color3, color4)
# slicing in tuple
sliced_colors= colors[1:3] # green, blue
print("Sliced colors from index 1 to 2: ", sliced_colors)
# max and min in tuple
numbers_tuple= (10, 20, 5, 30, 15)
max_number_tuple= max(numbers_tuple)
min_number_tuple= min(numbers_tuple)
print("Maximum number in the tuple: ", max_number_tuple)
print("Minimum number in the tuple: ", min_number_tuple)
# count method in tuple
count_red= colors.count("red")
print("Count of 'red' in colors tuple: ", count_red)
# find index in tuple
index_blue= colors.index("blue")

# empty tuple
empty_tuple= ()

#single element tuple
single_element_tuple= (10,)



