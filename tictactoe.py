"""
Tic Tac Toe Player
"""

import math

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

    count_X = (val for val in flattened_board if val == X)
    count_O = (val for val in flattened_board if val == O)

    if count_X == count_O:
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
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
