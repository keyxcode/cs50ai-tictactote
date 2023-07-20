import tictactoe as ttt

X = "X"
O = "O"
E = None

board = [
    [O, X, E],
    [E, O, X],
    [X, E, O],
]

print(ttt.player(board))
print(ttt.minimax(board))
