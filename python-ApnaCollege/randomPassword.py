import random
import string
char_value=string.ascii_letters+ string.digits+string.punctuation
pass_length=int(input("Enter length of your password you want to generate: "))
password=""
for i in range(pass_length):
    password+=random.choice(char_value)
print(f"Your Password is : {password}")

# list comprehension
# result="".join([random.choice(char_value) for i in range(pass_length)])
# print(result)
