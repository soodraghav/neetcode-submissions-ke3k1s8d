from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, buy):

            if i >=len(prices): return 0

            if buy:
                return max(dp(i+1, False)-prices[i] , dp(i+1, True))

            else:
                return max(dp(i+2, True)+prices[i], dp(i+1, False))


        return dp(0, True)


