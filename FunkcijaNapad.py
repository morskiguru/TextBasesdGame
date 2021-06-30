def fight(main_character, enemy):
    while main_character.Health>0 and enemy.health>0:
        if main_character.attack()>=enemy.defense:
            print(f"Its a hit you did {main_character.attack_power} damage")
            enemy.health -= main_character.attack_power
            if enemy.attack()>=main_character.defense:
                print(f"You got hit for {enemy.attacking_power} damage")
                main_character.Health -= enemy.attacking_power
            print(f"You have {main_character.Health} health.")
            print(input("Press any key for next round"))
        else:
            print("You missed")
            if enemy.attack()>=main_character.defense:
                print(f"You got hit for {enemy.attacking_power} damage")
                main_character.Health -= enemy.attacking_power
            print(f"You have {main_character.Health} health.")
            print(input("Press any key for next round"))
        if main_character.Health <= 0:
            break
    if main_character.Health <= 0:
        return None
    else:
        return main_character.Health