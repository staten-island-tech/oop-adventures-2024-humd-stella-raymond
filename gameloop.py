import time

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
    
    user = User(name=name, HP=100, money=50, attack=10)
    
    print(f"Welcome to the game, {user.name}!")
    return user

def start_game():
    print("Starting the game...")
    for i in range(2): 
        time.sleep(1)  
        print(".", end="", flush=True) 
    # game logic

def game_loop():
    user = login()

    choice = input("Would you like to start the game? (yes to start, no to quit): ").lower()
    
    if choice == "yes":
        start_game()  
        print(f"{user.name}'s game has started.")
        print('Here is your user!')
        print(user)
    elif choice == "no":
        print("Exiting the game. Goodbye!")
    else:
        print("Invalid choice. Please try again")

if __name__ == "__main__":
    game_loop()