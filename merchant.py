class Merchant:
    def __init__(self, weapons, potions, armor):
        self.weapons = weapons
        self.potions = potions
        self.armor = armor
    def sell(self, item):
        self.products.remove(item)
        print(f'you have purchased {item}')
        print(self.products)
        return item
    def greeting():
        print("Welcome!")

weapons = {
    "Basic Sword": {"damage": 8, "cost": 9},
    "Silver Sword": {"damage": 10, "cost": 16, "crit chance": "20%"},
    "Basic Scythe": {"damage": 14, "cost": 20, "crit chance": "23%"},
    "Magic Wand": {"damage": 20, "cost": 40, "crit chance": "26%"},
    "Undead Scythe": {"damage": 23, "cost": 55, "crit chance": "29%"},
    "Staff": {"damage": 28, "cost": 86, "crit chance": "32%"},
    "Holy Staff": {"damage": 36, "cost": 130, "crit chance": "35%"},
    "Celestial Blade": {"damage": 47, "cost": 200, "crit chance": "38%"}
}

merchant = Merchant(
    weapons = weapons,
    potions = ["Healing Potion"],
    armor = ["Armor"]
)

class Armor:
    def __init__(self, defense, damage):
        self.defense = defense
        self.damage = damage

    def take_damage(self, damage):
        reduced_damage = max(0, damage - self.defense)
        print(f"Armor reduces damage by {self.defense}. Final damage taken: {reduced_damage}")
        return reduced_damage