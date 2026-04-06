class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        
        def isPalin(i,j):
            nonlocal count
            
            while i >=0 and j < len(s):
                
                if s[i] != s[j]: break
                count+=1
                i-=1
                j+=1


            return 


        for i in range(len(s)):

            isPalin(i,i)

            if i == len(s)-1: continue
            isPalin(i,i+1)


        return count
        