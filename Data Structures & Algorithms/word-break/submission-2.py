from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)

        @cache
        def help(i):

            if i >= len(s): return True

            for j in range(i,len(s)):

                if s[i:j+1] in  words and help(j+1): return True

            return False


        return help(0)
        