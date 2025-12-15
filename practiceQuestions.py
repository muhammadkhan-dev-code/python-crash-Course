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
