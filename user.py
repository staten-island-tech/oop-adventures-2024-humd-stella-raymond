class User:
    def __init__(self, name, max_health, gold=0):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.gold = gold
        self.inventory = {
            "weapons": [],
            "armor": [],
            "potions": [],
        }

    def modify_gold(self, amount):
        self.gold += amount
        print(f"Gold updated! Current gold: {self.gold}")

    def add_item(self, item_type, item):
        if item_type in self.inventory:
            self.inventory[item_type].append(item)
            print(f"Added {item} to {item_type}.")
        else:
            print("Invalid item type!")

    def use_potion(self):
        if self.inventory["potions"]:
            heal = self.inventory["potions"].pop(0)["heal"]
            self.current_health = min(self.max_health, self.current_health + heal)
            print(f"Used a potion! Restored {heal} HP. Health: {self.current_health}/{self.max_health}")
        else:
            print("No potions left!")

    def take_damage(self, amount):
        self.current_health = max(0, self.current_health - amount)
        status = "defeated" if self.current_health == 0 else f"{self.current_health}/{self.max_health} HP"
        print(f"Took {amount} damage. Current status: {status}")

    def display_inventory(self):
        print(f"\n{self.name}'s Inventory:")
        print(f"Gold: {self.gold}")
        print(f"Weapons: {[w.name for w in self.inventory['weapons']]}")
        print(f"Armor: {[a.name for a in self.inventory['armor']]}")
        print(f"Potions: {len(self.inventory['potions'])}\n")

    def __str__(self):
        return f"{self.name} - HP: {self.current_health}/{self.max_health}, Gold: {self.gold}"


# Main Menu
def main_menu(user):
    menu = {"M": user.display_inventory, "Q": lambda: print("Goodbye!")}
    while True:
        choice = input("\nEnter [M] for Inventory or [Q] to Quit: ").strip().upper()
        if choice in menu:
            menu[choice]()
            if choice == "Q":
                break
        else:
            print("Invalid choice!")
