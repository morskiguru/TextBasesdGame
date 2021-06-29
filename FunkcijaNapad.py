def fight(main_character, enemy):
    while main_character.Health>0 and enemy.health>0:
        if main_character.attack()>=enemy.defense:
            print(f"Its a hit you did {main_character.attack_power} damage")
            enemy.health -= main_character.attack_power
            if enemy.attack()>=main_character.defense:
                print(f"You got hit for {enemy.attacking_power} damage")
                main_character.Health -= enemy.attacking_power
            print(main_character.Health)
            print(input("Press any key for next round"))
    if main_character.Health <= 0:
        print("You have died")
    else:
        return main_character.Health