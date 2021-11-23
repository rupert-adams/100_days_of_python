# Coffee Machine Project, build software for a coffee machine.
# Coffee data provided although I chose to use json for file. everything else is the challenge.

import json

machine_f, coffee_f =  open('src/data/machine.json'), open('src/data/coffee.json')
machine_data, coffee_data = json.load(machine_f), json.load(coffee_f)

# 1. print report
def report(data: dict):

    return f"Report:\nwater: {data['water']}ml\nmilk: {data['milk']}ml\ncoffee: {data['coffee']}mg"


# 2. check resources sufficient

# 3. process coins, ask for quantity

# 4. give refund if not enough or too much

# 5. make coffee

print(report(machine_data['machine']))
machine_f.close()
coffee_f.close()