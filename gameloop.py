import time

""" class Weapon:
    def __init__(self, name, damage, cost, crit_chance=None):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.crit_chance = crit_chance  

    def __str__(self):
        crit_info = f" - Crit Chance: {self.crit_chance}" if self.crit_chance else ""
        return f"{self.name} - Damage: {self.damage} - Cost: {self.cost} coins{crit_info}"

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


merchant = Merchant(
    #weapons = ["weapon'],
    potions = ["Healing Potion"],
    armor = ["Armor"],
    products = ["products"]
) """

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
    
    print(f"Welcome to GAME NAME, {user.name}!")
    return user

def start_game():
    print("Starting the game...")
    for i in range(5): 
        time.sleep(0.5)  
        print(".", end="", flush=True) 
    # game logic

def loading():
    for i in range(3): 
        time.sleep(0.3)  
        print(".", end="", flush=True) 
    print()

def time_between():
    loading()
    time.sleep(1)

def story():
    time_between()
    print("You wake up in a dark and quiet forest. What happened? You can't remember...")

    time_between()
    print("There's suddenly a loud sound. BAM!")

    time.sleep(0.8)
    choice2 = input("Will you choose to investigate?").capitalize()

    if choice2 == "Yes":
        loading()
        print("You look around. In the bushes, there's something moving.")
        time.sleep(0.8)
        print ("Suddenly, a figure comes out, but it's familiar...")
    elif choice2 == "No":
        loading()
        print("You choose to stay down on the ground. Suddenly, you hear something getting closer!")
    else: 
        print("Invalid! Try again.")

def game_loop():
    user = login()

    choice1 = input("Would you like to start the game? (yes to start, no to quit): ").lower()
    Game = Not_started
    
    while Game == Not_started: 
        if choice1 == "yes":
            start_game()  
            print()
            print(f"{user.name}'s game has started.")
            print('Here is your user!')
            print(user)
            Game = started
            story()
        elif choice1 == "no":
            print("Exiting the game. Goodbye!")
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    game_loop()