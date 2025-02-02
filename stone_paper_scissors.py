import random
print(" __________Rock, paper, scissors Game__________")
list = ["rock", "paper", "scissors"]
read = ""
points_bot = 0
points_you = 0
round = int(input("Number of rounds: "))
i = 0
while i < round:
    choice_bot = random.choice(list)
    print(choice_bot)
    print("1. Press 'r' for rock\n2. Press 'p' for paper\n3. Press 's' for scissors")
    choice = input("Enter your choice: ")
    if choice == "r":
        if choice_bot == "rock":
            print(" __________This round is draw__________")
            print("______________________________________________")
        elif choice_bot == "scissors":
            points_you += 1
            print(" __________You won this round: )________")
            print("______________________________________________")
        else :
            points_bot += 1
            print(" __________You loose this round :_(__________")
            print("______________________________________________")
        i += 1
        continue
    elif choice == "p":
        if choice_bot == "paper":
            print(" __________This round is draw__________")
            print("______________________________________________")
        elif choice_bot == "rock":
            points_you += 1
            print(" __________You won this round: )________")
            print("______________________________________________")
        else :
            points_bot += 1
            print(" __________You loose this round :_(__________")
            print("______________________________________________")
        i += 1
        continue
    elif choice == "s":
        if choice_bot == "scissors":
            print(" __________This round is draw__________")
            print("______________________________________________")
        elif choice_bot == "paper":
            points_you += 1
            print(" __________You won this round: )________")
            print("______________________________________________")
        else :
            points_bot += 1
            print(" __________You loose this round :_(__________")
            print("______________________________________________")
        i += 1
        continue
    else : 
        print(" __________Invalid input__________")
        print("______________________________________________")
        continue
print("  __________   Your points =",points_you,"  __________")
print("  __________ Computer points =",points_bot,"__________")
if points_you > points_bot:
    print("  __________      You won!!      __________")
elif points_you < points_bot:
    print("  __________     You loose!!     __________")
else :
    print("  __________        Draw!        __________")


