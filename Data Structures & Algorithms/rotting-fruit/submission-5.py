class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        time = 1
        count = 0
        q = []

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1: count+=1
                elif grid[m][n] == 2: q.append((m,n))

        if count == 0: return 0

        while q:

            tempq = []

            for i,j in q:
                for d in directions:
                    x = i+ d[0]
                    y = j + d[1]

                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        count-=1
                        tempq.append((x,y))

            q = tempq
            if count == 0: return time
            time+=1

        return -1


        
        