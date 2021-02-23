#Algorithm

'''#--->create board
#--->two players
#--->flip(swap) players
-->check who is the winner
   -->rows(3)
   -->columns(3)
   -->diagonals(2)
-->drawn'''

#player-->X
#player2-->O

#creation of the board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

current_player="X"
gameisgoing=True
winner=None
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn():
    position=int(input("Choose a random position from 0 to 8:"))#0
    if position<8:
        board[position] = current_player


    if position>8:
        position = int(input("Choose a random position from 0 to 8:"))

    board[position] = current_player

def swap_players():
    global current_player
    if current_player=="X":
        current_player="Y"
    elif current_player=="Y":
        current_player="X"

def check_who_is_the_winner():
    global winner
    rowwinner=check_row()
    colwinner=check_column()
    diawinner=check_diagonal()
    check_tie()
    

    if rowwinner:
        winner=rowwinner
    elif colwinner:
        winner=colwinner
    else:
        winner=diawinner

def check_row():

    global gameisgoing
   #player can win in three rows
    row1 = board[0] == board[1] == board[2] != "-"#either X or O,X
    row2 = board[3] == board[4] == board[5] != "-"#either X or O,X
    row3 = board[6] == board[7] == board[8] != "-"#either X or O#X

    if row1 or row2 or row3:
        gameisgoing=False


    if row1:#in row1 if some thing is present
     return board[0]

    elif row2:
     return board[5]

    elif row3:
     return board[6]


def check_column():
    global gameisgoing
    # player can win in three rows
    col1 = board[0] == board[3] == board[6] != "-"  # either X or O,X
    col2 = board[1] == board[4] == board[7] != "-"  # either X or O,X
    col3 = board[2] == board[5] == board[8] != "-"  # either X or O#X

    if col1 or col2 or col3:
        gameisgoing = False

    if col1:  # in row1 if some thing is present
        return board[0]

    elif col2:
        return board[1]

    elif col3:
        return board[5]

def check_diagonal():
    global gameisgoing
    # player can win in three rows
    dia1 = board[0] == board[4] == board[8] != "-"  # either X or O,X
    dia2 = board[2] == board[4] == board[6] != "-"  # either X or O,X


    if dia1 or dia2:
        gameisgoing = False

    if dia1:  # in row1 if some thing is present
        return board[0]

    elif dia2:
        return board[4]

def check_tie():
    global gameisgoing
    if "-" not in board:
        gameisgoing=False
        print("Match is Tied")
        display_board()

def play_game():
    while gameisgoing:
        display_board()

        handle_turn()

        swap_players()

        check_who_is_the_winner()

    if winner=="X":
        print("X is the winner")
        display_board()
    elif winner=="Y":
        print("Y is the winner")
        display_board()
play_game()