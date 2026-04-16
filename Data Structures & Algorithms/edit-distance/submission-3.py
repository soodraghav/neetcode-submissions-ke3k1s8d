from functools import cache

class Solution:  

    
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i1,i2):

            if i1 >= len(word1) and i2 >= len(word2): return 0
            if i1 >= len(word1): return len(word2) - i2
            if i2 >= len(word2): return len(word1) - i1


            if word1[i1] == word2[i2]:
                return dp(i1+1, i2+1)

            else:

                c1 = dp(i1,i2+1)
                c2 = dp(i1+1,i2)
                c3 = dp(i1+1,i2+1)
                
                return 1+ min(c1,c2,c3)


        return dp(0,0)
        