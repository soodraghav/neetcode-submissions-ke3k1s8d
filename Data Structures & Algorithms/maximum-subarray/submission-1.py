class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        gmax = lmax = nums[0]


        for i,n in enumerate(nums):

            if i == 0: continue



            lmax = max(lmax+n,n)
            gmax = max(gmax,lmax)


        return gmax

