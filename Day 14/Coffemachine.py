from secrets import choice
from select import select


def coffy_machine():
    ingridients = {
        "Water": 1000,
        "Milk": 500,
        "coffe": 200
    }
    coins = {
        "Dime": 0.01,
        "Nickel": 0.05,
        "Quater": 0.25,
        "Cents": 0.10
    }

    coffey = {
        "A": ["Cappuccino", 5, 100, 50, 20],
        "B": ["latte", 10, 200, 80, 30],
        "C": ["Espresso", 5, 175, 30, 40],
        "D": ["Caffe mocha", 15, 150, 60, 30]
    }
    for key in coffey:
        print(f'{key}. for {coffey[key][0]}')
    choice = input('Select any one of the above').upper()


coffy_machine()
