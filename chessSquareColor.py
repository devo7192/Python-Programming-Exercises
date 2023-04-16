def getChessSquareColor(column, row):
    if column < 1 or row < 1 or column > 8 or row > 8:
        return ''
    if column % 2 == row % 2:
        return 'white'
    return 'black'

assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''