# Loops
# This chapter covers the basics of loops in Python, including for loops and while loops.
name="Muhammad Khan"
num=1
while num<=10:
    print( f" {num}: name {name}")
    num += 1 
# This code will print the name "Muhammad Khan" 100 times using a while loop.
print("\nUsing for loop:")
for i in range(1, 11):
    print(f"{i}: name {name}")

# using while Loop 
print("\nUsing while loop:")
n=1

while n<=5:
    print("*" * n)
    n += 1

food_list= ['Pizza', 'Burger', 'Pasta', 'Sushi', 'Tacos']
print("\nFood List:")
for food in food_list:
    print(food)

# tuple
college_list=('Engineering', 'Medical', 'Business', 'Arts', 'Law')
print("\nCollege List:")
for college in college_list:
    print(college)
    
# multiplication table of a number using function and for loop
def multiplication_table(number):
     for i in range(1,11):
         print(f"{number} * {i} = {number*i}")

num= int(input("Enter a number to print its multiplication table: ")) # 3
multiplication_table(num)

for i in range(2,21,2):
    print("Even number: ", i)


for i in range(1,21,2):
    print("Odd number: ", i)

# break and continue
print("Using break statement:")
for i in range(1,11):
    if i==6:
        break
    print("Number: ", i)
    # out put  1 2 3 4 5 

print("Using continue statement:")
for i in range(1,11):
    if i==6:
        continue
    print("Number: ", i)    
    # output 1 2 3 4 5 7 8 9 1

import time 
def countDown(n):
    while n>=1:
        print("Countdown: ", n)
        time.sleep(1)
        n -= 1
    print("Happy New Year!")
    