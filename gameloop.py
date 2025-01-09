import time

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

class Weapon:
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
        if user_balance >= item.cost:
            user_balance -= item.cost
            self.products.remove(item)  
            print(f"You have purchased {item.name} for {item.cost} coins.")
            print(f"Your remaining balance is {user_balance} coins.")
            return user_balance
        else:
            print("You do not have enough coins to purchase this item.")
            return user_balance

merchant = Merchant
weapons = [stick, basic_sword, silver_sword],  # Add weapons to the merchant's stock
potions = ["Healing Potion"],
armor = ["Armor"],
products = [stick, basic_sword, silver_sword]  

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

def story(user):
    loading()
    time.sleep(1)
    print("You wake up in a dark and quiet forest. What happened? You can't remember...")

    loading()
    time.sleep(1)
    print("There's suddenly a loud sound of leaves rustling!")

    time.sleep(0.8)

    while True:
        choice2 = input("Will you choose to investigate? Yes or no?").capitalize()

        if choice2 == "Yes":
            loading()
            print("You look around. In the bushes, there's something moving.")
            time.sleep(0.8)
            print ("Suddenly, a figure comes out, but it's familiar...")
            break
        elif choice2 == "No":
            loading()
            print("You choose to stay down on the ground. Suddenly, you hear something getting closer!")
            time.sleep(0.8)
            print ("You screamed in fear as it scared you from behind! But you recognized who it was...")
            break
        else: 
            print("Invalid! Try again.")
    
    loading()
    time.sleep(1)
    print("It's the wizard! Who lived in the village! And the Merchant!")

    time.sleep(0.8)
    choice3 = input("You're still confused. What would you like to ask them? 1) What happened? 2) Where am I?").capitalize()

    while True:
        if choice3 == "1":
            loading()
            print('"Where am I?" You ask.')
            time.sleep(0.8)
            print ('Merchant: Our village was burnt down by the evil king. They refused to give him extra money.')
            time.sleep(2)
            print ('Wizard: The king becomes more evil day by day. We need your help to stop him. Take this stick to start out.')
            time.sleep(0.8)
            user.inventory.append(stick)
            print ('You can check your inventory any time after the story is over in the options.')
            time.sleep(2)
            print("Your Inventory:")
            for item in user.inventory:
                print(f"{item.name} - Damage: {item.damage}")
            break

        elif choice3 == "2":
            loading()
            print("You choose to stay down on the ground. Suddenly, you hear something getting closer!")
            time.sleep(0.8)
            print ("You screamed in fear as it scared you from behind! But you recognized who it was...")
            break
        else: 
            print("Invalid! Try again.")



def game_loop():
    user = login()
    while True:
        choice1 = input("Would you like to start the game? (yes to start, no to quit): ").lower()

        if choice1 == "yes":
            start_game()  
            print()
            print(f"{user.name}'s game has started.")
            print('Here is your user!')
            print(user)
            loading()
            print("Starting your story...")
            story(user)
            break
        elif choice1 == "no":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    game_loop()