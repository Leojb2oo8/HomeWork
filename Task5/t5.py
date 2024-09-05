import random
MAX_RANDOM = 10
QUESTIONS = 5
quizInfo = []
userAnswer = []
score = 0

def newQuestion():
    equation = ["+", "-", "*"]
    equationChoice = random.choice(equation)
    
    num1 = random.randint(1,MAX_RANDOM)
    num2 = random.randint(1,MAX_RANDOM)
    
    if equationChoice == "+": 
        questionInfo = [num1, "+", num2, num1+num2]
    elif equationChoice == "-": 
        questionInfo = [num1, "-", num2, num1-num2]  
    elif equationChoice == "*": 
        questionInfo = [num1, "*", num2, num1*num2]    
         
    return(questionInfo)


for x in range(QUESTIONS):
    quizInfo.append(newQuestion())


for x in range(QUESTIONS):
    answer = input("(Q"+str(x+1)+") "+str(quizInfo[x][0])+str(quizInfo[x][1])+str(quizInfo[x][2])+"= ")
    userAnswer.append(answer)

for x in range(QUESTIONS):
    if quizInfo[x][3] == int(userAnswer[x]):
        score = score + 1
        
print("You got "+str(score)+"/5")