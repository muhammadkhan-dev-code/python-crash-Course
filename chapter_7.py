# functions
# we will perform the tasks repeatedly so we will create functions for that


def greet(name):
    print("Hello, " + name + ". Good morning!")
greet("Muhammad Khan")  # function call
greet("Ali Raza")  # function call

def inspire(name):
    print("Keep going " + name + "! You can do it!")

# function advantages 
# 1: to make the code more readable
# 2: to avoid repetition of code / to avoid redundancy
# 3: to organize code into logical blocks
# 4: to make code reusable  

# function Parameters vs Arguments
# Parameters are the variables defined in the function definition -> def sum(a,b):
# Arguments are the actual values passed to the function when it is called  ->  sum(10,12)  here 10 and 12 are arguments

# parameterized functions
def sum(a,b):
    return a+b

def avg (a,b):
    return (a+b)/2

# pass arguments to functions
print(sum(10,12))
print(avg(10,12))

# function with default parameters
def power(base=4, exponent=2):
    return base ** exponent
print(power(5,3))  # overrides default values
print(power()) # uses default values















