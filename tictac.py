square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
attempt = True
winner = 0
playing = True

def board():
    print(square[0], square[1], square[2])
    print(square[3], square[4], square[5])
    print(square[6], square[7], square[8])

board()
print("First turn...")
while attempt == True:
    try:
        turn1 = int(input("Player 1's turn: "))
        if turn1 < 1 or turn1 > 9:
            print("Error. Please enter a number from 1-9")
        else:
            attempt = False
    except ValueError:
        print("Error. Please enter a number from 1-9")

square[turn1 - 1] = "X"
board()

attempt = True
print("Second turn...")
while attempt == True:
    try:
        turn2 = int(input("Player 2's turn: "))
        if turn2 < 1 or turn2 > 9:
            print("Error. Please enter a number from 1-9")
        elif turn2 == turn1:
            print("Error. That place is already filled")
        else:
            attempt = False
    except ValueError:
        print("Error. Please enter a number from 1-9")

square[turn2 - 1] = "O"
board()

attempt = True
print("Third turn...")
while attempt == True:
    try:
        turn3 = int(input("Player 1's turn: "))
        if turn3 < 1 or turn3 > 9:
            print("Error. Please enter a number from 1-9")
        elif turn3 == turn2 or turn3 == turn1:
            print("Error. That place is already filled")
        else:
            attempt = False
    except ValueError:
        print("Error. Please enter a number from 1-9")

square[turn3 - 1] = "X"
board()

attempt = True
print("Fourth turn...")
while attempt == True:
    try:
        turn4 = int(input("Player 2's turn: "))
        if turn4 < 1 or turn4 > 9:
            print("Error. Please enter a number from 1-9")
        elif turn4 == turn1 or turn4 == turn2 or turn4 == turn3:
            print("Error. That place is already filled")
        else:
            attempt = False
    except ValueError:
        print("Error. Please enter a number from 1-9")

square[turn4 - 1] = "O"
board()

attempt = True
print("Fifth turn...")
while attempt == True:
    try:
        turn5 = int(input("Player 1's turn: "))
        if turn5 < 1 or turn5 > 9:
            print("Error. Please enter a number from 1-9")
        elif turn5 == turn1 or turn5 == turn2 or turn5 == turn3 or turn5 == turn4:
            print("Error. That place is already filled")
        else:
            attempt = False
    except ValueError:
        print("Error. Please enter a number from 1-9")

square[turn5 - 1] = "X"
board()
if square[0] == "X" and square[1] == "X" and square[2] == "X":
    winner = 1
elif square[3] == "X" and square[4] == "X" and square[5] == "X":
    winner = 1
elif square[6] == "X" and square[7] == "X" and square[8] == "X":
    winner = 1
elif square[0] == "X" and square[3] == "X" and square[6] == "X":
    winner = 1
elif square[1] == "X" and square[4] == "X" and square[7] == "X":
    winner = 1
elif square[2] == "X" and square[5] == "X" and square[8] == "X":
    winner = 1
elif square[0] == "X" and square[4] == "X" and square[8] == "X":
    winner = 1
elif square[2] == "X" and square[4] == "X" and square[6] == "X":
    winner = 1
elif square[0] == "O" and square[1] == "O" and square[2] == "O":
    winner = 2
elif square[3] == "O" and square[4] == "O" and square[5] == "O":
    winner = 2
elif square[6] == "O" and square[7] == "O" and square[8] == "O":
    winner = 2
elif square[0] == "O" and square[3] == "O" and square[6] == "O":
    winner = 2
elif square[1] == "O" and square[4] == "O" and square[7] == "O":
    winner = 2
elif square[2] == "O" and square[5] == "O" and square[8] == "O":
    winner = 2
elif square[0] == "O" and square[4] == "O" and square[8] == "O":
    winner = 2
elif square[2] == "O" and square[4] == "O" and square[6] == "O":
    winner = 2

if winner == 1:
    print("")
    print("")
    print("Player 1 wins!")
    playing = False
elif winner == 2:
    print("")
    print("")
    print("Player 2 wins!")
    playing = False

if playing == False:
    print("")
