import csv

INVENTORY_FILE = "inventory.csv"
MAX_INVENTORY_SIZE = 15


class Inventory:
    def __init__(self):
        self.items = []
        self._load_inventory()

    def _load_inventory(self):
        try:
            with open(INVENTORY_FILE, newline="") as file:
                reader = csv.reader(file)
                self.items = [row[0] for row in reader if row]
        except FileNotFoundError: #if inventory file does not exist it gets created
            self.items = []
            self._save_inventory()

    def _save_inventory(self):
        with open(INVENTORY_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            for item in self.items:
                writer.writerow([item])

    def add_item(self, item): #attempts to add an item to the inv. returns true if successful, false if inventory is full
        if len(self.items) >= MAX_INVENTORY_SIZE:
            return False

        self.items.append(item)
        self._save_inventory()
        return True

    def remove_item(self, item):#removes an item from the inv. returns true if the item was removed
      
        if item not in self.items:
            return False

        self.items.remove(item)
        self._save_inventory()
        return True

    def has_item(self, item):#checks whether the inv has an item
        return item in self.items
    
    def get_items(self):  
        return list(self.items)#returns copy of inv list

    def is_full(self):
        return len(self.items) >= MAX_INVENTORY_SIZE#teturns true if inv has reached its max size
