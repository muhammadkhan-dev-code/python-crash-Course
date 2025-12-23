# -----------Lecture 3---- Lists and Tuples in Python -----------

# Lists are mutable sequences, typically used to store collections of homogeneous items.
# mixed list 
mixed_list = [90, "A+", 78.5, True]
print("Mixed List:", mixed_list)
print("Type of mixed_list:", type(mixed_list)) # Output : <class 'list'>

marks=[90, 85, 78, 92, 88] # Creating a list of marks same as Array in other languages
print("Original Marks List:", marks)
print("Type of marks:", type(marks)) # Output: <class 'list'>

# Accessing elements
print("First mark:", marks[0])  # Output: 90
print("Last mark:", marks[-1])   # Output: 88
print("Marks from index 1 to 3:", marks[1:4])  # Output: [85, 78, 92]

# Modifying elements   
marks[2] = 80
print("Modified Marks List:", marks)  # Output: [90, 85, 80, 92, 88] 

# List methods
marks.append(95)  # Adding an element at the end
print("After appending 95:", marks)  # Output: [90, 85, 80, 92, 88, 95]
marks.remove(85)  # Removing an element
print("After removing 85:", marks)  # Output: [90, 80, 92, 88, 95]
sorted_list = sorted(marks)      # Sorting the  origional list 
print("Sorted Marks List:", sorted_list)  # Output: [80, 88, 90, 92, 95] 
marks.reverse()   # Reversing the list
print("Reversed Marks List:", marks)  # Output: [95, 92, 90, 88, 80] 
marks.sort(reverse=True)      # Sorting the original list in place in descending order

print("Length of Marks List:", len(marks))  # Output: 5
# insert (index, value) 
marks.insert(2, 89)  # Inserting 89 at index 2
print("After inserting 89 at index 2:", marks)  # Output: [95, 92, 89, 90, 88, 80]

# pop(index) if (index) is not defined then it remove the last element
popped_mark = marks.pop()  # Removing and returning the last element
print("Popped Mark:", popped_mark)  # Output: 80

# Tuple: 
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.

# Creating a tuple
student_info = ("John Doe", 21, "A+")
print("Student Info Tuple:", student_info)
print("Type of student_info:", type(student_info))  # Output: <class 'tuple'>

marks=(90, 85, 78, 92, 88)  # Creating a tuple of marks
print("Marks Tuple:", marks)
print("Type of marks:", type(marks))  # Output: <class 'tuple'

single_element_tuple = (95,)  # Tuple with a single element
print("Single Element Tuple:", single_element_tuple)

# Accessing elements
print("First mark in tuple:", marks[0])  # Output: 90
print("Marks from index 1 to 3 in tuple:", marks[1:4])  # Output: (85, 78, 92)
# Tuples are immutable, so we cannot modify them
# marks[2] = 80  # This will raise a TypeError 

# marks=(90, 85, 78, 92, 88) 
# Tuple methods
print(marks.index(92))  # Output: 3
print(marks.count(85))  # Output: 1
print("Length of Marks Tuple:", len(marks))  # Output: 5



