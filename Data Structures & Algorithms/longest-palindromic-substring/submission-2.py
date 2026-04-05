from functools import cache

class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxL = 0
        lPal = 0
        rPal = 0

        @cache
        def isPalin(l,r):
            nonlocal maxL, lPal, rPal
            while l >=0 and r < len(s):

                if s[l] == s[r]:
                    if r-l+1 > maxL:
                        maxL = r-l+1
                        lPal = l
                        rPal = r

                else:
                    break

                l-=1
                r+=1


        for i in range(len(s)):

            isPalin(i,i)
            if i <len(s)-1:
                isPalin(i,i+1)


        return s[lPal:rPal+1]



        