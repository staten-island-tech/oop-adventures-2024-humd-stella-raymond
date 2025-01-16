#IMPORTS
import time
import pygame
import random

pygame.init()  
pygame.mixer.init()  

#MUSIC
def play_music_for_day_one():
    # This function will play the music once the user has started the game
    pygame.mixer.music.load("dayoneaudio.ogg")  # Replace with the name of your music file
    
    pygame.mixer.music.set_volume(0.3)

    pygame.mixer.music.play(-1, 0.0)
    time.sleep(2)

def play_music_for_day_two():
    # This function will play the music once the user has started the game
    pygame.mixer.music.load("daytwoaudio.ogg")  # Replace with the name of your music file
    
    pygame.mixer.music.set_volume(0.3)

    pygame.mixer.music.play(-1, 0.0)
    time.sleep(2)

#CLASSES
class enemy:
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

Goblin = enemy("Goblin",20,7,5)
Zombie = enemy("Zombie",30,10,8)
Skeleton = enemy("Skeleton",35,13,9)
Plant = enemy("Plant",45,25,18)
Wolf = enemy("Wolf",50,32,25)
Mage = enemy("Mage",60,50,40)
Knight = enemy("Knight",75,40,45)
EvilKing = enemy("Evil King",125, 65, 0)

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
healing_potion = Potion("Healing Potion", 20, 5)

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
        user.money = self.sell(item, user.money)
        user.inventory.append(item)
        print("Your Inventory")
        for item in user.inventory:
            print(item)
        
class User:
    def __init__(self, name, HP, money):
        self.name = name
        self.HP = HP
        self.money = money
        self.inventory = []

    def __str__(self):
        return f"Name: {self.name}, HP: {self.HP}, Money: {self.money}, Inventory: {self.inventory}"

    def buy(self, item):
        if self.money >= item.cost:
            self.inventory.append(item)
            self.money -= item.cost
            print(f"Bought {item.name}. Inventory: {self.inventory}")
        else:
            print("Not enough money to buy this item.")
    
    def attack(self, weapon, enemy):
        damage = weapon.damage
        print(f"{self.name} attacks {enemy.name} with {weapon.name} for {damage} damage.")
        enemy.take_damage(damage, self)

    def heal(self):
        healing_potion = next((item for item in self.inventory if isinstance(item, Potion)), None)
        
        if healing_potion:
            self.HP += healing_potion.healing_amount
            self.inventory.remove(healing_potion)  # Remove the potion from inventory after use
            print(f"{self.name} used a {healing_potion.name}. Healed for {healing_potion.healing_amount} HP. Current HP: {self.HP}")
        else:
            print(f"{self.name} has no healing potions in their inventory!")

    def die(self):
        if self.HP <= 0:
            print(f"\n{self.name} has died.")
            print("Game Over!")
        restart_choice = input("Would you like to restart the game? (yes/no): ").lower()
        if restart_choice == "yes":
            game_loop()
        else:
            print("Goodbye!")
            return

#BATTLING:
def battle(user, Goblin):
    while user.HP > 0 and Goblin.HP > 0:
        Goblin.attack_user(user) 
        if user.HP <= 0:
            user.die()
            break

        print("Your turn!")
        print("Choose a weapon:")
        
        for item in user.inventory:
            if isinstance(item, Weapon): 
                print(f"- {item.name} (Damage: {item.damage})")
        
        valid_weapon = False
        while not valid_weapon:
            weapon_name = input("Enter the weapon name to use: ")
            
            selected_weapon = next((item for item in user.inventory if isinstance(item, Weapon) and item.name.lower() == weapon_name.lower()), None)
            
            if selected_weapon:
                valid_weapon = True
                print(f"You have selected {selected_weapon.name}.")
                action1 = input("Choose an action (1 for Attack, 2 for Heal): ")

                if action1 == "1":
                    user.attack(selected_weapon, Goblin)  
                elif action1 == "2":
                    user.heal() 
                else:
                    print("Invalid option. Please choose 1 or 2.")
            else:
                print(f"{weapon_name} is not in your inventory. Please choose a valid weapon.")

        if Goblin.HP <= 0:
            print(f"{Goblin.name} has been defeated!")
            break

        print("\n--- Goblin's Turn ---")

#SHOP, MAIN MENU, AND IMPORTANT THINGS:
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

def activate_menu(user,merchant):
    while True: 
        activation = input("Press M if you would like to access the main menu at this point. Press X to exit.").capitalize()
        if activation == "M":
            main_menu(user, merchant)
        elif activation == "X":
            break
        else:
            break

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
        elif choice == "E": 
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

