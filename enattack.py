import random




class Weapon:
    def __init__(self, name, damage, price, critchance):
        self.name = name
        self.damage = damage
        self.price = price
        self.critchance = critchance

class Stick(Weapon):
    def __init__(self, name):
        super().__init__(name, 5, 0, 0)

class BasicSword(Weapon):
    def __init__(self, name):
        super().__init__(name, 8, 9, 0)

class SilverSword(Weapon):
    def __init__(self, name):
        super().__init__(name, 10, 16, 20)

class BasicScythe(Weapon):
    def __init__(self, name):
        super().__init__(name, 14, 20, 23)

class MagicWand(Weapon):
    def __init__(self, name):
        super().__init__(name, 20, 40, 26)

class UndeadScythe(Weapon):
    def __init__(self, name):
        super().__init__(name, 23, 55, 29)

class Staff(Weapon):
    def __init__(self, name):
        super().__init__(name, 28, 86, 32)

class HolyStaff(Weapon):
    def __init__(self, name):
        super().__init__(name, 36, 130, 35)

class CelestialBlade(Weapon):
    def __init__(self, name):
        super().__init__(name, 47, 200, 38)

class User:
    def __init__(self, name, HP, money, attack):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money
        self.inventory = []

    def add_to_inventory(self, weapon):
        self.inventory.append(weapon)
        print(f"{weapon.name} has been added to your inventory.")

    def has_weapon(self, weapon_name):
        for weapon in self.inventory:
            if weapon.name == weapon_name:
                return True
        return False

def battle(user):
    print("Welcome to the Battle Function!")

    print("\nYour Inventory: ")
    for weapon in user.inventory:
        print(f"- {weapon.name}")
    
    weapon_name = input("Enter the weapon you want to use (from your inventory): ")

    if not user.has_weapon(weapon_name):
        print("You do not have this weapon in your inventory.")
        return
    weapons = {
        "Stick": Stick("Stick"),
        "BasicSword": BasicSword("BasicSword"),
        "SilverSword": SilverSword("SilverSword"),
        "BasicScythe": BasicScythe("BasicScythe"),
        "MagicWand": MagicWand("MagicWand"),
        "UndeadScythe": UndeadScythe("UndeadScythe"),
        "Staff": Staff("Staff"),
        "HolyStaff": HolyStaff("HolyStaff"),
        "CelestialBlade": CelestialBlade("CelestialBlade")
    }
    selected_weapon = weapons[weapon_name]
    critchance = selected_weapon.critchance
    base_damage = selected_weapon.damage
    
    print(f"\nYou've selected {weapon_name}.")
    print(f"Critical Chance: {critchance}%. Base Damage: {base_damage}.")

    correct_number = random.randint(1, 100)
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 
    
    if user_guess == correct_number:
        random_chance = random.randint(1, 100)
        if random_chance <= critchance:
            damage = base_damage * 1.5
            print(f"Critical Hit! You guessed correctly! Final Damage: {damage}")
        else:
            damage = base_damage
            print(f"You guessed correctly but no critical hit. Damage: {damage}")
    else:
        print(f"Incorrect guess. The correct number was {correct_number}.")
        print(f"Your damage is: {base_damage}")

def main():

    user = User(name="Hero", HP=100, money=50, attack=10)

    user.add_to_inventory(Stick("Stick"))
    user.add_to_inventory(HolyStaff("HolyStaff"))

    battle(user)

if __name__ == "__main__":
    main()