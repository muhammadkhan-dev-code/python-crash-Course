
# ---------Lecture 1  Variables and Data Types ------------
print("Python Course With Apna College")
print("Hello World!") # first program in python 
print("My name is muhammad Khan ","Age is 21")

# Variables in Python
name="Muhammad Khan" # values can be changed  = is the assignment operator
age=21 # integer value age is equal to 21 
print("My name is ",name," Age is ",age)
age2=age
print("My age is ",age2)
# Rules for defining variables in python
# 1. variable name can contain alphabets, digits and underscore(_)
# 2. variable name can not start with a digit
# 3. variable name can not contain special characters like !,@,#,$,%,^
# 4. variable name can not be a keyword (reserved word) in python
# 5. variable name should be meaningful
# 6. variable names are case sensitive

# Examples of valid variable names
my_name="Muhammad Khan"
age_1=21
# Examples of invalid variable names
# 1name="Muhammad Khan" # starts with digit
# my-name="Muhammad Khan" # contains special character -
# for="Muhammad Khan" # keyword
print("My name is ",my_name," Age is ",age_1)

# Data Types in Python
# 1. int (integer)
# 2. float (floating point number)
# 3. str (string)
# 4. bool (boolean)
# 5. list
# 6. tuple
# 7. dict (dictionary)
# 8. set

# Examples of data types

num1=10 # int
num2=10.5 # float

name="Muhammad Khan" # str
is_student=True # bool
marks=[90,85,88] # list
coordinates=(10.0,20.0) # tuple
student={"name":"Muhammad Khan","age":21} # dict
unique_numbers={1,2,3,4,5} # set

# Checking data types
print("Data type of num1 is ",type(num1))
print("Data type of num2 is ",type(num2))
print("Data type of name is ",type(name))
print("Data type of is_student is ",type(is_student))
print("Data type of marks is ",type(marks))
print("Data type of coordinates is ",type(coordinates))
print("Data type of student is ",type(student))
print("Data type of unique_numbers is ",type(unique_numbers))

# print sum of two numbers
a=5
b=10
sum=a+b
print("Sum of ",a," And ",b," is ",sum)
# print product of two numbers
product=a*b
print("Product of ",a," and ",b," is ",product)
# print difference of two numbers
difference=b-a
print("Difference of ",b," and ",a," is ",difference)
# print division of two numbers
division=b/a
print("Division of ",b," and ",a," is ",division)
# print floor division of two numbers
floor_division=b//a
print("Floor Division of ",b," and ",a," is ",floor_division)
# print modulus of two numbers
modulus=b%a
print("Modulus of ",b," and ",a," is ",modulus)