def start_shop(user, merchant):
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
                print("Invalid. Please try again.")
                continue

            # Buy the item and update the user’s balance
            merchant.buy_item(user, item_idx)

        except ValueError:
            print("Please enter a valid number.")

merchant = Merchant(items=[stick, basic_sword, silver_sword, basic_scythe, magic_wand, undead_scythe, staff, holy_staff, celestial_blade, healing_potion,])

def login():
    name = input("Enter your username: ")
    password = input("Enter your password: ") 
    
    user = User(name=name, HP=100, money=0)
    
    print(f"Welcome to GAME NAME, {user.name}!")
    return user

def start_game():
    print("Starting the game...")
    for i in range(3): 
        time.sleep(0.5)  
        print("☘︎",".", end="", flush=True) 

def loading():
    for i in range(3): 
        time.sleep(0.4)  
        print("☘︎", ".", end="", flush=True) 
    print()

#MINIGAMES:

def collect_wood_logs(user):
    required_logs = 5  # Need 5 logs of wood
    collected_logs = 0

    print("\nYou need to collect 5 logs of wood to build the shelter! You have 3 seconds for each one.")

    while collected_logs < required_logs:
        print(f"\nYou have {collected_logs} logs. {required_logs - collected_logs} more to go.")
        print("Press 'L' to collect a log of wood!")
        
        # Start time for reaction
        start_time = time.time()

        # Wait for the player to input the correct key
        user_input = input("Press 'L': ").lower()

        # Check if the correct key is pressed within 3 seconds
        if user_input == 'l' and time.time() - start_time < 3:
            collected_logs += 1
            print("Good job! You collected a log.")
        else:
            print("You missed! Try again.")

    print(f"\nYou collected {collected_logs} logs of wood! The shelter is now ready.")

def number_guess_game(user):
    print("Merchant: Okay. I'm thinking of a number between 1 and 15. You have 5 chances to get it right. If you get the number right, I'll give you 10 coins!")
    answer = random.randint(1, 15)
    chances = 5
    while chances > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Please enter your guess: "))
            if guess < 1 or guess > 15:
                print("Please guess a number between 1 and 15.")
                continue
            if guess == answer:
                print(f"Congratulations! You guessed the correct number {answer}!")
                user.money += 10
                print(f"Your Coins: {user.money}")
                break
            else:
                print("Wrong guess! Try again.")
                attempts -= 1
        
        except ValueError:
            print("Invalid input! Please enter a number.")

    if attempts == 0:
        print(f"Sorry! You've run out of attempts. The correct number was {answer}.")

#STORY:
def dayone(user):
    time.sleep(1)
    print("You wake up in a quiet forest. What happened? You can't remember...")

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
            print ('Merchant: Our village was burnt down by the evil king. We have been hiding out in the nearby bright forest, and we found you here.')
            time.sleep(2)
            print('Wizard: The evil king burnt the village down since we refused to give him gold. We need your help to stop him. Take this stick to start out.')
            break
        
        else:
            print("Invalid! Try again!")
    
    time.sleep(0.8)
    print(f"{user.name} has received a stick!")
    user.inventory.append(stick)
    time.sleep(0.8)
    print ('INSTRUCTION: You can check your inventory in the menu. This lets you see potions, armor, and weapons.')
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
    user.money += 6
    print(f"{user.name} has received 6 coins!")
    time.sleep(2)
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
    story_menu_choice = input("Press M to see the Main Menu:"). capitalize()

    while True:
        if story_menu_choice == "M":
            tutorial_main_menu(user, merchant)
            break
        else:
            print("Invalid! Try again!")
    
    time.sleep(1)
    print("Merchant: Here's the potions I promised you. During battles, you can use potions to heal.")
    for i in range(3):
        user.inventory.append(healing_potion)
    time.sleep(2)
    print(f"{user.name} has received 3 potions!")
    time.sleep(0.3)
    
    while True:
        choice5 = input("Check your inventory once more. (press i)").capitalize()
        if choice5 == "I":
            print("Your Inventory")
            for item in user.inventory:
                print(item)
            break
        else:
            print("Invalid! Try again!")

    time.sleep(2)
    print("Wizard: Now, we have to pass through a few areas to get to the Evil King. The Swamp, The Abandoned Village, The Dark Forest, and finally, the King's palace!")
    time.sleep(3)
    print("Merchant: Now let's make a shelter. Collect 5 logs of wood to help us.")
    time.sleep(2)
    print("Minigame starting...")
    loading()
    collect_wood_logs(user)
    
    loading()
    print("Merchant: Great job! Now we can sleep for the night.")
    time.sleep(1)
    loading()
    print(f"Congrats! {user.name} has gone through Day One!")
    user.inventory.append(healing_potion)
    time.sleep(2)
    print(f"{user.name} has received a healing potion!")
    time.sleep(2)
    print("Your Inventory")
    for item in user.inventory:
        print(item)
    time.sleep(1)
    print("to be continued...")
    loading()
    
