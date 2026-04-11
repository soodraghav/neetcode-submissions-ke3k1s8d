from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        directions = ((0,1),(1,0))
        
        @cache
        def help(i,j):

            if i == m-1 and j == n-1: return 1

            count = 0

            for d in directions:
                
                x = d[0] + i
                y = d[1] + j

                if 0<=x<m and 0<=y<n:
                    count+= help(x,y)

            return count

        return help(0,0)