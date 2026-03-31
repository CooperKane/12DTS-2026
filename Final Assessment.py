    # Vihaan Kapoor Final Assessment 91896

import random
import time

player_stats = {"Health" : 80, "Speed" : 60, "Brainpower" : 75, "Strength" : 70}    # This is my dictionary for the player's stats
inventory = []   # This is where any items that the player collects will be stored
questions_correct = 0   # This will be used during quizzes within the game
room_1_completed = False
room_2_completed = False
playing = True
room_2_board = []
ttt_result = 0

def spacing():   # This just adds some spacing where ever I need it to make the program look nicer
    print("")
    print("")
    print("")

def starting_sequence():   # This is the starting sequence of the game and will only be shown once
    print("")
    print("Welcome to Around The World Escape Room")
    print("You have to go through 3 different rooms to escape")
    print("Each room will have its own theme")

def display_player_stats():   # This shows the player's stats, and will be used whenever it is required
    print("Your stats:")
    print("Health:", player_stats["Health"])
    print("Speed:", player_stats["Speed"])
    print("Brainpower", player_stats["Brainpower"])
    print("Strength", player_stats["Strength"])

def menu():   # This is a simple menu that the player can use to play the game or not play the game
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

def quiz_room_1():
    global questions_correct
    questions_correct = 0
    print("")
    print("QUESTION 1: What was the ancient name for the African continent?")
    while True:
        try:
            print("Type the corresponding number to answer")
            player_choice = int(input("1. Africlanker | 2. Alkebulan | 3. Alpaca: "))
            if player_choice > 0 and player_choice < 4:
                break
            else:
                print("Error. Please enter a number for the answers listed")
        except ValueError:
            print("Error. Please enter a number for the answers listed")
    if player_choice == 1 or player_choice == 3:
        print("")
        print("INCORRECT. You have", questions_correct, "correct answer(s)")
    else:
        questions_correct = questions_correct + 1
        print("")
        print("CORRECT. You have", questions_correct, "correct answer(s)")

    print("")
    print("QUESTION 2: Which of these animals is not native to Africa")
    while True:
        try:
            print("Type the corresponding number to answer")
            player_choice = int(input("1. Leopard | 2. Ostrich | 3. Tiger: "))
            if player_choice > 0 and player_choice < 4:
                break
            else:
                print("Error. Please enter a number for the answers listed")
        except ValueError:
            print("Error. Please enter a number for the answers listed")
    if player_choice == 1 or player_choice == 2:
        print("")
        print("INCORRECT. You have", questions_correct, "correct answer(s)")
    else:
        questions_correct = questions_correct + 1
        print("")
        print("CORRECT. You have", questions_correct, "correct answer(s)")

    print("")
    print("QUESTION 3: Approximately what percentage of Africa is desert?")
    while True:
        try:
            print("Type the corresponding number to answer")
            player_choice = int(input("1. 10% | 2. 40% | 3. 90%: "))
            if player_choice > 0 and player_choice < 4:
                break
            else:
                print("Error. Please enter a number for the answers listed")
        except ValueError:
            print("Error. Please enter a number for the answers listed")
    if player_choice == 1 or player_choice == 3:
        print("")
        print("INCORRECT. You have", questions_correct, "correct answer(s)")
    else:
        questions_correct = questions_correct + 1
        print("")
        print("CORRECT. You have", questions_correct, "correct answer(s)")

    print("")
    print("QUESTION 4: What is the most widely spoken language in Africa?")
    while True:
        try:
            print("Type the corresponding number to answer")
            player_choice = int(input("1. Swahili | 2. English | 3. Mandarin: "))
            if player_choice > 0 and player_choice < 4:
                break
            else:
                print("Error. Please enter a number for the answers listed")
        except ValueError:
            print("Error. Please enter a number for the answers listed")
    if player_choice == 2 or player_choice == 3:
        print("")
        print("INCORRECT. You have", questions_correct, "correct answer(s)")
    else:
        questions_correct = questions_correct + 1
        print("")
        print("CORRECT. You have", questions_correct, "correct answer(s)")

    print("")
    print("QUESTION 5: What is the estimated population of Africa?")
    while True:
        try:
            print("Type the corresponding number to answer")
            player_choice = int(input("1. 600M people | 2. 1.5B people | 3. 5B people: "))
            if player_choice > 0 and player_choice < 4:
                break
            else:
                print("Error. Please enter a number for the answers listed")
        except ValueError:
            print("Error. Please enter a number for the answers listed")
    if player_choice == 1 or player_choice == 3:
        print("")
        print("INCORRECT. You have", questions_correct, "correct answer(s)")
    else:
        questions_correct = questions_correct + 1
        print("")
        print("CORRECT. You have", questions_correct, "correct answer(s)")

