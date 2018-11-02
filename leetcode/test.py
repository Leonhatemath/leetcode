import collections
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6","3",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
    ]
def isValidSudoku(board):
    seen = ([(c, i), (j, c), (i//3, j//3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.')
    seen = sum(seen,[])
    print(seen)
    print(len(seen))
    print(set(seen))
    print(len(set(seen)))
    return len(seen) == len(set(seen))
isValidSudoku(board)