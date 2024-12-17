class enemy:
    def __init__(self, name, HP, attack, coin_drop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.coin_drop = coin_drop

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