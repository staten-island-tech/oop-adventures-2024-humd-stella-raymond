class user:
     def __init__(self, name, HP, money, inventory):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money
        self.inventory = []

def buy(self,item):
        self.inventory.append(item)
        print(self.inventory)
        self.inventory.remove(money)

def die(self,item):
    if self.HP <0:
        return True
        self.inventory.remove(item)
        print(self.inventory)
        self.money = 0 
    else:
        return False
       
def heal(self, amount):
        self.HP += amount
        print(self.HP)

def alive(self):
        if self.HP > 0:
            return True
        else: 
            return False
