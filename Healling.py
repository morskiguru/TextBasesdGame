def healing(character_inventory, character_main):
    for item, value in character_inventory.items():
        print(f"{item.title()} will replenish {value} health.")
    input_item = input("Type the item name to replenish health: ")
    input_item=input_item.lower()
    try:
        character_main.Health = min(character_main.Health + character_inventory.pop(input_item), 100)
        print(character_main.Health)
    except KeyError:
        print(f"You have {character_main.Health} health")
