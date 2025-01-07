import time

class Merchant:
    def __init__(self, weapons, potions, armor, products):
        self.weapons = weapons
        self.potions = potions
        self.armor = armor
        self.products = products
    def sell(self, item, user_balance):
        item_cost = item["cost"]
        if user_balance >= item_cost:
            user_balance -= item_cost
            self.products.remove(item)
            print(f"You have purchased {item} for {item_cost} coins.")
            print(f"Your remaining balance is {user_balance} coins.")
            return user_balance
        else:
            print("You do not have enough coins to purchase this item.")
            return user_balance

weapons = {
    "Basic Sword": {"damage": 8, "cost": 9},
    "Silver Sword": {"damage": 10, "cost": 16, "crit chance": "20%"},
    "Basic Scythe": {"damage": 14, "cost": 20, "crit chance": "23%"},
    "Magic Wand": {"damage": 20, "cost": 40, "crit chance": "26%"},
    "Undead Scythe": {"damage": 23, "cost": 55, "crit chance": "29%"},
    "Staff": {"damage": 28, "cost": 86, "crit chance": "32%"},
    "Holy Staff": {"damage": 36, "cost": 130, "crit chance": "35%"},
    "Celestial Blade": {"damage": 47, "cost": 200, "crit chance": "38%"}
}

merchant = Merchant(
    weapons = weapons,
    potions = ["Healing Potion"],
    armor = ["Armor"],
    products = ["products"]
)

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
        if self.money >= item['price']: 
            self.inventory.append(item)
            self.money -= item['price']
            print(f"Bought {item['name']}. Inventory: {self.inventory}")
        else:
            print("Not enough money to buy this item.")

    def die(self):
        if self.HP <= 0:
            print(f"{self.name} has died!")
            self.inventory.clear() 
            self.money = 0
            return True
        else:
            return False

    def heal(self, amount):
        self.HP += amount
        print(f"{self.name} healed! Current HP: {self.HP}")

    def alive(self):
        return self.HP > 0


def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")  # Password is not being validated here
    
    user = User(name=name, HP=100, money=0, attack=10)
    
    print(f"Welcome to the game, {user.name}!")
    return user

def start_game():
    print("Starting the game...")
    for i in range(5): 
        time.sleep(0.5)  
        print(".", end="", flush=True) 
    # game logic

def game_loop():
    user = login()

    choice = input("Would you like to start the game? (yes to start, no to quit): ").lower()
    
    if choice == "yes":
        start_game()  
        print()
        print(f"{user.name}'s game has started.")
        print('Here is your user!')
        print(user)
    elif choice == "no":
        print("Exiting the game. Goodbye!")
    else:
        print("Invalid choice. Please try again")

if __name__ == "__main__":
    game_loop()