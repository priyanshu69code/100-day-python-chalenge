import random
from art import logo, vs
from game_data import data
from clear_screan import clr


def compare(a, b, guess):
    if a["follower_count"] > b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


def game_over():
    game_over = False
    b = random.choice(data)
    score = 0

    while not game_over:
        a = b
        b = random.choice(data)
        while a == b:
            b = random.choice(data)
        print(
            f"{a['name']}, A {a['description']} with {a['follower_count']} million follwers from {a['country']}")
        print(vs)
        print(f"{b['name']}, A {b['description']} from {b['country']}")
        guess = input(
            f"Enter \"A\" for {a['name']} and \"B\" for {b['name']}").lower()

        is_correct = compare(a=a, b=b, guess=guess)
        if is_correct:
            score += 1
            print(f"You guessed it correct, your score is {score}")
        else:
            print(f"You losse the game,And your final score is {score}")
            game_over = True


game_over()
