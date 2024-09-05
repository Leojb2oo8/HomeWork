import os
total = 0

def newNumber():
    isNumeric = False
    os.system('clear')
    while isNumeric == False:
        num = input("Choose a number\n> ")
        try:
            fNum = float(num)
            isNumeric = True
            
        except ValueError:
            isNumeric = False
            os.system('clear')
            print("///Try again/// \n")

    choice = input("Do you want to include this number in the total? (YES), (NO) \n>> ")
    while choice != "YES" and choice != "NO":
        os.system('clear')
        print("///Try again/// \n")
        choice = input("Do you want to include this number in the total? (YES), (NO) \n>> ")

    if choice == "YES":
        return(fNum)
    else:
        return(0)

for x in range(5):
    total = total + newNumber()
print("Your total is: "+ total)