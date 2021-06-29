import random

from Intro import intro
from Character import Character
from Location import Location
from EnemyNPC import EnemyNPC
from FunkcijaNapad import fight

start_text, quest1, quest2, quest3 = intro()
print(start_text)
Character = Character()
quest = 0
bio = ""

while True:
    quest = input("Chose a number 1, 2 or 3 representing the quest: ")
    if quest == "1":
        print(quest1)
        quest = quest1
        bio = "forest"
        break
    elif quest == "2":
        print(quest2)
        quest = quest2
        bio = "city"
        break
    elif quest == "3":
        print(quest3)
        quest = quest3
        bio = "mountain"
        break
    else: print("You picked wrongly chose 1, 2 or 3")

loc = Location(bio, quest)
event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
current_enemy = EnemyNPC(current_enemy)
while event:
    print(f"""
You have reached {current_location} and have encountered {current_enemy.name}.
How will you proceed?
1)Fight it
2)Run for it
3)Use the environment """)
    decision = input("Declare your action: ")
    if decision == "1":
        fight(Character, current_enemy)
        print(f"After inspecting the {current_location} you have found {item}.")
        Character.inventory[item] = item_value
        print(Character.inventory)
        for key, value in Character.inventory.items():
            print(f"{key.title()} will replenish {value} health.")
        health_regeneration = input("Type the name to replensih health: ")
        try:
            Character.Health = min(Character.Health+Character.inventory.pop(health_regeneration), 100)
            print(Character.Health)
        except KeyError:
            print(Character.Health)
        event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
        current_enemy = EnemyNPC(current_enemy)
    elif decision == "2":
        if random.choice(range(1, 20))>10:
            print("You have escaped")
            event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
            current_enemy = EnemyNPC(current_enemy)
        else:
            print(f"The monster got a bite behind you hurting you for {current_enemy.attacking_power} health.")
            Character.Health -= current_enemy.attacking_power
            fight(Character, current_enemy)
            print(f"After inspecting the {current_location} you have found {item}.")
            Character.inventory[item] = item_value
            for item, value in Character.inventory.items():
                print(f"{item.title()} will replenish {value} health.")
            health_regeneration = input("Type the name to replensih health: ")
            try:
                Character.Health = min(Character.Health + Character.inventory.pop(health_regeneration), 100)
                print(Character.Health)
            except KeyError:
                print(Character.Health)
            event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
            current_enemy = EnemyNPC(current_enemy)
    elif decision == "3":
        if random.choice(range(1, 20))>15:
            print("You've used the environment and defeated the enemy")
            print(f"After inspecting the {current_location} you have found {item}.")
            Character.inventory[item] = item_value
            for item, value in Character.inventory.items():
                print(f"{item.title()} will replenish {value} health.")
            health_regeneration = input("Type the name to replensih health: ")
            try:
                Character.Health = min(Character.Health + Character.inventory.pop(health_regeneration), 100)
                print(Character.Health)
            except:
                print(Character.Health)
            event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
            current_enemy = EnemyNPC(current_enemy)
        else:
            print(f"The monster got a bite behind you hurting you for {current_enemy.attacking_power} health.")
            Character.Health -= current_enemy.attacking_power
            fight(Character, current_enemy)
            print(f"After inspecting the {current_location} you have found {item}.")
            Character.inventory[item] = item_value
            for item, value in Character.inventory.items():
                print(f"{item.title()} will replenish {value} health.")
            health_regeneration = input("Type the name to replensih health: ")
            try:
                Character.Health = min(Character.Health + Character.inventory.pop(health_regeneration), 100)
                print(Character.Health)
            except KeyError:
                print(Character.Health)
            event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
            current_enemy = EnemyNPC(current_enemy)
if event == False:
    print(f"""
You have reached {current_location} and have encountered {current_enemy}.
Its all in see you om the other side""")
fight(Character, current_enemy)


