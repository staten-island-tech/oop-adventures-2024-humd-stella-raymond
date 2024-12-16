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
    "Silver Sword": {"damage": 10, "cost": 16},
    "Basic Scythe": {"damage": 14, "cost": 20},
    "Magic Wand": {"damage": 20, "cost": 40},
    "Undead Scythe": {"damage": 23, "cost": 55},
    "Staff": {"damage": 28, "cost": 86},
    "Holy Staff": {"damage": 36, "cost": 130},
    ""
}

merchant = Merchant(
    weapons = weapons,
    potions = ["Healing Potion"],
    armor = ["Armor"]
)