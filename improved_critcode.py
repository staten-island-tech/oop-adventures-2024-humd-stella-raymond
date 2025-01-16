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
def battle():
    print("Welcome to the Battle Function!")
    weapon_name = input("Enter your weapon (Stick, BasicSword, SilverSword, BasicScythe, MagicWand, UndeadScythe, Staff, HolyStaff, CelestialBlade): ")
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
    if weapon_name not in weapons:
        print("Invalid weapon choice. Try again.")
        return battle()
    selected_weapon = weapons[weapon_name]
    critchance = selected_weapon.critchance
    base_damage = selected_weapon.damage
    
    print(f"You've selected {weapon_name}.")
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
battle()
