import os
isNumeric = False
while isNumeric == False:
    age = input("\n What is your age? \n> ")
    try:
        fAge = float(age)
        isNumeric = True
        
    except ValueError:
        isNumeric = False
        os.system('clear')
        print("///Try again/// \n")


if fAge >= 18:
    print("You can vote")
elif fAge >= 17:
    print("You can learn to drive")
elif fAge >= 16:
    print("You can buy a lottery ticket")
elif fAge < 16:
    print("You can go Trick-orTreating")