def daytwo(user):
    print("You wake up in the morning, coming out of the shelter. It's sunny outside.")
    time.sleep(1)
    print(f"Merchant: {user.name}, are you ready to leave for the swamp?")
    while True:
        choice6 = input(" 1) Yes! Let's go! 2) No... I need to pack.").capitalize()
        if choice6 == "1":
            time.sleep(1.3)
            print("Yes! Let's go! You say.")
            time.sleep(0.8)
            print ('Merchant: First stop, the Swamp!')
            time.sleep(2)
            print ('Wizard: Be careful. There are goblins here. You can use your stick to attack them now.')
            break

        elif choice6 == "2":
            time.sleep(2)
            print('Merchant: Hurry and pack everything!')
            time.sleep(0.8)
            print ('Wizard: We must leave for the Swamp soon! Make sure to bring your stick. There are goblins here.')
            time.sleep(2)
            print('You pack your bags quickly. Soon enough, you are ready to go!')
            break
        
        else:
            print("Invalid! Try again!")

    print("INSTRUCTION: Each zone has different enemies. There are only goblins around the Swamp. One can potentially attack at any time.")
    time.sleep(1)
    print("Wizard: Okay, we just need to get through this area without being attacked...")
    time.sleep(2)
    print(f"Merchant: {user.name}! Watch out!")
    time.sleep(1)
    print("Wizard: Nevermind.")
    time.sleep(1)
    print("You've been attacked by a goblin!")
    time.sleep(1)
    print("INSTRUCTION: This is a battle! Enter the weapon in your inventory you'd like to use, and attack. Healing potions allow you to heal during battles, but take up your turn. \nStrategize wisely!")
    loading()
    battle(user, Goblin)
    loading()
    print("Merchant: Wow! You got more coins. Try to check the shop, see if you can get something new!")
    activate_menu(user,merchant)
    loading()
    print("Wizard: Okay, let's keep going.")
    time.sleep(1)
    print("Merchant: Yikes, there's a lot of goblins. Might have to battle some more.")
    time.sleep(1)
    print("Wizard: We just have to pull through though. We need to defeat the evil king after all.")
    time.sleep(1)
    print("You suddenly hear some water splashing.")

    while True:
        choice7 = input("Will you choose to investigate? Yes or no?").capitalize()
        if choice7  == "Yes":
            loading()
            time.sleep(2)
            print("You look around, and slowly move closer to the area behind one of the trees.")
            time.sleep(0.8)
            Goblin.HP = 20
            print("A goblin scares you! You've been attacked!!")
            battle(user, Goblin) 
            break
        elif choice7 == "No":
            loading()
            time.sleep(2)
            print("You choose to continue walking forward.")
            break
        else: 
            print("Invalid! Try again.")
    
    activate_menu(user,merchant)
    time.sleep(1)
    print("Wizard: These Goblins are all over the place.")
    time.sleep(2)
    print(f"Merchant: This is kind of boring, {user.name}.")
    choice8 = input("Merchant: Would you like to play a game? Yes, or no?").capitalize()
    while True:
        if choice8  == "Yes":
            print("Minigame starting...")
            loading()
            time.sleep(2)
            number_guess_game(user)
            break
        elif choice8 == "No":
            Goblin.HP = 20
            print("Instead of playing a game with the Merchant, you walk forward on your own. Suddenly, a goblin surprises you!")
            battle(user, Goblin)
            break
        elif choice7 == "No" and choice8 == "Yes":
            Goblin.HP = 20
            print("The merchant changed his mind, and played with the wizard instead.")
            print("You ended up walking around the swamp on your own, and suddenly got ambushed by a goblin!!")
            battle(user,Goblin)
        else: 
            print("Invalid! Try again.")
    
    print("Wizard: We're finally out of the swamp!")
    time.sleep(1)
    print(f"Congrats! {user.name} has gone through Day Two!")
    user.inventory.append(healing_potion)
    time.sleep(2)
    print(f"{user.name} has received a healing potion!")
    time.sleep(1)
    print(f"The wizard has healed {user.name}!")
    user.HP = 100
    time.sleep(2)
    print("Your Inventory")
    for item in user.inventory:
        print(item)
    print(f"Your HP: {user.HP}")
    time.sleep(1)
    print("to be continued...")
    loading()
    
#GENERAL:
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
            dayone(user)
            pygame.mixer.music.stop()
            print("DAY TWO")
            play_music_for_day_two()
            daytwo(user)
            break
        elif choice1 == "no":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    game_loop()