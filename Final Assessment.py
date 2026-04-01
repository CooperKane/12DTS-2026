    #----------Vihaan Kapoor Final Assessment 91896----------

#IMPORTS

import random
import time

#VARIABLES

player_stats = {"Health" : 80, "Speed" : 60, "Brainpower" : 75, "Strength" : 70}    # This is my dictionary for the player's stats
inventory = []   # This is where any items that the player collects will be stored
questions_correct = 0   # This will be used during quizzes within the game
room_1_completed = False
room_2_completed = False
room_3_completed = False
playing = True
room_2_board = []
ttt_result = 0
blackjack_winner = 0

#FUNCTIONS

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

def stats_boost():      # This will give the player a slight stats boost throughout the game
    global player_stats
    player_stats["Health"] += random.randint(5, 25)
    player_stats["Speed"] += random.randint(5, 25)
    player_stats["Brainpower"] += random.randint(5, 25)
    player_stats["Strength"] += random.randint(5, 25)

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
            if play_game == "Y" or play_game == "N":        # Some error detection
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

def quiz_room_1():      # This will be used as the quiz in the first room
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

def blackjack():        # This will be used in the second room
    global blackjack_winner
    player_hand = [random.randint(1, 11), random.randint(1, 10)]        # Gives the player 2 cards with a max value of 21
    man_hand = [random.randint(1, 11), random.randint(1, 10)]           # Gives the man 2 cards with a max value of 21
    spacing()
    print("Man's first card: ", man_hand[0])        # Shows the first card in the man's hand
    print("Your cards: ", player_hand)              # Shows the cards in players hand
    print("Your hand value: ", sum(player_hand))    # Shows the sum of the players hand
    player_choice = "y"
    while sum(player_hand) < 21 and player_choice == "y":       # This will run whenever the player asks for a hit
        while True:
            try:
                player_choice = input("Would you like to hit? (Y/N): ").lower()
                if player_choice == "y" or player_choice == "n":        #Error detection
                    break
                else:
                    print("Error. Please choose either Y or N")
            except ValueError:
                print("Error. Please choose either Y or N")
        if player_choice == "n":
            break

        player_hand.append(random.randint(1, 10))       #Gives the player a random card
        print("Your cards: ", player_hand)
        print("Your hand value: ", sum(player_hand))
        print("")

    if sum(player_hand) > 21:       # Checks if the player's hand is a bust
        print("Bust! You lose.")
        blackjack_winner = "Lose"
    else:
        while sum(man_hand) < 17:       # Checks if the man has lower than 17, then they will hit
            man_hand.append(random.randint(1, 10))
        print("Man's hand: ", man_hand)
        print("Man's hand value: ", sum(man_hand))
        if sum(man_hand) > 21 or sum(player_hand) > sum(man_hand):  # Checks if the player wins
            print("You win!")
            blackjack_winner = "Win"
        elif sum(player_hand) < sum(man_hand):      # Checks if the man wins
            print("You lose!")
            blackjack_winner = "Lose"
        else:                                       # If player and man have the same card value then it'll be a tie
            print("Tie")
            blackjack_winner = "Tie"



def room_1():   # This is the function for the first room of my escape room
    global player_stats
    global questions_correct         # Making a few variables global as they will be changed in the room
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
            print("Would you like to: 1. Run away quickly | 2. Slowly walk away | 3. Try and attack them")      # Gives the player choices so that they can choose their own storyline
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
    print("WELCOME TO THE AFRICAN CONTINENT QUIZ")
    print("YOU MUST GET 3 OUT OF 5 QUESTIONS CORRECT TO UNLOCK THE SECRET CODE")
    quiz_room_1()
    if questions_correct >= 3:
        spacing()
        print("CONGRATULATIONS YOU HAVE UNLOCKED THE SECRET CODE")
        print("CODE: 4830")
        inventory.append(4830)
    else:
        questions_correct = 0
        player_stats["Brainpower"] -= 10        # Lowers player brainpower stat as they lost the quiz
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
    if questions_correct >= 3:      # Makes sure this line doesnt run if the player gets less than 3 questions correct in the quiz
        print("")
        print("You have obtained the secret code")
        print("You open your phone and start typing in the code")
        time.sleep(1)
        print("4830")
        time.sleep(2)
        print("")
        print("Your phone starts shaking and the world around you starts to fall apart")
        print("The ground underneath you starts breaking and you fall into a void")
        room_1_completed = True

