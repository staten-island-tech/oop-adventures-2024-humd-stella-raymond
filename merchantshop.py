class Potion:
    def __init__(self, name, healing_amount, cost):
        self.name = name
        self.healing_amount = healing_amount
        self.cost = cost

    def __str__(self):
        return f"{self.name} - Heals {self.healing_amount} HP - Cost: {self.cost} coins"
    
class Weapon:
    def __init__(self, name, damage, cost, crit_chance=None):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.crit_chance = crit_chance  

    def __str__(self):
        crit_info = f" - Crit Chance: {self.crit_chance}" if self.crit_chance else ""
        return f"{self.name} - Damage: {self.damage} - Cost: {self.cost} coins{crit_info}"

stick = Weapon("Stick", 5, 0)  
basic_sword = Weapon("Basic Sword", 8, 9)
silver_sword = Weapon("Silver Sword", 10, 16, crit_chance=20)
basic_scythe = Weapon("Basic Scythe", 14, 20, crit_chance=23)
magic_wand = Weapon("Magic Wand", 20, 40, crit_chance=26)
undead_scythe = Weapon("Undead Scythe", 23, 55, crit_chance=29)
staff = Weapon("Staff", 28, 86, crit_chance=32)
holy_staff = Weapon("Holy Staff", 36, 130, crit_chance=35)
celestial_blade = Weapon("Celestial Blade", 47, 200, crit_chance=38)

class Merchant:
    def __init__(self, items):
        self.items = items  # List of all items (weapons, potions, armor, etc.)
    
    def sell(self, item, user_balance):
        """Sell an item to the user if they can afford it."""
        if user_balance >= item.cost:
            user_balance -= item.cost
            print(f"You have purchased {item.name} for {item.cost} coins.")
            print(f"Your remaining balance is {user_balance} coins.")
            return user_balance
        else:
            print("You do not have enough coins to purchase this item.")
            return user_balance

    def show_shop(self):
        """Display the available items in the merchant's shop."""
        print("\nWelcome to the Merchant's Shop! Here are the available items:\n")
        
        for idx, item in enumerate(self.items):
            print(f"{idx + 1}. {item}")

    def buy_item(self, user, item_idx):
        """Allows the user to buy an item based on the index."""
        item = self.items[item_idx]
        # Sell the item to the user and update their balance
        user.money = self.sell(item, user.money)
        user.inventory.append(item)
        print(f"Your inventory: {user.inventory}")
        

class User:
    def __init__(self, name, HP, money, attack):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money
        self.inventory = []

    def __str__(self):
        return f"Name: {self.name}, HP: {self.HP}, Money: {self.money}, Attack: {self.attack}, Inventory: {self.inventory}"

    def buy(self, item):
        if self.money >= item.cost:
            self.inventory.append(item)
            self.money -= item.cost
            print(f"Bought {item.name}. Inventory: {self.inventory}")
        else:
            print("Not enough money to buy this item.")

    def heal(self, amount):
        self.HP += amount
        print(f"{self.name} healed! Current HP: {self.HP}")


def start_shop(user, merchant):
    """A simple shop interaction where the user can buy items from the merchant."""
    while True:
        # Show available items
        merchant.show_shop()

        # Get user input for selection
        try:
            item_idx = int(input(f"Enter the number of the item to buy, or '0' to exit: ")) - 1
            if item_idx == -1:
                print("Exiting shop...")
                break

            if item_idx < 0 or item_idx >= len(merchant.items):
                print("Invalid selection. Please try again.")
                continue

            # Buy the item and update the user’s balance
            merchant.buy_item(user, item_idx)

        except ValueError:
            print("Please enter a valid number.")

class Weapon:
    def __init__(self, name, damage, cost, crit_chance=None):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.crit_chance = crit_chance  

    def __str__(self):
        crit_info = f" - Crit Chance: {self.crit_chance}" if self.crit_chance else ""
        return f"{self.name} - Damage: {self.damage} - Cost: {self.cost} coins{crit_info}"

def main_menu(user, merchant):
    while True:
        print("\nWhat would you like to do?")
        print("1. View inventory (Press 'I')")
        print("2. Go to the shop (Press 'S')")
        print("3. Check your coins (Press 'C')")
        print("4. Exit the game (Press 'E')")
        print("5. Go back to the story (Press 'G')")

        choice = input("Please enter your choice: ").capitalize()

        if choice == "I":
            print(f"\nYour Inventory: {user.inventory}")
        elif choice == "S":  
            start_shop(user, merchant) 
        elif choice == "C":
            print(f"\nYour Coins: {user.money}")
        elif choice == "E":  # Exit the game
            print("Goodbye!")
            break
        elif choice == "G": 
            print("continuing...")
            break
        else:
            print("Invalid choice. Please try again.")

# Shop-related code remains the same
def start_shop(user, merchant):
    """A simple shop interaction where the user can buy items from the merchant."""
    while True:
        # Show available items
        merchant.show_shop()

        # Get user input for selection
        try:
            item_idx = int(input(f"Enter the number of the item to buy, or '0' to exit: ")) - 1
            if item_idx == -1:
                print("Exiting shop...")
                break

            if item_idx < 0 or item_idx >= len(merchant.items):
                print("Invalid selection. Please try again.")
                continue

            # Buy the item and update the user’s balance
            merchant.buy_item(user, item_idx)

        except ValueError:
            print("Please enter a valid number.")

# Example Setup
stick = Weapon("Stick", 5, 0)
basic_sword = Weapon("Basic Sword", 8, 9)
healing_potion = Potion("Healing Potion", 20, 5)
basic_armor = "Basic Armor"  # Example armor (no class needed for simplicity)

# Create the Merchant with all items
merchant = Merchant(items=[stick, basic_sword, healing_potion, basic_armor])

# Create a user with initial money and health
user = User(name="Hero", HP=100, money=50, attack=10)

# Start the main menu interaction
main_menu(user, merchant)