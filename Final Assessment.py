    #----------Vihaan Kapoor Final Assessment 91896----------

#IMPORTS

import random
import time

#VARIABLES

player_stats = {"Health" : 80, "Speed" : 60, "Brainpower" : 75, "Strength" : 70}    # This is my dictionary for the player's stats. These stats will affect the players score at the end of the game
inventory = []   # This is where any items that the player collects will be stored
questions_correct = 0   # This will be used during quizzes within the game
room_1_completed = False
room_2_completed = False       # These tell the program if each room has been completed
room_3_completed = False
playing = True
player_choice = 0       # This will be the variable that changes depending on what the player chooses throughout the game
room_2_board = []       # This will be the tic tac toe board in the second room
ttt_result = 0
blackjack_winner = 0
rugby_game_winner = 0
combination_lock_winner = 0
room_3_fishing_chance = 0
room_3_lock_combination = []

#FUNCTIONS

def reset_variables():
    global player_stats
    global inventory
    global questions_correct
    global room_1_completed
    global room_2_completed
    global room_3_completed
    global room_2_board
    global ttt_result
    global blackjack_winner
    global rugby_game_winner
    global combination_lock_winner
    global room_3_fishing_chance
    global room_3_lock_combination
    player_stats = {"Health": 80, "Speed": 60, "Brainpower": 75, "Strength": 70}
    inventory = []
    questions_correct = 0
    room_1_completed = False
    room_2_completed = False
    room_3_completed = False
    room_2_board = []
    ttt_result = 0
    blackjack_winner = 0
    rugby_game_winner = 0
    combination_lock_winner = 0
    room_3_fishing_chance = 0
    room_3_lock_combination = []

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
    player_stats["Speed"] += random.randint(5, 25)      # Each stat can have a random 5-25 value added to it
    player_stats["Brainpower"] += random.randint(5, 25)
    player_stats["Strength"] += random.randint(5, 25)

def stat_drop():
    global player_stats
    player_stats["Speed"] -= random.randint(5, 25)
    player_stats["Brainpower"] -= random.randint(5, 25)     # Each stat is reduced except for health so that the player does not lose the game immediately from the stat drop
    player_stats["Strength"] -= random.randint(5, 25)

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

    if play_game == "Y" or play_game == "YES":      # Allows the player to say Yes as well as Y
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
            player_choice = int(input("1. Africlanker | 2. Alkebulan | 3. Alpaca: "))       # Questions are simple and get progressively harder
            if player_choice > 0 and player_choice < 4:
                break
            else:
                print("Error. Please enter a number for the answers listed")
        except ValueError:
            print("Error. Please enter a number for the answers listed")
    if player_choice == 1 or player_choice == 3:
        print("")
        print("INCORRECT. You have", questions_correct, "correct answer(s)")        # Tells the player how many correct answers they have
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
            if player_choice > 0 and player_choice < 4:     # Error detection for every player choice
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
    print(room_2_board[3], "|", room_2_board[4], "|", room_2_board[5])      # Prints the board so that it looks normal visually to the player
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
        room_2_board.append(i + 1)      # Quickly adds all the values to the board
    display_board(room_2_board)
    print("Your pieces are Xs. The mans pieces are Os")
    time.sleep(1)

    for turn in range(8):   # Max of 9 turns in a tic tac toe game (starting at 0)
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:       # Even number turns will be the player's turn
            print("Your turn...")
            while True:
                try:
                    player_move = int(input("Choose your position from 1-9: "))
                    if player_move < 1 or player_move > 9:
                        print("Error. Please choose a number from 1-9")
                    elif room_2_board[player_move - 1] == "X" or room_2_board[player_move - 1] == "O":      # Makes sure player chooses an empty space
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

