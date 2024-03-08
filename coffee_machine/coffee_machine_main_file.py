

# TODO: 1. Print report of all coffee resources
# TODO: 2. Check resources sufficient to make drink order
# TODO: 3. Process Coins
# TODO: 4. Check if the transaction is successful
# TODO: 5. Make the coffee


from data import MENU, resources

# Global variables
is_machine_off = False
money_in_machine = 0


def update_resources(order_ingredients):
    for item, quantity in order_ingredients.items():
        resources[item] -= quantity


def give_change(total_money, drink):
    change = round(total_money - drink['cost'], 2)
    return change


def sum_coins(quarters, dimes, nickels, pennies):
    total_cents = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1
    return total_cents/100


def report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${money_in_machine}")


def check_resources_available(order_ingredients):
    for item, quantity in order_ingredients.items():
        if resources[item] < quantity:
            print(f"Not enough {item}.")
            return False
    return True


def coffee_machine():
    global is_machine_off, money_in_machine
    while not is_machine_off:
        user_input = input("What would you like? espresso/latte/cappuccino: ").lower()
        if user_input == "off":
            is_machine_off = True
        elif user_input == "report":
            report()
        elif user_input in MENU:
            drink = MENU[user_input]
            if check_resources_available(drink['ingredients']):
                print(f"That will be ${drink['cost']}")
                quarters = int(input("Please insert number of quarters: "))
                dimes = int(input("Please insert number of dimes: "))
                nickels = int(input("Please insert number of nickels: "))
                pennies = int(input("Please insert number of pennies: "))
                total_money = sum_coins(quarters, dimes, nickels, pennies)
                # Just for testing print(total_money) #
                if total_money == drink['cost']:
                    money_in_machine += total_money
                    update_resources(drink['ingredients'])
                    print(f"Thank you! Here's you {user_input}! ☕")
                elif total_money >= drink['cost']:
                    money_in_machine += total_money
                    change_given = give_change(total_money, drink)
                    print(f"Here's your change! ${change_given}")
                    print(f"Thank you! Here's you {user_input}! ☕")
                    update_resources(drink['ingredients'])
                else:
                    print("Sorry not coins! Money refunded.")
        else:
            print("Invalid input. Please try again.")


coffee_machine()
