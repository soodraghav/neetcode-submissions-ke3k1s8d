class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        gmax = gmin = nums[0]
        tsum = 0
        lmax = lmin = 0

        for n in nums:

            lmax = max(lmax+n,n)
            gmax = max(gmax,lmax)

            lmin = min(lmin +n,n)
            gmin = min(gmin, lmin)

            tsum+=n

        if gmax <= 0: return gmax
        return max(gmax, tsum-gmin)







