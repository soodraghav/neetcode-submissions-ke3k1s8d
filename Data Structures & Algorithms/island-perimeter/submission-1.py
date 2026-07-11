class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:


        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        total = 0
  
        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if grid[x][y] != 1: continue
                
                for d in directions:

                    m,n = x + d[0], y + d[1]

                    if m < 0 or m >= len(grid): total+=1
                    elif n < 0 or n >= len(grid[0]): total+=1
                    elif grid[m][n] != 1: total+=1
                    
        return total