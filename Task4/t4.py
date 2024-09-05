import random, os

headsOrTails = ["h", "t"]

pcChoice = random.choice(headsOrTails)

os.system('clear')
choice = input("Choose heads or tails? (h), (t) \n>> ")
while choice != "h" and choice != "t":
    os.system('clear')
    print("///Try again/// \n")
    choice = input("Choose heads or tails? (h), (t) \n>> ")

if pcChoice == choice:
    print("You win\n")
else:
    print("Bad luck\n")

print("The computer chose: "+ pcChoice)