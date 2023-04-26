starter_board = [
  [".", ".", "."],
  [".", ".", "."],
  [".", ".", "."]
]


# format board
def format_board(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid

# print(format_board(starter_board))


def make_move(board, row, column, player):
    board[row][column] = player
    return board

# get_cells extracts three cells from the board - get the values of the coordinates
def get_cells(board, coord_1, coord_2, coord_3):
    return [
        board[coord_1[0]][coord_1[1]],
        board[coord_2[0]][coord_2[1]],
        board[coord_3[0]][coord_3[1]]
    ]

# is group complete check if there are not empty cells
# it takes a board and three coordinates
def is_group_complete(board, coord_1, coord_2, coord_3):
    # call the function get_cells
    cells = get_cells(board, coord_1, coord_2, coord_3)
    # return true if there's not a dot in cells
    return "." not in cells

# check if there is a winner - all grops have the same player sign
def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
    cells = get_cells(board, coord_1, coord_2, coord_3)
    return cells[0] == cells[1] and cells[1] == cells[2]

# check all winning combinations
winning_combinations = [
    # rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# make a move function by assigning the 'player sign' to the row and column of the board he select

# define when game is over (tie or win, no empty spaces)
def game_over(board):
    for combination in winning_combinations:
        # make sure there are no empty cells
        if is_group_complete(board, combination[0], combination[1], combination[2]):
            # check if there is a winning, if all cells are the same
            if are_all_cells_the_same(board, combination[0], combination[1], combination[2]):
                return True
    return False

def play_game():
    board = starter_board
    player = "X"
    while not game_over(board):
        print(format_board(board))
        print("It's " + player + "'s turn.")
        row = int(input("Enter a row: "))
        column = int(input("Enter a column: "))
        if not is_move_valid(board, row, column):
            print('ah-ah, this cell is already taken, try again')
            continue
        board = make_move(board, row, column, player)
        if player == 'X':
            player = 'O'
        else :
            player = "X"
    print(format_board(board))
    print("Game over!")

def is_move_valid(board, row, column):
    #if board[row][column] == '.' return True
    return board[row][column] == '.'

#try now!
print("Game time!")
play_game()