# Expression Execution
#1 String and Numeric Values can operate togather with *
A,B=2,3
Txt="@"
print(Txt*(A+B)) # prints @@@@@
#2 String and String Values can operate togather with +
A,B="2",3
print((A+Txt)*B) # prints 2@2@2@  Concatenation of string and integer is not allowed
#3 Numeric values can operate togather with +,-,*,/,//,%
A,B=5,2
print("Addition:",A+B) # prints 7
print("Subtraction:",A-B) # prints 3
print("Multiplication:",A*B) # prints 10
print("Division:",A/B) # prints 2.5
print("Floor Division:",A//B) # prints 2
print("Modulus:",A%B) # prints 1
#4 Arithmetic expression with integer and float will result in float
A,B=5,2.0
print("Addition:",A+B) # prints 7.0
print("Subtraction:",A-B) # prints 3.0
print("Multiplication:",A*B) # prints 10.0
#5 result of division operator with two integers wil be float
print("Division:",A/B) # prints 2.5
print("Floor Division:",A//B) # prints 2.0
#6 Integer division with  float will result in float
A,B=5.0,2
print("Floor Division:",A//B) # prints 2.0
#7 Modulus operator with float will result in float
print("Modulus:",A%B) # prints 1.0

# A//B is same as floor(A/B)
# remainder is -ve when denominator is -ve
A,B=5,-2
print("Floor Division:",A//B) # prints -3.0
print("Modulus:",A%B) # prints -1.0

# is used for single line comment 
# multi line comment can be done using triple quotes
"""
multi line comment 
"""


# input in python 
name=input("Enter your name: ")
age=input("Enter your age: ")
print("My name is ",name," Age is ",age)
# input function always returns string value
# to take integer input we need to typecast it
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print("Sum of ",num1," and ",num2," is ",sum)
# to take float input we need to typecast it
# typecasting in python
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean
# operator preceduence  not > and > or

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
sum=num1+num2
print("Sum of ",num1," and ",num2," is ",sum)

# operators in Python

# Arithmetic operators: +, -, *, /, //, %, **
num1=10
num2=3
print("Addition:",num1+num2)
print("Subtraction:",num1-num2)
print("Multiplication:",num1*num2)
print("Division:",num1/num2)
print("Floor Division:",num1//num2)
print("Modulus:",num1%num2)
print("Exponentiation:",num1**num2)

# Comparison operators: ==, !=, >, <, >=, <=
print("Equal to:",num1==num2)
print("Not equal to:",num1!=num2)
print("Greater than:",num1>num2)
print("Less than:",num1<num2)
print("Greater than or equal to:",num1>=num2)
print("Less than or equal to:",num1<=num2)  

# Logical operators: and, or, not
a=True
b=False 
print("Logical AND:",a and b)
print("Logical OR:",a or b)
print("Logical NOT:",not a)


# Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
x=5
print("Initial value of x:",x)
x+=2
print("After x+=2:",x)
x-=3
print("After x-=3:",x)
x*=4
print("After x*=4:",x)
x/=2
print("After x/=2:",x)
x//=3
print("After x//=3:",x) # output will be float if x is float
x%=2
print("After x%=2:",x)
x**=3
print("After x**=3:",x)


# Identity operators: is, is not
y=x
print("x is y:",x is y)
print("x is not y:",x is not y)
z=10
print("x is z:",x is z)
print("x is not z:",x is not z)

# Membership operators: in, not in
fruits=["apple","banana","cherry"]
print("apple in fruits:", "apple" in fruits)
print("grape in fruits:", "grape" in fruits)
print("banana not in fruits:", "banana" not in fruits)
print("grape not in fruits:", "grape" not in fruits)


# conditional statements in python
# if, elif, else
# indentation is very important in python
# example 1
num=int(input("Enter a number: "))
if num>0:
    print(num," is positive")
elif num<0:
    print(num," is negative")
else:
    print(num," is zero")

# traffic light 
light=input("Enter traffic light color (red/yellow/green): ")
if light=="red":
    print("Stop")
elif light=="yellow":
    print("Get Ready")
elif light=="green":
    print("Go")
else:
    print("Invalid color")

# Ternary Operator in Python

# syntax: value_if_true if condition else value_if_false
age=int(input("Enter your age: "))
status="Adult" if age>=18 else "Minor"
print("You are an ",status)
# check even or odd
num=int(input("Enter a number: "))
even= "Even " if num%2==0 else "Odd"
print(num," is ",even)

food= input("Enter food name: ")
print("Sweet") if food=="Gulab Jamun" else print("Salty")
# check positive, negative or zero using nested ternary operator
num=int(input("Enter a number: "))
result= "Positive" if num>0 else "Negative" if num<0 else "Zero"
print(num," is ",result)

# Clever if /Ternary trick
age=int(input("Enter your age: "))
vote=("yes","no")[age<18]
print("Can you vote? ",vote)


# Type Conversion in Python
# Implicit Type Conversion
# when we mix int and float in an expression, python converts int to float  
a,b=2,2.5
sum=a+b
print("Sum of ",a," and ",b," is ",sum) # int -> float

# Explicit Type Conversion
# we can convert one data type to another using type casting functions  
# int(), float(), str(), bool()   used for type casting
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print("Sum of ",num1," and ",num2," is ",sum ,"Type of sum is ",type(sum))
# converting float to int
# this will truncate the decimal part
num3=float(input("Enter a float number: "))
num4=int(num3)
print("Float number: ",num3," after converting to int: ",num4)

# input from user input() function will be used to take input from user
# input() function always returns string value
num5=int(input("Enter an integer number: "))
print("Integer number: ",num5," Type: ",type(num5))

name= input("Enter your name: ")
age= int(input("Enter your age: "))
marks= float(input("Enter your marks: "))
print(" Student's Name: ",name)
print(" Student's Age: ",age)
print(" Student's Marks: ",marks)















