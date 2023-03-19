import random
import os
from art import logo


HARD_LEVEL = 5
EASSY_LEVEL = 10


def clr():
    os.system("cls")


def check_answer(guess, answer, turns):
    if guess > answer:
        print(" Too Heigh")
        print("   Guess Again")
        return turns - 1
    elif guess < answer:
        print(" Too Low")
        print("   Guess Again")
        return turns - 1
    else:
        print(f"You guessed it Right. The Answer was {answer}")
        return "win"


def dificult():
    Right_guess = False
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while not Right_guess:
        level = input(
            "Chosse the level of Difficultie \"Easy\" for Easy and \"Hard\" for hard\n").lower()
        if level == "hard":
            Right_guess = True
            return HARD_LEVEL
        elif level == "easy":
            Right_guess = True
            return EASSY_LEVEL
        else:
            print("You have chosse Wrong Option plese select Right")
            Right_guess = False


def game():
    game_over = False
    answer = random.randint(1, 100)
    turns = dificult()
    clr()
    print(logo)
    while not game_over:
        guess = int(input("Make a Guess\n"))
        turns = check_answer(guess=guess, answer=answer, turns=turns)
        if not turns == "win":
            print(f"You have left with {turns} life")
        if turns == 0:
            game_over = True
            print("You lose the game\n")
        elif turns == "win":
            game_over = True
    if input("Do you wants to Play the game again press Y for Yes N for No. \n").lower() == "y":
        clr()
        game()


game()
