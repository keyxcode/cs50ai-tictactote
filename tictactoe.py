"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flattened_board = [val for row in board for val in row]

    if all(val == EMPTY for val in flattened_board):
        return X

    count_X = [val for val in flattened_board if val == X]
    count_O = [val for val in flattened_board if val == O]

    if len(count_X) == len(count_O):
        return X

    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    board_size = len(board)
    avail_actions = set()

    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == EMPTY:
                avail_actions.add((i, j))

    return avail_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    i, j = action
    board[i][j] = current_player

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        flattened_board = [val for row in board for val in row]
        count_X = [val for val in flattened_board if val == X]
        count_O = [val for val in flattened_board if val == O]

        if len(count_X) > len(count_O):
            return X
        else:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    won_rows = (
        (board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY)
        or (board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY)
        or (board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY)
    )
    won_cols = (
        (board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY)
        or (board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY)
        or (board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY)
    )
    won_diags = (
        board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY
    ) or (board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY)

    return won_rows or won_cols or won_diags


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    avail_actions = list(actions(board))
    print(avail_actions)

    rand_idx = random.randrange(len(avail_actions))

    return avail_actions[rand_idx]
