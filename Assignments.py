# Assignment_1
for i in range(1,11):
    print(i, " Muhammad Khan")

# Assignment_2
diameter= float(input("Enter the value for diameter of circle: "))
radius = float(diameter)/2
area= 3.14 * radius * radius
print("Area of circle with diameter ", diameter, " is: ", area) 

# Assignment_3
#  take input as celcius  and convert it into kelin and fahrenait

temp= int(input ("Enter temperature In Celsius : "))
fahrenheit=(temp * 9/5) + 32
kelvin= temp + 273.15
print("Temperature in Fahrenheit: ", fahrenheit)
print("Temperature in Kelvin: ", kelvin)

amount= float(input("Enter Total amount  : "))
friends= int(input("Enter number of friends: "))
share= amount / friends
print("Each friend has to pay: ", share)


#Emoji Converter
message= input("Enter your message: ")
if not message:
    print("No message entered.")
elif len(message) > 100:
    print("Message is too long. Please limit to 100 characters.")
else:
    message=message.replace(":)","😊")
    message=message.replace(":(","😞")
    message=message.replace("<3","❤️")
    message= message.replace(":D","😃")
    message= message.replace(";)", "😉")
    print("Converted message: ", message)

# Assignment_4
# #  take a sentence as input and print lowercase, uppercase and replace spaces with underscores
sentence= input("Enter a sentence: ")
lowercase_sentence= sentence.lower()
uppercase_sentence= sentence.upper()
replaced_sentence= sentence.replace(" ","_")
total_characters= len(sentence)
print("Total characters in the sentence: ", total_characters)
print("Lowercase: ", lowercase_sentence)
print("Uppercase: ", uppercase_sentence)
print("Spaces replaced with underscores: ", replaced_sentence)
    
# chapter_4 assignments
#1 :  3 movies as input and store them in a list and print the list 
movies= []
for i in range(3):
    movie= input(str(i) + ": Enter movie name: ")
    movies.append(movie)
print("Movies list: ", movies)
# 2:  print the highest and lowest marks from the given tuple 
marks=(87,62,33,95,76)
print("Highest marks: ", max(marks))
print("Lowest marks: ", min(marks))

# chapter_5 assignments
# 1: Create a dictionary to store meaning of 3 english words and print them
dictionary={
    "aberration":"a departure from what is normal, usual, or expected",
    "convivial":"friendly, lively, and enjoyable",
    "ephemeral":"lasting for a very short time"
}
for word, meaning in dictionary.items():
    print(f"{word}: {meaning}") 

# 2  create a set of numbers and perform Union and Intersection with another set of numbers
set1={1,2,3,4,5}
set2={4,5,6,7,8}
union_set= set1.union(set2)
intersection_set= set1.intersection(set2)
print("Union of set1 and set2: ", union_set)
print("Intersection of set1 and set2: ", intersection_set)

