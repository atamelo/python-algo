def knight(board, row, column):
    if row == len(board) and column == len(board[0]):
        return 1

    if row > len(board) - 1 or column > len(board[0]) - 1:
        return 0

    if board[row][column] != 'x':
        return board[row][column]

    moves = knight(board, row + 1, column + 2) + knight(board, row + 2, column + 1)

    board[row][column] = moves

    return moves

m = 6
n = 6
board = [['x'] * m for _ in range(n)]
result = knight(board, 0, 0)
print(result)
