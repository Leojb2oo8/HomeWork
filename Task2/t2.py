import os

name = input("\n What is your name? \n> ")

isNumeric = False
while isNumeric == False:
    num = input("\n Choose a whole number \n> ")
    try:
        fNum = int(num)
        isNumeric = True
        
    except ValueError:
        isNumeric = False
        os.system('clear')
        print("///Try again/// \n")
       
if fNum >-1 and fNum < 10:
    for x in range(fNum):
        print(name)

elif fNum <0:
    for x in range(3):
        print("Too low")
else:
    for x in range(3):
        print("Too high")
    