def room_3_rugby_game():
    global rugby_game_winner
    print("")
    print("You will have 2 attempts to score a try from a random distance")
    print("You can choose how to play each attempt, and you will have 3 phases in each attempt to get to the try line")
    for attempt in range(1,3):      # repeats twice for 2 attempts
        print("Attempt", attempt, "of 2")

        distance_to_try = random.randint(10,50)     # Makes the distance to the try line random
        print("You are", distance_to_try, "m from the try line")

        for phase in range(1,4):    # repeats 3 times for 3 phases
            print("")
            print("Phase", phase, "|", distance_to_try, "m to try line")
            while True:
                try:
                    print("What would you like to do?")
                    player_choice = int(input("1. Run | 2. Pass | 3. Kick: "))
                    if player_choice < 1 or player_choice > 3:
                        print("Error. Please choose a number from 1 to 3")
                    else:
                        break
                except ValueError:
                    print("Error. Please choose a number from 1 to 3")

            print("")
            time.sleep(1)

            if player_choice == 1:      # If the player chooses to run
                territory_gain = random.randint(3,12)
                print("You run forward through the defence and gain", territory_gain, "m")
            elif player_choice == 2:    # If the player chooses to pass
                territory_gain = random.randint(4,15)
                print("A well placed pass gains", territory_gain, "m")
            else:                       # If the player chooses to kick
                territory_gain = random.randint(5,25)
                print("A kick up past the defence gains", territory_gain, "m")
            distance_to_try -= territory_gain

            if distance_to_try <= 0:        # If the player has scored a try
                print('TRY! You scored the try for your team')
                rugby_game_winner = "win"
                break
        if rugby_game_winner == "win":
            break
        if distance_to_try > 0:     # If player does not score a try
            print("")
            print("You ran out of phases and did not score a try")
            print("You were", distance_to_try, "m short of a try")
            if attempt < 2:     # If player has another attempt
                time.sleep(2)
                print("")
                print("You have one more chance to score")
            else:
                print("")
                print("Game over. You couldn't score a try")
                rugby_game_winner = "lose"

def combination_lock_puzzle():      # This will be the cobination lock in the
    global combination_lock_winner
    global room_3_lock_combination
    spacing()
    print("Welcome to the combination lock puzzle")
    print("")
    print("There are 4 dials which have to be turned to match the code to get in the hut")
    print("Solve each clue given to find the digits for the lock")
    time.sleep(2)

    clues = [                                       # These are the questions as well as the answers
        ("How many sides does a triangle have?", 3),
        ("What is 20 divided by 5?", 4),
        ("How many legs does a spider have minus 7?", 1),
        ("What is 3 squared minus 2?", 7)
    ]
    answers = []            # The player's answers will go in here
    tries = 3               # The player gets 3 tries before failing the lock

    for i in range(len(clues)):
        clue, answer = clues[i]     # clue will be the clue itself, and answer will be the number that corresponds to the clue
        solved = False
        print("Dial", i + 1, ":", clue)
        while solved == False:
            if tries <=0:
                break
            else:
                try:
                    print("")
                    guess = int(input("Your answer: "))
                    if guess == answer:                     # If the player guesses correctly
                        print("")
                        print("Correct!")
                        answers.append(guess)
                        solved = True
                    else:                                   # If the player guesses wrong
                        tries -=1
                        print("")
                        print("Incorrect! Tries remaining:", tries)
                        if tries <= 0:
                            break
                        else:
                            print("Dial", i + 1, ":", clue)
                except ValueError:
                    print("Error. Please enter a number from 0-9")

        if tries <= 0:
            break

    spacing()
    if tries > 0:
        print("You cracked the lock")
        print(answers)                              # Shows the players the answers
        room_3_lock_combination.append(answers)     # Puts the answers that the player got into a global variable to be used later
        combination_lock_winner = True              # Tells the game if the player has cracked the combination lock
    else:
        print("You ran out of tries")
        print("The lock stays closed")
        print("You are left with", answers)
        room_3_lock_combination.append(answers)
        combination_lock_winner = False             # Tells the game that the player failed to crack the combination lock