def display_board(room_2_board):    # This function will display the tic tac toe board for room 2
    print("")
    print(room_2_board[0], "|", room_2_board[1], "|", room_2_board[2])
    print(room_2_board[3], "|", room_2_board[4], "|", room_2_board[5])
    print(room_2_board[6], "|", room_2_board[7], "|", room_2_board[8])
    print("")

def room_2_check_winner(room_2_board, X_or_O):  # This function will check if the player or computer has won yet in room 2
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]     # These are all of the possible winning combinations for the player and the computer
    for combination in winning_combinations:
        if room_2_board[combination[0]] == room_2_board[combination[1]] == room_2_board[combination[2]] == X_or_O:
            return True
    return False

def tic_tac_toe():      # This function will be the tic tac toe game in room 2
    global room_2_board
    global ttt_result
    for i in range(9):
        room_2_board.append(i + 1)
    display_board(room_2_board)
    print("Your pieces are Xs. The mans pieces are Os")
    time.sleep(1)


    for turn in range(9):
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:
            print("Your turn...")
            while True:
                try:
                    player_move = int(input("Choose your position from 1-9: "))
                    if player_move < 1 or player_move > 9:
                        print("Error. Please choose a number from 1-9")
                    elif room_2_board[player_move - 1] == "X" or room_2_board[player_move - 1] == "O":
                        print("Error. That position is already taken. Please choose another position")
                    else:
                        room_2_board[player_move - 1] = "X"
                        break
                except ValueError:
                    print("Error. Please choose a number from 1-9")
            display_board(room_2_board)

            if room_2_check_winner(room_2_board, "X"):      # This will check if the player has won the tic tac toe and change the ttt_result to win if they have
                print("You win!")
                ttt_result = "win"
                return

        else:
            print("Man's Turn...")
            time.sleep(1)
            spots_left = []
            for i in range(9):     # This part will make sure the man only picks a spot on the board which isn't taken by the player
                if room_2_board[i] != "X" and room_2_board[i] != "O":
                    spots_left.append(i)
            opponent_move = random.choice(spots_left)   # The man will randomly choose from one of the remaining spots
            room_2_board[opponent_move] = "O"
            display_board(room_2_board)

            if room_2_check_winner(room_2_board, "O"):  # This part will make the player lose if the opponent has won
                print("You lose!")
                ttt_result = "lose"
                return

    display_board(room_2_board)     # This part will make the game a draw if the player or opponent don't win
    print("Draw!")
    ttt_result = "draw"
    return

