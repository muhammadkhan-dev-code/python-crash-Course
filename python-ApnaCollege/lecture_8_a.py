# ---------Lecture 8 OOP A  Concepts in Python------------
# procedural->functional programming->OOP 

# OOP ---- OBJECTS AND CLASSES 
# CLASS -> BLUEPRINT FOR CREATING OBJECTS

# Constructor ->invoked at object creation time

 
#Creating Class (attributes and methods or functions)


class Student:
# attributes
    college_name="MUET College Jamshoro"

# constructor      # self -> reference to current class  for object
    def __init__(self,full_name,marks):
        # print("Adding new Student")
        self.name=full_name 
        self.marks=marks
# methods
    @staticmethod # decorator  
    def say_hello():
        print("Hello")
    
    def get_name(self):
        return self.name
    

    def get_avg(self):
        sum=0
        for val in (self.marks):
            sum+=val
        return float(sum/3)
    def get_marks(self):
        for value in self.marks:
            print(f" {value}", end=" " )
    def display_info(self):
        print(f"Student's Name :{self.name} ")
        print(f" Marks :", end="")
        self.get_marks()
        print(f"Avg Of {self.name} is : {self.get_avg()}")

# creating a instance for class  
# constructor invoked automatically  while creating the obj for class
std1= Student("Muhammad Ali",[70,80,85])
std1.display_info()



# print(f"Student Name: {std1.name} and Marks : {std1.marks} in {std1.college_name}")
# print(f"{std1.say_hello()} and Marks:{std1.get_marks()}")
# std2= Student("Akram Ali",96)
# print(f"Student Name: {std2.name} and Marks : {std2.marks} in {std2.college_name}")


# class Attribute
class Person:
    name="xyz"
    @classmethod
    def change_name(cls,name):
        cls.name=name

p1=Person()
p1.change_name("Muhammad")
print(p1.name) # Muhammad
print(Person.name) # Muhammad 


#Property Decorator
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return str((self.chem+self.phy+self.math)/3)+"%"
    
s= Student(90,90,89)
print(s.percentage)
s.chem=76
print(s.percentage)



    
    





