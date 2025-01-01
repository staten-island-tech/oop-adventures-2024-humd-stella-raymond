from enemies import Enemy, Slime  # Import enemy classes
from classofweapons import Weapon, BasicSword  # Import weapon classes

def attack_enemy(weapon, enemy):
    if enemy.HP > 0:
        print(f"\n{weapon.name} is used to attack {enemy.name}!")
        damage = weapon.calculate_damage()
        defeated = enemy.take_damage(damage)
        if defeated:
            print(f"You have defeated {enemy.name} and earned {enemy.coin_drop} coins!")
        else:
            print(f"{enemy.name} is still alive!")
    else:
        print(f"{enemy.name} is already defeated.")

if __name__ == "__main__":
    weapon = BasicSword()
    enemy = Slime()

    print(f"Weapon: {weapon.name}, Damage: {weapon.damage}, Crit Chance: {weapon.critchance}%")
    print(f"Enemy: {enemy.name}, HP: {enemy.HP}, Attack: {enemy.attack}")

    # Simulate attacks
    attack_enemy(weapon, enemy)
    attack_enemy(weapon, enemy)
    attack_enemy(weapon, enemy)
