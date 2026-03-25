from data import MENU, resources


def check_resource(current,ingredient_name, ingredient_amount):
    required_ingredient = ingredient_amount
    ingredient_sufficient = current[ingredient_name] >= required_ingredient
    if not ingredient_sufficient:
        print(f"Sorry, you don't have enough {ingredient_name}.")
        return False
    else:
        return True

def coffee_machine():
    current = resources
    current_money = 0
    is_on = True

    # TODO: 4. Loop if is_on
    while is_on:
        # TODO: 1. Prompt user the question - "What would you like?"
        order = input("What would you like? (espresso/latte/cappuccino").lower()
        if order == "off":
            is_on = False
            # TODO: 2. Turn off the machine
            print("Goodbye!")

        elif order == "report":
            # TODO: 3. Print report
            is_on = True
            print(f"Water: {current['water']}ml")
            print(f"Milk: {current['milk']}ml")
            print(f"Coffee: {current['coffee']}g")
            print(f"Money: ${current_money}")
        else:
            is_on = True
            water = MENU[order]["ingredients"]["water"]
            milk = MENU[order]["ingredients"].get('milk',0)
            coffee = MENU[order]["ingredients"]["coffee"]
            cost = MENU[order]["cost"]

            # TODO: 4 check stock
            water_sufficient = check_resource(current,"water", water)
            milk_sufficient = check_resource(current,"milk", milk)
            coffee_sufficient = check_resource(current,"coffee", coffee)

            if water_sufficient and milk_sufficient and coffee_sufficient:
                n_quarters = int( input('Please insert coins.\nHow many quarters?:'))
                n_dimes = int(input('How many dimes?:'))
                n_nickles = int(input('How many nickles?:'))
                n_pennies = int(input('How many pennies?:'))
                total = n_quarters * 0.25 + n_dimes * 0.1 + n_nickles * 0.05 + n_pennies * 0.01
                # TODO: 5. Check if the transaction successful?
                if total < cost:
                    print(f"Sorry that's not enough money. Money refunded.")
                else:
                    change = total - cost
                    print(f"Here is ${change:.2f} in change.")
                    # TODO: 6. Update the ingredients in stock.
                    current_money += cost
                    current["water"] -= water
                    current["milk"] -= milk
                    current["coffee"] -= coffee
                    print(f"Here is your {order}.")




coffee_machine()