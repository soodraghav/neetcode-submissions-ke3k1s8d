class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxReach = 0

        for i,n in enumerate(nums):

            if i > maxReach: return False

            maxReach = max(maxReach,i+nums[i])

            if maxReach >= len(nums)-1: return True

        return False

            
        