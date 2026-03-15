import random
import time

player_stats = {"Health" : 80, "Speed" : 60, "Brainpower" : 75, "Strength" : 70}
inventory = []
play_game = 0


def spacing():
    print("")
    print("")
    print("")

def starting_sequence():
    print("Welcome to Around The World Escape Room")
    print("You have to go through 5 different rooms to escape")
    print("Each room will have its own theme")

def player_stats():
    print("Your stats:")
    print("Health:", player_stats["Health"])
    print("Speed:", player_stats["Speed"])
    print("Brainpower", player_stats["Brainpower"])
    print("Strengh", player_stats["Strength"])

def menu():
    global playing
    spacing()
    print("Each room will have sets of questions that you can answer to recieve items in your inventory")
    print("Use these items to get through the rooms and escape")
    print("Each room will have a hidden code that you can plug into your phone to escape")
    print("")
    print("Would you like to take on the challenge?")
    while True:
        try:
            play_game = input("Y for Yes or N for No: ").upper()
            if play_game == "Y" or play_game == "N":
                break
            elif play_game == "YES" or play_game == "NO":
                break
            else:
                print("Error. Please choose an answer from the choices listed")
        except ValueError:
            print("Error. Please enter either Y or N")

    if play_game == "Y" or play_game == "YES":
        playing = True
    else:
        playing = False

def room_1():
    global player_stats
    spacing()
    print("Welcome to Room 1")
    print("This room has a theme of Africa")
    print("Find the code to escape. Good luck")
    print("")
    print("While exploring the savannah, you come across a pride of lions")
    while True:
        try:
            print("Would you like to: 1. Run away quickly | 2. Slowly walk away | 3. Try and attack them")
            user_choice = int(input("Choose by pressing the corresponding number: "))
            if user_choice > 0 and user_choice < 4:
                break
            else:
                print("Error. Please enter a number from the choices listed")
        except ValueError:
            print("Error. Please enter a number from the choices listed")
    if user_choice == 1:
        random_chance = random.randint(1,10)
        if random_chance > 8:
            print("You try running away, but you twist your ankle")
            print("Player speed has decreased from", player_stats["Speed"], "to", player_stats["Speed"] - 10)
            player_stats["Speed"] = player_stats["Speed"] - 10
            print("Luckily the lions don't notice you running away")
        else:
            print("You run away, and the lions don't see you")
    elif user_choice == 2:
        print("You slowly walk away from the lions without them noticing you")
    else:
        print("You lunge towards the lions and they get ready to fight back")
        random_chance = random.randint(1,2)
        if random_chance == 1:
            print("The lions get scared of your confidence and back away leaving you unharmed")
            print("Where the lions were sitting, you see a potion...")
            print("Would you like to drink the mysterious potion?")
            print("")
            while True:
                try:
                    player_choice = int(input("1 to drink | 2 to leave"))
                    if player_choice == 1:
                        print("You choose to drink the potion")
                        print("The potion gives you some extra health but lowers some strength")
                        print("Player health has increased from", player_stats["Health"], "to", player_stats["Health"] + 10)
                        print("Player strength has decreased from", player_stats["Strength"], "to", player_stats["Strength"] - 10)
                        player_stats["Health"] = player_stats["Health"] + 10
                        player_stats["Strength"] = player_stats["Strength"] - 10
                    elif player_choice == 2:
                        print("You chose to leave the potion alone and continue exploring")
                    else:
                        print("Error. Please enter 1 or 2")
                except ValueError:
                    print("Error. Please enter either 1 or 2")
        else:
            print("The lions all group up and chase you down")
            print("Eventually your legs give up and you fall over into some tall grass")
            print("You try playing dead, but the lions still attack you")
            print("The lions start clawing at you but a herd of wildebeest catch their attention")
            print("The lions leave you in a bad condition but you survive")
            print("")
            print("Player health has decreased from", player_stats["Health"], "to", player_stats["Health"] - 50)
            player_stats["Health"] = player_stats["Health"] - 50

    print("After your encounter with the lions, you see a faint building in the distance")
    print("You start walking towards the building and a man greets you when you arrive")
    print("'What are you doing out here'")
    print("'I assume you must be looking for the code to escape'")

starting_sequence()
time.sleep(2)
menu()
time.sleep(0.5)
if playing == True:
    room_1()
else:
    spacing()
    print("Come back and play again another time")