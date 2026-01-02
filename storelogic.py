import json

def load_inventory(): #This function loads the inventory from a JSON file
    with open("inventory.json", "r") as file:
        return json.load(file)

def save_inventory(inventory): #This function will update the inventory JSON file
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

def sell_treasure(): #This is the main function to sell treasure items
    inventory = load_inventory() #setting the variable inventory to the loaded inventory data

    treasures = [item for item in inventory["items"] if item["type"] == "treasure" and item["quantity"] > 0] #This will scan the list of items in the inventory and create a new list of only treasure items that have a quantity greater than 0 to be used by the store

    if not treasures:
        print("You have no treasure to sell.")
        return #if there are no treasures found, the function will exit here

    choice = input("Do you want to sell all your owned treasure? (y/n): ").lower() #this asks for user input to confirm selling treasures, the lower function makes it case insensitive
    if choice != "y": #if the user does not input 'y', the function will exit here
        print("You leave the store without selling.")
        return

    total_coins_earned = 0 #creating the variable for the amount of coins earned from the transaction

    for item in inventory["items"]: #this loop goes through each item in the inventory
        if item["type"] == "treasure" and item["quantity"] > 0: #if the item is marked as a treasure and has a quantity greater than 0 the following code will run
            sale = item["value"] * item["quantity"] #this variable will be the total sale amount for that item based on its value and quantity
            total_coins_earned += sale #this adds the sale value to the total coins earned
            print(f"Sold {item['quantity']} {item['name']} for {sale} gold.") #This is a confirmation message showing the user what happened.
            item["quantity"] = 0   # This wil reduce the quantity of the sold treasures to 0

    inventory["coins"] += total_coins_earned #This will add the total coins earned to the users overeall coin balance for the game

    save_inventory(inventory) #this runs the previously created function to update the inventory JSON file with the new data

    print(f"\nTotal coins earned: {total_coins_earned}") #This prints the total coins earned from the transaction
    print(f"Coins owned: {inventory['coins']}") #This prints the total coins owned after the transaction

sell_treasure()