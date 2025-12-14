# ----------------data types in python---------------
# integer
a = 10
print(type(a))  # Output: <class 'int'>
# float
b = 10.5
print(type(b))  # Output: <class 'float'>
# string
c = "Hello, World!"
print(type(c))  # Output: <class 'str'>
# boolean
d = True
print(type(d))  # Output: <class 'bool'>
# list
e = [1, 2, 3, 4, 5]
print(type(e))  # Output: <class 'list'>
# tuple
f = (1, 2, 3, 4, 5)
print(type(f))  # Output: <class 'tuple'>
# dictionary
g = {"name": "Alice", "age": 25}
print(type(g))  # Output: <class 'dict'>
# set
h = {1, 2, 3, 4, 5}
print(type(h))  # Output: <class 'set'>
# NoneType
i = None
print(type(i))  # Output: <class 'NoneType'>   
  
# -----------------keywords in python -------------------
#reserved words that have special meaning in Python and cannot be used as identifiers (variable names, function names, etc.)
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not

#  syntax is the set of rules that defines the combinations of symbols that
#  are considered to be correctly structured programs in that language.
#  semantics is the meaning of those syntactical elements and structures.

#  type conversion in python two  types
# implicit conversion
j= 5 # integer
k=2.5 # float
result= j+k     #  7.5 implicit conversion to float  int -> float

# explicit conversion
l= "100"  # string
m=int(l) # explicit conversion str -> int
print(m+ 5) # 105 

# -----------------Operators in python-------------------
# arithmetic  +-*/%  ** 
# Comparision == => =< != < >
# logical and or not 
# assignment = += -= *= /= %= 
# bitwise & | ^ ~ << >>
# assignment operators 
