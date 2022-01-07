game_active = True
player_round = "X"

field = [" ",
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

def field_print():
    print(field[1] + " " + field[2] + " " + field[3])
    print(field[4] + " " + field[5] + " " + field[6])
    print(field[7] + " " + field[8] + " " + field[9])

def player_change():
    global player_round
    if player_round == "X":
        player_round = "O"
    else:
        player_round = "X"

def control_win():
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    if field[1] == field[5] == field[9]:
        return field[1]
    if field[3] == field[5] == field[7]:
        return field[3]

def control_tie():
    if (field[1] == "X" or field[1] == "O") \
    and (field[2] == "X" or field[2] == "O") \
    and (field[3] == "X" or field[3] == "O") \
    and (field[4] == "X" or field[4] == "O") \
    and (field[5] == "X" or field[5] == "O") \
    and (field[6] == "X" or field[6] == "O") \
    and (field[7] == "X" or field[7] == "O") \
    and (field[8] == "X" or field[8] == "O") \
    and (field[9] == "X" or field[9] == "O"):
        return("It's a tie")

def player_input():
    while True:
        move = input("Please enter field: ")
        try:
            move = int(move)
        except ValueError:
            print("Please enter a number from 1 to 9")
        else:
            if move >=1 and move <=9:
                return move
            else:
                print("Please enter a number from 1 to 9")

while game_active:
    print("It's player " + player_round + " round")
    player_move = player_input()
    if player_move:
        field[player_move] = player_round
        field_print()
    print("Move:" + str(player_move))
    won = control_win()
    if won:
        print("Player " + won + " wins")
        game_active = False
        break
    tie = control_tie()
    if tie:
        print(tie)
        game_active = False
        break
    player_change()