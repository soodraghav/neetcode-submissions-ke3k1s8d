class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(m,n):

            grid[row][col] = "0"            

            q = [(m,n)]

            while q:

                tempq = []
                
                for x,y in q:

                    for d in directions:
                        i,j = x + d[0], y + d[1]

                        if 0<=i< len(grid) and 0<=j< len(grid[0]) and grid[i][j] == "1":
                            grid[i][j] = "0"
                            tempq.append((i,j))


                q = tempq

            
            return 

                            



            

                

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1":
                    count+=1
                    bfs(row,col)


        return count

        