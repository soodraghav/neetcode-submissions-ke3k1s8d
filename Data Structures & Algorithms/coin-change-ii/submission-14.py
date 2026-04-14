from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        @cache
        def dp(i,summ):

            if summ > amount: return 0
            if summ == amount: return 1

            ways = 0

            for j in range(i,len(coins)):

                ways+=dp(j,summ + coins[j])

            return ways

        return dp(0,0)
        