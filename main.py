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
    "money": 2.5,
}


def coffee_machine(coffee_type: str):
    # TODO: 4. Check resources sufficient?
    for key, value in resources.items():
        if key in MENU[coffee_type]["ingredients"]:
            if value < MENU[coffee_type]["ingredients"][key]:
                print(f"Sorry there is not enough {key}.")
                return

    # TODO: 5. Process coins.
    print("Insert coins: ")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    monetary_value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    # TODO: 6. Check transaction successful?
    if monetary_value < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return
    elif monetary_value == MENU[coffee_type]["cost"]:
        resources["money"] += monetary_value
    else:
        resources["money"] += MENU[coffee_type]["cost"]
        change = monetary_value - MENU[coffee_type]["cost"]
        print(f"Here is ${change} dollars in change.")

    # TODO: 7. Make Coffee.
    # Deduct resources
    for key, value in MENU[coffee_type]["ingredients"].items():
        resources[key] -= MENU[coffee_type]["ingredients"][key]
    print(f"Here is your {coffee_type}. Enjoy!")


if __name__ == "__main__":
    while True:
        # TODO: 1. Prompt user by asking “​ What would you like? (espresso/latte/cappuccino)
        user_input = input("What would you like? (espresso/latte/cappuccino)?")

        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
        if user_input == "off":
            break

        # TODO: 3. Print report.
        if user_input == "report":
            print("Water: ", resources["water"])
            print("Milk: ", resources["milk"])
            print("Coffee: ", resources["coffee"])
            print(f"Money: ${resources['money']}")
        elif user_input in MENU.keys():
            coffee_machine(user_input)
