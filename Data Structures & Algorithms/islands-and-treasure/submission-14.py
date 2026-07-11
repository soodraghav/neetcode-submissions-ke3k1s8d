class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        q = []
        

        def bfs(q):
            step = 1

            
            while q:
                tempq = []
                for m,n in q:
                    for d in directions:
                        x,y = m+d[0], n + d[1]

                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 2147483647:
                            grid[x][y] = step
                            tempq.append((x,y))
                            

                q = tempq
                step+=1

            


        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 0:
                    q.append((row,col))

        bfs(q)


                
                

