import random


def guess_game():
    condition = True
    while condition:
        print("Guess a number between 1 and 1000 ")
        userInput = int(input())
        randomNumber = random.randrange(1, 10)
        if userInput < randomNumber:
            print("Too low    Try again!!!")
        if userInput > randomNumber:
            print("Too High    Try again!!!")
        elif userInput != randomNumber:
            print("enter your next guess!!!")
            userInput = int(input())
        if userInput == randomNumber:
            print("Congratulation you guessed the number !!!")
            print("Do you wish to play again ")
        play_again = input()
        if play_again == "no":
            condition = False

            return randomNumber


print(guess_game())
