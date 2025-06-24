import random

choices = ["rock", "paper", "scissors"]
a_pc = random.choice(choices)
user_score = 0
pc_score = 0
run = True

print("You can choose \"rock\", \"paper\", or \"scissors\"")
while(run):
    a = str(input("Please enter your choice: "))
    if(a in choices):
        print("Computer choice:", a_pc)
        if(a == a_pc):
            print("Equals! please try again")
        elif(a == "rock" and a_pc == "paper"):
            pc_score += 1
            print("1 point for PC!")
        elif(a == "rock" and a_pc == "scissors"):
            user_score +=1
            print("1 point for You!")
        elif(a == "paper" and a_pc == "rock"):
            user_score +=1
            print("1 point for You!")
        elif(a == "paper" and a_pc == "scissors"):
            pc_score += 1
            print("1 point for PC!")
        elif(a == "scissors" and a_pc == "rock"):
            pc_score += 1
            print("1 point for PC!")
        elif(a == "scissors" and a_pc == "paper"):
            user_score +=1
            print("1 point for You!")
            
        if(user_score == 3):
            print("You won!!!")
            run = False
        elif(pc_score == 3):
            print("You Lost!!!")
            run = False
    else:
        print("Error ===> Please type one of choices that says in the top.")
        break