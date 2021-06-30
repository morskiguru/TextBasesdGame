import random

class EnemyNPC:
    def __init__(self, name):
        self.name = name
        self.health = random.choice(range(40, 80))
        self.attacking_power = random.choice(range(7,20))
        self.defense = random.choice(range(7,12))

    def attack(self):
        roll = (random.choice(range(5, 20)))
        return roll




