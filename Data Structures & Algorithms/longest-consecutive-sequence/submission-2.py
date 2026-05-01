class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        gmax = 0

        for n in nums:

            if n-1 in nums: continue

            num = n

            lmax = 0

            while num in nums:
                num+=1

            gmax = max(gmax,num-n)

        return gmax
        


        