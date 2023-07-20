import tictactoe as ttt

X = "X"
O = "O"
E = None

board = [
    [O, O, E],
    [X, X, O],
    [O, X, X],
]

board2 = [
    [O, O, X],
    [X, X, O],
    [O, X, X],
]

# print(ttt.player(board))
# print(ttt.result(board, (0, 0)))
# print(ttt.minimax(board))

print(ttt.actions(board))
print(ttt.max_value(board))

print(ttt.terminal(board2))
print(ttt.utility(board2))
