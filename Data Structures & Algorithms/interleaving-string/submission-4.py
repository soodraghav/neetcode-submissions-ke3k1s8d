from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3): return False
        
        @cache
        def dp(i1,i2):

            if i1 == len(s1) and i2 == len(s2): return True

            c1 = c2 =False

            if i1 < len(s1) and s1[i1] == s3[i1+i2]: c1 = dp(i1+1,i2)

            if i2 < len(s2) and s2[i2] == s3[i1+i2]: c2 = dp(i1,i2+1)


            return c1 or c2


        return dp(0,0)
            
        