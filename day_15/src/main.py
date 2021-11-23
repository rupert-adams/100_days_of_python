# Coffee Machine Project, build software for a coffee machine.
# Coffee data provided although I chose to use json for files. everything else is the challenge.

import json

machine_f, coffee_f =  open('src/data/machine.json'), open('src/data/coffee.json')
machine_data, coffee_data = json.load(machine_f), json.load(coffee_f)


def report(data: dict = machine_data["machine"]):
    '''
    Returns a report of the current resources in the machine.
    '''
    return f"Report:\nwater: {data['water']}ml\nmilk: {data['milk']}ml\ncoffee: {data['coffee']}mg"


def check_levels(choice: str, machine_data: dict = machine_data["machine"], coffee_data: dict = coffee_data):
    '''
    Checks the level of each resource in the coffee machine against what is needed
    for the coffee choice. Returns True if enough resources
    '''
    checks_completed = 0
    for item in ["water", "milk", "coffee"]:
        if coffee_data[choice][item] > machine_data[item]:
            print(f"{item} level at {machine_data[item]}, {coffee_data[choice][item]} for {choice}, please refill")
        else:
            checks_completed+=1
    if checks_completed == 3:
        return True
    else:
        return False


def coin_process(coin_list: list, coffee_price: int, coins_accepted: list = machine_data["accepted coins"]):
    '''
    Processes the list of coins and checks first if the coin is allowed.
    Next it checks the amount you've entered against the price and either returns
    True if enough, refunds you and returns True if too much or refunds you and returns
    False if not enough.
    '''
    for item in coin_list:
        if item not in coins_accepted:
            print(f"£{item} coin not accepted, please use one of the following coins:{coins_accepted}")
            print(f"refunding £{item} coin")
            return False
    total_coins = sum(coin_list)
    refund_value = 0
    if total_coins >= coffee_price:
        if total_coins > coffee_price:
            refund_value = total_coins-coffee_price
            print(f"paid too much, refunding £{'{0:.2f}'.format(refund_value)}")
        return True
    else:
        refund_value = total_coins
        print(f"Not enough coins, you paid £{'{0:.2f}'.format(refund_value)}, £{'{0:.2f}'.format(coffee_price)} is needed, refunding your money")
        return False


def make_coffee(choice: str, machine_data: dict = machine_data["machine"], coffee_data: dict = coffee_data):
    '''
    Updates the resources in machine_data['machine'] account for the coffee
    that has been made.
    '''
    print(f"Making {choice.capitalize()}...")
    for item in ["water", "milk", "coffee"]:
        machine_data[item] = machine_data[item] - coffee_data[choice][item]
    return machine_data


def main(machine_data: dict = machine_data, coffee_data: dict = coffee_data):
    '''
    The main function. Takes a choice input and runs a check for the resources in the machine.
    Then requests the coins for the transaction, first the user inputs the amount of coins,
    then the individual coins.
    The coins are processed and then the machine_data is updated to account for the depleted
    resources.
    Currently depleted resources are written to a new file 'new_machine.json' instead of 
    over the old one.
    '''
    print("Welcome to the Coffee-o-matic, please choose one of the following options:\n")
    choice = input(str("'espresso', 'latte', 'cappuccino' or 'report':\n"))
    if choice not in ['espresso', 'latte', 'cappuccino', 'report']:
        choice = input(str("please choose either 'espresso', 'latte', 'cappuccino' or 'report':\n"))
    if choice == 'report':
        print(f"\n{report()}\n")
    elif choice in ['espresso', 'latte', 'cappuccino']:
        if check_levels(choice):
            print(f"Please insert £{'{0:.2f}'.format(coffee_data[choice]['price'])}\n")
            coin_list = []
 
            n = int(input("Enter number of coins: "))
            for i in range(0, n):
                coins = float(input("Please add the coins for your choice:\n"))
            
                coin_list.append(coins)
            if coin_process(coin_list, coffee_data[choice]['price']):
                machine_data['machine'] = make_coffee(choice)
                # This could be used to re-write the machine.json file in production
                with open('src/data/new_machine.json', 'w') as json_file:
                    json.dump(machine_data, json_file)
                print(f"Your {choice} is complete, have a nice day!")


if __name__ == "__main__":
    main()
    machine_f.close()
    coffee_f.close()