

import random


cards = {"Ace": 1,
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

print(cards)


def cards_user():
    face, values = random.choice(list(cards.items()))
    return face, values


def cards_deller():
    cface, cvalues = random.choice(list(cards.items()))
    return cface, cvalues


sum = 0
temp = 1
game_end = False
while not game_end:
    if temp == 1:
        face, values = cards_user()
        face1, values2 = cards_user()
        print(f'Your cards are {face} and {values}')
        print(f'Your cards are {face1} and {values2}')
        sum = values+values2
        print(f"Your\'s sum total {sum}")

        dface, dvalues = cards_deller()
        dface1, dvalues2 = cards_deller()
        print(f'Your cards are {dface} and {dvalues}')
        print(f'Your cards are {dface1} and {dvalues2}')
        dsum = dvalues+dvalues2
        print(f"deller\'s sum total {dsum}")
        temp = 0