def room_1():   # This is the function for the first room of my escape room
    global player_stats
    global questions_correct
    global inventory
    global room_1_completed
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
            print("")
            print("You try running away, but you twist your ankle")
            print("Player speed has decreased from", player_stats["Speed"], "to", player_stats["Speed"] - 10)
            player_stats["Speed"] = player_stats["Speed"] - 10
            print("Luckily the lions don't notice you running away")
        else:
            print("")
            print("You run away, and the lions don't see you")
    elif user_choice == 2:
        print("")
        print("You slowly walk away from the lions without them noticing you")
    else:
        print("")
        print("You lunge towards the lions and they get ready to fight back")
        random_chance = random.randint(1,2)
        if random_chance == 1:
            print("The lions get scared of your confidence and back away leaving you unharmed")
            print("Where the lions were sitting, you see a potion...")
            print("Would you like to drink the mysterious potion?")
            print("")
            while True:
                try:
                    player_choice = int(input("1 to drink | 2 to leave: "))
                    if player_choice == 1:
                        print("")
                        print("You choose to drink the potion")
                        print("The potion gives you some extra health but lowers some strength")
                        print("Player health has increased from", player_stats["Health"], "to", player_stats["Health"] + 10)
                        print("Player strength has decreased from", player_stats["Strength"], "to", player_stats["Strength"] - 10)
                        player_stats["Health"] = player_stats["Health"] + 10
                        player_stats["Strength"] = player_stats["Strength"] - 10
                        break
                    elif player_choice == 2:
                        print("")
                        print("You chose to leave the potion alone and continue exploring")
                        break
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

    print("")
    print("After your encounter with the lions, you see a faint building in the distance")
    print("You start walking towards the building and a man greets you when you arrive")
    print("'What are you doing out here'")
    print("'I assume you're looking for the code to escape'")
    print("'Follow me. If you answer some of these questions I have right, maybe I'll give you the code'")
    print("")
    print("You follow the mysterious man into his home and you find yourself in a room with nothing but a computer with a quiz on it")
    print("You sit down and start answering the questions that you see")
    time.sleep(1)
    print("")
    print("WELCOME TO THE AFRICAN HISTORY QUIZ")
    print("YOU MUST GET 3 OUT OF 5 QUESTIONS CORRECT TO UNLOCK THE SECRET CODE")
    quiz_room_1()
    if questions_correct >= 3:
        spacing()
        print("CONGRATULATIONS YOU HAVE UNLOCKED THE SECRET CODE")
        print("CODE: 4830")
        inventory.append(4830)
    else:
        questions_correct = 0
        player_stats["Brainpower"] -= 10
        spacing()
        print("YOU HAVE NOT GOTTEN ENOUGH CORRECT QUESTIONS")
        print("YOU MUST RETRY THE QUIZ")
        quiz_room_1()
        if questions_correct >= 3:
            spacing()
            print("CONGRATULATIONS YOU HAVE UNLOCKED THE SECRET CODE AFTER 2 TRIES")
            print("CODE: 4830")
            inventory.append(4830)
        else:
            questions_correct = 0
            player_stats["Brainpower"] -= 10
            spacing()
            print("YOU HAVE FAILED THE QUIZ TWICE")
            print("YOU HAVE ONE MORE ATTEMPT TO PASS THE QUIZ OTHERWISE YOU WILL DIE")
            quiz_room_1()
            if questions_correct >= 3:
                spacing()
                print("CONGRATULATIONS YOU HAVE FINALLY PASSED THE QUIZ")
                print("CODE: 4830")
                inventory.append(4830)
            else:
                questions_correct = 0
                spacing()
                print("YOU HAVE FAILED AGAIN AND NOW WILL DIE")
                print("")
                player_stats["Health"] = 0
    spacing()
    if questions_correct >= 3:
        print("You have obtained the secret code")
        print("You open your phone and start typing in the code")
        print("4830")
        print("Your phone starts shaking and the world around you starts to fall apart")
        print("The ground underneath you starts breaking and you fall into a void")
        room_1_completed = True

