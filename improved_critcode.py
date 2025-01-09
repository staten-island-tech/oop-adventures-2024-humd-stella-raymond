import random

def generate_random_numbers(count, start=1, end=100):
    return [random.randint(start, end) for _ in range(count)]

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

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I've selected some random numbers between 1 and 100.")

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
        print("Invalid weapon choice!")
        return

    selected_weapon = weapons[weapon_name]
    critchance = selected_weapon.critchance
    base_damage = selected_weapon.damage
    print(f"You've selected {weapon_name}. Your critical chance is {critchance}%.")
    print(f"You also have a base damage of {base_damage}.")
    
    correct_numbers = generate_random_numbers(critchance) 
    print(f"Hint: There are {len(correct_numbers)} possible correct numbers.")

    try:
        user_guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if user_guess in correct_numbers:
        # Always calculate the boosted damage
        random_chance = random.randint(1, 100)
        if random_chance <= critchance:
            damage = base_damage * 1.5
            print("Critical Hit! You guessed correctly and scored a critical hit!")
        else:
            damage = base_damage * 1.5  # Always apply the boost, even if it's not a critical hit
        
        print(f"You guessed correctly! You landed a critical hit!")
        print(f"Your final boosted damage is {damage}.")
    else:
        print("Incorrect. Here are all the possible correct answers:")
        print(", ".join(map(str, correct_numbers)))

guess_the_number()