def room_3_number_guessing(x):       # This is the function for the player guessing the last number(s) of the code in the 3rd room
    answer = x
    spacing()
    print("Guess a number from 0-9")
    while True:
        try:
            guess = int(input("Your guess: "))
            if guess == answer:
                print("Correct! The number was", x)
                break
            elif guess < answer:
                print("Incorrect. The number is higher")
            else:
                print("Incorrect. The number is lower")
        except ValueError:
            print("Error. Please enter a number from 0-9")

def fishing_slot_game():        # This is the function for the fishing game in the third room
    global room_3_fishing_chance
    spacing()
    print("Welcome to the fishing game")
    print("")
    print("Press 1 to cast your rod, or 2 to quit and take your chances with whatever you have caught")
    time.sleep(1)

    score = 0

    while True:         # The player can reroll for as long as they want
        try:
            print("Score: ", score)
            print("Would you like to cast again or quit?")
            player_choice = int(input("Press 1 to cast | Press 2 to quit: "))

            if player_choice == 2:
                print("You step back and will take your chances with whatever you have caught with score: ", score)
                break
            else:
                print("You cast your rod")
                print("")

            slot_1 = random.randint(1, 9)
            slot_2 = random.randint(1, 9)
            slot_3 = random.randint(1, 9)

            print(slot_1, slot_2, slot_3)
            time.sleep(0.5)

            score = slot_1 + slot_2 + slot_3

        except ValueError:
            print("Error. Please enter a number either 1 or 2")

    if score >= 25:
        room_3_fishing_chance = 100         # Gives the player different odds based on what fish they end up with
    elif score >= 20:
        room_3_fishing_chance = 90
    elif score >= 15:
        room_3_fishing_chance = 80
    elif score >= 10:
        room_3_fishing_chance = 70
    else:
        room_3_fishing_chance = 50





