""" #Classes:
Merchant (button on the side)
Inventory = (weapons, potions w/ effects, armor)

#Weapons:
Better weapons grow in price (when you buy a new weapon, old weapon is deleted)
(with every weapon the chance to get a crit becomes higher)
Spawn in with a stick - 5 hp
Basic Sword - 8 hp - 9 coins
Silver Sword - 10 hp - 16 coins - crits start 20%
Basic Scythe - 14 hp - 20 coins? - crit chance 23%
Magic Wand- 20 hp - 40 coins- crit chance 26%
Undead Scythe - 23 hp - 55 coins - crit chance 29%
Staff - 28 hp - 86 coins - crit chance 32%
Holy Staff - 36 hp - 130 coins - crit chance 35%
Celestial Blade- 47 hp - 200 coins - crit chance 38%
	

Weapons 
Attack (turnbased)
Critical Hit (guess the number correctly)(2x weapon attack) 1-3 range
Guess number to avoid attack - every 2 turns - 1-7 range
User
HP: 100 - heal at each town
Inventory
8 types of Enemies split across 4 areas
Slimes: 15 HP - 5 damage/hit - 3 coins
Goblins : 20 HP - 7 damage/hit - 4 coins
Zombies: 30 HP - 10 damage/hit -  8 coins
Skeletons: 35 HP - 13 damage/hit - 9 coins
Carnivorous plant 45 HP - 25 damage/hit  - 18 coins
Wolves: 50 HP - 32 damage/hit - 25 coins
Mages: 60 HP - 50 damage/hit - 40 coins
Knight: 75 HP - 40 damage/hit - 45 coins 


 """

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

def printing_inventory_story(user):
    print_inventory = input("Press I to show your inventory.").capitalize()
    while True:
        if print_inventory == "I":
            print("Your Inventory:")
            for item in user.inventory:
                print(f"{item.name} - Damage: {item.damage}")
            break
        else:
            print("Invalid! Try again!")

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
    choice3 = input("You're still confused. What would you like to ask them? 1) What happened? 2) Where am I?").capitalize()

    while True:
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
    
    time.sleep(0.8)
    user.inventory.append(stick)
    print ('INSTRUCTION: You can check your inventory any time after the story is over in the options. This lets you see potions, armor, and weapons.')
    time.sleep(2)
    printing_inventory_story(user)

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
            print_money = input("Press C to show your coins.").capitalize()
            


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
