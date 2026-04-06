from functools import cache 

class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dp(i):

            if i >= len(s): return 1

            count = 0

            if 1<=int(s[i])<=9:
                print("ist if")
                count+= dp(i+1)

            if i < len(s)-1  and 10<= int(s[i:i+2]) <=26:
                print("2nd if")
                count+= dp(i+2)


            return count

        
        return dp(0)








        