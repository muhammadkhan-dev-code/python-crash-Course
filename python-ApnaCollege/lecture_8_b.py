# # # ---------Lecture 8 OOP B Concepts in Python------------
# # #1 ---- ABSTRACTION ------------
# # # HIDING THE IMPLEMENTATION DETAILS OF CLASS SHOW ONLY IMPORTANT FEATURES  show only necessary details
# class Car:
#     def __init__(self,):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def started(self):
#            self.clutch=True
#            self.acc=True
#            print("Car started ...")


# car1=Car()
# # del keyword is used to delete the object 
# # del car1
# # print(car1)

# #2 ----ENCAPSULATION ----------
# # Wrapping data and functions into a single unit 
# class Account:
#     def __init__(self,acc_holder,acc_no,balance=0):
#         self.acc_holder=acc_holder
#         self.acc_no=acc_no
#         self.balance=balance
    
#     def debit(self,amount):
#          self.balance-=amount
#          print(f"An Amount of {amount} credited from Your Account ")
#          print(f"total Balance : {self.total_balance()}")
#     def credit(self,amount):
#          self.balance+=amount
#          print(f"An Amount of {amount} Credited in you Account ")
#          print(f"total Balance : {self.total_balance()}")

#     def total_balance(self):
#          return self.balance
#     def display_info(self):
#          print(f"Account Holder Name: {self.acc_holder} ")
#          print(f"Account number: {self.acc_no} ")
#          print(f"Total Amount: {self.balance} ")
        

# cus_1=Account("Muhammad Khan",1234567,450)
# cus_1.credit(450)
# cus_1.debit(200)
# cus_1.display_info()

# class BankAccount:
#      def __init__(self,acc_no,acc_pass):
#           self.__acc_no=acc_no
#           self.__acc_pass=acc_pass

#      def getAccount_Number(self):
#           return self.__acc_no
#      def getAccount_pass(self):
#           return self.__acc_pass

     
# bankAcc1=BankAccount("12345","abcde")
# print(bankAcc1.getAccount_pass())

# #3 -----INHERITANCE -------------
# class Car:
#      color="black"
#      @staticmethod
#      def start():
#           print("Car started..")
#      @staticmethod
#      def stopped():
#           print("Car Stopped..")

# class ToyotaCar(Car):
#      def __init__(self,name,model):
#           self.name=name
#           self.model=model
# fortuner=ToyotaCar("FORTUNER","2026")
# alto=ToyotaCar("Alto","1990")

# fortuner.start()
# # fortuner.color

# # ------TYPES OF INHERITANCE

# # i single inheritance single parent -> signle child

# class Car:
#      color="black"
#      @staticmethod
#      def start():
#           print("Car started..")
#      @staticmethod
#      def stopped():
#           print("Car Stopped..")

# class ToyotaCar(Car):
#      def __init__(self,name,model):
#           self.name=name
#           self.model=model
# fortuner=ToyotaCar("FORTUNER","2026")
# alto=ToyotaCar("Alto","1990")

# fortuner.start()

# # # ii  Multilevel Inheritance

# class Car:
     
#      def __init__(self,color):
#           self.color=color
#      @staticmethod
#      def start():
#           print("Car started..")
#      @staticmethod
#      def stopped():
#           print("Car Stopped..")


# class ToyotaCar(Car):
#      def __init__(self,brand,model,color):
#           self.brand=brand
#           self.model=model
#           super().__init__(color)
#           super().start()

# # c=ToyotaCar("FORTUNER","2026","White")

# class Fortuner(ToyotaCar):
#      def __init__(self,type):
#           self.type=type

# fortuner=Fortuner("diesel")
# fortuner.start()

# # iii Multiple Inheritance
# class A:
#      varA="Welcome to class A"
# class B:
#      varB="Welcome To class B"
# class C(A,B):
#      varC="Welcome To class C"

# c= C()
# print(c.varC)
# print(c.varB)
# print(c.varA)

# # 4 ---------- POLYMORIPHISM 
# # OPERATOR OVERLOADING  implicit overloading
# print(1+2)#3
# print("muhammad"+"khan")# concatination
# print([1,2]+[3,4]) # merge

# # complex number a+3b

class Complex:
     def __init__(self,real,img):
          self.real=real
          self.img=img
     def show_num(self):
          print(self.real ,"i+", self.img,"j")
# dunder function
     def __add__(self,num2):
         newReal= self.real+num2.real
         newImg= self.img +num2.img
         return Complex(newReal,newImg)
     def __sub__(self,num2):
         newReal= self.real-num2.real
         newImg= self.img -num2.img
         return Complex(newReal,newImg)

num1=Complex(4,9)
num1.show_num()

num2=Complex(2,5)
num2.show_num()

num3=num1+num2
num3.show_num()
num4=num1-num2
num4.show_num()



