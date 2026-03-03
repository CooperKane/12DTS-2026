import random
import time

wild_pokemon = [
    {"Name" : "Charizard", "Type" : "Fire", "Level" : random.randint(1, 3), "Health" : random.randint(75, 100), "Attack" : ["Ember", random.randrange(10, 25), "Flamethrower", random.randrange(25, 45)]},
    {"Name" : "Venusaur", "Type" : "Grass", "Level" : random.randint(1, 3), "Health" : random.randint(75, 100), "Attack" : ["Razor Leaf", random.randrange(30,40), "Poison Powder", random.randrange(10,20)]},
    {"Name" : "Blastoise", "Type" : "Water", "Level" : random.randint(1, 3), "Health" : random.randint(75, 100), "Attack" : ["Hydro Pump", random.randrange(28,42), "Bubble", random.randrange(14,23)]},
    {"Name" : "Pikachu", "Type" : "Electric", "Level" : random.randint(1, 3), "Health" : random.randint(75, 100), "Attack" : ["Thunder", random.randrange(30,40), "Quick Attack", random.randrange(10,20)]},
    {"Name" : "Snorlax", "Type" : "Normal", "Level" : random.randint(1, 3), "Health" : random.randint(85, 100), "Attack" : ["Body Slam", random.randrange(10, 17), "Snore", random.randrange(30,50)]},
    {"Name" : "Magikarp", "Type" : "Water", "Level" : random.randint(1, 3), "Health" : random.randint(50, 100), "Attack" : ["Splash", random.randrange(25, 45), "Flop", random.randrange(10, 25)]}
]

own_pokemon = [{"Name" : "Charizard", "Type" : "Fire", "Level" : 3, "Health" : 90, "Attack" : ["Ember", random.randrange(10, 25), "Flamethrower", random.randrange(25, 45)]}]
def overworld_timer():
    timer = random.randint(1, 5)
    time.sleep(timer)
    print("Battle begins")
    battle()

def battle():
    x = random.randint(0, len(wild_pokemon) - 1)
    enemy_pokemon = wild_pokemon[x]
    player_pokemon = own_pokemon[0]
    player_pokemon_hp = player_pokemon["Health"]
    print("Player Pokemon:", player_pokemon["Name"])
    print("Player Pokemon HP:", player_pokemon_hp)
    print("")
    print("A wild", enemy_pokemon["Name"], "appeared")
    print("It's a", enemy_pokemon["Type"], "type Pokemon")
    print("It's level", enemy_pokemon["Level"])
    print("It has", enemy_pokemon["Health"], "health")
    print("")

    while True:
        try:
            print("Press 1 to battle or 2 to run away")
            player_choice = int(input())
            if player_choice < 1 or player_choice > 2:
                print("Error. Please enter a number either 1 or 2")
            else:
                break
        except ValueError:
            print("Error. Please enter a number either 1 or 2")

    print("Player's", player_pokemon["Name"], "has", player_pokemon_hp, "HP")

    if player_choice == 1:
        enemy_attack_randomiser = random.randrange(0, 3, 2)
        print("Enemy", enemy_pokemon["Name"], "attacks with", enemy_pokemon["Attack"][enemy_attack_randomiser], "and does", enemy_pokemon["Attack"][enemy_attack_randomiser + 1], "damage")
        player_pokemon_hp = player_pokemon_hp - enemy_pokemon["Attack"][enemy_attack_randomiser + 1]
        print("Player's", player_pokemon["Name"], "has", player_pokemon_hp, "HP")
        print("")
        print("What attack would you like to use")
        print(own_pokemon[0]["Attack"][0], "90% chance of working. ", own_pokemon[0]["Attack"][2], "70% chance of working")

        while True:
            try:
                player_attack = int(input("1 for Ember or 2 for Flamethrower: "))
                if player_attack < 1 or player_attack > 2:
                    print("Error. Please enter a number either 1 or 2")
                else:
                    break
            except ValueError:
                print("Error. Please enter a number either 1 or 2")

        random_chance = random.randint(1, 10)
        if player_attack == 1:
            if random_chance == 10:
                print("Players", player_pokemon["Name"], "attempts", player_pokemon["Attack"][0])
                print("The attack missed")
            else:
                print("Player's", player_pokemon["Name"], "attempts", player_pokemon["Attack"][0])
                print("Player's", player_pokemon["Name"], "attacks with", player_pokemon["Attack"][0], "and does", player_pokemon["Attack"][1], "damage")
                enemy_pokemon["Health"] = enemy_pokemon["Health"] - player_pokemon["Attack"][1]
                print("Enemy", enemy_pokemon["Name"], "has", enemy_pokemon["Health"], "HP")
                print("")
        else:
            if random_chance >= 8:
                print("Players", player_pokemon["Name"], "attempts", player_pokemon["Attack"][2])
                print("The attack missed")
            else:
                print("Player's", player_pokemon["Name"], "attempts", player_pokemon["Attack"][2])
                print("Player's", player_pokemon["Name"], "attacks with", player_pokemon["Attack"][2], "and does", player_pokemon["Attack"][3], "damage")
                enemy_pokemon["Health"] = enemy_pokemon["Health"] - player_pokemon["Attack"][3]
                print("Enemy", enemy_pokemon["Name"], "has", enemy_pokemon["Health"], "HP")
                print("")

        if player_pokemon_hp > 0:

        else:





    else:
        overworld_timer()


overworld_timer()

