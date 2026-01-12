# --------------function And Recursion in Python ------------
# functions : block of statements that perform specific task
# we use functions to reduce the redundency 
# by using function code reuseablity will increase and redundancy decrease

#function definition  ->def fun_name(param1,param2):
def calc_sum(a, b): # parameters  
    return a+b

sum= calc_sum(3,4) # function call along with arguments 
print("Sum of numbers ",sum)

# function does not return anything will be automatically return None 
def print_hello(): # function without parameters
    print("Hello ")

output=print_hello()
print(output) # None

def calc_avg(a,b,c):
    return (a+b+c)/3

avg= calc_avg(10,12,14)
print(f"Average of three numbers 10,12,14 is :{avg}")
def calc_product(a=1,b=1): # default parameters 
    return a*b
print(calc_product(2)) # 2 

# -------------Types of Functions---------- 
# Built-in Function
# 1.print()         2.len()
# 3.type()         4.range()

# User-define Function  we create our own functions

def len_cities(cities):
    return len(cities)

def print_cities(cities):
    for item in cities:
        print(item,end=", ")

cities=["delhi","hyderabad","gurgon","noida","puni","mumbai ","chennai"]
print( "length for cities :",len_cities(cities))
print_cities(cities)

print()

def cal_fact(num):
    fact=1
    if num<=1:
        return 1
    else:
       for i in range(1,num+1):
        fact*=i
    return fact 
num=int(input("Enter any Number : "))

fact=cal_fact(num)
print(f"factorial of number {num}! is {fact} ")

def check_num(num):
    if(num%2==0):
        return f"Given Number is Even  and Number is  {num} "
    else:
        print(f" Given Number is odd {num}")
        
num=int(input("Enter any Number : "))
print(check_num(num))

# Recursion ------ A function calls itself repeatedly

def show (n):
    # base condition

    if(n==0):
        return 
    print(n)
    show(n-1)

show(5)



def fact(n):
    if (n<=1):
        return 1
    return n*fact(n-1)

print(fact(5))

l=["a","b","c","d","e","f"]
def print_list(list,idx):
    if(idx==len(list)):
        return 
    print( list[idx])
    print_list(list,idx+1)

print_list(l,0)




