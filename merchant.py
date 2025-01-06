class Merchant:
    def __init__(self, weapons, potions, armor, products):
        self.weapons = weapons
        self.potions = potions
        self.armor = armor
        self.products = products
    def sell(self, item, user_balance):
        item_cost = item["cost"]
        if user_balance >= item_cost:
            user_balance -= item_cost
            self.products.remove(item)
            print(f"You have purchased {item} for {item_cost} coins.")
            print(f"Your remaining balance is {user_balance} coins.")
            return user_balance
        else:
            print("You do not have enough coins to purchase this item.")
            return user_balance

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
    armor = ["Armor"],
    products = ["products"]
)

class Armor:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        reduced_damage = max(0, self.health - damage)
        print(f"Armor reduces damage by {self.health}. Final damage taken: {reduced_damage}")
        return reduced_damage

