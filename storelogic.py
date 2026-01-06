import json

def load_pouch(): #This function loads the treasure pouch from a JSON file
    with open("treasure_pouch.json", "r") as file:
        return json.load(file)

def save_pouch(pouch): #This function will update the treasure pouch JSON file
    with open("treasure_pouch.json", "w") as file:
        json.dump(pouch, file, indent=4)

def sell_treasure(): #This is the main function to sell treasure items
    pouch = load_pouch() #setting the variable pouch to the loaded pouch data

    treasures = [item for item in pouch["items"] if item["type"] == "treasure" and item["quantity"] > 0] #This will scan the list of items in the pouch and create a new list of only treasure items that have a quantity greater than 0 to be used by the store

    if not treasures:
        print("You have no treasure to sell.")
        return #if there are no treasures found, the function will exit here

    choice = input("Do you want to sell all your owned treasure? (y/n): ").lower() #this asks for user input to confirm selling treasures, the lower function makes it case insensitive
    if choice != "y": #if the user does not input 'y', the function will exit here
        print("You leave the store without selling.")
        return

    total_coins_earned = 0 #creating the variable for the amount of coins earned from the transaction

    for item in pouch["items"]: #this loop goes through each item in the pouch
        if item["type"] == "treasure" and item["quantity"] > 0: #if the item is marked as a treasure and has a quantity greater than 0 the following code will run
            sale = item["value"] * item["quantity"] #this variable will be the total sale amount for that item based on its value and quantity
            total_coins_earned += sale #this adds the sale value to the total coins earned
            print(f"Sold {item['quantity']} {item['name']} for {sale} gold.") #This is a confirmation message showing the user what happened.
            item["quantity"] = 0   # This wil reduce the quantity of the sold treasures to 0

    pouch["coins"] += total_coins_earned #This will add the total coins earned to the users overeall coin balance for the game

    save_pouch(pouch) #this runs the previously created function to update the treasure pouch JSON file with the new data

    print(f"\nTotal coins earned: {total_coins_earned}") #This prints the total coins earned from the transaction
    print(f"Coins owned: {pouch['coins']}") #This prints the total coins owned after the transaction
