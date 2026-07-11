class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:


        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        total = 0
        visited = set()

        def dfs(x,y):
            nonlocal total
            visited.add((x,y))

            for d in directions:

                m,n = x + d[0], y + d[1]

                if m < 0 or m >= len(grid):
                    total+=1
                elif n < 0 or n >= len(grid[0]):
                    total+=1
                elif (m,n) in visited: continue
                elif grid[m][n] != 1: total+=1
                else: dfs(m,n)
                





        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1: dfs(i,j)

        return total