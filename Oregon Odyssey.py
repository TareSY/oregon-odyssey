import random

# Define list of scenarios
scenarios = [
    "You encounter an asteroid field.",
    "Your ship's engine malfunctions.",
    "You run out of food supplies.",
    "You encounter a hostile alien race.",
    "One of your crew members gets sick.",
    "You discover an abandoned space station.",
    "Your ship's life support system is failing.",
    "You encounter a mysterious space anomaly.",
    "Your ship's navigation system is offline.",
    "You are hit by a solar flare."
]


# Define list of items
items = {
    "Food": 100,
    "Fuel": 100,
    "Medicine": 50,
    "Ammunition": 100,
    "Repair Kit": 50
}

# Define function to display current status
def display_status():
    print("Location: USS Oregon")
    print("Inventory:")
    for item in items:
        print(item + ": " + str(items[item]))


# Define function to prompt player for decision
def make_decision():
    print("Available options: hunt, trade, continue")
    decision = input("What would you like to do? ")
    if decision == "hunt":
        items["Food"] += random.randint(50, 100)
    elif decision == "trade":
        trade_decision = input("What item do you want to trade and what item do you want in return? (e.g. fuel for ammunition) ")
        trade_items = trade_decision.split(" ")
        if len(trade_items) == 4 and trade_items[1] == "for":
            item1 = trade_items[0].title()
            item2 = trade_items[2].title()
            if item1 in items and item2 in items:
                trade_amount = min(items[item1], items[item2])
                items[item1] -= trade_amount
                items[item2] += trade_amount
            else:
                print("Invalid items. Please try again.")
        else:
            print("Invalid input. Please try again.")
    elif decision == "continue":
        # Move the game forward
        pass
    else:
        print("Invalid input. Please try again.")


# Define function to select and apply a random scenario
def random_scenario():
    scenario = random.choice(scenarios)
    print(scenario)
    if scenario == "You encounter an asteroid field.":
        # Apply asteroid field scenario
        items["Fuel"] -= 20
        items["Ammunition"] -= 20
    elif scenario == "Your ship's engine malfunctions.":
        # Apply engine malfunction scenario
        items["Repair Kit"] -= 1
    elif scenario == "You run out of food supplies.":
        # Apply food shortage scenario
        items["Food"] -= 20
    elif scenario == "You encounter a hostile alien race.":
        # Apply hostile alien scenario
        items["Ammunition"] -= 30
    elif scenario == "One of your crew members gets sick.":
        # Apply sickness scenario
        items["Medicine"] -= 1
    elif scenario == "You discover an abandoned space station.":
        # Apply space station scenario
        items["Fuel"] += 50
        items["Ammunition"] += 50
    elif scenario == "Your ship's life support system is failing.":
        # Apply life support failure scenario
        items["Repair Kit"] -= 1
    elif scenario == "You encounter a mysterious space anomaly.":
        # Apply space anomaly scenario
        items["Fuel"] -= 10
        items["Medicine"] += 10
    elif scenario == "Your ship's navigation system is offline.":
        # Apply navigation failure scenario
        items["Repair Kit"] -= 1
    elif scenario == "You are hit by a solar flare.":
        # Apply solar flare scenario
        items["Fuel"] -= 20
        items["Ammunition"] -= 20
   
        

# Main game loop
while True:
    display_status()
    make_decision()
    random_scenario()
