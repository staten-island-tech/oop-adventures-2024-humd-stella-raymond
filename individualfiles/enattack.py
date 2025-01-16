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

class Enemy:
    def __init__(self, name, HP, attack, coin_drop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.coin_drop = coin_drop

class Slime(Enemy):
    def __init__(self, name):
        super().__init__(name, 15, 5, 3)

class Goblins(Enemy):
    def __init__(self, name):
        super().__init__(name, 20, 7, 5)

class Zombies(Enemy):
    def __init__(self, name):
        super().__init__(name, 30, 10, 8)

class Skeleton(Enemy):
    def __init__(self, name):
        super().__init__(name, 35, 13, 9)

class CarnivorousPlant(Enemy):
    def __init__(self, name):
        super().__init__(name, 45, 25, 18)

class Wolf(Enemy):
    def __init__(self, name):
        super().__init__(name, 50, 32, 25)

class Mage(Enemy):
    def __init__(self, name):
        super().__init__(name, 60, 50, 40)

class Knight(Enemy):
    def __init__(self, name):
        super().__init__(name, 75, 40, 45)

class EvilKing(Enemy):
    def __init__(self, name):
        super().__init__(name, 125, 65, 0)

def battle(player_hp, player_coins):
    print("Welcome to the Battle Function!")
    
    # Select weapon
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
        return battle(player_hp, player_coins)
    selected_weapon = weapons[weapon_name]
    critchance = selected_weapon.critchance
    base_damage = selected_weapon.damage
    
    print(f"You've selected {weapon_name}.")
    print(f"Critical Chance: {critchance}%. Base Damage: {base_damage}.")

    # Select enemy
    enemies = [Slime("Slime"), Goblins("Goblins"), Zombies("Zombies"), Skeleton("Skeleton"),
               CarnivorousPlant("Carnivorous Plant"), Wolf("Wolf"), Mage("Mage"),
               Knight("Knight"), EvilKing("Evil King")]
    
    enemy = random.choice(enemies)
    print(f"A wild {enemy.name} appears with {enemy.HP} HP!")

    # Battle Loop
    while player_hp > 0 and enemy.HP > 0:
        print(f"\nYour HP: {player_hp} | Enemy HP: {enemy.HP}")
        # Player's Turn
        correct_number = random.randint(1, 100)
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
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
            damage = base_damage
            print(f"Your damage is: {damage}")
        
        # Apply damage to enemy
        enemy.HP -= damage
        
        # If enemy is dead
        if enemy.HP <= 0:
            print(f"You defeated the {enemy.name}! You gain {enemy.coin_drop} coins.")
            player_coins += enemy.coin_drop
            break
        
        # Enemy's Turn (Enemy attacks)
        print(f"\nThe {enemy.name} attacks you!")
        player_hp -= enemy.attack
        if player_hp <= 0:
            print(f"You were defeated by {enemy.name}!")
            break

    return player_hp, player_coins

def main():
    player_hp = 100
    player_coins = 0

    while player_hp > 0:
        print("\n--- New Turn ---")
        player_hp, player_coins = battle(player_hp, player_coins)
        
        if player_hp > 0:
            continue_battle = input("\nDo you want to fight another enemy? (y/n): ").lower()
            if continue_battle != 'y':
                print(f"Thanks for playing! You finished with {player_coins} coins!")
                break
        else:
            print(f"You died with {player_coins} coins. Game Over.")
            break

if __name__ == "__main__":
    main()
