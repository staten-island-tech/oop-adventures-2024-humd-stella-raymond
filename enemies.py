class enemy:
    def __init__(self, name, HP, attack, coin_drop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.coin_drop = coin_drop

    def take_damage(self, damage):
        self.HP -= damage
        print(f"{self.name} takes {damage} damage. Remaining HP: {self.HP}")
        if self.HP <= 0:
            self.defeat()

    def defeat(self):
        print(f"{self.name} was defeated!")
        global user_money
        user_money += self.coin_drop
        print(f"{user_name} earned {self.coin_drop} coins. Total money: {user_money}")

    def attack_user(self):
        global user_hp
        print(f"{self.name} attacks {user_name} for {self.attack} damage.")
        user_hp -= self.attack
        print(f"{user_name} takes {self.attack} damage. Remaining HP: {user_hp}")

class Slime(enemy):
    def __init__(self, name): 
        super().__init__(name, 15, 5, 3)

class Goblins(enemy):
    def __init__(self, name): 
        super().__init__(name, 20, 7, 5)

class Zombies(enemy):
    def __init__(self, name): 
        super().__init__(name, 30, 10, 8)

class Skeleton(enemy):
    def __init__(self, name): 
        super().__init__(name, 35, 13, 9)                                                                                                                                                                                          

class CarnivorousPlant(enemy):
    def __init__(self, name): 
        super().__init__(name, 45, 25, 18)

class Wolf(enemy):
    def __init__(self, name): 
        super().__init__(name, 50, 32, 25)

class Mage(enemy):
    def __init__(self, name): 
        super().__init__(name, 60, 50, 40)

class Knight(enemy):
    def __init__(self, name): 
        super().__init__(name, 75, 40, 45)

class EvilKing(enemy):
    def __init__(self, name): 
        super().__init__(name, 125, 65, 0)

slime = Slime("Slime")
goblin = Goblins("Goblin")
zombie = Zombies("Zombie")
skeleton = Skeleton("Skeleton")
plant = CarnivorousPlant("Carnivorous Plant")
wolf = Wolf("Wolf")
mage = Mage("Mage")
knight = Knight("Knight")
evil_king = EvilKing("Evil King")

print(f"{slime.name}: HP = {slime.HP}, Attack = {slime.attack}, Coin Drop = {slime.coin_drop}")