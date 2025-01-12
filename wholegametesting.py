import time
import pygame

pygame.init()  # Initialize all pygame modules
pygame.mixer.init()  # Initialize mixer


def play_music_for_day_one():
    # This function will play the music once the user has started the game
    pygame.mixer.music.load("audio-_1_.ogg")  # Replace with the name of your music file
    
    pygame.mixer.music.set_volume(0.3)

    pygame.mixer.music.play(-1, 0.0)
    time.sleep(2)

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
        print("6. Check your HP (Press 'H')")

        choice = input("Please enter your choice: ").capitalize()

        if choice == "I":
            print(f"\nYour Inventory: {user.inventory}")
        elif choice == "S":  
            start_shop(user, merchant) 
        elif choice == "C":
            print(f"\nYour Coins: {user.money}")
        elif choice == "E":  # Exit the game
            loading()
            print("Goodbye!")
            break
        elif choice == "G": 
            print("continuing...")
            break
        elif choice == "H":
            print(f"Your HP: {user.HP}")
        else:
            print("Invalid choice. Please try again.")

def tutorial_main_menu(user, merchant):
    while True:
        print("\nHere's an example of the main menu.")
        print("\nWhat would you like to do?")
        print("1. View inventory (Press 'I')")
        print("2. Go to the shop (Press 'S')")
        print("3. Check your coins (Press 'C')")
        print("4. Exit the game (Press 'E')")
        print("5. Go back to the story (Press 'G')")
        print("6. Check your HP (Press 'H')")

        choice = input("For now, enter the letter G to continue the story.").capitalize()

        if choice == "G": 
            print("continuing...")
            loading()
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
silver_sword = Weapon("Silver Sword", 10, 16, crit_chance=20)
basic_scythe = Weapon("Basic Scythe", 14, 20, crit_chance=23)
magic_wand = Weapon("Magic Wand", 20, 40, crit_chance=26)
undead_scythe = Weapon("Undead Scythe", 23, 55, crit_chance=29)
staff = Weapon("Staff", 28, 86, crit_chance=32)
holy_staff = Weapon("Holy Staff", 36, 130, crit_chance=35)
celestial_blade = Weapon("Celestial Blade", 47, 200, crit_chance=38)
healing_potion = Potion("Healing Potion", 20, 5)
basic_armor = "Basic Armor"  # Example armor (no class needed for simplicity)

# Create the Merchant with all items
merchant = Merchant(items=[stick, basic_sword, silver_sword, basic_scythe, magic_wand, undead_scythe, staff, holy_staff, celestial_blade, healing_potion, basic_armor])


def login():
    name = input("Enter your username: ")
    password = input("Enter your password: ")  # Password is not being validated here
    
    user = User(name=name, HP=100, money=0, attack=10)
    
    print(f"Welcome to GAME NAME, {user.name}!")
    return user

def start_game():
    print("Starting the game...")
    for i in range(3): 
        time.sleep(0.5)  
        print("☘︎",".", end="", flush=True) 
    # game logic

def loading():
    for i in range(3): 
        time.sleep(0.4)  
        print("☘︎", ".", end="", flush=True) 
    print()

def story(user):
    time.sleep(1)
    print("You wake up in a dark and quiet forest. What happened? You can't remember...")

    time.sleep(2)
    print("There's suddenly a loud sound of leaves rustling!")

    time.sleep(0.8)

    while True:
        choice2 = input("Will you choose to investigate? Yes or no?").capitalize()

        if choice2 == "Yes":
            loading()
            time.sleep(2)
            print("You look around. In the bushes, there's something moving.")
            time.sleep(0.8)
            print ("Suddenly, a figure comes out, but it's familiar...")
            break
        elif choice2 == "No":
            loading()
            time.sleep(2)
            print("You choose to stay down on the ground. Suddenly, you hear something getting closer!")
            time.sleep(0.8)
            print ("You screamed in fear as it scared you from behind! But you recognized who they were...")
            break
        else: 
            print("Invalid! Try again.")
    
    time.sleep(2)
    print("It's the wizard! Who lived in the village! And the Merchant!")

    time.sleep(2)

    while True:
        choice3 = input("You're still confused. What would you like to ask them? 1) What happened? 2) Where am I?").capitalize()
        if choice3 == "1":
            time.sleep(2)
            print('"What happened?" You ask.')
            time.sleep(0.8)
            print ('Merchant: Our village was burnt down by the evil king. They refused to give him extra money.')
            time.sleep(2)
            print ('Wizard: The king becomes more evil day by day. We need your help to stop him. Take this stick to start out.')
            break

        elif choice3 == "2":
            time.sleep(2)
            print('"Where am I?" You ask.')
            time.sleep(0.8)
            print ('Merchant: Our village was burnt down by the evil king. We have been hiding out in the dark forest, and we found you here.')
            time.sleep(2)
            print('Wizard: The evil king burnt the village down since we refused to give him gold. We need your help to stop him. Take this stick to start out.')
            break
        
        else:
            print("Invalid! Try again!")
    
    time.sleep(0.8)
    user.inventory.append(stick)
    print ('INSTRUCTION: You can check your inventory any time after the story is over in the options. This lets you see potions, armor, and weapons.')
    time.sleep(2)
    while True:
        choice4 = input("Press I to see your inventory").capitalize()
        if choice4 == "I":
            print("Your Inventory")
            for item in user.inventory:
                print(item)
            break
        else:
            print("Invalid! Try again!")


    time.sleep(2)
    print("Merchant: Take some coins and potions too.")
    time.sleep(2)
    print("INSTRUCTION: You can always buy some weapons or potions to heal.Enemies in each zone drop coins.")
    user.money += 20
    print_money = input("Press C to show your coins.").capitalize() 
    while True:
        if print_money == "C":
            print(f"Your Coins: {user.money}")
            break
        else:
            print("Invalid! Try again!")
    
    time.sleep(3)
    print("INSTRUCTION: In the future, you'll be able to access these options through the Main Menu between parts of the story. Try it now.")
    time.sleep(0.8)
    story_menu_choice = input("Press M to see the Main Menu"). capitalize()

    while True:
        if story_menu_choice == "M":
            tutorial_main_menu(user, merchant)
            break
        else:
            print("Invalid! Try again!")
    
    time.sleep(1.0)
    print("Merchant: Here's the potions I promised you. During battles, you can use potions to heal.")
            
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
            loading()
            play_music_for_day_one()
            print("DAY ONE") 
            story(user)
            break
        elif choice1 == "no":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    game_loop()
