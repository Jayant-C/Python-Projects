import random

Numbers = (1, 2, 3, 4, 5, 6)
ImposterNumber = random.choice(Numbers)

Status = "Lose"
while Status == "Lose":
    UserNumber = int(input("Choose a number from 1 to 6: "))
    
    if UserNumber == ImposterNumber:
        print("You Found The Imposter Number")
        Status = "Win"
    else:
        print("Try Again")
