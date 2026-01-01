#1  input two Numbers from user and print their sum
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print("Sum of ",num1," and ",num2," is ",sum)
#2  input the side of square from user and print its area
side=float(input("Enter the side of square: "))
area=side*side
print("Area of square with side ",side," is ",area)
#3 input two numbers from user and print their avg
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
avg=(num1+num2)/2
print("Average of ",num1," and ",num2," is ",avg)
# 4 input two numbers as int and swap them
num1=int(input("Enter first number: "))# 3
num2=int(input("Enter second number: "))# 4
swap=num1
num1=num2
num2=swap
print("After swapping, first number is ",num1," and second number is ",num2)
# 4 input two number if num1>num2 print true else false

num1=int(input("Enter first number: "))# 3
num2=int(input("Enter second number: "))# 4
print("True" if num1>num2 else "False")

# input marks in between 0-100 and print grade
marks=int(input("Enter marks between 0-100: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
elif marks>=60 and marks<70:
    print("Grade D")    
else:
    print("You are Fail")

# input year and check if it is leap year or not
year=int(input("Enter year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")

# input a number and check if it is even or odd
num=int(input("Enter a number: "))
if num%2==0:
    print(num," is even")
else:
    print(num," is odd")
# input a number and check that a num is largest
num1=int(input("Enter a 1st number: "))
num2=int(input("Enter a 2nd number: "))
num3=int(input("Enter a 3rd number: "))
num4=int(input("Enter a number: "))

if num1>=num2 and num1>=num3 and num1>=num4:
    print(num1," is the largest number")

elif num2>=num1 and num2>=num3 and num2>=num4  :
    print(num2," is the largest number")    
elif num3>=num1 and num3>=num2 and num3>=num4:
    print(num3," is the largest number")
else:
    print(num4," is the largest number")

# input a number check it is multiple of 7 or not

num=int(input("Enter a number: "))
print("Mutliple of 7" if num%7==0 else "Not multiple of 7")

# List:
# Enter the name of three moives and stroe in list
movies=[]
for i in range(3):
    movie=input("Enter the name of movie {}: ".format(i+1))
    movies.append(movie)

print("Movies List:", movies) # Output: ['Movie1', 'Movie2', 'Movie3']

# check the list that contain the pailndrome or not 
list1=[1,2,3,2,1]
list2= list1.copy()

list2.reverse()
if list1==list2:
    print("The list is palindrome original list:",list1 ," Reversed list:",list2)
else:
    print("The list is not palindrome", list1 ," Reversed list:",list2)

grade=("C","D","A","A","A","B","A","C","D","B")
print("Original Grades Tuple:", grade)
print("count of Grade A", grade.count("A")) # Output: 4
print("Index of first occurrence of Grade B:", grade.index("B")) # Output: 5

grade=["C","D","A","A","A","B","A","C","D","B"]
grade.sort()
print("Sorted Grades List:", grade)

# Dict and Sets 

word_meaning={
    "table":[
        "a piece of furniture",
        "list of facts and figures"
        ],
    "cat":"A small element"
}
print(word_meaning)

subjects_list={
    "Python","Java","C++","JavaScript","Java","Python"," Java","C","Python"," Java","C"
}

# print(len(set(subjects_list)))
marks={}
mark1=int(input("Enter Marks : "))
mark2=int(input("Enter 2nd marks : "))
mark3=int(input("Enter 3rd marks : "))
marks.update({"physics":mark1})
marks.update({"maths":mark2})
marks.update({"chem":mark3})

# store 9 , 9.0 in sets
value={("float",9.0),("int",9)}

#------------ lOOPS Assignment----------

count=1
while count<=100:
    print(count, ",")
    count+=1

num= int(input("Enter any Number : "))
print(f"Multiplication Table  of {num}")
a=1
while a<=10:
    print(f" {a} * {num}= {a*num}")
    a+=1

# print [1,4,9,16,25,36,49,64,81,100]

nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1


# search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]
nums =(1,4,9,16,25,36,49,64,81,100)
n= int(input("Enter any Number : "))

i=0
while i<len(nums):
    if  nums[i]==n:
        print("Found : ", nums[i])
        break
    else:
        print("Number not found")
    i+=1

# [1,4,9,16,25,36,49,64,81,100] using for 

nums=[1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)

tup=(1,4,9,16,25,36,49,64,81,100)
x=49
idx=0
for el in tup:
    if (el == x):
        print(" Found Number at index ",idx)
        break
    idx+=1 # track the index of do 

# for i in range(1,101):
#     print(i)

# for i in range(101,0,-1):
#     print(i)

num= int(input("Enter any number : "))
sum=0

i=1
while i<=num:
    sum=+i

print(sum)
# factorial 
fact=1
num= int(input("Enter any number : "))
for i in range(1,num+1):
    fact*=i










