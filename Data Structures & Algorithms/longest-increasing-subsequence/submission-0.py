class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        def dp(i,prev):

            if i == len(nums): return 0

            gmax = 0
            for j in range(i,len(nums)):

                if nums[j] > prev:
                    lmax = dp(j+1, nums[j]) +1
                    gmax = max(gmax,lmax)

            return gmax 

        return dp(0,-float('inf'))

            



        