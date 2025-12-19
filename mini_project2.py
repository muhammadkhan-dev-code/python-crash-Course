# chat assistance Ai Assistance 
import datetime
import time



def greetUser(name):
    present_time=datetime.datetime.now().hour
    if present_time<12:
        print(f"Hi {name}, Good Morning  ! Welcome to Your buddy ChatBot ")
    elif 12<=present_time<16:
        print(f"Hi {name}, Good Afternoon  ! Welcome to Your buddy ChatBot ")
    else:
        print(f"Hi {name}, Good Evening  ! Welcome to Your buddy ChatBot ")

def getRespone(user_input):
    for eachKey in responses:
       if eachKey in user_input:
           return responses[eachKey]
    return "I'm sorry, I don't understand. Can you please rephrase?"

# chatBot Memory dict of responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a program, but thanks for asking! How can I help you?",
    "what is your name?": "I'm your friendly ChatBot!",
    "who are you": "I'm an AI designed to assist you with your questions.",
    "motivate me ": "Believe in yourself! You can achieve anything you set your mind to.",
    "happy": "Happiness is a choice! Choose to be happy every day.",
    "sad": "It's okay to feel sad sometimes. Remember, after the rain comes the rainbow.",
    "what is python": "Python is a versatile programming language known for its readability and wide range of applications.",
    "tell me a joke": "Why did the programmer quit his job? Because he didn't get arrays (a raise)!",
    "bye": "Goodbye! Have a great day!"
}

def main():
    name = input("Enter your name: ")
    greetUser(name)
    print("You can ask me the basic questions & Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        time.sleep(1)
        if user_input.lower() == "bye":
            print("ChatBot: " + responses["bye"])
            break
        reply = getRespone(user_input.lower())
        print("ChatBot: " + reply)

if __name__ == "__main__":
    main()