def room_1():   # This is the function for the first room of my escape room
    global player_stats
    global questions_correct         # Making a few variables global as they will be changed in the room
    global inventory
    global room_1_completed
    spacing()       # Adds some spacing to make the game look cleaner
    print("Welcome to Room 1")
    print("This room has a theme of Africa")
    print("Find the code to escape. Good luck")
    print("")
    print("While exploring the savannah, you come across a pride of lions")
    while True:     # Error detection
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
        random_chance = random.randint(1,10)        # Taking some random numbers so there is some randomness in the game
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
        random_chance = random.randint(1,2)     # 50/50 chance
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

    print("")       # Story goes back to a normal place after the lion encounter no matter what happens with the lions
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
        inventory.append(4830)      # Adds the code to the player's inventory for future use
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
                player_stats["Health"] = 0      # Breaks the while health is greater than 0 loop in the main loop and finishes the game as a loss
    spacing()
    if questions_correct >= 3:      # Makes sure this line doesn't run if the player gets less than 3 questions correct in the quiz
        print("")
        print("You have obtained the secret code")
        print("You open your phone and start typing in the code")
        time.sleep(1)
        print("4830")
        time.sleep(2)
        print("")
        print("Your phone starts shaking and the world around you starts to fall apart")
        print("The ground underneath you starts breaking and you fall into a void")
        room_1_completed = True     # Makes sure room 1 is not repeated after the player has finished the game

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
        try:        # Error detection
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
        blackjack()     # Blackjack game in another function so it can be edited easily and won't be too complicated
        if blackjack_winner == "Tie":   # variable comes from the blackjack() function
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
            inventory[1] = 2415     # Completes the code in player's inventory
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
            if player_stats["Brainpower"] >= 60:
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
                time.sleep(1)       # time.sleep used to create some tension for the player typing in the code
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
        random_chance = random.randint(1,3)     # Gives the player a 33% chance of surviving after making a bad decision earlier in the game by attacking the samurai
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
    print("Welcome to room 3 (The final room)")     # Reminds the player that this is the final room
    print("This room has a theme of New Zealand")
    print("Find the code to escape. Good luck")
    spacing()
    time.sleep(1)
    print("With a new burst of confidence, you remember what you learned from the previous rooms, and you immediately start searching for any clues towards the code")
    print("")
    time.sleep(1.5)
    print("In the distance, you see a group of people playing a game of rugby")
    print("You approach them, and someone asks you if you would like to join in")
    time.sleep(1)
    print("You say yes, as it might take your mind off the code a little bit")
    spacing()
    print("You join into the rugby game, and are placed on the wing")
    print("Somehow, the captain of the opposition team knows that you are looking for the code. He tells you that if you can score a try, he will give you a hint of what the code is")
    print("")
    room_3_rugby_game()             # This function runs the rugby game
    if rugby_game_winner == "win":          # This variable comes from the rugby game function
        spacing()
        print("You won the rugby game")
        print("The opposing captain approaches you and hands you a piece of paper with the hint for the code on it")
        print("The paper says 'The code is the score from the rugby world cup final in 2015 NZ-AUS'")
        print("")
        while True:
            try:
                print("")
                print("Would you like to try and guess the code? (Getting the code wrong can lead to a stat loss)")
                player_choice = input("Y for Yes | N for No: ").upper()         # Lets the player choose if they want to risk their stats to try and win early
                if player_choice == "Y" or player_choice == "YES" or player_choice == "N" or player_choice == "NO":
                    break
                else:
                    print("Error. Please choose either Y or N")
            except ValueError:
                print("Error. Please choose either Y or N")

        if player_choice == "Y" or player_choice == "YES":      # If player says yes to guessing the code
            while True:
                try:
                    print("")
                    player_choice = int(input("What would you like to guess?: "))
                    spacing()
                    print("You pull out your phone and start typing in the code")
                    print(player_choice)
                    print("")
                    time.sleep(2)
                    print("...")
                    time.sleep(2)
                    print("")
                    if player_choice == 3417:
                        print("Code accepted.")
                        inventory.append(3417)      # Adds the final code to the player's inventory
                        print("You let out a sigh of relief as your phone starts shaking again to teleport you out of the escape room")
                        room_3_completed = True
                        break
                    else:
                        print("Code not accepted.")
                        print("")
                        stat_drop()         # Gives the player a stat drop for getting the code wrong
                        break
                except ValueError:
                    print("Error. Please enter the code as a 4 digit number")

        elif player_choice == "N" or player_choice == "NO":     # If the player says no to guessing the code
            print("")
            print("You are not too sure about what the code could be yet, but you keep the hint in your mind so if you see another hint you can work it out")

        if room_3_completed != True:
            spacing()
            print("You walk away from the rugby game, still thinking about what the code could be when rain starts pouring down violently")
            print("You see a small hutt in the distance, so you run towards it in hope of shelter")
            time.sleep(2)
            print("When you get to the hut, you notice there is a combination lock attached to the door, with a sign with instructions on how to open it...")
            combination_lock_puzzle()
            time.sleep(2)
            spacing()
            if combination_lock_winner == True:         # If the player beats the combination lock puzzle
                print("You enter the hut, and look outside. It's still pouring down with rain")
                time.sleep(1)
                print("You hold the combination lock in your hand and think to yourself: it would be crazy if the code to escape was the combination lock's code")
                time.sleep(1)
                print("With nothing really to lose, you pull out your phone and start typing")
                print("")
                time.sleep(1)
                print("3417")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("Code accepted.")
                print("Your jaw drops as your phone starts shaking again and you prepare to teleport out of the escape room")
            else:           # If the player does not beat the combination lock puzzle
                print("You are stuck outside in the rain, slowly getting colder and colder")
                player_stats["Strength"] -= 20    # Player strength drops due to cold
                print("You are left with digits: ", room_3_lock_combination)
                print("")
                time.sleep(1)
                print("You think to yourself. Maybe the combination lock is the code to escape this room")
                print("")
                time.sleep(2)
                if len(room_3_lock_combination) == 3:       # If the player has 3 digits
                    print("You look at the numbers you have: 341 and think about what the last digit could be")
                    print("You know that the code is the score of a rugby game, so you start thinking to yourself, what would have the score been")
                    print("It would be 34-1_ but you can't think of what the missing number would be")
                    print("")
                    time.sleep(1.5)
                    print("You look at your phone and it says: TRY AND GUESS THE MISSING NUMBER AND I WILL TELL YOU IF THE ANSWER IS HIGHER OR LOWER")
                    print("")
                    time.sleep(1)
                    print("You decide to try and guess the number as you don't have any better ideas")
                    room_3_number_guessing(7)
                    spacing()
                    print("Now that you have found the last number, you enter the code into your phone")
                    print("")
                    time.sleep(1)
                    print("3417")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Code accepted.")
                    print("")
                    print("You close your eyes and prepare to be teleported out of the escape room")
                elif len(room_3_lock_combination) == 2:          # If the player has 2 digits
                    print("You look at the numbers you have: 34 and think about what the last 2 digits could be")
                    print("You know that the code is the score of a rugby game, so you start thinking to yourself, what would have the score been")
                    print("It would be 34-__ but you can't think of what the missing numbers would be")
                    print("")
                    time.sleep(1.5)
                    print("You look at your phone and it says: TRY AND GUESS THE MISSING NUMBERS AND I WILL TELL YOU IF THE ANSWERS ARE HIGHER OR LOWER")
                    print("")
                    time.sleep(1)
                    print("You decide to try and guess the numbers as you don't have any better ideas")
                    room_3_number_guessing(1)
                    print("")
                    time.sleep(1)
                    print("Now you have 3 numbers, so you try to guess the last number as well")
                    room_3_number_guessing(7)
                    time.sleep(2)
                    spacing()
                    print("Now that you have found the last numbers, you enter the code into your phone")
                    print("")
                    time.sleep(1)
                    print("3417")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Code accepted.")
                    print("")
                    print("You close your eyes and prepare to be teleported out of the escape room")
                elif len(room_3_lock_combination) == 1:      # If the player has 1 digit
                    print("You look at the number you have: 3 and think about what the last 3 digits could be")
                    print("You know that the code is the score of a rugby game, so you start thinking to yourself, what would have the score been")
                    print("It would be 3_-__ but you can't think of what the missing numbers would be")
                    print("")
                    time.sleep(1.5)
                    print("You look at your phone and it says: TRY AND GUESS THE MISSING NUMBERS AND I WILL TELL YOU IF THE ANSWERS ARE HIGHER OR LOWER")
                    print("")
                    time.sleep(1)
                    print("You decide to try and guess the numbers as you don't have any better ideas")
                    room_3_number_guessing(4)
                    print("")
                    time.sleep(1)
                    print("Now you have 2 numbers, so you try to guess the last 2 numbers as well")
                    room_3_number_guessing(1)
                    print("")
                    time.sleep(1)
                    print("Now you have 3 numbers, so you try to guess the final number")
                    room_3_number_guessing(7)
                    time.sleep(2)
                    spacing()
                    print("Now that you have found all the missing numbers, you enter the code into your phone")
                    print("")
                    time.sleep(1)
                    print("3417")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Code accepted.")
                    print("")
                    print("You close your eyes and prepare to be teleported out of the escape room")
                else:           # If the player has 0 digits of the code
                    print("You have none of the numbers that you need to get the code")
                    print("You look at your phone and it says: TRY AND GUESS THE MISSING NUMBERS AND I WILL TELL YOU IF YOUR ANSWERS ARE TOO HIGH OR TOO LOW")
                    print("")
                    time.sleep(1)
                    print("You decide to try and guess the numbers as you don't have any better ideas")
                    room_3_number_guessing(3)
                    print("")
                    time.sleep(1)
                    print("Now you have 1 number, so you try to guess the other 3 numbers")
                    room_3_number_guessing(4)
                    print("")
                    time.sleep(1)
                    print("Now you have 2 numbers, so you try to guess the final 2 numbers")
                    room_3_number_guessing(1)
                    time.sleep(1)
                    print("Now you have 3 numbers, so you try and guess the final number")
                    time.sleep(2)
                    spacing()
                    print("Now that you have found all the missing numbers, you enter the code into your phone")
                    print("")
                    time.sleep(1)
                    print("3417")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Code accepted.")
                    print("")
                    print("You close your eyes and prepare to be teleported out of the escape room")
                inventory.append(3417)      # Adds the code to the player's inventory
                room_3_completed = True          # Tells the program that the player has completed the third room

    if rugby_game_winner == "lose":     # If the player loses the rugby game
        spacing()
        print("You lost the rugby game")
        print("You leave the park without saying anything except 'Good Game' to all of your teammates")
        print("")
        print("Back into the search for clues to the code, you come across the mysterious man again")
        print("")
        print("You walk towards the man, and ask him to help you")
        time.sleep(1)
        print("The man tells you that he will tell you the code, as long as you help him catch a fish")
        print("You quickly agree, and he tells you to follow him to his boat")
        print("The man tells you on the ride to the fishing spot that the better score the fish is, the higher the chance that he'll give you the code")
        time.sleep(1)
        print("'But if the fish isn't a high enough score, I might have to throw you overboard'")
        print("")
        time.sleep(1)
        print("A shiver runs down your spine, but you take the chances, and agree")
        print("You know that you need to make sure the fish is as good as possible")
        fishing_slot_game()
        spacing()
        random_chance = random.randint(1,100)       # This is a percentage chance and will determine if the player gets the code from the man or not
        if random_chance > room_3_fishing_chance:       # This is for when the fish isn't good enough
            print("The man looks at you and says 'That fish isn't good enough'")
            print("He throws you overboard, and you are unable to get back to the shore")
            print("You slowly drown, as you watch the man speed away")
            player_stats["Health"] = 0          # Makes the player lose the game instantly
        else:       # This is for when the player will get the code
            print("The man looks at the fish that you caught for him and is pleased")
            print("He hands you a piece of paper with 4 digits on it, and he tells you to put it in your phone and get out of here")
            print("")
            time.sleep(2)
            print("You take out your phone and start typing the code in")
            time.sleep(1)
            print("")
            print("...")
            time.sleep(1)
            print("")
            print("Code accepted.")
            print("Your phone starts shaking and you nod to the man as you prepare to teleport out of the escape room")
            inventory.append(3417)
            room_3_completed = True     # Finishes the room

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
        if room_1_completed == True and room_2_completed == True and room_3_completed == True:
            spacing()
            print("You have completed the escape room")
            print("You wake up in Te Papa Museum and the familiar face of the man from the escape room greets you")
            print("The man tells you that it was all a simulation, and you are one of the first to complete the entire thing")
            final_score = player_stats["Health"] + player_stats["Strength"] + player_stats["Speed"] + player_stats["Brainpower"]
            print("He also tells you that your score was", final_score)
            spacing()
            print("The man asks you. 'Do you want to try again?'")
            while True:
                try:
                    player_choice = int(input("1 to play again | 2 to quit"))       # Lets the player choose to play again or quit
                    if player_choice == 1 or player_choice == 2:
                        break
                    else:
                        print("Error. Please enter either 1 or 2")
                except ValueError:
                    print("Error. Please enter either 1 or 2")
            if player_choice == 1:      # If the player wants to play again
                playing = True
                reset_variables()
                starting_sequence()
                time.sleep(2)
            else:                   # If the player does not want to play again
                playing = False
        else:
            spacing()
            print("You have died...")
            print("You were not able to escape")
            playing = False

spacing()
print("Come back and play again another time")