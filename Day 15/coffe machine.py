from clear_screan import clr
coffe = 100
water = 100
milk = 100
sugar = 100
money = 0

resourses = [coffe, water, milk, sugar]

penny = 0
nickle = 0
dime = 0
quater = 0
dollers = 0

coins = [penny, nickle, dime, quater, dollers]
coinsname = ["penny", "nickle", "dime", "quater", "dollers"]

c1 = ["Espresso", 3, 4, 8, 2, 2]
c2 = ["Cappuccino", 3, 4, 8, 2, 3]
c3 = ["Latte", 3, 4, 8, 2, 5]
cs = [c1, c2, c3]


def moneycal():
    global money
    for i in range(len(coins)):
        coins[i] = int(input(f"How many {coinsname[i]}"))
    money += coins[0] * 0.01
    money += coins[1] * 0.05
    money += coins[2] * 0.1
    money += coins[3] * 0.25
    money += coins[4] * 1
    print(f"Balance is {money}")
    return


def maker(coffee):
    global money
    for i in range(len(resourses)):
        if resourses[i] < coffee[i+1]:
            print("The Resourcess are insuffcient")
            return
        else:
            resourses[i] -= coffee[i+1]
    money -= coffee[5]
    print("Coffee is Ready")
    print(f"Yor Balance Amount is {money}")
    return


Working = True


def main():
    global money
    global Working
    print("Enter Your choice")
    for i in range(len(cs)):
        print(f"{i+1} for {cs[i][0]}")
    choice = input()
    if (choice == "off"):
        Working = False
        return
    else:
        choice = (int(choice) - 1)
    while (choice < 0 or choice > 2):
        choice = int(input("The Choice is Wrong Enter Right choice"))
    while (money < cs[choice][5]):
        print("Money is Insufficient. Enter More coins")
        moneycal()
    maker(cs[choice])
    wants = int(input("Do You wants more coffee \n 1. For yes \n 0. For No"))
    if wants == 1:
        clr()
        main()
    else:
        print("Thanks for Use")
        print(f"${money} is Your Refunds")
        money = 0


while (Working):
    print("Welcome to Coffee Machine")
    main()
