#time O(M*N)
#space O(M*N)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m=len(board)
        n=len(board[0])
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        def dfs(board,i,j):
            if board[i][j]!="E":
                return
            directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
            mine_count = 0
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':        
                    mine_count += 1
            if mine_count == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(mine_count)
                return

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n:
                    dfs(board, ni, nj)
        dfs(board,click[0],click[1])
        return board