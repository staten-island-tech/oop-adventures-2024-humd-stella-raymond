class Weapon:
    def __init__(self, name, damage, price, critchance):
        self.name = name
        self.damage = damage
        self.price = price
        self.critchance = critchance

    def calculate_damage(self):
        import random
        # Calculate critical hit
        is_critical = random.uniform(0, 100) <= self.critchance
        final_damage = self.damage * (2 if is_critical else 1)
        if is_critical:
            print(f"Critical hit! {self.name} dealt {final_damage} damage!")
        return final_damage


class Staff(Weapon):
    def __init__(self, name):
        super().__init__(name, 28, 86, 32)


class HolyStaff(Weapon):
    def __init__(self, name):
        super().__init__(name, 36, 130, 35)


class CelestialBlade(Weapon):
    def __init__(self, name):
        super().__init__(name, 47, 200, 38)


class Mob:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")


class Goblin(Mob):
    def __init__(self):
        super().__init__("Goblin", 150)


class Dragon(Mob):
    def __init__(self):
        super().__init__("Dragon", 500)


class Knight(Mob):
    def __init__(self):
        super().__init__("Knight", 300)


# Attack System
def attack(attacker, weapon, target):
    print(f"{attacker} attacks {target.name} with {weapon.name}!")
    damage = weapon.calculate_damage()
    target.take_damage(damage)


# Example Usage
if __name__ == "__main__":
    # Create weapons
    staff = Staff("Basic Staff")
    holy_staff = HolyStaff("Holy Staff")
    blade = CelestialBlade("Celestial Blade")

    # Create mobs
    goblin = Goblin()
    dragon = Dragon()
    knight = Knight()

    # Perform attacks
    attack("Mage", staff, goblin)
    attack("Priest", holy_staff, knight)
    attack("Hero", blade, dragon)
