import os, random

def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    userAnswer = input("What is " + str(num1) + " plus " + str(num2) +"?\n>> ")
    return[userAnswer, num1+num2]

def subtraction():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    userAnswer = input("What is " + str(num1) + " plus " + str(num2) + "?\n>> ")
    return[userAnswer, num1+num2]

def answerCheck(answers):
    if int(answers[0]) == int(answers[1]):
        print("Correct")
    else:
        print("Incorrect, the answer is " + str(answers[1]))

os.system('clear')
choice = input("(1)Addition \n(2)Subtraction \n>> ")
while choice != "1" and choice != "2":
    os.system('clear')
    print("///Try again/// \n")
    choice = input("(1)Addition \n(2)Subtraction \n>> ")
    
if choice == "1":
    answerCheck(addition())
    
    
elif choice == "2":
    answerCheck(subtraction())
