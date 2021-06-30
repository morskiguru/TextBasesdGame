import random


class Character:
    Health = 100
    attack_power = 15
    defense = 15
    inventory ={"health potion" : 100, "fresh meal": 20 }
    def __init(self, name):
        self.name = name
    def __repr__(self):
        print(f"your hero has {self.Health} health, {self.attack_power} attacking power and {self.defense} defense")

    def attack(self):
        roll=(random.choice(range(1,20)))
        return roll


