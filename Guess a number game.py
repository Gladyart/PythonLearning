# Guess a number game
import random

randomRange = 101
secretNumber = random.randint(0, randomRange)


print(f"Lets guess a number!!!\nPick a number from 1 to {randomRange-1}")
while True:    
    playerGuess = input("> ").lower()

    if playerGuess == "quit":
        print("Program stopped..")
        exit()

    print("I guess.. " + playerGuess)

    if playerGuess.isdigit():
        playerGuess = int(playerGuess)
        if playerGuess == secretNumber:
            print("Correct! You won!")
            break
        if playerGuess > randomRange-1:
            print("Out of range..")
        elif playerGuess > secretNumber:
            print("Too much.. Guess again!")
        elif playerGuess < secretNumber:
            print("Too little.. Guess again!")
    elif playerGuess.startswith("-"):
        print("Don't play negative! :)")
    else:
        print("Input is not a number..")
    
