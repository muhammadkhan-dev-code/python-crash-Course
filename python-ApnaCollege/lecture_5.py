# ------ lecture 5  loops in Python-----------
# used to do the tak in repeat way while loop and for loop

# Break keyword is used to terminate the loop
# Continue Keyword is used to terminate the current iteration

#---------- while loop----------
count=1
while count<=5: # stopping condition

    print("print : ", count)
    count+=1

while count>=1:
    print("Print ", count)
    count-=1

# search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]


nums =(1,4,9,16,25,36,49,64,81,100)
n= int(input("Enter any Number : "))
i=0
while i<len(nums):
    if  nums[i]==n:
        print("Found : ", nums[i])
        break
    else:
        print("Number not found")
    i+=1


i=1
while i<=5:
    if( i==3):
        continue
    print(i)
    i+=1
    

# for loop 
list=[1,2,3,4,5]
for num in list:
    print(num)

veg=["potato","brijal","lady finger"]
for v in veg:
    print(v)
else:
    print("End")

 # Range -> return the no of sequence

for i in range(6):
    print("hello")

for i in range(1,4):
    print(i)

for i in range(1,19,3):
    print(i)

# pass statement is null statement 
for i in range(19):
    pass   # placeholoder for future work

