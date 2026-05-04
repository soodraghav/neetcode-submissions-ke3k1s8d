from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0 
        maxx = 0
        d = defaultdict(int)
        maxf = 0

        for r in range(len(s)):

            d[s[r]] +=1
            maxf = max(maxf, d[s[r]])

            if r-l+1 - maxf  > k:
                d[s[l]]-=1 
                l+=1

            maxx = max(maxx, r-l+1)


        return maxx

            



