import random
import time

wild_pokemon = [
    {"Name" : "Charizard", "Type" : "Fire", "Level" : random.randint(1, 3), "Health" : random.randint(15, 25), "Attack" : ["Ember", random.randrange(3, 6), "Flamethrower", random.randrange(8, 11)]},
    {"Name" : "Venasaur", "Type" : "Grass", "Level" : random.randint(1, 3), "Health" : random.randint(15, 25)},
    {"Name" : "Blastoise", "Type" : "Water", "Level" : random.randint(1, 3), "Health" : random.randint(15, 25)},
    {"Name" : "Pikachu", "Type" : "Electric", "Level" : random.randint(1, 3), "Health" : random.randint(15, 25)},
    {"Name" : "Snorlax", "Type" : "Normal", "Level" : random.randint(1, 3), "Health" : random.randint(15, 25)},
    {"Name" : "Magikarp", "Type" : "Water", "Level" : random.randint(1, 3), "Health" : random.randint(15, 25)}
]

def overworld_timer():
    timer = random.randint(1, 5)
    time.sleep(timer)
    print("Battle begins")
    battle()

def battle():
    x = random.randint(0, len(wild_pokemon) - 1)
    pokemon = wild_pokemon[x]
    print("A wild", pokemon["Name"], "appeared")
    print("It's a", pokemon["Type"], "type Pokemon")
    print("It's level", pokemon["Level"])
    print("It has", pokemon["Health"], "health")

overworld_timer()