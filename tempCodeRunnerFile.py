import random
print(" __________Rock, paper, scissors Game__________")
list = ["rock", "paper", "scissors"]
read = ""
points_bot = 0
points_you = 0
points_play = int(input("Number of rounds: "))
i = 0
while i < points_play:
    choice_bot = random.choice(list)
    print(choice_bot)
    print("1. Press 'r' for rock\n2. Press 'p' for paper\n3. Press 's' for scissors")
    choice = input("Enter your choice: ")
    if choice == "r":
        read = "rock"
    elif choice == "p":
        read == "paper"
    elif choice == "s":
        read == "scissors"
    else : 
        print(" __________Invalid input__________")
        print("______________________________________________")
        continue
    print(read)
    if read == choice_bot:
        print(" __________This round is draw__________")
        print("______________________________________________")
    elif (read == "paper" and choice_bot == "rock") or (read == "scissors" and choice_bot == "paper") or (read == "rock" and choice_bot == "scissors"):
        points_you += 1
        print(" __________You won this round: )________")
        print("______________________________________________")
    else :
        points_bot += 1
        print(" __________You loose this round :_(__________")
        print("______________________________________________")
    i += 1
print("  __________   Your points =",points_you,"  __________")
print("  __________ Computer points =",points_bot,"__________")
if points_you > points_bot:
    print("  __________      You won!!      __________")
elif points_you < points_bot:
    print("  __________     You loose!!     __________")
else :
    print("  __________        Draw!        __________")


