class Solution:
    def dfs(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    continue
                for result in {1,2,3,4,5,6,7,8,9} - {board[row][j] for j in range(9)} - {board[i][col] for i in range(9)} - {board[row//3*3 + i][col//3*3 + j] for i in range(3) for j in range(3)}:
                    board[row][col] = result
                    if self.dfs(board):
                        return True
                    board[row][col] = '.'
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    board = [
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
    solution.dfs(board)
    print(board)