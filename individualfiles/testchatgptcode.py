# Weapon class
class Weapon:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def __str__(self):
        return f"{self.name} - Damage: {self.damage} - Cost: {self.cost} coins"

# Define the Potion class for healing potions
class Potion:
    def __init__(self, name, healing_amount, cost):
        self.name = name
        self.healing_amount = healing_amount
        self.cost = cost

    def __str__(self):
        return f"{self.name} - Heals {self.healing_amount} HP - Cost: {self.cost} coins"

# User class (with inventory and action choices)
class User:
    def __init__(self, name, HP, money, inventory):
        self.name = name
        self.HP = HP
        self.money = money
        self.inventory = inventory  # List of items the user owns

    def __str__(self):
        return f"Name: {self.name}, HP: {self.HP}, Money: {self.money}, Inventory: {self.inventory}"

    def attack(self, weapon, enemy):
        """Attack using the selected weapon."""
        damage = weapon.damage
        print(f"{self.name} attacks {enemy.name} with {weapon.name} for {damage} damage.")
        enemy.take_damage(damage, self)

    def heal(self):
        """Use a healing potion if available in inventory."""
        healing_potion = next((item for item in self.inventory if isinstance(item, Potion)), None)
        
        if healing_potion:
            self.HP += healing_potion.healing_amount
            self.inventory.remove(healing_potion)  # Remove the potion from inventory after use
            print(f"{self.name} used a {healing_potion.name}. Healed for {healing_potion.healing_amount} HP. Current HP: {self.HP}")
        else:
            print(f"{self.name} has no healing potions in their inventory!")

# Enemy class
class Enemy:
    def __init__(self, name, HP, attack, coin_drop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.coin_drop = coin_drop

    def take_damage(self, damage, user):
        self.HP -= damage
        print(f"{self.name} takes {damage} damage. Remaining HP: {self.HP}")
        if self.HP <= 0:
            self.defeat(user)

    def defeat(self, user):
        print(f"{self.name} was defeated!")
        user.money += self.coin_drop
        print(f"{user.name} earned {self.coin_drop} coins. Total money: {user.money}")

    def attack_user(self, user):
        print(f"{self.name} attacks {user.name} for {self.attack} damage.")
        user.HP -= self.attack
        print(f"{user.name} takes {self.attack} damage. Remaining HP: {user.HP}")


# Initialize some weapons and potions
stick = Weapon("Stick", 5, 0)
basic_sword = Weapon("Basic Sword", 8, 9)
silver_sword = Weapon("Silver Sword", 10, 16)

healing_potion = Potion("Healing Potion", 20, 5)  # Define a healing potion

# Initialize a user with inventory containing weapons and potions
player_inventory = [stick, basic_sword, silver_sword, healing_potion]  # Player starts with several weapons and potions
player = User("Hero", 100, 50, player_inventory)

# Initialize an enemy (Goblin)
goblin = Enemy("Goblin", 30, 7, 5)

# Battle sequence
def battle(user, goblin):
    while user.HP > 0 and goblin.HP > 0:
        goblin.attack_user(user)  # Goblin attacks first

        if user.HP <= 0:
            print(f"{user.name} has been defeated!")
            break

        print("\nYour turn!")
        print("Choose a weapon:")
        
        # Display the available weapons in the player's inventory
        for item in user.inventory:
            if isinstance(item, Weapon):  # Only display weapons
                print(f"- {item.name} (Damage: {item.damage})")
        
        # Get the user's weapon choice by name
        valid_weapon = False
        while not valid_weapon:
            weapon_name = input("Enter the weapon name to use: ")
            
            # Check if the entered weapon is in the inventory
            selected_weapon = next((item for item in user.inventory if isinstance(item, Weapon) and item.name.lower() == weapon_name.lower()), None)
            
            if selected_weapon:
                valid_weapon = True
                print(f"You have selected {selected_weapon.name}.")
                action_choice = input("Choose an action (1 for Attack, 2 for Heal): ")

                if action_choice == "1":
                    user.attack(selected_weapon, goblin)  # User attacks using selected weapon
                elif action_choice == "2":
                    user.heal()  # Attempt to heal using a potion
                else:
                    print("Invalid option. Please choose 1 or 2.")
            else:
                print(f"{weapon_name} is not in your inventory. Please choose a valid weapon.")

        if goblin.HP <= 0:
            print(f"{goblin.name} has been defeated!")
            break

        # Goblin attacks back if still alive
        print("\n--- Goblin's Turn ---")

# Start the battle
battle(player, goblin)
