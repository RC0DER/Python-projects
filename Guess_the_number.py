import random
print("Press the number to choose the difficulty level")
print("1.Beginner(0-10)\n2.Intermediate(0-20)\n3.Pro(0-50)\n4.Hacker(0-100)\n5.God(0-200)")
choice = int(input("Enter here->"))
#Beginner(0-10)
if choice == 1 :
    random_num = random.randint(0,10)
    print("3 Gusses. Best of luck, detective! 😄🔍✨")
    for i in range(3):
        guess = int(input("Guess a number 😁: "))
        if i < 2:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
                break
            elif guess > random_num:
                print("Guess a teeny-tiny number! 🤏🤔")
            else:
                print("Guess a huge number! 🌋🤔")
        else:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
            else:
                print("Oops, you guessed it wrong 😔💔.","It was",random_num)
#Intermediate(0-20)
elif choice == 2 :
    random_num = random.randint(0,20)
    print("4 Gusses. Best of luck, detective! 😄🔍✨")
    for i in range(4):
        guess = int(input("Guess a number 😁: "))
        if i < 3:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
                break
            elif guess > random_num:
                print("Guess a teeny-tiny number! 🤏🤔")
            else:
                print("Guess a huge number! 🌋🤔")
        else:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
            else:
                print("Oops, you guessed it wrong 😔💔.","It was",random_num)
#Pro(0-50)
elif choice == 3 :
    random_num = random.randint(0,50)
    print("5 Gusses. Best of luck, detective! 😄🔍✨")
    for i in range(5):
        guess = int(input("Guess a number 😁: "))
        if i < 4:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
                break
            elif guess > random_num:
                print("Guess a teeny-tiny number! 🤏🤔")
            else:
                print("Guess a huge number! 🌋🤔")
        else:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
            else:
                print("Oops, you guessed it wrong 😔💔.","It was",random_num)
#Hacker(0-100)
elif choice == 4 :
    random_num = random.randint(0,100)
    print("8 Gusses. Best of luck, detective! 😄🔍✨")
    for i in range(8):
        guess = int(input("Guess a number 😁: "))
        if i < 7:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
                break
            elif guess > random_num:
                print("Guess a teeny-tiny number! 🤏🤔")
            else:
                print("Guess a huge number! 🌋🤔")
        else:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
            else:
                print("Oops, you guessed it wrong 😔💔","It was",random_num)
#God(0-100)
elif choice == 5 :
    random_num = random.randint(0,200)
    print("10 Gusses. Best of luck, detective! 😄🔍✨")
    for i in range(10):
        guess = int(input("Guess a number 😁: "))
        if i < 9:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
                break
            elif guess > random_num:
                print("Guess a teeny-tiny number! 🤏🤔")
            else:
                print("Guess a huge number! 🌋🤔")
        else:
            if guess == random_num:
                print("wohoo!! You guessed it right🎉🎉")
            else:
                print("Oops, you guessed it wrong 😔💔.","It was",random_num)
else :
    print("Enter a valid Input")
print("__________GAME OVER__________")