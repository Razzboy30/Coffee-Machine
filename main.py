# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# from six.moves import input
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money" : 0.0
}



coff = ''


def start():
    user_q = input("​What would you like? (espresso/latte/cappuccino):")
    if user_q == "report":
        report()
    elif user_q == "off":
        print("Bye!")
    elif user_q == "espresso" or user_q == "latte" or user_q == "cappuccino":
        global coff
        coff = user_q
        coffee(coff)


def report():
    print(f'Water : {resources["water"]}ml')
    print(f'Milk : {resources["milk"]}ml')
    print(f'Coffee : {resources["coffee"]}ml')
    print(f'Money : ${resources["Money"]}')
    start()

def mon():
    print("Please insert coins")
    quarters = int(input("Enter quarters:"))
    dimes = int(input("Enter dimes:"))
    nickles = int(input("Enter nickles:"))
    pennies = int(input("Enter pennies:"))
    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    round(money,2)
    return money


def coffee(CoffeT):
    global resources
    if CoffeT == "espresso":
        if resources["water"] <= 50:
            print("Not enough water")
        elif resources["coffee"] <= 18:
            print("Not enough coffee")
        else:
            eMoney = mon()
            if eMoney >= 1.50:
                resources["Money"]= resources["Money"] + 1.50
                resources["water"]= resources["water"] - 50
                resources["coffee"]= resources["coffee"]- 18
                print(f"Heres your change : ${round(eMoney - 1.50,2)}")
                print("Here is your espresso, enjoy!")
                start()
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif CoffeT == "latte":
        if resources["water"] <= 200:
            print("Not enough water")
        elif resources["milk"] <= 150:
            print("Not enough milk")
        elif resources["coffee"] <= 24:
            print("Not enough coffee")
        else:
            eMoney = mon()
            if eMoney >= 2.50:
                resources["Money"]= resources["Money"] + 2.50
                resources["water"]= resources["water"] - 200
                resources["milk"]= resources["milk"] + 150
                resources["coffee"]= resources["coffee"]- 24
                print(f"Heres your change : ${eMoney - 2.50}")
                print("Here is your latte, enjoy!")
                start()
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif CoffeT == "cappuccino":
        if resources["water"] <= 250:
            print("Not enough water")
        elif resources["milk"] <= 100:
            print("Not enough milk")
        elif resources["coffee"] <= 24:
            print("Not enough coffee")
        else:
            eMoney = mon()
            if eMoney >= 3:
                resources["Money"]= resources["Money"] + 3
                resources["water"]= resources["water"] - 250
                resources["milk"]= resources["milk"] + 100
                resources["coffee"]= resources["coffee"]- 24
                print(f"Heres your change : ${eMoney - 3}")
                print("Here is your cappuccino, enjoy!")
                start()
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("no")


start()
