import os, random

def pickNumbers():
    os.system('clear')
    isNumeric = False
    while isNumeric == False:
        num1 = input("Pick a low number.\n>> ")
        try:
            fNum1 = int(num1)
            isNumeric = True
            
        except ValueError:
            isNumeric = False
            os.system('clear')
            print("///Try again/// \n")
    
    isNumeric = False
    isHiger = False
    while isNumeric == False or isHiger == False:
        num2 = input("Pick a high number.\n>> ")
        try:
            fNum2 = int(num2)
            isNumeric = True
            if fNum2 > fNum1:
                isHiger = True
            else:
                os.system('clear')
                print("///Try again/// \n")
                isHiger = False
            
        except ValueError:
            isNumeric = False
            os.system('clear')
            print("///Try again/// \n")
    return(random.randint(fNum1,fNum2))

def guess():
    print("I am thinking of a number…")
    isNumeric = False
    while isNumeric == False:
        userGuess = input("Pick a number between the numbers that you picked.\n>> ")
        try:
            fUserGuess = int(userGuess)
            isNumeric = True
            
            
        except ValueError:
            isNumeric = False
            os.system('clear')
            print("///Try again/// \n")
    return(fUserGuess)

def compare(num1, num2):
    if num1 == num2:
        print("Correct, you win!")
        return(True)
    else:
        return(False)
    
    
    
comp_num = pickNumbers()
user_num = guess()

while compare(comp_num, user_num) == False:
    os.system('clear')
    print("Wrong try again")
    user_num = guess()