else:
    attempt = True
    print("Sixth turn...")
    while attempt == True:
        try:
            turn6 = int(input("Player 2's turn: "))
            if turn6 < 1 or turn6 > 9:
                print("Error. Please enter a number from 1-9")
            elif turn6 == turn1 or turn6 == turn2 or turn6 == turn3 or turn6 == turn4 or turn6 == turn5:
                print("Error. That place is already filled")
            else:
                attempt = False
        except ValueError:
            print("Error. Please enter a number from 1-9")

    square[turn6 - 1] = "O"
    board()
    if square[0] == "X" and square[1] == "X" and square[2] == "X":
        winner = 1
    elif square[3] == "X" and square[4] == "X" and square[5] == "X":
        winner = 1
    elif square[6] == "X" and square[7] == "X" and square[8] == "X":
        winner = 1
    elif square[0] == "X" and square[3] == "X" and square[6] == "X":
        winner = 1
    elif square[1] == "X" and square[4] == "X" and square[7] == "X":
        winner = 1
    elif square[2] == "X" and square[5] == "X" and square[8] == "X":
        winner = 1
    elif square[0] == "X" and square[4] == "X" and square[8] == "X":
        winner = 1
    elif square[2] == "X" and square[4] == "X" and square[6] == "X":
        winner = 1
    elif square[0] == "O" and square[1] == "O" and square[2] == "O":
        winner = 2
    elif square[3] == "O" and square[4] == "O" and square[5] == "O":
        winner = 2
    elif square[6] == "O" and square[7] == "O" and square[8] == "O":
        winner = 2
    elif square[0] == "O" and square[3] == "O" and square[6] == "O":
        winner = 2
    elif square[1] == "O" and square[4] == "O" and square[7] == "O":
        winner = 2
    elif square[2] == "O" and square[5] == "O" and square[8] == "O":
        winner = 2
    elif square[0] == "O" and square[4] == "O" and square[8] == "O":
        winner = 2
    elif square[2] == "O" and square[4] == "O" and square[6] == "O":
        winner = 2

    if winner == 1:
        print("")
        print("")
        print("Player 1 wins!")
        playing = False
    elif winner == 2:
        print("")
        print("")
        print("Player 2 wins!")
        playing = False

    if playing == False:
        print("")
    else:
        attempt = True
        print("Seventh turn...")
        while attempt == True:
            try:
                turn7 = int(input("Player 1's turn: "))
                if turn7 < 1 or turn7 > 9:
                    print("Error. Please enter a number from 1-9")
                elif turn7 == turn1 or turn7 == turn2 or turn7 == turn3 or turn7 == turn4 or turn7 == turn5 or turn7 == turn6:
                    print("Error. That place is already filled")
                else:
                    attempt = False
            except ValueError:
                print("Error. Please enter a number from 1-9")

        square[turn7 - 1] = "X"
        board()
        if square[0] == "X" and square[1] == "X" and square[2] == "X":
            winner = 1
        elif square[3] == "X" and square[4] == "X" and square[5] == "X":
            winner = 1
        elif square[6] == "X" and square[7] == "X" and square[8] == "X":
            winner = 1
        elif square[0] == "X" and square[3] == "X" and square[6] == "X":
            winner = 1
        elif square[1] == "X" and square[4] == "X" and square[7] == "X":
            winner = 1
        elif square[2] == "X" and square[5] == "X" and square[8] == "X":
            winner = 1
        elif square[0] == "X" and square[4] == "X" and square[8] == "X":
            winner = 1
        elif square[2] == "X" and square[4] == "X" and square[6] == "X":
            winner = 1
        elif square[0] == "O" and square[1] == "O" and square[2] == "O":
            winner = 2
        elif square[3] == "O" and square[4] == "O" and square[5] == "O":
            winner = 2
        elif square[6] == "O" and square[7] == "O" and square[8] == "O":
            winner = 2
        elif square[0] == "O" and square[3] == "O" and square[6] == "O":
            winner = 2
        elif square[1] == "O" and square[4] == "O" and square[7] == "O":
            winner = 2
        elif square[2] == "O" and square[5] == "O" and square[8] == "O":
            winner = 2
        elif square[0] == "O" and square[4] == "O" and square[8] == "O":
            winner = 2
        elif square[2] == "O" and square[4] == "O" and square[6] == "O":
            winner = 2

        if winner == 1:
            print("")
            print("")
            print("Player 1 wins!")
            playing = False
        elif winner == 2:
            print("")
            print("")
            print("Player 2 wins!")
            playing = False

        if playing == False:
            print("")
        else:
            attempt = True
            print("Eighth turn...")
            while attempt == True:
                try:
                    turn8 = int(input("Player 2's turn: "))
                    if turn8 < 1 or turn8 > 9:
                        print("Error. Please enter a number from 1-9")
                    elif turn8 == turn1 or turn8 == turn2 or turn8 == turn3 or turn8 == turn4 or turn8 == turn5 or turn8 == turn6 or turn8 == turn7:
                        print("Error. That place is already filled")
                    else:
                        attempt = False
                except ValueError:
                    print("Error. Please enter a number from 1-9")

            square[turn8 - 1] = "O"
            board()
            if square[0] == "X" and square[1] == "X" and square[2] == "X":
                winner = 1
            elif square[3] == "X" and square[4] == "X" and square[5] == "X":
                winner = 1
            elif square[6] == "X" and square[7] == "X" and square[8] == "X":
                winner = 1
            elif square[0] == "X" and square[3] == "X" and square[6] == "X":
                winner = 1
            elif square[1] == "X" and square[4] == "X" and square[7] == "X":
                winner = 1
            elif square[2] == "X" and square[5] == "X" and square[8] == "X":
                winner = 1
            elif square[0] == "X" and square[4] == "X" and square[8] == "X":
                winner = 1
            elif square[2] == "X" and square[4] == "X" and square[6] == "X":
                winner = 1
            elif square[0] == "O" and square[1] == "O" and square[2] == "O":
                winner = 2
            elif square[3] == "O" and square[4] == "O" and square[5] == "O":
                winner = 2
            elif square[6] == "O" and square[7] == "O" and square[8] == "O":
                winner = 2
            elif square[0] == "O" and square[3] == "O" and square[6] == "O":
                winner = 2
            elif square[1] == "O" and square[4] == "O" and square[7] == "O":
                winner = 2
            elif square[2] == "O" and square[5] == "O" and square[8] == "O":
                winner = 2
            elif square[0] == "O" and square[4] == "O" and square[8] == "O":
                winner = 2
            elif square[2] == "O" and square[4] == "O" and square[6] == "O":
                winner = 2

            if winner == 1:
                print("")
                print("")
                print("Player 1 wins!")
                playing = False
            elif winner == 2:
                print("")
                print("")
                print("Player 2 wins!")
                playing = False

            if playing == False:
                print("")
            else:
                attempt = True
                print("Ninth turn...")
                while attempt == True:
                    try:
                        turn9 = int(input("Player 1's turn: "))
                        if turn9 < 1 or turn9 > 9:
                            print("Error. Please enter a number from 1-9")
                        elif turn9 == turn1 or turn9 == turn2 or turn9 == turn3 or turn9 == turn4 or turn9 == turn5 or turn9 == turn6:
                            print("Error. That place is already filled")
                        else:
                            attempt = False
                    except ValueError:
                        print("Error. Please enter a number from 1-9")

                square[turn9 - 1] = "X"
                board()
                if square[0] == "X" and square[1] == "X" and square[2] == "X":
                    winner = 1
                elif square[3] == "X" and square[4] == "X" and square[5] == "X":
                    winner = 1
                elif square[6] == "X" and square[7] == "X" and square[8] == "X":
                    winner = 1
                elif square[0] == "X" and square[3] == "X" and square[6] == "X":
                    winner = 1
                elif square[1] == "X" and square[4] == "X" and square[7] == "X":
                    winner = 1
                elif square[2] == "X" and square[5] == "X" and square[8] == "X":
                    winner = 1
                elif square[0] == "X" and square[4] == "X" and square[8] == "X":
                    winner = 1
                elif square[2] == "X" and square[4] == "X" and square[6] == "X":
                    winner = 1
                elif square[0] == "O" and square[1] == "O" and square[2] == "O":
                    winner = 2
                elif square[3] == "O" and square[4] == "O" and square[5] == "O":
                    winner = 2
                elif square[6] == "O" and square[7] == "O" and square[8] == "O":
                    winner = 2
                elif square[0] == "O" and square[3] == "O" and square[6] == "O":
                    winner = 2
                elif square[1] == "O" and square[4] == "O" and square[7] == "O":
                    winner = 2
                elif square[2] == "O" and square[5] == "O" and square[8] == "O":
                    winner = 2
                elif square[0] == "O" and square[4] == "O" and square[8] == "O":
                    winner = 2
                elif square[2] == "O" and square[4] == "O" and square[6] == "O":
                    winner = 2

                if winner == 1:
                    print("")
                    print("")
                    print("Player 1 wins!")
                    playing = False
                elif winner == 2:
                    print("")
                    print("")
                    print("Player 2 wins!")
                    playing = False

                if playing == False:
                    print("")
                else:
                    print("")
                    print("")
                    print("Draw.")