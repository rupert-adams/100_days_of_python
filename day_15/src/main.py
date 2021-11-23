# Coffee Machine Project, build software for a coffee machine.
# Coffee data provided although I chose to use json for file. everything else is the challenge.

import json
from decimal import *

machine_f, coffee_f =  open('src/data/machine.json'), open('src/data/coffee.json')
machine_data, coffee_data = json.load(machine_f), json.load(coffee_f)

# 1. print report
def report(data: dict = machine_data["machine"]):

    return f"Report:\nwater: {data['water']}ml\nmilk: {data['milk']}ml\ncoffee: {data['coffee']}mg"


# 2. check resources sufficient
def check_levels(choice: str, machine_data: dict = machine_data["machine"], coffee_data: dict = coffee_data):
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

# 3. process coins, ask for quantity
def coin_process(coin_list: list, coffee_price: int, coins_accepted: list = machine_data["accepted coins"]):
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



# 4. give refund if not enough or too much

# 5. make coffee

# if check_levels("espresso"):
#     print("Hurray!")
coin_process([1,2,1], 3)
machine_f.close()
coffee_f.close()