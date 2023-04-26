starter_board = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
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
# make program more generic across the size of the grid


def get_cells_by_list(board, coords):
    cells = []
    for coord in coords:
        cells.append(board[coord[0]][coord[1]])
    return cells

# is group complete check if there are not empty cells
# it takes a board and three coordinates


def is_group_complete(board, coords):
    # call the function get_cells
    cells = get_cells_by_list(board, coords)
    # return true if there's not a dot in cells
    return "." not in cells


# check if there is a winner - all grops have the same player sign
def are_all_cells_the_same(board, coords):
    cells = get_cells_by_list(board, coords)
    return cells[0] == cells[1] and cells[1] == cells[2]


# check all winning combinations
# winning_combinations = [
#     # rows
#     [(0, 0), (0, 1), (0, 2), (0,3),(0,4) ],
#     [(1, 0), (1, 1), (1, 2), (1,3),(1,4)],
#     [(2, 0), (2, 1), (2, 2), (2,3), (2,4)],
#     [(3, 0), (3, 1), (3, 2), (3,3), (3,4)],
#     [(4, 0), (4, 1), (4, 2), (4,3), (4,4)],
#     # columns
#     [(0, 0), (1, 0), (2, 0), (3,0), (4,0)],
#     [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
#     [(0, 2), (1, 2), (2, 2),(3,2),(4,2)],
#      [(0, 3), (1, 3), (2, 3),(3,3),(4,3)],
#     [(0, 4), (1, 4), (2, 4),(3,4),(4,4)],
#     # diagonals
#     [(0, 0), (1, 1), (2, 2),(3,3),(4,4)],
#     [(0, 4), (1, 3), (2, 2),(3,1),(4,0)]
# ]

#method 1
#def generate_winning_combinations(board_size):
    # row_combinations = []
    # for row in range(board_size):
    #     row_combinations.append([(row, col) for col in range(board_size)])

    # col_combinations = []
    # for col in range(board_size):
    #     col_combinations.append([(row, col) for row in range(board_size)])

    # diag_combinations = [[(i, i) for i in range(board_size)]]
    # diag_combinations.append([(i, board_size - i - 1) for i in range(board_size)])

    # winning_combinations = row_combinations + col_combinations + diag_combinations

#method 2
def generate_winning_combinations(board_size):
    combinations = []
    for row in range(board_size):
        row_combinations = []
        col_combinations = []
        for col in range(board_size):
            row_combinations.append((row, col))
            col_combinations.append((col, row))
        combinations.append(row_combinations)
        combinations.append(col_combinations)
    diag_fwd = []
    diag_bwd = []
    for i in range(board_size):
        diag_fwd.append((i, i))
        diag_bwd.append((i, board_size - i - 1))
    combinations.append(diag_fwd)
    combinations.append(diag_bwd)
    return combinations





# make a move function by assigning the 'player sign' to the row and column of the board he select

# define when game is over (tie or win, no empty spaces)


def game_over(board, board_size):
    winning_combinations = generate_winning_combinations(board_size)
    for combination in winning_combinations:
        # make sure there are no empty cells
        if is_group_complete(board, combination):
            # check if there is a winning, if all cells are the same
            if are_all_cells_the_same(board, combination):
                return True
    # if there are no empty cells end the game
    for row in board:
        if '.' in row:
            return False
    print("it's a tie!")
    return True


def play_game(board_size):
    board = make_blank_board(board_size)
    player = "X"
    while not game_over(board, board_size):
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
        else:
            player = "X"
    print(format_board(board))
    print("Game over!")

def make_blank_board(board_size):
    grid = []
    for row in range(0, board_size):
        row = ['.'] * board_size
        grid.append(row) 
    return grid


def is_move_valid(board, row, column):
    # if board[row][column] == '.' return True
    return board[row][column] == '.'


# try now!
print("Game time!")
play_game(5)
