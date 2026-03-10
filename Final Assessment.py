import random
import time

player_stats = {"Health" : 100, "Speed" : 60, "Brainpower" : 75, "Strength" : 70}
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

def menu():
    global playing
    spacing()
    print("Each room will have a set of questions that you must answer correctly to recieve items in your inventory")
    print("Use these items to get through the rooms and escape")
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
    print("Find the key to escape. Good luck")
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
            print("Luckily the lions don't notice you, but ")

        else:

starting_sequence()
time.sleep(2)
menu()
time.sleep(0.5)
if playing == True:
    room_1()
else:
    spacing()
    print("Come back and play again another time")