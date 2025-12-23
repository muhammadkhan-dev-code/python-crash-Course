# ---------Lecture 2 ------------

# Python Strings

str1="Hello"
str2='World'
print(str1+" "+str2)

# \n is used for new line and \t is used for tab space
str3="Hello\nWorld \t Python"
print(str3)

# Operations on strings

# 1 Concatenation + operator
str1="Apna"
str2='College'
print(str1+" "+str2)

#2 length of string empty space also counts 
print("Length of str1:",len(str1))

#3 indexing and slicing of strings

# indexing starts from 0 help to access individual characters in a string   
str1="Apna College"
print("First character of str1:",str1[0]) # A string[index]
print("Last character of str1:",str1[-1]) # e
# String can not be changed as they are immutable
# str1[0]="a" # This will give error

# Slicing   Access the parts of strings
# String[start :end ]  end index is not included
str1="Apna College"
print("Slicing str1 from index 0 to 3:",str1[0:4]) # Apna
print("Slicing str1 from index 5 to 11:",str1[5:12]) # College
print("Slicing str1 from index 0 to end:",str1[0:]) # Apna College
print("Slicing str1 from start to index 4:",str1[:5]) # Apna
print("Slicing str1 with step 2:",str1[::2]) # An olge

# negative indexing and slicing
str="Apple"
print("Last character using negative indexing:",str[-1]) # e
print("Slicing using negative indexing:",str[-4:-1]) # ppl
print(str[-1:-4]) # empty string because we are moving from right to left

# Strings Functions/Methods
str1="  ApnaCollege  "

# 1. lower() - converts string to lowercase
print("Lowercase:",str1.lower()) # apna college

# 2. upper() - converts string to uppercase
print("Uppercase:",str1.upper()) # APNA COLLEGE

# 3. endsWith() - checks if string ends with given substring
print("Ends with 'ge':",str1.strip().endswith("ge")) # True

# 4. startsWith() - checks if string starts with given substring
print("Starts with 'Apna':",str1.strip().startswith("Apna")) # True

# 5. strip() - removes leading and trailing whitespace
print("Stripped string:",str1.strip()) # "Apna College" 

# 6. capitalize() - capitalizes first character of string
# create a new String with leading spaces to demonstrate capitalize but origional string remains same
print("Capitalized string:",str1.strip().capitalize()) # Apna college
# 7. replace() - replaces a substring with another substring
print("Replace 'College' with 'Institute':",str1.strip().replace("College","Institute")) # Apna Institute
print("Original string after replace:",str1) # original string Apna College will remains same

# 8 find() - finds the index of first occurrence of a substring
print("Index of 'College':",str1.strip().find("College")) # 5

# 9 count() - counts occurrences of a substring
print("Count of 'a':",str1.strip().lower().count("a")) # 2

str= " Hi, i am $ a student at Apna College!   and $ I love programming. $100"
print(str.count("$"))  # 3
 

# Conditional Statements and Nesting 
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1>num2:
    print(num1," is greater than ",num2)
elif num1<num2:
    print(num2," is greater than ",num1)
else:
    print("Both numbers are equal")

# Nesting 
age=34
if age>=18:
    print("You are eligible to drive")
    if age>=60:
        print("You are  not  eligible to drive and Your age is ",age)
    else:
        print("You are eligible to drive")
else:
    print("You are not eligible to vote")    