def room_2():
    global room_2_completed
    global ttt_result
    global player_stats
    global inventory
    spacing()
    display_player_stats()
    spacing()
    time.sleep(2)
    print("Welcome to room 2")
    print("You fell into the void and landed on the coastline of what seems to be Japan")
    print("This room has the theme of Japan")
    print("Find the code to escape. Good luck")
    spacing()
    time.sleep(1)
    print("You start walking across the beach and see a bunch of sticks on the ground in a pattern")
    print("The pattern resembles a tic tac toe board")
    print("The man who you saw in room 1 walks up behind you and asks if you want to play the game with him")
    print("You don't know if you should play or not but as he helped you in room 1, you decide to play him")
    tic_tac_toe()
    if ttt_result == "win":
        print("")
        print("You have won the tic tac toe game against the mysterious man")
        print("He smiles at you and says 'Congratulations, you really are better at these games than I thought'")
        print("The man pulls a piece of paper out of his pocket and hands it to you")
        time.sleep(1)
        print("The paper has 2 numbers on it followed by 2 empty spaces")
        print("You assume it must be the code to escape the second room")
        print("Before you can say anything else, you look up at the man and he has disappeared")
        print("24__")
        inventory.append(2400)      # The 0s fill in the empty 2 numbers
    elif ttt_result == "lose":
        print("You have lost the tic tac toe game against the mysterious man")
        print("He laughs and says 'Well that was a good game, shame you couldn't beat me")
        print("He pulls out a piece of paper with numbers on it, which you assume must be the code to escape the second room")
        print("Before you can react, the man pulls out a lighter and burns the paper to ashes")
        print("'Good luck' the man says before disappearing before your eyes")
    else:
        print("You have drawn the tic tac toe game against the mysterious man")
        print("He lets out a deep breath and says 'What an exciting game'")
        print("You shrug, disappointed in your loss, but the man tells you one thing before vanishing")
        print("The man quickly says 'remember this number, it might be of use to you. 2'")
        print("You don't know for sure what to do with this information, but you piece together that it must be the first number in the code to escape the second room")
        inventory.append(2000)      # The 0s fill in the empty 3 numbers
    spacing()
    print("After your game with the mysterious man, you start looking around the beach again and in the distance you see some light")
    while True:
        try:
            print("")
            print("Would you like to go towards the light, or keep searching around the beach")
            player_choice = int(input("1. Go to the light | 2. Keep searching the beach: "))
            if player_choice == 1 or player_choice == 2:
                break
            else:
                print("Error. Please enter a number either 1 or 2")
        except ValueError:
            print("Error. Please enter a number either 1 or 2")
    if player_choice == 1:
        print("You choose to follow the light and as you walk you notice that the light is coming from a small village")
        print("As you approach the village, what seems to be a samurai guard notices you and yells out a signal to the village warning them")
        print("You try to explain that you come in peace and mean no harm but before you can explain yourself, many other samurai surround you")
        while True:
            try:
                print("")
                print("What would you like to do?")
                player_choice = int(input("1. Try and run away from the village | 2. Intimidate the samurai | 3. Run through the samurai into the village: "))
                if player_choice < 1 or player_choice > 3:
                    print("Error. Please enter a number from 1 to 3")
                else:
                    break
            except ValueError:
                print("Error. Please enter a number from 1 to 3")
        if player_choice == 1:
            print("")
            print("You start sprinting away from the village as fast as you can without looking behind at all")
            random_chance = random.randint(1, 2)
            if random_chance == 1:
                print("")
                print("The samurais watch you run away with a smile on their faces")
                print("They trust that you will not come back, so they leave you alone")
                print("")
                print("Exhausted from running, you don't see where you're going in the dark night and you end up walking straight into a tree, where your already weak body gives up and you pass out")
                spacing()
            else:
                print("")
                print("The samurais split up and chase after you in different directions")
                print("You don't see any way to run from them on land, so you run to the ocean and start swimming away")
                print("")
                print("The samurais, pleased with their work of running you out of their territory, go back to the village, but remain vigilant on lookout")
                print("Meanwhile, you have drained all of your energy while running away, and swimming against the current of the ocean becomes impossible")
                print("The last thing you remember is hearing the loud horn of a passing ship before you pass out")
                spacing()
            print("You wake up again in the morning, now in a bed in a room which looks to be in someone's home")
            print("You get up and see a family in the living room of the home")
            print("'I was wondering when you would wake up'")
            print("You look around in confusion and think to yourself. Where am I? Who are these people?")
            print("While looking around, you see the mysterious man again, now in the living room")
            print("You walk towards him and ask where you are but he just smiles and walks out of the house")
            print("You follow him out to a table where he has set out a deck of cards")
            print("")
            print("The man tells you if you can beat him in a game of blackjack, he will give you the remaining part of the code to escape room 2")
            # Add blackjack game here

        elif player_choice == 2:
            print("")
            print("You start shouting at the samurai one by one yelling that they are weak and must stand down now otherwise you will unleash your wrath")
            if player_stats["Strength"] >= 90:
                time.sleep(1)
                print("")
                print("The samurais look at each other and then at you")
                print("All at once they agree to stand down, intimidated by your aura")
                print("They give you free access to the village and all of its resources")
                print("")
                time.sleep(2)
                print("You go into the village and notice each house has a number on it either 2 or 4")
                if inventory[1] == 2400:
                    time.sleep(1)
                    print("You see two houses in front of you with the numbers 1 and 5")
                    print("As you have no better idea of what to do, you decide to type a code into your phone with the 24 from before, and now the 15 you noticed")
                    print("You type it into your phone slowly...")
                    print("2415")
                    time.sleep(1)
                    print("...")
                    time.sleep(2)
                    print("Code accepted.")
                    print("Your phone starts shaking again and you prepare to be teleported to the final room")
                    inventory[1] = 2415
                    room_2_completed = True
                else:
                    time.sleep(1)
                    print("You see three houses in front of you with the numbers 4, 1 and 5")
                    print("As you have no better idea of what to do, you decide to type a code into your phone with the 2 from before, and now the 415 you noticed")
                    print("You type it into your phone slowly...")
                    print("2415")
                    time.sleep(1)
                    print("...")
                    time.sleep(2)
                    print("Code accepted.")
                    print("Your phone starts shaking again and you prepare to be teleported to the final room")
                    inventory[1] = 2415
                    room_2_completed = True
            else:
                print("")
                time.sleep(1)
                print("The samurai look at each other, and then start attacking you")
                print("")









starting_sequence()
time.sleep(2)
menu()
time.sleep(0.5)
while playing == True:
    spacing()
    display_player_stats()
    while player_stats["Health"] > 0:
        if room_1_completed == False and player_stats["Health"] > 0:
            room_1()
        if room_2_completed == False and player_stats["Health"] > 0:
            room_2()

    print("You have died...")
    print("You were not able to escape")
    playing = False

spacing()
print("Come back and play again another time")