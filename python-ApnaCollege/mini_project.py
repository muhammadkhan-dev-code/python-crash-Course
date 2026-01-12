import random
target=random.randint(1,100)
while True:
    user_choice=input("Guess the Target or for Quit press (Q) :")
    if user_choice=='Q':
        print("Thanks for playing ")
        break
    elif (int(user_choice)==target):
        print("Success: Correct Guess!..")
        break
    
    elif(int(user_choice)<target):
        print("Your choice is less than target ... Enter a greater Choice")
    else:
        print("Your choice is greater than target ... Enter a lesser Choice")


print("Game Over ...")