import random
from Intro import intro, choose_quest
from Character import Character
from Location import Location
from EnemyNPC import EnemyNPC
from FunkcijaNapad import fight
from Healling import healing

start_text, quest1, quest2, quest3 = intro()
print(start_text)
Character = Character()

quest, bio = choose_quest(quest1, quest2, quest3)

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
        if Character.Health <1:
            print("""
              Game Over
            You have died""")
            break
        print(f"After inspecting the {current_location} you have found {item}.")
        Character.inventory[item] = item_value
        print(Character.inventory)
        healing(Character.inventory, Character)
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
            if Character.Health < 1:
                print("""
                  Game Over
                You have died""")
                break
            print(f"After inspecting the {current_location} you have found {item}.")
            Character.inventory[item] = item_value
            healing(Character.inventory, Character)
            event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
            current_enemy = EnemyNPC(current_enemy)
    elif decision == "3":
        if random.choice(range(1, 20))>15:
            print("You've used the environment and defeated the enemy")
            print(f"After inspecting the {current_location} you have found {item}.")
            Character.inventory[item] = item_value
            healing(Character.inventory, Character)
            event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
            current_enemy = EnemyNPC(current_enemy)
        else:
            print(f"The monster got a bite behind you hurting you for {current_enemy.attacking_power} health.")
            Character.Health -= current_enemy.attacking_power
            fight(Character, current_enemy)
            if Character.Health < 1:
                print("""
                  Game Over
                You have died""")
                break
            print(f"After inspecting the {current_location} you have found {item}.")
            Character.inventory[item] = item_value
            healing(Character.inventory, Character)
            event, current_location, current_enemy, item, item_value = loc.new_step_of_adventure()
            current_enemy = EnemyNPC(current_enemy)
if event == False:
    print(f"""
You have reached {current_location} and have encountered {current_enemy}.
Its all in see you on the other side""")
fight(Character, current_enemy)
if Character.Health < 1:
    print("""
      Game Over
    You have died""")
else:
    print("You are victorious")





