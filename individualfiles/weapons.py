class weapon:
    def __init__(self, name, damage, price, critchance):
        self.name = name
        self.damage = damage
        self.price = price
        self.critchance = critchance

    def calculate_damage(self):
        import random
        is_critical = random.uniform(0, 100) <= self.critchance
        final_damage = self.damage * (2 if is_critical else 1)
        if is_critical:
            print(f"Critical hit! {self.name} dealt {final_damage} damage!")
        return final_damage
    
class Stick(weapon):
    def __init__(self, name):
        super().__init__(name, 5, 0, 0)
    
class BasicSword:
    def __init__(self, name):
        super().__init__(name, 8, 9, 0)

class SilverSword:
    def __init__(self, name):
        super().__init__(name, 10, 16, 20)

class BasicScythe:
    def __init__(self, name):
        super().__init__(name, 14, 20, 23)

class MagicWand:
    def __init__(self, name):
        super().__init__(name, 20, 40, 26)

class UndeadScythe:
    def __init__(self, name):
        super().__init__(name, 23, 55, 29)

class Staff:
    def __init__(self, name):
         super().__init__(name, 28, 86, 32)  

class HolyStaff:
    def __init__(self, name):
        super().__init__(name, 36, 130, 35)

class CelestialBlade:
    def __init__(self, name):
        super().__init__(name, 47, 200, 38)