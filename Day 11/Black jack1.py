import os
import random
from art import logo


cards = {"Ace": 11,
         2: 2,
         3: 3,
         4: 4,
         5: 5,
         6: 6,
         7: 7,
         8: 8,
         9: 9,
         10: 10,
         "Jack": 10,
         "Queen": 10,
         "King": 10, }


def clr():
    '''This function is for clearing screen in windows'''
    os.system("cls")


def deals_card():
    '''This function is for taking random cards from the dictionary'''
    face, values = random.choice(list(cards.items()))
   # print(f'Your cards are {face} and {values}')
    return values


def calculate_score(cards):
    '''This function is for Calculating the Sum of all the cards and if the Score Went more than 21 and have ace it will change the value of ace with 1'''
    if cards == 21 and len(cards):
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


user_cards = []
computer_cards = []


def black_jack():
    user_cards = []
    computer_cards = []
    clr()
    print(logo)
    game_over = False
    for _ in range(2):
        computer_cards.append(deals_card())
        user_cards.append(deals_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards} and Score is {user_score}")
        print(f"Computer Card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deals_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deals_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print("********************Game Has Ended Thanks For Playing************************")
    print("")
    print("")

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        black_jack()


black_jack()
input()
