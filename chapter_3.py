# Strings basics
#  strings are immutable sequences of characters used to store text data.
str1="Hello, World!"
str2='Python Programming'
str3='''This is a multi-line
string example.'''
print(str1)
print(str2)
print(str3)

# String Concatenation
greeting = "Hello"
name = "Muhammad Khan"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# length of a string
length = len(full_greeting) # 
print("Length of full_greeting:", length) # length of full_greeting: 21

# indexing  each character in a string has a unique index starting from 0
str4="HelloWorld"
str5="Python's Fun"

print(str4[0])  # H
print(str4[4])  # o
print(str4[-1]) # d
print(str4[-3]) # r
# slicing a substring can be extracted using slicing end index will be excluded
substring1 = str4[0:5]  # Hello
substring2 = str4[5:]   # World last index will be length - 1
substring3 = str4[:5]   # Hello
print(substring1)
print(substring2)
print(substring3)
#  Negative Index Slicing
substring4 = str4[-5:]  # World
substring5 = str4[:-5]  # Hello

# String Methods
str6="Muhammad Khan"
print(str6.lower())      # muhammad khan
print(str6.upper())      # MUHAMMAD KHAN
print(str6.replace("Khan", "Ali"))  # Muhammad Ali
print(str6)             # original string remains unchanged: Muhammad Khan
print(str6.split(" "))   # ['Muhammad', 'Khan']
print(str6.find("Khan")) # 9 index of first occurrence 
print(str6.count("a"))   # 4  how many times 'a' appears
print(str6.title())   # Muhammad Khan first later of each string will be capitalized
print(str6.strip())   # removes leading and trailing whitespace

# f-Strings (formatted string literals) 
age = 21
height = 5.9
name="Muhammad Khan"
info = f"My name is {name}, I am {age} years old and my height is {height} feet."
print(info)

# Escape Characters
str7="He said, \"Hello!\"\nWelcome to Python programming.\tEnjoy coding"
print(str7)
