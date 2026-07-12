class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = []
        visited = set()
        directions = ((1,0), (-1,0), (0,-1), (0,1))

        for i in range(0,len(board)):
            if board[i][0] == "O": 
                q.append((i,0))
                board[i][0] = "#"
            if board[i][len(board[0])-1] == "O": 
                q.append((i,len(board[0])-1))
                board[i][len(board[0])-1] = "#"

        for j in range(0,len(board[0])):
            if board[0][j] == "O": 
                q.append((0,j))
                board[0][j] = "#"
            if board[len(board)-1][j] == "O": 
                q.append((len(board)-1,j))
                board[len(board)-1][j] = "#"

        print(q)
        while q:
            tq = []
            for i,j in q:
                for d in directions:
                    x,y = i + d[0], j+ d[1]

                    if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == "O":
                        board[x][y] = "#"
                        tq.append((x,y))


            q = tq


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O": board[row][col] = "X"
                if board[row][col] == "#": board[row][col] = "O"