def room_2():       # This function will run the second room of the game
    global room_2_completed
    global ttt_result        # Making a few variables global as they will be changed in the room
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
    if ttt_result == "win":     # ttt_result comes from the tic_tac_toe() function
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
        inventory.append(0)     # The 0 adds a number so that there is a space in the inventory for the code
    else:
        print("You have drawn the tic tac toe game against the mysterious man")
        print("He lets out a deep breath and says 'What an exciting game'")
        print("You shrug, disappointed in your loss, but the man tells you one thing before vanishing")
        print("The man quickly says 'remember this number, it might be of use to you. 2'")
        print("You don't know for sure what to do with this information, but you piece together that it must be the first number in the code to escape the second room")
        inventory.append(2000)      # The 0s fill in the empty 3 numbers
    spacing()
    print("After your game with the mysterious man, you start looking around the beach again and in the distance you see some light")
    print("")
    print("You decide to follow the light and as you walk you notice that the light is coming from a small village")
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
    if player_choice == 1:      # This is when the player chooses to run away from the village
        print("")
        print("You start sprinting away from the village as fast as you can without looking behind at all")
        random_chance = random.randint(1, 2)    # This will give the player a 50/50 if they get left alone or they get chased
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
        blackjack()
        if blackjack_winner == "Tie":
            spacing()
            print("The man shrugs at the tie, but liked the amount of effort you put in")
            print("He decides to give you a hint on what the code is")
            print("")
            print("The hint is: take half of the first rooms number and you'll see what you need")
            print("")
            print("You look into your inventory and see: 4830")
            print("You use your quick maths skills and figure out that the code must be 2415")
            print("")
            time.sleep(2)
            print("You take out your phone and start typing the code in")
            print("")
            print("2415")
            print("")
            time.sleep(2)
            print("Code accepted.")
            print("Your phone starts shaking and you prepare to be teleported to the final room")
            inventory[1] = 2415
            room_2_completed = True

        elif blackjack_winner == "Lose":
            spacing()
            print("The man feels bad for beating you, so he decides to give you a hint")
            time.sleep(1)
            print("")
            print("'Half'")
            print("")
            time.sleep(2)
            print("You think for a second before realising that maybe half means half of the code that you got from the first room")
            print("You remember the code is 4830")
            print("")
            if player_stats["Brainpower"] >= 60
                print("As you are smart, you figure out that the code must be 2415")
                print("")
                time.sleep(2)
                print("You take out your phone and start typing the code in")
                print("")
                print("2415")
                print("")
                time.sleep(2)
                print("Code accepted.")
                print("Your phone starts shaking and you prepare to be teleported to the final room")
                inventory[1] = 2415
                room_2_completed = True
            else:
                print("As you aren't very smart, you have to try and guess the number")
                print("You narrow it down to either 2415, 2345, or 8860")
                while True:
                    try:
                        player_choice = int(input("What would you like to guess? 1. 2415 | 2. 2345 | 3. 8860"))
                        if player_choice < 1 or player_choice > 3:
                            print("Error. Please enter a number from 1 to 3")
                        else:
                            break
                    except ValueError:
                        print("Error. Please enter a number from 1 to 3")
                if player_choice == 1:
                    print("")
                    time.sleep(2)
                    print("You take out your phone and start typing the code in")
                    print("")
                    print("2415")
                    print("")
                    time.sleep(2)
                    print("Code accepted.")
                    print("Your phone starts shaking and you prepare to be teleported to the final room")
                    inventory[1] = 2415
                    room_2_completed = True
                else:
                    print("")
                    print("You type the code into your phone but your phone starts violently shaking and blasts you with a stat-reducing beam")
                    player_stats["Brainpower"] -= random.randint(1,10)      # These lines give the player a stat reduction
                    player_stats["Strength"] -= random.randint(1,10)
                    player_stats["Health"] -= random.randint(1,10)
                    player_stats["Speed"] -= random.randint(1,10)
                    print("")
                    display_player_stats()
                    print("")
                    print("You decide to try and do the calculation again and you figure out that the code was actually 2415")
                    print("")
                    time.sleep(2)
                    print("You take out your phone and start typing the code in")
                    print("")
                    print("2415")
                    print("")
                    time.sleep(2)
                    print("Code accepted.")
                    print("Your phone starts shaking and you prepare to be teleported to the final room")
                    inventory[1] = 2415
                    room_2_completed = True
        else:
            spacing()
            print("The man congratulates you on winning the blackjack game and hands you a piece of paper with the code to escape on it")
            print("")
            print("'2415'")
            print("")
            time.sleep(2)
            print("You take out your phone and start typing the code in")
            print("")
            print("2415")
            print("")
            time.sleep(2)
            print("Code accepted.")
            print("Your phone starts shaking and you prepare to be teleported to the final room")
            inventory[1] = 2415
            room_2_completed = True

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
            print("You try attacking them back, but they overpower you")
            player_stats["Health"] -= 20
            player_stats["Strength"] -= 20
            time.sleep(1)
            print("")
            print("After pinning you down to the ground, the lead samurai asks you 'What are you doing here?'")
            print("You explain how you are just looking for a code, and wish to be out of their way after you get it")
            time.sleep(1)
            print("The samurai look confused, as they do not know what this code is")
            print("")
            print("Thinking quickly, you decide to try and distract the samurai by telling them theres a flying piece of sushi in the distance")
            spacing()
            print("The gullible samurai actually decide to look at where you're pointing and you take the opportunity to run past them into the village")
            time.sleep(3)
            spacing()
            print("You enter the village, and immediately start searching for clues to the code")
            print("")
            while True:
                try:
                    print("Where would you like to search?")
                    player_choice = int(input("1. Count every blade of grass in a garden | 2. Ask every person there until you get a code: "))
                    if player_choice == 1 or player_choice == 2:
                        break
                    else:
                        print("Error. Please enter either 1 or 2")
                except ValueError:
                    print("Error. Please enter either 1 or 2")
            if player_choice == 1:
                print("")
                print("You decide to count every blade of grass in a garden")
                print("After counting for many hours, you finally land on a number of 2415")
                print("Everyone in the village watches you confused as to what you could possibly be doing but you ignore them and type the numbers into your phone")
                print("")
                time.sleep(1)
                print("2415")
                time.sleep(1)
                print("...")
                time.sleep(2)
                print("Code accepted.")
                print("Your phone starts shaking again and you prepare to be teleported to the final room")
                inventory[1] = 2415
                room_2_completed = True
            elif player_choice == 2:
                print("")
                random_chance = random.randint(1,50)
                print("After asking", random_chance, "people, you finally get the code: 2415")
                print("Due to asking all of these people, your brainpower has dropped")
                print("Your brainpower has dropped", random_chance, "points to", player_stats["Brainpower"] - random_chance)
                player_stats["Brainpower"] -= random_chance
                spacing()
                time.sleep(2)
                print("You start typing the code into your phone")
                print("")
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
        print("You try running through the samurai but get stopped immediately by a katana")
        print("You look down, and a katana has gone through your chest and you fall down onto the ground defeated")
        time.sleep(2)
        print("While the samurais walk away, you see a 4 digit code on the back of all of their clothes reading 2415")
        print("")
        print("With no other option, you quickly take your phone out and frantically start typing out the code...")
        time.sleep(2)
        random_chance = random.randint(1,3)
        if random_chance == 1:
            print("")
            print("You type in 2415 and hit enter")
            print("")
            time.sleep(1)
            print("Code accepted.")
            print("Your phone starts shaking and you prepare to be teleported to the final room")
            inventory[1] = 2415
            room_2_completed = True
        else:
            print("")
            print("You try typing in the code, but you are too slow")
            print("You succomb to the injuries from the katana wound...")
            player_stats["Health"] = 0

def room_3():       # This will be the third and final room of the escape room
    global room_3_completed
    global player_stats     # Making a few variables global as they will be changed in the room
    global inventory
    spacing()
    display_player_stats()
    spacing()
    time.sleep(2)





# MAIN

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
            stats_boost()
            room_2()
        if room_3_completed == False and player_stats["Health"] > 0:
            stats_boost()
            room_3()

    spacing()
    print("You have died...")
    print("You were not able to escape")
    playing = False

spacing()
print("Come back and play again another time")