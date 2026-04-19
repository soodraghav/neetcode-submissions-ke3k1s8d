class Solution:
    def jump(self, nums: List[int]) -> int:

        l = r = 0
        steps = 0

        while r < len(nums)-1:
            max_reach = 0

            for i in range(l,r+1):
                max_reach = max(max_reach,nums[i]+i)

            steps+=1
            l = r+1
            r = max_reach

        return steps



        