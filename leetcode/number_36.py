class Solution(object):
    def isValidSudoku1(self, board):
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        gro = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                k = i // 3 * 3 + j // 3
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in gro[k]:
                    return False
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                gro[k].append(board[i][j])
        return True
    #use len(set)
    def isValidSudoku(self,board):
        seen = sum(([(c, i), (j, c), (i // 3, j // 3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'),[])
        # print(seen)
        # print(len(seen))
        # print(set(seen))
        # print(len(set(seen)))
        return len(seen) == len(set(seen))

if __name__ == '__main__':
    solution = Solution()
    nums = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
    ]
    print(solution.isValidSudoku1(nums))