from cmath import sqrt
import os
from art import logo


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def clr():
    os.system("cls")


operation = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("Enter the First Number").title())
    print("Enter the function you wants to perform")
    for i in operation:
        print(i)
    operends = input("")
    num2 = float(input("Enter the second number").title())
    function = operation[operends]
    answer = function(num1=num1, num2=num2)
    print(f"{num1} {operends} {num2} = {answer}")
    temp = False
    while not temp:
        anythingelse = input(
            "Do you want to perform any other task y for yes and n for NO").lower()
        if anythingelse == "y":
            clr()
            print("Enter the function you wants to perform")
            for i in operation:
                print(i)
            operends = input("")
            num2 = float(input("What is Next number").title())
            temp1 = answer
            function = operation[operends]
            answer = function(num1=answer, num2=num2)
            print(f"{temp1} {operends} {num2} = {answer}")

        else:
            clr()

            temp = True
            calculator()

    # print(answer)
calculator()
