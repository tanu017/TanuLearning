import random
game= ["Rock", "Paper", "Scissors"] 
while True:
    print('''    1. Rock
    2. Paper
    3. Scissors''')
    choice = int(input("Enter your choice: "))
    ran= random.randint(1, 3)
    print("You have chosen:", game[choice-1])
    print(game[choice-1], "vs", game[ran-1])
    if choice==ran:
        print("It's a tie")
    elif choice==1 and ran==2 or choice==2 and ran==3:
        print("You lost")
    elif choice==2 and ran==1 or choice==3 and ran==2:
        print("You win")
        rep= input("Do you want to continue(Y/N): ")
        if rep.upper()=="Y":
            pass
        else: 
            break
    else:
        print("Please try again")
