class Matrix2Dboard(object):
    def Board2d(self, board, word):
        if 1 < len(board) <= 200:
            n = len(board)
            m = len(board[0])
            for i in range(n):
                for j in range(m):
                    if word[0] == board[i][j]:
                        if self.findWord(board, word, i, j):
                            return True
        return False

    def findWord(self, board, word, row, col, i=0):
        if i == len(word):
            return True
        if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or word[i] != board[row][col]:
            return False
        board[row][col] = '$'
        res = self.findWord(board, word, row+1, col, i+1) or self.findWord(board, word, row-1, col, i+1) or self.findWord(board, word, row, col+1, i+1) or self.findWord(board, word, row, col-1, i+1)
        board[row][col] = word[i]
        return res


mat = Matrix2Dboard()
print(mat.Board2d([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
