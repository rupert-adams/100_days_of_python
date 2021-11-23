# Coffee Machine Project, build software for a coffee machine.
# Coffee data provided although I chose to use json for file. everything else is the challenge.

import json

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

# 4. give refund if not enough or too much

# 5. make coffee

if check_levels("espresso"):
    print("Hurray!")
machine_f.close()
coffee_f.close()