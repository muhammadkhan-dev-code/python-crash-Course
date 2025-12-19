# take age as input and print age and their type
age= int(input("Enter your age: "))
print("Your age is: ", age)
print("Type of age variable is: ", type(age)) 

# take num  as input convert it into float
num= float(input("Enter a number: ")) # converted string into float
print("Your number is: ", num)
print("Type of num variable is: ", type(num)) # float data type

#  take input as string and print first character, last character and length of string
text= input("Enter a string: ")
print("First character: ", text[0]) # first character
print("Last character: ", text[-1]) # last character
print("Length of string: ", len(text)) # length of string

# take color as variable and print middle 3 characters and last 2 char

color= input("Enter a color: ")
middle_index= len(color)//2 # find middle index just we can get whole number not decimal
middle_characters= color[middle_index-1:middle_index+2]
last_two_characters= color[-2:]
print("Middle 3 characters: ", middle_characters)
print("Last 2 characters: ", last_two_characters)

#  take a sentence as input and print lowercase, uppercase and replace spaces with underscores
sentence= input("Enter a sentence: ")
lowercase_sentence= sentence.lower()
uppercase_sentence= sentence.upper()
replaced_sentence= sentence.replace(" ","_")
print("Lowercase: ", lowercase_sentence)
print("Uppercase: ", uppercase_sentence)
print("Spaces replaced with underscores: ", replaced_sentence)

# take input num and positive if num is greater than 0 else negative or zero
num= int(input("Enter a number: "))
if num>0:
    print("Positive number", num)
elif num<0:
    print("Negative number", num)
else:
    print("Zero")

# take input as take 3  foods name in a list and print list and length of list
foods= []
for i in range(3):
    food= input(str(i) + ": Enter food name: ")
    foods.append(food)
print("Foods list: ", foods)
print("Length of foods list: ", len(foods)) 

# dictionaries
marks={}
for i in range(3):
    subject= input(str(i) + ": Enter subject name: ")
    mark= int(input("Enter marks for " + subject + ": "))
    marks[subject]= mark
print("Marks dictionary: ", marks)

# list of programming language and convert it into sets and print unique languages 
programming_langugages= ['Python', 'Java', 'C++', 'JavaScript', 'Python', 'Java','C']
print(type(programming_langugages))
programming_set= set(programming_langugages)
print("Unique programming languages: ", programming_set)
print("Type of programming_set variable is: ", type(programming_set))

# loops
num=1
while num<=10:
    print("Number: ", num)
    num += 1
even=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)

print("Even numbers from 1 to 50: ", even)

#  sum of natural Numbers up to n 
def sum_of_natural_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum += i
    return sum
n= int(input("Enter a number to find sum of natural numbers up to n: ")) # 5 
result= sum_of_natural_numbers(n) # 1+2+3+4+5=15
print("Sum of natural numbers up to", n, "is:", result)

# funtions question

def show_age(name,age):
   print(f"Hello, my name is {name} and I am {age} years old.")
show_age("Alice", 30)
show_age("Bob", 25)

def vowel_constants(str):
    vowels= "aeiou"
    count_vowel=0
    count_constant=0
    for char in str.lower():
        if char.isalpha():
            if char in vowels:
                count_vowel += 1
            else:
                count_constant += 1
    return (count_vowel, count_constant)
vowels, constants= vowel_constants("Hello World")
print("Vowels:", vowels)
print("Constants:", constants) 

# local and global variables
# gloabl variable can also  be accessed inside function but local variable cannot be accessed outside function
x= "global x"
def my_function():
    y= "local y"
    print(x)  # accessing global variable
    print(y)  # accessing local variable

