class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        atl_q = []
        pac_q = []
        atl_visited = set()
        pac_visited = set()
        directions = ((1,0), (-1,0), (0,-1), (0,1))


        def dfs(i,j,ocean):

            
            for d in directions:
                x, y = i + d[0], j+ d[1]

                if 0<=x<len(heights) and 0<=y<len(heights[0]) and heights[x][y] >= heights[i][j]:
                    if ocean == "pac" and (x,y) not in pac_visited:
                        pac_visited.add((x,y))
                        dfs(x,y,ocean)
                    elif ocean == "atl" and (x,y) not in atl_visited:
                        atl_visited.add((x,y))
                        dfs(x,y,ocean)



        for i in range(0,len(heights)):
                pac_q.append((i,0))
                atl_q.append((i,len(heights[0])-1))


        for j in range(0,len(heights[0])):
                pac_q.append((0,j))
                atl_q.append((len(heights)-1,j))

        for x,y in pac_q:
            pac_visited.add((x,y))
            dfs(x,y,"pac")
        for x,y in atl_q:
            atl_visited.add((x,y))
            dfs(x,y,"atl")

        return list(atl_visited.intersection(pac_visited))

        

