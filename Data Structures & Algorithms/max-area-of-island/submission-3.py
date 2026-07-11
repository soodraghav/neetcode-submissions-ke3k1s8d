class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        maxT = 0

        def bfs(m,n):     

            count = 0

            q = [(m,n)]

            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            while q:

                tempq = []

                for i,j in q:

                    for d in directions:

                        x,y= i +d[0], j + d[1]

                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                            grid[x][y] = "0"
                            count+=1
                            tempq.append((x,y))

                q = tempq
            
            return count

        def dfs(i,j):
            count = 0

            for d in directions:
                
                x,y= i +d[0], j + d[1]

                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = "#"

                    count+=1 + bfs(x,y)


            return count

                






        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count = 0
                if grid[row][col] == 1:
                    grid[row][col] = "0"
                    # count=1+dfs(row,col)
                    count=1+bfs(row,col)
                
                maxT = max(maxT,count)

        return maxT
