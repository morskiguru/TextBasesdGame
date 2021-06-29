import random
class Location:
    locations = {"forest": ["camp", "groove", "dense forest", "cave", "Special"],
                "city": ["museum", "cemetery", "abandoned building", "store", "Special"],
                "mountain": ["cave", "rock slide", "landslide", "clearing", "special"]}
    enemysNPC = {"forest": ["wolf", "bear", "forest troll", "young green dragon"],
                 "city": ["gladiator", "swashbuckler", "bandit", "guard"],
                 "mountain": ["goblin", "great rock worm", "hag", "owlbear"]}
    items = {"snack": 15, "roast beef": 50, "small potion of healing": 25}

    def __init__(self, bio, quest):
        self.biom=bio
        self.quest=quest
    def new_step_of_adventure(self):
        new_location = random.choice(self.locations[self.biom])
        location_enemy = random.choice(self.enemysNPC[self.biom])
        if new_location == "Special":
            item, item_value = random.choice(list(self.items.items()))
            return False, new_location, location_enemy, item, item_value
        else:
            item, item_value = random.choice(list(self.items.items()))
            return True, new_location, location_enemy, item, item_value
