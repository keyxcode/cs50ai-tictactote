"""
Tic Tac Toe Player
"""

import math
import random
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]


def flatten_board(board):
    return [val for row in board for val in row]


def board_is_empty(board):
    flattened_board = flatten_board(board)
    return all(val == EMPTY for val in flattened_board)


def board_is_full(board):
    flattened_board = flatten_board(board)
    return all(val != EMPTY for val in flattened_board)


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board_is_empty(board):
        return X

    flattened_board = flatten_board(board)
    count_X = [val for val in flattened_board if val == X]
    count_O = [val for val in flattened_board if val == O]

    if len(count_X) == len(count_O):
        return X

    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    board_size = 3
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

    new_board = deepcopy(board)
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        won_rows = (
            (board[0][0] == board[0][1] == board[0][2] and board[0][0] == player)
            or (board[1][0] == board[1][1] == board[1][2] and board[1][0] == player)
            or (board[2][0] == board[2][1] == board[2][2] and board[2][0] == player)
        )
        won_cols = (
            (board[0][0] == board[1][0] == board[2][0] and board[0][0] == player)
            or (board[0][1] == board[1][1] == board[2][1] and board[0][1] == player)
            or (board[0][2] == board[1][2] == board[2][2] and board[0][2] == player)
        )
        won_diags = (
            board[0][0] == board[1][1] == board[2][2] and board[0][0] == player
        ) or (board[0][2] == board[1][1] == board[2][0] and board[0][2] == player)

        if won_rows or won_cols or won_diags:
            return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or board_is_full(board):
        return True

    return False


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

    if board_is_empty(board):
        return (random.randrange(2), random.randrange(2))

    current_player = player(board)
    avail_actions = list(actions(board))

    value_func = min_value if current_player == X else max_value
    best_utility = -math.inf if current_player == X else math.inf
    best_action = None

    for action in avail_actions:
        new_board = result(board, action)
        action_utility = value_func(new_board)
        if current_player == X and action_utility > best_utility:
            best_utility = action_utility
            best_action = action
        elif current_player == O and action_utility < best_utility:
            best_utility = action_utility
            best_action = action

    return best_action


def max_value(board):
    if terminal(board):
        return utility(board)

    avail_actions = list(actions(board))
    chosen_utility = -math.inf

    for action in avail_actions:
        new_board = result(board, action)
        action_utility = min_value(new_board)
        if action_utility > chosen_utility:
            chosen_utility = action_utility

    return chosen_utility


def min_value(board):
    if terminal(board):
        return utility(board)

    avail_actions = list(actions(board))
    chosen_utility = math.inf

    for action in avail_actions:
        new_board = result(board, action)
        action_utility = max_value(new_board)
        if action_utility < chosen_utility:
            chosen_utility = action_utility

    return chosen_utility
