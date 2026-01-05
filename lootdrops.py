import json
import random

def add_random_drop(): #defines the function to add a random loot drop to the treasure pouch
    file_name = "treasure_pouch.json"
    with open(file_name, "r") as file:
        data = json.load(file)

    item = random.choice(data["items"]) #randomly selects a treasure from the list of items in treasure pouch
    item["quantity"] += 1 #increases its quantity by 1

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print(f"You received a {item['name']}!") #displays a message to let the user know what loot they received
