import json
import os

class Weapon:
    weapon_type = "Melee"  

    def __init__(self, name, damage, durability, weapon_type=None):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.weapon_type = weapon_type if weapon_type else Weapon.weapon_type
    def attack(self, target):
        if self.durability > 0:
            print(f"{self.name} attacks {target} for {self.damage} damage!")
            self.durability -= 1
            print(f"Weapon durability: {self.durability}")
        else:
            print(f"{self.name} is too damaged to fight.")
    def is_broken(self):
        return self.durability <= 0

    def __str__(self):
        return f"{self.name} ({self.weapon_type}) - Damage: {self.damage}, Durability: {self.durability}"

sword = Weapon(name="Holy_Sun", damage=45, durability=15)
print(sword)
sword.attack("Slime")
if sword.is_broken():
    print(f"{sword.name} is broken and cannot be used!")
else:
    print(f"{sword.name} is still usable.")
print(sword)
