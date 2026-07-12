"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return None

        visited = set()
        d = {}

        def dfs(node):
            visited.add(node)
            if node not in d:
                d[node] = Node(node.val)
            new = d[node]

            for nei in node.neighbors:

                if nei not in visited:
                    new_nei = dfs(nei)
                else:
                    new_nei = d[nei]
                new.neighbors.append(new_nei)

            return new


        return dfs(node)
        