# File Handling
# two types of files Text files and Binary files
# Text files - .txt, .csv, .py
# Binary files - .jpg, .png, .exe

# open files  using open() function
# modes - 'r' - read, 'w' - write, 'a' - append, 'b' - binary
# 'r+' - read and write, 'wb' - write binary, 'rb' - read binary
# 'a+' - append and read
# Syntax: open(filename, mode)

file = open("file.txt",'r')
# read() - reads entire file
content = file.read()
print(content)
if "Live" in content:
    print("Yes, 'live' is present in the file.")
else:
    print("No, 'live' is not present in the file.")

file.close()

file= open("report.txt",'w')
file.write("My up Comming projects would be \n")
file.write("1. Web Development\n")
file.write("2. Data Science\n") 
file.write("3. Machine Learning\n")
file.close()
print("Data written to file successfully.")

file = open("report.txt",'a')
file.write("4. Artificial Intelligence\n")
file.close()

# file = open("file.txt",'r') will give us error because we have  because file is not found 
# file= open("file.txt",'w') will create a new file if file is not found
#file= open("file.txt",'a') append the text
# file = open("file.txt",'r+') read and write
# file = open("file.txt",'wb') write binary
# file = open("file.txt",'x') create a new file and give error if file already exists

# read file another way

with open('file,txt','r') as file:
    content = file.read()
    print(content)
# no need to close the file when using with statement
# read line by line
with open('file.txt','r') as file:
    for line in file:
        print(line.strip())  # strip() to remove extra newlines

# readline - reads one line at a time
with open('file.txt','r') as file:
    line1 = file.readline()
    print(line1)
    line2 = file.readline()
    print(line2)


# readlines() - reads all lines and returns a list
with open('file.txt','r') as file:
    lines = file.readlines()
    print(lines) 

with open("noes.txt",'w') as file:
    file.write("These are some notes.\n")
    file.write("Remember to review them later.\n")
    file.write("File handling is important in programming.\n")
print("Notes written to noes.txt successfully.")
with open('noes.txt','r') as file:
    list_lines = file.readlines()
    print(len(list_lines)) # output: 3

# copy file
import shutil
shutil.copy('noes.txt','noes_copy.txt')
print("File copied successfully.")

# rename file
import os
os.rename('noes_copy.txt','notes_backup.txt')
print("File renamed successfully.")

# delete file
os.remove('notes_backup.txt')
print("File deleted successfully.")

# check if file exists
if os.path.exists('noes.txt'):
    print("File exists.")
else:
    print("File does not exist.")







