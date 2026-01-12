# --------------File Input and Output in Python ------------
# python can be used to perform operations on file  Read and Write
import os

# Types of Files
# 1 Text files .txt,docx,.log
# 2 Binary files .mp4 .mov .png .jpeg


# file Options
# 'r' for reading
# 'w' for Writing in file truncating the file first
# 'x' for  creating a new file and open it for writing
# 'a' for writing appending to the end of file if it exist
# 't' text mode
# 'b' binary mode
# '+' open a disk  file for updating

# Open a file   open("filename","mode") 
file= open("demo.txt",'r')
data= file.read(5) # 5 no of character
readline=file.readline() # read the one line

print("read the entire file along with characters ")
print(data)
print("Read the file line by line one line at a time")
print(readline)

file.close()

file= open("demo.txt",'r')
readlines=file.readlines()
print("Read all the lines from file")
print(readlines)

# writing to file if file does not exist then file automatically will be created 
f= open('demo.txt','w') 
data=f.write("i am Muhammad Khan")
# print(data)
f.close()

# Append data  file does not exist then created automatically

f2=open('muhammad.txt','a')
f2.write("End of program")
f2.close()

sample= open('sample.txt','r+')
sample.write('abc')
print(sample.read())
sample.close()


# ---- open file with syntax
with open("with_file.txt",'w') as file:
    data= file.write("by using the with syntax the file data ill be stored")
    # print(data)
os.remove("with_file.txt")

def even_nums(filename):
    count=0
    with open(filename,mode='r') as f:
        data=f.read()
        print(data)
        # print(int(data.split(",")))
        nums=data.split(",")
        print(nums)
        for val in nums:
            if(int(val)%2==0):
                count+=1
                # print(val)
    print(count)            




even_nums("practice.txt")












